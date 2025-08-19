import http.server
import socketserver
import socket
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import webbrowser

PORT = 8001

# Custom request handler that disables caching
class NoCacheRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

# File change handler
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"\nFile {event.src_path} has been modified")
            print("Reload your browser to see changes")

def start_server():
    try:
        # Enable IPv6 support
        socketserver.TCPServer.address_family = socket.AF_INET6
        with socketserver.TCPServer(('::', PORT), NoCacheRequestHandler) as httpd:
            print(f"\nServing at http://[::1]:{PORT} (IPv6)")
            print("Press Ctrl+C to stop the server")
            
            # Open browser automatically
            webbrowser.open(f'http://[::1]:{PORT}')
            
            # Set up file watching
            event_handler = FileChangeHandler()
            observer = Observer()
            observer.schedule(event_handler, path='.', recursive=True)
            observer.start()
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                observer.stop()
                print("\nShutting down server...")
            observer.join()
            
    except OSError as e:
        if e.errno == 98:  # Port already in use
            print(f"Port {PORT} is already in use. Please choose a different port.")
            sys.exit(1)
        else:
            raise

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("Starting development server with auto-reload capability...")
    start_server()
