#!/usr/bin/env python3
"""
Mobile App Testing Script for Yoga Belly Fat Loss App
This script helps you test the mobile app functionality
"""

import subprocess
import sys
import os
import time

def test_mobile_app():
    """Test the mobile app functionality"""
    print("🧘 Testing Yoga Belly Fat Loss Mobile App")
    print("=" * 50)
    
    # Check if main.py exists
    if not os.path.exists("main.py"):
        print("❌ Error: main.py not found!")
        print("Please make sure main.py exists in the current directory.")
        return False
    
    # Check if required packages are installed
    print("📦 Checking dependencies...")
    try:
        import kivy
        print(f"✅ Kivy version: {kivy.__version__}")
    except ImportError:
        print("❌ Kivy not installed. Run: pip install kivy")
        return False
    
    try:
        import requests
        print("✅ Requests library found")
    except ImportError:
        print("❌ Requests not installed. Run: pip install requests")
        return False
    
    # Test the app
    print("\n🚀 Starting mobile app test...")
    print("The app will open in a new window.")
    print("Please test the following features:")
    print("1. Scroll through yoga poses")
    print("2. Tap timer buttons")
    print("3. Open diet tips and workout routine")
    print("4. Close the app when done")
    
    try:
        # Run the mobile app
        process = subprocess.Popen([sys.executable, "main.py"])
        
        print("\n⏳ App is running... Press Ctrl+C to stop testing")
        
        # Wait for user to test
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Stopping app...")
        process.terminate()
        process.wait()
        print("✅ Test completed!")
        
    except Exception as e:
        print(f"❌ Error running app: {e}")
        return False
    
    return True

def check_mobile_optimization():
    """Check if the app is optimized for mobile"""
    print("\n📱 Mobile Optimization Check")
    print("=" * 30)
    
    with open("main.py", "r") as f:
        content = f.read()
    
    checks = [
        ("Touch-friendly buttons", "size_hint_y=None, height=", "Buttons have fixed height"),
        ("Responsive text", "font_size=", "Text sizing is implemented"),
        ("Mobile window size", "Window.size = (400, 700)", "Window size is set for mobile"),
        ("Scrollable content", "ScrollView", "Content is scrollable"),
        ("Popup dialogs", "Popup", "Popup dialogs are used"),
        ("Timer functionality", "Clock.schedule_interval", "Timer is implemented"),
    ]
    
    for check_name, search_term, description in checks:
        if search_term in content:
            print(f"✅ {check_name}: {description}")
        else:
            print(f"⚠️  {check_name}: Not found")
    
    print("\n📊 Mobile Readiness Score:")
    score = sum(1 for _, search_term, _ in checks if search_term in content)
    percentage = (score / len(checks)) * 100
    print(f"Score: {score}/{len(checks)} ({percentage:.1f}%)")
    
    if percentage >= 80:
        print("🎉 App is well-optimized for mobile!")
    elif percentage >= 60:
        print("👍 App has good mobile features")
    else:
        print("⚠️  App needs more mobile optimization")

def show_testing_tips():
    """Show testing tips"""
    print("\n💡 Testing Tips")
    print("=" * 20)
    print("1. Test on different screen sizes")
    print("2. Check touch responsiveness")
    print("3. Verify timer accuracy")
    print("4. Test with slow internet")
    print("5. Check battery usage")
    print("6. Test in different orientations")

def main():
    """Main testing function"""
    print("🧘‍♀️ Yoga Belly Fat Loss - Mobile Testing Suite")
    print("=" * 55)
    
    # Test the app
    if test_mobile_app():
        # Check optimization
        check_mobile_optimization()
        
        # Show tips
        show_testing_tips()
        
        print("\n🎯 Next Steps:")
        print("1. Test on actual mobile device")
        print("2. Build APK using buildozer")
        print("3. Publish to app store")
        
    else:
        print("\n❌ Testing failed. Please fix the issues above.")

if __name__ == "__main__":
    main() 