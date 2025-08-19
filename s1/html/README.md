# Notes Web Server Setup Guide

## 🚀 Quick Start

### 1. Start the Service
**Double-click:** `start-notes-server.bat`

This will:
- ✅ Update directory listings automatically
- 🌐 Start a web server on port 8000
- 📱 Show you URLs for local and mobile access
- 🔍 Display your IP address for remote access

### 2. Access Your Notes

**On Same Computer:**
```
http://localhost:8000/1.html
```

**From Mobile/Other Devices:**
```
http://[YOUR_IP]:8000/1.html
```
(The script will show your actual IP address)

### 3. Stop the Service
- **Option 1:** Press `Ctrl+C` in the server window
- **Option 2:** Double-click `stop-notes-server.bat`
- **Option 3:** Close the server window

## 📋 What You Need

### Prerequisites:
- ✅ **Python** (version 3.6 or higher)
  - Check: Run `python --version` in Command Prompt
  - Download: https://python.org/downloads/

### Optional (Backup):
- 🟡 **Node.js** (if Python fails)
  - Download: https://nodejs.org/

## 🔧 Manual Setup (Advanced)

If the batch file doesn't work, you can run commands manually:

```batch
# 1. Update directory listings
cd "d:\my\Whiteboards\study\notes\html"
python generate-directory-listing.py

# 2. Start web server
python -m http.server 8000

# 3. Open browser to:
http://localhost:8000/1.html
```

## 🌐 Network Access

### For Mobile Access:
1. **Connect mobile to same WiFi network**
2. **Use the IP address shown by the server**
3. **Make sure Windows Firewall allows Python**

### Firewall Setup:
- Go to Windows Defender Firewall
- Allow Python through firewall
- Or temporarily disable firewall for testing

## 🔄 When You Add New Files

The server automatically updates directory listings when you start it. If you add files while the server is running:

1. **Stop the server** (Ctrl+C)
2. **Restart:** Double-click `start-notes-server.bat`
3. **Or use the refresh button (🔄)** in the browser

## 📱 Mobile-Friendly Features

- ✅ Responsive design
- ✅ Touch-friendly buttons
- ✅ Folder navigation
- ✅ File browser with refresh
- ✅ MathJax support
- ✅ Markdown rendering

## 🐛 Troubleshooting

### "Python not found"
- Install Python from python.org
- Add Python to PATH during installation

### "Port 8000 already in use"
- Stop other services using port 8000
- Or change port in the batch file (edit 8000 to 8080, etc.)

### "Can't access from mobile"
- Check if both devices are on same WiFi
- Disable Windows Firewall temporarily
- Try different port (8080, 3000, etc.)

### "No folders showing"
- Restart the server (it auto-updates listings)
- Check if `directory-listing.json` files exist
- Refresh browser and click 🔄 button

## 📂 File Structure

```
html/
├── 1.html                    # Main page
├── 1.css                     # Styles
├── 1.md                      # Default markdown
├── start-notes-server.bat    # 🚀 START SERVICE
├── stop-notes-server.bat     # 🛑 Stop service
├── QUICK-START.bat          # � One-click start
├── generate-directory-listing.py  # Directory scanner
└── README.md                 # This guide
```
