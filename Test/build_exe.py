import os
import subprocess
import sys

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller is already installed.")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully!")

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable...")
    
    # PyInstaller command with optimizations
    cmd = [
        "pyinstaller",
        "--onefile",  # Create a single executable file
        "--windowed",  # Don't show console window
        "--name=YogaBellyFatProgram",  # Name of the executable
        "--icon=icon.ico",  # Icon file (if you have one)
        "--add-data=requirements.txt;.",  # Include requirements file
        "--hidden-import=PIL._tkinter_finder",  # Include PIL dependencies
        "--hidden-import=pygame",  # Include pygame
        "--hidden-import=requests",  # Include requests
        "--hidden-import=urllib3",  # Include urllib3
        "--hidden-import=tkinter",  # Include tkinter
        "--hidden-import=tkinter.ttk",  # Include ttk
        "--hidden-import=tkinter.messagebox",  # Include messagebox
        "yoga_belly_fat_program.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executable built successfully!")
        print("📁 Check the 'dist' folder for your executable file.")
        print("📄 File name: YogaBellyFatProgram.exe")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error building executable: {e}")
        return False
    
    return True

def create_icon():
    """Create a simple icon file if it doesn't exist"""
    if not os.path.exists("icon.ico"):
        print("Creating a simple icon file...")
        try:
            from PIL import Image, ImageDraw
            
            # Create a simple yoga icon
            img = Image.new('RGBA', (256, 256), (240, 248, 255, 255))
            draw = ImageDraw.Draw(img)
            
            # Draw a simple yoga pose symbol
            draw.ellipse([80, 60, 176, 156], fill=(44, 85, 48, 255))  # Head
            draw.rectangle([120, 156, 136, 220], fill=(44, 85, 48, 255))  # Body
            draw.ellipse([100, 220, 156, 240], fill=(44, 85, 48, 255))  # Base
            
            # Save as ICO
            img.save("icon.ico", format='ICO')
            print("✅ Icon created successfully!")
        except Exception as e:
            print(f"⚠️ Could not create icon: {e}")
            print("Continuing without custom icon...")

def main():
    print("🚀 Yoga Belly Fat Program - Executable Builder")
    print("=" * 50)
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Create icon
    create_icon()
    
    # Build executable
    if build_executable():
        print("\n🎉 Build completed successfully!")
        print("\n📋 Next steps:")
        print("1. Find your executable in the 'dist' folder")
        print("2. Test it on another computer")
        print("3. Share the .exe file with others")
        print("\n💡 Tips:")
        print("- The executable might take a few seconds to start")
        print("- Make sure the target computer has internet for web images")
        print("- The file size will be larger than the Python script")
    else:
        print("\n❌ Build failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 