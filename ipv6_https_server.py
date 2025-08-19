#!/usr/bin/env python3
"""
Ultra Fast IPv6 HTTPS Server
Single file, maximum performance, IPv6 only
Just run: python ipv6_https_server.py
"""

import asyncio
import ssl
import os
import sys
import mimetypes
import gzip
import hashlib
import time
import json
import threading
import signal
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import webbrowser
import subprocess
from urllib.parse import unquote
from dataclasses import dataclass, field
from typing import Dict, Set, Optional, Tuple
import socket

# IPv6 Configuration
IPV6_HTTP_PORT = 8080
IPV6_HTTPS_PORT = 80
IPV6_HOST = '::'  # Listen on all IPv6 interfaces
CERT_DIR = Path("./ipv6_certs")
CERT_FILE = CERT_DIR / "ipv6_server.crt"
KEY_FILE = CERT_DIR / "ipv6_server.key"

# Ultra Performance Settings
MAX_WORKERS = min(32, (os.cpu_count() or 1) * 2)  # Reduced workers for stability
MAX_CONNECTIONS = 1000  # Reduced connection limit for stability
BUFFER_SIZE = 64 * 1024  # 64KB buffer
CACHE_SIZE = 100 * 1024 * 1024  # 100MB cache
CHUNK_SIZE = 8192  # 8KB chunks
REQUEST_TIMEOUT = 30  # 30 second timeout

@dataclass
class UltraStats:
    """Ultra-fast server statistics"""
    requests: int = 0
    bytes_served: int = 0
    cache_hits: int = 0
    cache_misses: int = 0
    connections: int = 0
    errors: int = 0
    ssl_errors: int = 0
    encoding_errors: int = 0
    start_time: float = field(default_factory=time.time)

class UltraCache:
    """Ultra-fast LRU cache with minimal overhead"""
    
    def __init__(self, max_size: int = CACHE_SIZE):
        self.max_size = max_size
        self.cache: Dict[str, Tuple[bytes, Dict, float]] = {}
        self.access_times: Dict[str, float] = {}
        self.current_size = 0
        self.lock = threading.RLock()
    
    def get(self, key: str) -> Optional[Tuple[bytes, Dict]]:
        with self.lock:
            if key in self.cache:
                content, headers, _ = self.cache[key]
                self.access_times[key] = time.time()
                return content, headers
            return None
    
    def put(self, key: str, content: bytes, headers: Dict):
        with self.lock:
            size = len(content)
            
            # Don't cache huge files
            if size > 50 * 1024 * 1024:  # 50MB
                return
            
            # Fast eviction if needed
            while self.current_size + size > self.max_size and self.cache:
                self._evict_lru()
            
            self.cache[key] = (content, headers, time.time())
            self.access_times[key] = time.time()
            self.current_size += size
    
    def _evict_lru(self):
        if not self.access_times:
            return
        lru_key = min(self.access_times.items(), key=lambda x: x[1])[0]
        if lru_key in self.cache:
            content, _, _ = self.cache[lru_key]
            self.current_size -= len(content)
            del self.cache[lru_key]
            del self.access_times[lru_key]

class UltraFastIPv6Server:
    def __init__(self):
        self.stats = UltraStats()
        self.cache = UltraCache()
        self.executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
        self.connections: Set[asyncio.StreamWriter] = set()
        
        print(f"🚀 Initializing Ultra Fast IPv6 Server...")
        print(f"⚡ Workers: {MAX_WORKERS}")
        print(f"💾 Cache: {CACHE_SIZE // 1024 // 1024}MB")
        print(f"🌐 IPv6 Only Mode")
    
    def generate_ipv6_ssl_cert(self):
        """Generate IPv6-optimized SSL certificate"""
        CERT_DIR.mkdir(exist_ok=True)
        
        if CERT_FILE.exists() and KEY_FILE.exists():
            print("✓ IPv6 SSL certificates exist")
            return
        
        print("🔐 Generating IPv6 SSL certificate...")
        
        try:
            # Generate key faster
            subprocess.run([
                'openssl', 'genrsa', '-out', str(KEY_FILE), '2048'
            ], check=True, capture_output=True, timeout=30)
            
            # IPv6-specific certificate
            subprocess.run([
                'openssl', 'req', '-new', '-x509', '-key', str(KEY_FILE),
                '-out', str(CERT_FILE), '-days', '365', '-subj',
                '/C=US/ST=CA/L=Local/O=UltraFastIPv6/CN=2405:201:500f:584d:8dfd:87c9:a456:286',
                '-addext', 'subjectAltName=IP:2405:201:500f:584d:8dfd:87c9:a456:286,IP:::1,DNS:localhost'
            ], check=True, capture_output=True, timeout=30)
            
            print("✓ IPv6 SSL certificate generated")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Certificate generation failed: {e}")
            raise
        except FileNotFoundError:
            print("❌ OpenSSL not found. Install from: https://slproweb.com/products/Win32OpenSSL.html")
            raise
    
    def create_ultra_ssl_context(self) -> ssl.SSLContext:
        """Create ultra-fast SSL context with better error handling"""
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.load_cert_chain(CERT_FILE, KEY_FILE)
        
        # More compatible cipher selection
        try:
            context.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:!aNULL:!MD5:!DSS')
        except ssl.SSLError:
            # Fallback to default ciphers if custom ones fail
            pass
        
        # Performance optimizations with error handling
        try:
            context.options |= ssl.OP_SINGLE_DH_USE | ssl.OP_SINGLE_ECDH_USE
            # Suppress SSL errors for better user experience
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
        except Exception:
            pass
        
        # Enable ALPN with fallback -REMOVED h2 to prevent HTTP/2 protocol errors
        try:
            context.set_alpn_protocols(['http/1.1'])
        except Exception:
            pass
        
        return context
    
    def fast_etag(self, file_path: Path) -> str:
        """Ultra-fast ETag generation"""
        stat = file_path.stat()
        return f'"{int(stat.st_mtime)}-{stat.st_size}"'
    
    def should_compress(self, content_type: str, size: int) -> bool:
        """Fast compression check"""
        if size < 1024 or size > 10 * 1024 * 1024:  # Don't compress small or huge files
            return False
        return content_type.startswith(('text/', 'application/javascript', 'application/json', 'application/xml'))
    
    def ultra_compress(self, data: bytes) -> bytes:
        """Ultra-fast compression"""
        return gzip.compress(data, compresslevel=1)  # Fastest compression
    
    async def ultra_read_file(self, file_path: Path) -> bytes:
        """Ultra-fast file reading"""
        def _read():
            with open(file_path, 'rb') as f:
                return f.read()
        
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self.executor, _read)
    
    async def handle_ultra_request(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """Ultra-fast request handling with robust error handling"""
        start_time = time.time()
        self.stats.connections += 1
        self.connections.add(writer)
        
        try:
            # Fast request reading with better error handling
            request_line = await asyncio.wait_for(reader.readline(), timeout=10.0)
            if not request_line:
                return
            
            # Handle encoding errors gracefully
            try:
                request_line = request_line.decode('utf-8').strip()
            except UnicodeDecodeError:
                try:
                    request_line = request_line.decode('latin-1').strip()
                except UnicodeDecodeError:
                    self.stats.encoding_errors += 1
                    # Only log first few encoding errors to avoid spam
                    if self.stats.encoding_errors <= 5:
                        print(f"Request decoding error: Invalid encoding (total: {self.stats.encoding_errors})")
                    return
            
            if not request_line:
                return
            
            try:
                method, path, protocol = request_line.split(' ', 2)
            except ValueError:
                await self.send_error(writer, 400, "Bad Request")
                return
            
            # Fast header reading with encoding safety
            headers = {}
            try:
                while True:
                    line = await asyncio.wait_for(reader.readline(), timeout=5.0)
                    if line == b'\r\n' or line == b'\n':
                        break
                    if not line:
                        break
                    if line:
                        try:
                            header_line = line.decode('utf-8').strip()
                        except UnicodeDecodeError:
                            try:
                                header_line = line.decode('latin-1').strip()
                            except UnicodeDecodeError:
                                continue  # Skip malformed headers
                        
                        if ':' in header_line:
                            key, value = header_line.split(':', 1)
                            headers[key.strip().lower()] = value.strip()
            except asyncio.TimeoutError:
                # Continue with headers we have so far
                pass
            
            # Handle special endpoints
            if path == '/ultra-stats':
                await self.send_ultra_stats(writer)
                return
            elif path == '/ultra-info':
                await self.send_ultra_info(writer)
                return
            
            # Fast file serving
            await self.serve_ultra_fast(writer, method, path, headers)
            
        except asyncio.TimeoutError:
            try:
                await self.send_error(writer, 408, "Timeout")
            except:
                pass
        except ConnectionResetError:
            # Client forcibly closed connection - this is normal, don't log
            pass
        except ConnectionAbortedError:
            # Connection was aborted - this is normal, don't log
            pass
        except OSError as e:
            # Handle various socket errors silently
            if e.errno not in [10054, 10053, 10038]:  # Common Windows socket errors
                print(f"Socket error: {e}")
        except ssl.SSLError:
            # SSL errors are common with browsers/bots, don't spam logs
            self.stats.ssl_errors += 1
            # Only log first few SSL errors
            if self.stats.ssl_errors <= 3:
                print(f"SSL connection error (total: {self.stats.ssl_errors})")
        except Exception as e:
            self.stats.errors += 1
            # Only log first few general errors to avoid spam
            if self.stats.errors <= 10:
                print(f"Request error: {e} (total errors: {self.stats.errors})")
            try:
                await self.send_error(writer, 500, "Server Error")
            except:
                pass
        finally:
            self.connections.discard(writer)
            try:
                if not writer.is_closing():
                    writer.close()
                await writer.wait_closed()
            except:
                pass
    
    async def serve_ultra_fast(self, writer: asyncio.StreamWriter, method: str, path: str, headers: Dict):
        """Ultra-fast file serving"""
        # Fast path processing
        path = unquote(path)
        if path == '/':
            path = '/index.html'
        
        file_path = Path('.') / path.lstrip('/')
        
        # Fast security check
        try:
            file_path = file_path.resolve()
            if not str(file_path).startswith(str(Path('.').resolve())):
                await self.send_error(writer, 403, "Forbidden")
                return
        except:
            await self.send_error(writer, 400, "Bad Request")
            return
        
        if not file_path.exists():
            await self.send_error(writer, 404, "Not Found")
            return
        
        if file_path.is_dir():
            await self.send_ultra_listing(writer, file_path, path)
            return
        
        # Ultra-fast caching
        cache_key = str(file_path)
        cached = self.cache.get(cache_key)
        
        etag = self.fast_etag(file_path)
        
        # Fast conditional check
        if headers.get('if-none-match') == etag:
            await self.send_response(writer, 304, "Not Modified", {})
            return
        
        # Serve from cache if valid
        if cached:
            content, cached_headers = cached
            if cached_headers.get('etag') == etag:
                await self.send_response(writer, 200, "OK", cached_headers, content)
                self.stats.cache_hits += 1
                self.stats.requests += 1
                self.stats.bytes_served += len(content)
                return
        
        # Cache miss - read file ultra-fast
        self.stats.cache_misses += 1
        
        try:
            content = await self.ultra_read_file(file_path)
        except:
            await self.send_error(writer, 500, "Read Error")
            return
        
        # Fast content type detection
        content_type, _ = mimetypes.guess_type(str(file_path))
        if not content_type:
            content_type = 'application/octet-stream'
        
        if 'text/html' in content_type:
            pass

        # Ultra-fast headers
        response_headers = {
            'content-type': content_type,
            'etag': etag,
            'cache-control': 'no-cache, no-store, must-revalidate',
            'pragma': 'no-cache',
            'expires': '0',
            'server': 'UltraFastIPv6/1.0',
            'x-frame-options': 'SAMEORIGIN',
            'accept-ranges': 'bytes'
        }
        
        # Fast compression
        accept_encoding = headers.get('accept-encoding', '')
        if 'gzip' in accept_encoding and self.should_compress(content_type, len(content)):
            content = self.ultra_compress(content)
            response_headers['content-encoding'] = 'gzip'
        
        response_headers['content-length'] = str(len(content))
        
        # Cache the response
        self.cache.put(cache_key, content, response_headers)
        
        # Ultra-fast response
        await self.send_response(writer, 200, "OK", response_headers, content)
        
        # Update stats
        self.stats.requests += 1
        self.stats.bytes_served += len(content)
    
    async def send_ultra_stats(self, writer: asyncio.StreamWriter):
        """Send ultra-fast stats page"""
        uptime = time.time() - self.stats.start_time
        
        stats_html = f"""<!DOCTYPE html>
<html><head><title>⚡ Ultra Fast IPv6 Server</title>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:'Segoe UI',sans-serif;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);min-height:100vh;color:white;display:flex;align-items:center;justify-content:center}}
.container{{max-width:1000px;padding:40px;background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);border-radius:20px;text-align:center}}
h1{{font-size:3em;margin-bottom:30px;text-shadow:2px 2px 4px rgba(0,0,0,0.3)}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:20px;margin:30px 0}}
.stat{{background:rgba(255,255,255,0.1);padding:20px;border-radius:10px;border:1px solid rgba(255,255,255,0.2)}}
.stat-value{{font-size:2em;font-weight:bold;margin-bottom:5px}}
.stat-label{{font-size:0.9em;opacity:0.8}}
.pulse{{animation:pulse 2s infinite}}@keyframes pulse{{0%{{opacity:1}}50%{{opacity:0.5}}100%{{opacity:1}}}}
.error-stats{{background:rgba(255,0,0,0.1);border-color:rgba(255,100,100,0.3)}}
</style></head>
<body><div class="container"><h1><span class="pulse">⚡</span> Ultra Fast IPv6 Server</h1>
<div class="stats">
<div class="stat"><div class="stat-value">{uptime:.1f}s</div><div class="stat-label">Uptime</div></div>
<div class="stat"><div class="stat-value">{self.stats.requests:,}</div><div class="stat-label">Requests</div></div>
<div class="stat"><div class="stat-value">{self.stats.bytes_served//1024//1024:.1f}MB</div><div class="stat-label">Data Served</div></div>
<div class="stat"><div class="stat-value">{(self.stats.cache_hits/(max(1,self.stats.cache_hits+self.stats.cache_misses))*100):.1f}%</div><div class="stat-label">Cache Hit</div></div>
<div class="stat"><div class="stat-value">{len(self.connections)}</div><div class="stat-label">Connections</div></div>
<div class="stat"><div class="stat-value">{MAX_WORKERS}</div><div class="stat-label">Workers</div></div>
<div class="stat error-stats"><div class="stat-value">{self.stats.errors}</div><div class="stat-label">Errors</div></div>
<div class="stat error-stats"><div class="stat-value">{self.stats.ssl_errors}</div><div class="stat-label">SSL Errors</div></div>
<div class="stat error-stats"><div class="stat-value">{self.stats.encoding_errors}</div><div class="stat-label">Encoding Errors</div></div>
</div><p>🌐 IPv6 Only • 🚀 Ultra Performance • ⚡ {self.stats.requests/max(1,uptime):.1f} req/s</p></div></body></html>"""
        
        headers = {
            'content-type': 'text/html; charset=utf-8',
            'content-length': str(len(stats_html)),
            'cache-control': 'no-cache'
        }
        
        await self.send_response(writer, 200, "OK", headers, stats_html)
    
    async def send_ultra_info(self, writer: asyncio.StreamWriter):
        """Send server info as JSON"""
        info = {
            'server': 'Ultra Fast IPv6 HTTPS Server',
            'version': '1.0',
            'ipv6_only': True,
            'uptime': time.time() - self.stats.start_time,
            'requests': self.stats.requests,
            'bytes_served': self.stats.bytes_served,
            'cache_hits': self.stats.cache_hits,
            'cache_misses': self.stats.cache_misses,
            'active_connections': len(self.connections),
            'workers': MAX_WORKERS,
            'cache_size_mb': self.cache.current_size // 1024 // 1024,
            'requests_per_second': self.stats.requests / max(1, time.time() - self.stats.start_time),
            'errors': self.stats.errors,
            'ssl_errors': self.stats.ssl_errors,
            'encoding_errors': self.stats.encoding_errors
        }
        
        content = json.dumps(info, indent=2).encode()
        headers = {
            'content-type': 'application/json',
            'content-length': str(len(content)),
            'access-control-allow-origin': '*'
        }
        
        await self.send_response(writer, 200, "OK", headers, content)
    
    async def send_ultra_listing(self, writer: asyncio.StreamWriter, dir_path: Path, url_path: str):
        """Ultra-fast directory listing"""
        files = []
        total_size = 0
        
        try:
            for item in sorted(dir_path.iterdir()):
                if item.name.startswith('.'):
                    continue
                stat_info = item.stat()
                if item.is_file():
                    size = stat_info.st_size
                    total_size += size
                    size_str = f"{size//1024}KB" if size > 1024 else f"{size}B"
                else:
                    size_str = "-"
                files.append((item.name, item.is_dir(), size_str))
        except:
            await self.send_error(writer, 500, "Directory Error")
            return
        
        # Ultra-compact HTML
        html = f"""<!DOCTYPE html><html><head><title>📁 {url_path}</title>

<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<style>*{{margin:0;padding:0}}body{{font-family:'Segoe UI',sans-serif;background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:20px}}
.container{{max-width:1000px;margin:0 auto;background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);border-radius:15px;padding:30px}}
h1{{text-align:center;margin-bottom:20px}}
.file{{display:grid;grid-template-columns:50px 1fr 100px;gap:15px;padding:10px;border-bottom:1px solid rgba(255,255,255,0.1);align-items:center}}
.file:hover{{background:rgba(255,255,255,0.1)}}
.file a{{color:white;text-decoration:none}}.file a:hover{{color:#ffeb3b}}
.dir a{{color:#81c784;font-weight:600}}
</style></head><body><div class="container"><h1>📁 {url_path}</h1>"""
        
        if url_path != '/':
            html += '<div class="file"><div>⬆️</div><div class="dir"><a href="../">../</a></div><div>-</div></div>'
        
        for name, is_dir, size in files:
            icon = '📁' if is_dir else '📄'
            href = f"{name}/" if is_dir else name
            css_class = 'dir' if is_dir else 'file'
            html += f'<div class="file"><div>{icon}</div><div class="{css_class}"><a href="{href}">{name}</a></div><div>{size}</div></div>'
        
        html += f'<p style="text-align:center;margin-top:20px;opacity:0.8">📊 {len(files)} items • 💾 {total_size//1024}KB total</p></div></body></html>'
        
        headers = {
            'content-type': 'text/html; charset=utf-8',
            'content-length': str(len(html)),
            'cache-control': 'no-cache'
        }
        
        await self.send_response(writer, 200, "OK", headers, html)
    
    async def send_response(self, writer: asyncio.StreamWriter, status: int, status_text: str, headers: Dict, body: bytes = b''):
        """Ultra-fast response sending with error handling"""
        try:
            if writer.is_closing():
                return
            
            response_lines = [f"HTTP/1.1 {status} {status_text}"]
            response_lines.extend(f"{k}: {v}" for k, v in headers.items())
            response_lines.append("")
            
            response_header = "\r\n".join(response_lines).encode('utf-8') + b"\r\n"
            
            writer.write(response_header)
            if body:
                if isinstance(body, str):
                    body = body.encode('utf-8')
                writer.write(body)
            
            await writer.drain()
        except (ConnectionResetError, ConnectionAbortedError, ssl.SSLError, OSError):
            # Connection was closed by client - this is normal
            pass
        except Exception as e:
            print(f"Response error: {e}")
    
    async def send_error(self, writer: asyncio.StreamWriter, code: int, message: str):
        """Ultra-fast error response with connection safety"""
        try:
            if writer.is_closing():
                return
                
            body = f"""<!DOCTYPE html><html><head><title>{code} {message}</title>
<style>body{{font-family:'Segoe UI',sans-serif;background:linear-gradient(135deg,#667eea,#764ba2);color:white;display:flex;align-items:center;justify-content:center;min-height:100vh;margin:0}}
.error{{text-align:center;background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);padding:60px;border-radius:20px}}
.code{{font-size:4em;margin-bottom:20px}}.msg{{font-size:1.5em}}
</style></head><body><div class="error"><div class="code">{code}</div><div class="msg">{message}</div><p>Ultra Fast IPv6 Server</p></div></body></html>"""
            
            headers = {
                'content-type': 'text/html; charset=utf-8',
                'content-length': str(len(body.encode('utf-8'))),
                'connection': 'close'
            }
            
            await self.send_response(writer, code, message, headers, body)
        except Exception:
            # If we can't send error response, just close connection
            pass

async def start_ultra_ipv6_server():
    """Start the ultra-fast IPv6 server with better error handling"""
    
    # Set up a custom exception handler to suppress connection errors
    def exception_handler(loop, context):
        exception = context.get('exception')
        if isinstance(exception, (ConnectionResetError, ConnectionAbortedError, ssl.SSLError, OSError)):
            # These are normal connection errors, don't log them
            return
        # For other exceptions, use default handling
        loop.default_exception_handler(context)
    
    # Get the current event loop and set our exception handler
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(exception_handler)
    
    # Check IPv6 support
    try:
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        sock.bind(('::1', 0))
        sock.close()
        print("✅ IPv6 support detected")
    except Exception as e:
        print(f"❌ IPv6 not supported: {e}")
        print("💡 Enable IPv6 in Windows network settings")
        return
    
    server = UltraFastIPv6Server()
    
    # Generate certificates
    try:
        server.generate_ipv6_ssl_cert()
    except Exception as e:
        print(f"❌ Certificate error: {e}")
        return
    
    http_server = None
    https_server = None
    
    try:
        # Start HTTP server (IPv6) with better error handling
        http_server = await asyncio.start_server(
            server.handle_ultra_request,
            IPV6_HOST,
            IPV6_HTTP_PORT,
            family=socket.AF_INET6,
            limit=MAX_CONNECTIONS,
            backlog=100
        )
        
        # Start HTTPS server (IPv6) with better error handling
        ssl_context = server.create_ultra_ssl_context()
        https_server = await asyncio.start_server(
            server.handle_ultra_request,
            IPV6_HOST,
            IPV6_HTTPS_PORT,
            ssl=ssl_context,
            family=socket.AF_INET6,
            limit=MAX_CONNECTIONS,
            backlog=100
        )
        
        print("🚀 ULTRA FAST IPv6 SERVER RUNNING!")
        print("=" * 50)
        print(f"🌐 HTTP:  http://[::1]:{IPV6_HTTP_PORT}")
        print(f"🔒 HTTPS: https://[::1]:{IPV6_HTTPS_PORT}")
        print(f"📊 Stats: https://[::1]:{IPV6_HTTPS_PORT}/ultra-stats")
        print(f"🔧 Info:  https://[::1]:{IPV6_HTTPS_PORT}/ultra-info")
        print(f"📁 Directory: {Path('.').resolve()}")
        print(f"⚡ {MAX_WORKERS} workers • 💾 {CACHE_SIZE//1024//1024}MB cache")
        print("🎯 Press Ctrl+C to stop")
        print("=" * 50)
        
        # Open in browser (with error handling)
        try:
            webbrowser.open(f'https://[::1]:{IPV6_HTTPS_PORT}/ultra-stats')
        except Exception:
            pass  # Browser opening is optional
        
        # Run servers with proper task management
        try:
            async with asyncio.TaskGroup() as tg:
                tg.create_task(http_server.serve_forever())
                tg.create_task(https_server.serve_forever())
        except* Exception as eg:
            for e in eg.exceptions:
                if not isinstance(e, (KeyboardInterrupt, asyncio.CancelledError)):
                    print(f"Server task error: {e}")
    
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Server startup error: {e}")
    finally:
        # Cleanup
        print("🧹 Cleaning up...")
        
        if http_server:
            http_server.close()
            try:
                await http_server.wait_closed()
            except Exception:
                pass
        
        if https_server:
            https_server.close()
            try:
                await https_server.wait_closed()
            except Exception:
                pass
        
        # Close all active connections
        for writer in list(server.connections):
            try:
                if not writer.is_closing():
                    writer.close()
                await writer.wait_closed()
            except Exception:
                pass
        
        server.executor.shutdown(wait=True)

if __name__ == '__main__':
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        sys.exit(1)
    
    print("⚡ Ultra Fast IPv6 HTTPS Server")
    print("Single file • Maximum performance • IPv6 only")
    print()
    
    try:
        asyncio.run(start_ultra_ipv6_server())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)
