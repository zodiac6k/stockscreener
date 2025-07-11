#!/usr/bin/env python3
"""
Prepare Yoga App Files for Google Colab
This script creates a ZIP file with all necessary files for building the APK
"""

import zipfile
import os
import shutil

def create_yoga_app_zip():
    """Create a ZIP file with all necessary files for Google Colab"""
    print("📦 Preparing Yoga App Files for Google Colab")
    print("=" * 50)
    
    # Files to include
    files_to_zip = [
        "main.py",
        "buildozer.spec",
        "requirements.txt"
    ]
    
    # Folders to include
    folders_to_zip = [
        "Yoga Poses",
        "yoga_music"
    ]
    
    # Create ZIP file
    zip_filename = "yoga_app_files.zip"
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add individual files
        for file in files_to_zip:
            if os.path.exists(file):
                zipf.write(file)
                print(f"✅ Added: {file}")
            else:
                print(f"❌ Missing: {file}")
        
        # Add folders
        for folder in folders_to_zip:
            if os.path.exists(folder):
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arc_name = file_path
                        zipf.write(file_path, arc_name)
                        print(f"✅ Added: {arc_name}")
            else:
                print(f"❌ Missing folder: {folder}")
    
    # Check ZIP file size
    zip_size = os.path.getsize(zip_filename) / (1024 * 1024)  # MB
    print(f"\n📦 ZIP file created: {zip_filename}")
    print(f"📏 Size: {zip_size:.1f} MB")
    
    # Verify contents
    print("\n📋 ZIP file contents:")
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        for info in zipf.infolist():
            print(f"  📄 {info.filename}")
    
    return zip_filename

def check_requirements():
    """Check if all required files exist"""
    print("\n🔍 Checking Requirements")
    print("=" * 30)
    
    required_files = [
        "main.py",
        "buildozer.spec",
        "Yoga Poses/Plank.jpg",
        "Yoga Poses/Bhujangasana.jpg",
        "Yoga Poses/Setu Bhandasana.jpg",
        "Yoga Poses/Virabhadrasana.jpg",
        "Yoga Poses/Vashistasana.jpg",
        "Yoga Poses/Bakasana.jpg",
        "Yoga Poses/Marjarasana.jpg",
        "Yoga Poses/Nvasana Pose.jpg",
        "yoga_music/Relax Music.mp3",
        "yoga_music/music_info.json"
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file}")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  Missing {len(missing_files)} files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print(f"\n🎉 All {len(required_files)} required files found!")
        return True

def show_colab_instructions():
    """Show Google Colab instructions"""
    print("\n🚀 Google Colab Instructions")
    print("=" * 40)
    print("1. Go to: https://colab.research.google.com")
    print("2. Click 'New Notebook'")
    print("3. Rename to 'Yoga App Builder'")
    print("4. Click folder icon (left sidebar)")
    print("5. Upload 'yoga_app_files.zip'")
    print("6. Follow the step-by-step guide in:")
    print("   google_colab_instructions.md")
    print("\n📱 Your APK will be ready in 10-15 minutes!")

def main():
    """Main function"""
    print("🧘‍♀️ Yoga App - Google Colab Preparation")
    print("=" * 50)
    
    # Check requirements first
    if not check_requirements():
        print("\n❌ Please fix missing files before creating ZIP")
        return
    
    # Create ZIP file
    zip_filename = create_yoga_app_zip()
    
    # Show instructions
    show_colab_instructions()
    
    print(f"\n🎯 Next Steps:")
    print(f"1. Upload {zip_filename} to Google Colab")
    print(f"2. Follow the instructions in google_colab_instructions.md")
    print(f"3. Download your APK file")
    print(f"4. Install on your Android phone")
    
    print(f"\n✅ You're ready for Google Colab!")

if __name__ == "__main__":
    main() 