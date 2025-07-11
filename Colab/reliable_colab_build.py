# Reliable Google Colab Build for Yoga App
# Copy this entire script into ONE cell in Google Colab

import os
import subprocess
import time

print("🧘‍♀️ Reliable Yoga App Builder for Google Colab")
print("=" * 55)

# Step 1: Clean environment and install dependencies
print("🧹 Cleaning environment...")
!rm -rf .buildozer
!rm -rf buildozer.spec

print("📦 Installing dependencies...")
!pip install --upgrade pip
!pip install buildozer
!pip install cython==0.29.33
!pip install kivy

# Install system packages
print("🔧 Installing system packages...")
!apt-get update -qq
!apt-get install -y -qq python3-pip build-essential git python3 python3-dev
!apt-get install -y -qq libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
!apt-get install -y -qq libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
!apt-get install -y -qq zlib1g-dev openjdk-8-jdk autoconf libtool pkg-config
!apt-get install -y -qq libncurses5-dev libncursesw5-dev libtinfo5 cmake

print("✅ Dependencies installed!")

# Step 2: Set environment variables
print("🔧 Setting environment variables...")
import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-8-openjdk-amd64'
os.environ['ANDROID_HOME'] = '/root/.buildozer/android/platform/android-sdk'
os.environ['ANDROID_NDK_HOME'] = '/root/.buildozer/android/platform/android-ndk'

# Verify Java installation
print("☕ Checking Java installation...")
!java -version

# Step 3: Create minimal main.py
print("📝 Creating minimal main.py...")
main_code = '''from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class YogaApp(App):
    def build(self):
        # Set window size for mobile
        Window.size = (400, 800)
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical')
        
        # Title
        title = Label(
            text="🧘 Yoga for Belly Fat Loss",
            font_size='24sp',
            bold=True,
            size_hint_y=None,
            height=80
        )
        main_layout.add_widget(title)
        
        # Scrollable content
        scroll = ScrollView()
        grid = GridLayout(
            cols=1,
            spacing=20,
            size_hint_y=None,
            padding=[20, 20]
        )
        grid.bind(minimum_height=grid.setter('height'))
        
        # Add yoga poses
        poses = [
            ("Plank Pose", "🦾", "30-60 seconds", "Beginner"),
            ("Boat Pose", "🚣", "15-30 seconds", "Intermediate"),
            ("Cobra Pose", "🐍", "15-30 seconds", "Beginner"),
            ("Bridge Pose", "🌉", "30-60 seconds", "Beginner"),
            ("Warrior III", "⚔️", "15-30 seconds", "Intermediate"),
            ("Side Plank", "⚖️", "15-30 seconds", "Intermediate")
        ]
        
        for pose_name, emoji, duration, difficulty in poses:
            pose_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=150)
            
            # Pose header
            header = BoxLayout(size_hint_y=None, height=50)
            header.add_widget(Label(text=emoji, font_size='24sp'))
            header.add_widget(Label(text=pose_name, font_size='18sp', bold=True))
            pose_layout.add_widget(header)
            
            # Pose details
            pose_layout.add_widget(Label(
                text=f"Duration: {duration} | Difficulty: {difficulty}",
                size_hint_y=None,
                height=30
            ))
            
            # Timer button
            timer_btn = Button(
                text="⏱️ Start Timer",
                size_hint_y=None,
                height=50,
                on_press=lambda x, name=pose_name: self.show_timer(name)
            )
            pose_layout.add_widget(timer_btn)
            
            grid.add_widget(pose_layout)
        
        scroll.add_widget(grid)
        main_layout.add_widget(scroll)
        
        # Bottom button
        bottom_btn = Button(
            text="🥗 Diet Tips",
            size_hint_y=None,
            height=60,
            on_press=self.show_diet_tips
        )
        main_layout.add_widget(bottom_btn)
        
        return main_layout
    
    def show_timer(self, pose_name):
        from kivy.uix.popup import Popup
        from kivy.uix.button import Button
        from kivy.uix.label import Label
        
        content = BoxLayout(orientation='vertical', padding=20)
        content.add_widget(Label(text=f"Timer for {pose_name}", font_size='20sp'))
        content.add_widget(Label(text="⏱️ 30 seconds", font_size='48sp', bold=True))
        content.add_widget(Button(text="Close", on_press=lambda x: popup.dismiss()))
        
        popup = Popup(title="Timer", content=content, size_hint=(0.8, 0.6))
        popup.open()
    
    def show_diet_tips(self, instance):
        from kivy.uix.popup import Popup
        from kivy.uix.button import Button
        from kivy.uix.label import Label
        
        content = BoxLayout(orientation='vertical', padding=20)
        content.add_widget(Label(
            text="🥗 Vegan Diet Tips\\n\\n• Eat more protein\\n• Include healthy fats\\n• Stay hydrated\\n• Exercise regularly",
            font_size='16sp'
        ))
        content.add_widget(Button(text="Close", on_press=lambda x: popup.dismiss()))
        
        popup = Popup(title="Diet Tips", content=content, size_hint=(0.9, 0.8))
        popup.open()

if __name__ == '__main__':
    YogaApp().run()
'''

with open('main.py', 'w') as f:
    f.write(main_code)

print("✅ main.py created successfully!")

# Step 4: Initialize buildozer
print("🔧 Initializing buildozer...")
!buildozer init

# Step 5: Create optimized buildozer.spec
print("📝 Creating optimized buildozer.spec...")
buildozer_config = '''[app]
title = Yoga Belly Fat Loss
package.name = yogabellyfat
package.domain = org.yoga
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,mp3,wav
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = android.permission.INTERNET
android.api = 31
android.minapi = 21
android.ndk = 23b
android.ndk_api = 21
android.private_storage = True
android.accept_sdk_license = True
android.allow_backup = True
android.logcat_filters = *:S python:D
android.arch = arm64-v8a
android.allow_newer_versions = True
android.skip_update = False
android.auto_accept_sdk_license = True
'''

with open('buildozer.spec', 'w') as f:
    f.write(buildozer_config)

print("✅ buildozer.spec created successfully!")

# Step 6: Check available memory
print("💾 Checking available memory...")
!free -h

# Step 7: Build APK with detailed logging
print("🔨 Starting APK build...")
print("⏳ This will take 10-15 minutes. Please wait...")
print("📋 Build progress will be shown below...")

# Start build with verbose output
!buildozer -v android debug

print("✅ APK build completed!")

# Step 8: Find and download APK
print("📱 Looking for APK file...")
import os

# Check multiple possible locations
possible_paths = [
    'bin/',
    '.buildozer/android/platform/build-*/build/outputs/apk/debug/',
    '.buildozer/android/platform/build-*/build/outputs/apk/',
    '.buildozer/android/platform/build-*/build/outputs/',
    '.buildozer/android/platform/build-*/build/',
    '.buildozer/android/platform/build-*/',
    '.buildozer/android/platform/',
    '.buildozer/android/',
    '.buildozer/'
]

apk_path = None
for path in possible_paths:
    try:
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.apk'):
                    apk_path = os.path.join(root, file)
                    break
            if apk_path:
                break
        if apk_path:
            break
    except:
        continue

if apk_path:
    print(f"🎉 APK created successfully!")
    print(f"📁 Location: {apk_path}")
    print(f"📏 Size: {os.path.getsize(apk_path) / (1024*1024):.1f} MB")
    
    # Create download link
    from google.colab import files
    files.download(apk_path)
else:
    print("❌ APK not found. Checking buildozer logs...")
    
    # Check buildozer logs
    try:
        !find .buildozer -name "*.log" -exec echo "=== {} ===" \; -exec head -20 {} \;
    except:
        print("No log files found")
    
    # Check buildozer directory structure
    print("📁 Checking buildozer directory structure...")
    !find .buildozer -type d | head -20
    
    # Check for any APK files anywhere
    print("🔍 Searching for any APK files...")
    !find . -name "*.apk" 2>/dev/null || echo "No APK files found"
    
    print("\\n💡 Troubleshooting tips:")
    print("1. Check the build output above for errors")
    print("2. Try running the build again")
    print("3. Check if you have enough memory (need ~4GB)")
    print("4. Try using a different Colab runtime")
    print("5. Consider using an online APK builder")

print("\\n🎯 Next steps:")
print("1. If APK was created, download and install on your phone")
print("2. If build failed, check the error messages above")
print("3. Try the troubleshooting guide in buildozer_troubleshooting.md") 