#!/usr/bin/env python3
"""
Dynamic Directory Listing Generator
Scans the notesob directory and generates JSON files for each subdirectory
that the browser can fetch to discover files and folders dynamically.
"""

import os
import json
import sys
from pathlib import Path

def scan_directory(directory_path):
    """Scan a directory and return files and folders."""
    try:
        path = Path(directory_path)
        if not path.exists():
            return {"files": [], "folders": [], "error": "Directory not found"}
        
        files = []
        folders = []
        
        for item in path.iterdir():
            if item.is_file():
                files.append(item.name)
            elif item.is_dir():
                folders.append(item.name)
        
        return {
            "files": sorted(files),
            "folders": sorted(folders),
            "path": str(path),
            "last_updated": str(path.stat().st_mtime) if path.exists() else None
        }
    
    except Exception as e:
        return {"files": [], "folders": [], "error": str(e)}

def generate_listings_recursively(base_path, max_depth=5, current_depth=0):
    """Generate directory listings recursively."""
    if current_depth > max_depth:
        return
    
    base_path = Path(base_path)
    
    # Generate listing for current directory
    listing = scan_directory(base_path)
    listing_file = base_path / "directory-listing.json"  # Changed from .directory-listing.json
    
    try:
        with open(listing_file, 'w', encoding='utf-8') as f:
            json.dump(listing, f, indent=2, ensure_ascii=False)
        print(f"✅ Generated: {listing_file}")
    except Exception as e:
        print(f"❌ Error generating {listing_file}: {e}")
    
    # Recursively generate for subdirectories
    for folder in listing.get("folders", []):
        subfolder_path = base_path / folder
        if subfolder_path.is_dir():
            generate_listings_recursively(subfolder_path, max_depth, current_depth + 1)

def main():
    # Base directory to scan (relative to this script)
    script_dir = Path(__file__).parent
    notesob_path = script_dir.parent / "notesob"
    
    if len(sys.argv) > 1:
        notesob_path = Path(sys.argv[1])
    
    print(f"🔍 Scanning directory: {notesob_path.absolute()}")
    
    if not notesob_path.exists():
        print(f"❌ Directory not found: {notesob_path}")
        print("Usage: python generate-directory-listing.py [path_to_notesob]")
        return
    
    print("🚀 Generating directory listings...")
    generate_listings_recursively(notesob_path)
    print("✨ Done! Directory listings generated.")
    print("\n📝 Note: Re-run this script whenever you add/remove files or folders.")

if __name__ == "__main__":
    main()
