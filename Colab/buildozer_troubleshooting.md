# 🔧 Buildozer Troubleshooting Guide

## 🚨 Common Issues & Solutions

### Issue 1: Buildozer Fails to Start
**Symptoms:** Buildozer command not found or fails immediately

**Solutions:**
```bash
# Reinstall buildozer
!pip uninstall buildozer -y
!pip install buildozer

# Install system dependencies
!apt-get update
!apt-get install -y python3-pip build-essential git python3 python3-dev
!apt-get install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
!apt-get install -y libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
!apt-get install -y zlib1g-dev openjdk-8-jdk autoconf libtool pkg-config
```

### Issue 2: Java/Android SDK Issues
**Symptoms:** Java not found, Android SDK errors

**Solutions:**
```bash
# Install Java 8
!apt-get install -y openjdk-8-jdk

# Set JAVA_HOME
import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-8-openjdk-amd64'

# Verify Java installation
!java -version
```

### Issue 3: Cython Version Conflicts
**Symptoms:** Cython compilation errors

**Solutions:**
```bash
# Install specific Cython version
!pip install cython==0.29.33

# Or try latest version
!pip install --upgrade cython
```

### Issue 4: Memory Issues
**Symptoms:** Build fails due to insufficient memory

**Solutions:**
```bash
# Check available memory
!free -h

# Use swap if needed
!fallocate -l 2G /swapfile
!chmod 600 /swapfile
!mkswap /swapfile
!swapon /swapfile
```

### Issue 5: Network/Download Issues
**Symptoms:** Failed to download Android SDK or NDK

**Solutions:**
```bash
# Clear buildozer cache
!rm -rf .buildozer

# Try with different mirrors
# Add to buildozer.spec:
# android.sdk_url = https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip
```

## 🛠️ Alternative Build Methods

### Method 1: Use Pre-built Docker Image
```bash
# Pull buildozer Docker image
!docker pull kivy/buildozer

# Run build in container
!docker run --volume "$HOME/.buildozer":/home/user/.buildozer \
    --volume "$PWD":/home/user/hostcwd \
    kivy/buildozer --workdir /home/user/hostcwd android debug
```

### Method 2: Use GitHub Actions
Create `.github/workflows/build.yml`:
```yaml
name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Build APK
      uses: ArtemSBulgakov/buildozer-action@v1
      with:
        command: android debug
```

### Method 3: Use Local Build (Windows WSL)
```bash
# Install WSL2
wsl --install

# Install Ubuntu
wsl --install -d Ubuntu

# In WSL, install buildozer
sudo apt update
sudo apt install -y python3-pip build-essential git python3 python3-dev
pip3 install buildozer
```

## 📋 Minimal Working Configuration

### Simple buildozer.spec
```ini
[app]
title = Yoga App
package.name = yogaapp
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
```

### Minimal main.py
```python
from kivy.app import App
from kivy.uix.button import Button

class YogaApp(App):
    def build(self):
        return Button(text='Hello Yoga!')

if __name__ == '__main__':
    YogaApp().run()
```

## 🔍 Debugging Steps

### Step 1: Check Buildozer Logs
```bash
# View buildozer logs
!cat .buildozer/android/platform/build-*/build/outputs/logs/buildozer.log

# Check for specific errors
!grep -i error .buildozer/android/platform/build-*/build/outputs/logs/buildozer.log
```

### Step 2: Verify Dependencies
```bash
# Check Python version
!python3 --version

# Check pip packages
!pip list | grep -E "(kivy|buildozer|cython)"

# Check system packages
!dpkg -l | grep -E "(openjdk|android|sdk)"
```

### Step 3: Test Minimal Build
```bash
# Create minimal test
echo 'from kivy.app import App; from kivy.uix.button import Button; class TestApp(App): def build(self): return Button(text="Test"); TestApp().run()' > test.py

# Try building minimal app
!buildozer android debug
```

## 🎯 Success Indicators

### ✅ Good Signs:
- Buildozer starts without errors
- Java version shows correctly
- Android SDK downloads successfully
- Cython compiles without warnings
- APK file is created in `bin/` directory

### ❌ Bad Signs:
- Java not found errors
- Network timeout errors
- Memory allocation failures
- Cython compilation errors
- Missing APK file

## 🚀 Quick Fix Commands

### Reset Everything:
```bash
# Clean buildozer
!rm -rf .buildozer

# Reinstall buildozer
!pip uninstall buildozer -y
!pip install buildozer

# Reinstall system dependencies
!apt-get update
!apt-get install -y python3-pip build-essential git python3 python3-dev libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev openjdk-8-jdk autoconf libtool pkg-config libncurses5-dev libncursesw5-dev libtinfo5 cmake

# Try build again
!buildozer android debug
```

### Use Different Python Version:
```bash
# Try Python 3.9
!apt-get install -y python3.9 python3.9-dev
!python3.9 -m pip install buildozer
!python3.9 -m buildozer android debug
```

## 📞 Getting Help

### If Still Failing:
1. **Check the exact error message**
2. **Try the minimal configuration above**
3. **Use a different Colab runtime** (Runtime → Change runtime type)
4. **Try a different buildozer version**
5. **Consider using a pre-built APK template**

### Useful Resources:
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Kivy Android Guide](https://kivy.org/doc/stable/installation/installation-android.html)
- [Buildozer GitHub Issues](https://github.com/kivy/buildozer/issues)

## 🎉 Success Checklist

- [ ] Buildozer installs without errors
- [ ] Java 8 is installed and working
- [ ] Android SDK downloads successfully
- [ ] Cython compiles without issues
- [ ] APK file is created
- [ ] APK installs on Android device
- [ ] App launches without crashes

**Remember: Sometimes it takes a few tries to get the build working. Don't give up!** 🧘‍♀️📱 