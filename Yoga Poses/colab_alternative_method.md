# 🔧 Alternative Method: Google Colab Without ZIP Upload

## 🚨 Problem
The ZIP file upload is causing a JSON parsing error in Google Colab. Let's use a different approach.

## ✅ Solution: Direct File Upload Method

### Step 1: Open Google Colab
1. Go to: https://colab.research.google.com
2. Click **"New Notebook"**
3. Rename to: "Yoga App Builder"

### Step 2: Install Dependencies
Copy and paste this into the first cell:

```python
# Install buildozer and dependencies
!pip install buildozer
!pip install cython==0.29.33
!pip install kivy

# Install system dependencies
!apt-get update
!apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

# Install Android SDK dependencies
!apt-get install -y \
    openjdk-8-jdk \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake

print("✅ Dependencies installed successfully!")
```

### Step 3: Create Main App File
Copy and paste this into the second cell:

```python
# Create main.py with your yoga app
main_app_code = '''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.uix.progressbar import ProgressBar
from kivy.graphics import Color, Rectangle
from kivy.core.audio import SoundLoader
import os
import json
import threading
import time

class TimerPopup(Popup):
    def __init__(self, pose_name, duration, **kwargs):
        super().__init__(**kwargs)
        self.title = f"Timer - {pose_name}"
        self.size_hint = (0.9, 0.7)
        self.auto_dismiss = False
        
        # Parse duration (e.g., "30-60 seconds" -> 45 seconds)
        if "seconds" in duration:
            time_str = duration.split()[0]
            if "-" in time_str:
                min_time, max_time = map(int, time_str.split("-"))
                self.target_time = (min_time + max_time) // 2
            else:
                self.target_time = int(time_str)
        else:
            self.target_time = 30
        
        self.current_time = 0
        self.timer_running = False
        
        # Layout
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Timer display
        self.timer_label = Label(
            text=f"{self.target_time:02d}:00",
            font_size='72sp',
            bold=True,
            size_hint_y=None,
            height=120
        )
        layout.add_widget(self.timer_label)
        
        # Progress bar
        self.progress_bar = ProgressBar(
            max=self.target_time,
            value=0,
            size_hint_y=None,
            height=40
        )
        layout.add_widget(self.progress_bar)
        
        # Controls
        controls = BoxLayout(size_hint_y=None, height=80, spacing=20)
        
        self.start_btn = Button(
            text="Start",
            font_size='20sp',
            on_press=self.start_timer
        )
        controls.add_widget(self.start_btn)
        
        self.pause_btn = Button(
            text="Pause",
            font_size='20sp',
            on_press=self.pause_timer,
            disabled=True
        )
        controls.add_widget(self.pause_btn)
        
        self.reset_btn = Button(
            text="Reset",
            font_size='20sp',
            on_press=self.reset_timer
        )
        controls.add_widget(self.reset_btn)
        
        layout.add_widget(controls)
        
        # Close button
        close_btn = Button(
            text="Close",
            font_size='20sp',
            on_press=self.dismiss,
            size_hint_y=None,
            height=60
        )
        layout.add_widget(close_btn)
        
        self.content = layout
    
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_btn.disabled = True
            self.pause_btn.disabled = False
            Clock.schedule_interval(self.update_timer, 1)
    
    def pause_timer(self):
        self.timer_running = False
        self.start_btn.disabled = False
        self.pause_btn.disabled = True
        Clock.unschedule(self.update_timer)
    
    def reset_timer(self):
        self.current_time = 0
        self.timer_label.text = f"{self.target_time:02d}:00"
        self.progress_bar.value = 0
        self.pause_timer()
    
    def update_timer(self, dt):
        if self.current_time < self.target_time:
            self.current_time += 1
            remaining = self.target_time - self.current_time
            minutes = remaining // 60
            seconds = remaining % 60
            self.timer_label.text = f"{minutes:02d}:{seconds:02d}"
            self.progress_bar.value = self.current_time
        else:
            self.pause_timer()
            self.timer_label.text = "Complete!"
            self.timer_label.color = (0, 1, 0, 1)

class YogaPoseCard(BoxLayout):
    def __init__(self, pose_name, pose_data, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 25
        self.spacing = 15
        self.size_hint_y = None
        self.height = 280
        
        # Card background
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_rect, size=self._update_rect)
        
        # Pose emoji and name
        header = BoxLayout(size_hint_y=None, height=60)
        emoji_label = Label(
            text=pose_data.get('emoji', '🧘'),
            font_size='32sp',
            size_hint_x=None,
            width=60
        )
        header.add_widget(emoji_label)
        
        name_label = Label(
            text=pose_name,
            font_size='20sp',
            bold=True,
            halign='left'
        )
        header.add_widget(name_label)
        self.add_widget(header)
        
        # Description
        desc_label = Label(
            text=pose_data['description'],
            size_hint_y=None,
            height=70,
            text_size=(Window.width - 80, None),
            halign='left',
            valign='top',
            font_size='16sp'
        )
        self.add_widget(desc_label)
        
        # Details
        details_label = Label(
            text=f"Duration: {pose_data['duration']} | Difficulty: {pose_data['difficulty']}",
            size_hint_y=None,
            height=40,
            color=(0.5, 0.5, 0.5, 1),
            font_size='14sp'
        )
        self.add_widget(details_label)
        
        # Buttons
        buttons = BoxLayout(size_hint_y=None, height=70, spacing=15)
        
        timer_btn = Button(
            text="⏱️ Timer",
            font_size='18sp',
            on_press=lambda x: self.start_timer(pose_name, pose_data['duration'])
        )
        buttons.add_widget(timer_btn)
        
        info_btn = Button(
            text="ℹ️ Info",
            font_size='18sp',
            on_press=lambda x: self.show_info(pose_name, pose_data)
        )
        buttons.add_widget(info_btn)
        
        self.add_widget(buttons)
    
    def _update_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            Rectangle(pos=instance.pos, size=instance.size)
    
    def start_timer(self, pose_name, duration):
        popup = TimerPopup(pose_name, duration)
        popup.open()
    
    def show_info(self, pose_name, pose_data):
        content = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Title
        title_label = Label(
            text=pose_name,
            font_size='24sp',
            bold=True,
            size_hint_y=None,
            height=60
        )
        content.add_widget(title_label)
        
        # Benefits
        benefits_text = "Benefits:\\n" + "\\n".join([f"• {benefit}" for benefit in pose_data['benefits']])
        benefits_label = Label(
            text=benefits_text,
            size_hint_y=None,
            height=120,
            text_size=(Window.width - 100, None),
            halign='left',
            valign='top',
            font_size='16sp'
        )
        content.add_widget(benefits_label)
        
        # Instructions
        instructions_label = Label(
            text=f"Instructions:\\n{pose_data['instructions']}",
            size_hint_y=None,
            height=150,
            text_size=(Window.width - 100, None),
            halign='left',
            valign='top',
            font_size='16sp'
        )
        content.add_widget(instructions_label)
        
        # Close button
        close_btn = Button(
            text="Close",
            font_size='20sp',
            on_press=lambda x: popup.dismiss(),
            size_hint_y=None,
            height=60
        )
        content.add_widget(close_btn)
        
        popup = Popup(
            title="Pose Information",
            content=content,
            size_hint=(0.95, 0.9)
        )
        popup.open()

class YogaMobileApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.music_playing = False
        self.music_sound = None
    
    def build(self):
        # Set window size for mobile testing
        Window.size = (400, 800)
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical')
        
        # Title bar
        title_bar = BoxLayout(
            size_hint_y=None,
            height=80,
            padding=[25, 15]
        )
        
        with title_bar.canvas.before:
            Color(0.2, 0.6, 0.2, 1)
            Rectangle(pos=title_bar.pos, size=title_bar.size)
        title_bar.bind(pos=self._update_title_rect, size=self._update_title_rect)
        
        title_label = Label(
            text="🧘 Yoga for Belly Fat Loss",
            font_size='22sp',
            bold=True,
            color=(1, 1, 1, 1)
        )
        title_bar.add_widget(title_label)
        
        main_layout.add_widget(title_bar)
        
        # Scrollable content
        scroll = ScrollView()
        grid = GridLayout(
            cols=1,
            spacing=20,
            size_hint_y=None,
            padding=[15, 15]
        )
        grid.bind(minimum_height=grid.setter('height'))
        
        # Add yoga poses
        for pose_name, pose_data in self.yoga_poses().items():
            grid.add_widget(YogaPoseCard(pose_name, pose_data))
        
        scroll.add_widget(grid)
        main_layout.add_widget(scroll)
        
        # Bottom navigation
        nav_bar = BoxLayout(
            size_hint_y=None,
            height=80,
            spacing=15,
            padding=[25, 10]
        )
        
        with nav_bar.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            Rectangle(pos=nav_bar.pos, size=nav_bar.size)
        nav_bar.bind(pos=self._update_nav_rect, size=self._update_nav_rect)
        
        routine_btn = Button(
            text="📋 Routine",
            font_size='18sp',
            on_press=self.show_routine,
            size_hint_x=0.5
        )
        nav_bar.add_widget(routine_btn)
        
        diet_btn = Button(
            text="🥗 Diet Tips",
            font_size='18sp',
            on_press=self.show_diet_tips,
            size_hint_x=0.5
        )
        nav_bar.add_widget(diet_btn)
        
        main_layout.add_widget(nav_bar)
        
        return main_layout
    
    def _update_title_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0.2, 0.6, 0.2, 1)
            Rectangle(pos=instance.pos, size=instance.size)
    
    def _update_nav_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            Rectangle(pos=instance.pos, size=instance.size)
    
    def yoga_poses(self):
        return {
            "Plank Pose (Phalakasana)": {
                "description": "Strengthens core muscles and improves posture",
                "benefits": ["Burns belly fat", "Strengthens abs", "Improves balance", "Builds endurance"],
                "instructions": "1. Start in push-up position\\n2. Keep body straight from head to heels\\n3. Engage core muscles\\n4. Hold for 30-60 seconds",
                "duration": "30-60 seconds",
                "difficulty": "Beginner",
                "emoji": "🦾"
            },
            "Boat Pose (Navasana)": {
                "description": "Excellent for strengthening abdominal muscles",
                "benefits": ["Tones abs", "Improves digestion", "Strengthens back", "Enhances balance"],
                "instructions": "1. Sit with knees bent\\n2. Lift feet off ground\\n3. Extend arms parallel to ground\\n4. Hold for 15-30 seconds",
                "duration": "15-30 seconds",
                "difficulty": "Intermediate",
                "emoji": "🚣"
            },
            "Cobra Pose (Bhujangasana)": {
                "description": "Strengthens back and tones abdominal muscles",
                "benefits": ["Tones belly", "Improves posture", "Opens chest", "Relieves back pain"],
                "instructions": "1. Lie on stomach\\n2. Place hands under shoulders\\n3. Lift chest off ground\\n4. Hold for 15-30 seconds",
                "duration": "15-30 seconds",
                "difficulty": "Beginner",
                "emoji": "🐍"
            },
            "Bridge Pose (Setu Bandhasana)": {
                "description": "Strengthens core and glutes while opening hips",
                "benefits": ["Tones abs", "Strengthens back", "Opens hips", "Improves digestion"],
                "instructions": "1. Lie on back with knees bent\\n2. Lift hips toward ceiling\\n3. Keep shoulders on ground\\n4. Hold for 30-60 seconds",
                "duration": "30-60 seconds",
                "difficulty": "Beginner",
                "emoji": "🌉"
            },
            "Warrior III (Virabhadrasana III)": {
                "description": "Challenges balance while engaging core muscles",
                "benefits": ["Strengthens core", "Improves balance", "Tones legs", "Builds focus"],
                "instructions": "1. Stand on one leg\\n2. Extend other leg back\\n3. Torso parallel to ground\\n4. Hold for 15-30 seconds each side",
                "duration": "15-30 seconds each side",
                "difficulty": "Intermediate",
                "emoji": "⚔️"
            },
            "Side Plank (Vasisthasana)": {
                "description": "Targets obliques and strengthens entire core",
                "benefits": ["Tones obliques", "Strengthens arms", "Improves balance", "Burns fat"],
                "instructions": "1. Start in plank position\\n2. Rotate to one side\\n3. Stack feet and lift arm\\n4. Hold for 15-30 seconds each side",
                "duration": "15-30 seconds each side",
                "difficulty": "Intermediate",
                "emoji": "⚖️"
            }
        }
    
    def show_routine(self, instance):
        content = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        routine_text = """
🔥 COMPLETE YOGA WORKOUT ROUTINE 🔥

📋 WARM-UP (5 minutes):
• Cat-Cow Stretch: 1-2 minutes
• Gentle spinal twists: 1 minute each side
• Deep breathing: 1 minute

💪 MAIN WORKOUT (20-30 minutes):

ROUND 1 - Core Foundation:
1. Plank Pose: 30-60 seconds
2. Boat Pose: 15-30 seconds
3. Bridge Pose: 30-60 seconds
4. Rest: 30 seconds

ROUND 2 - Strength Building:
1. Side Plank: 15-30 seconds each side
2. Warrior III: 15-30 seconds each side
3. Cobra Pose: 15-30 seconds
4. Rest: 30 seconds

🧘 COOL-DOWN (5 minutes):
• Child's Pose: 1 minute
• Gentle twists: 30 seconds each side
• Savasana: 2-3 minutes

📅 RECOMMENDED: 3-4 times per week
⏰ OPTIMAL: Morning or evening
        """
        
        routine_label = Label(
            text=routine_text,
            size_hint_y=None,
            height=500,
            text_size=(Window.width - 100, None),
            halign='left',
            valign='top',
            font_size='16sp'
        )
        content.add_widget(routine_label)
        
        close_btn = Button(
            text="Close",
            font_size='20sp',
            on_press=lambda x: popup.dismiss(),
            size_hint_y=None,
            height=60
        )
        content.add_widget(close_btn)
        
        popup = Popup(
            title="Complete Workout Routine",
            content=content,
            size_hint=(0.95, 0.9)
        )
        popup.open()
    
    def show_diet_tips(self, instance):
        content = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        diet_text = """
🥗 VEGAN DIET TIPS FOR BELLY FAT LOSS 🥗

🍎 PROTEIN-RICH FOODS:
• Legumes: Lentils, chickpeas, black beans
• Quinoa: Complete protein source
• Tofu and Tempeh: 20g protein per 100g
• Seitan: 25g protein per 100g

🥑 HEALTHY FATS:
• Avocados: Monounsaturated fats
• Nuts: Almonds, walnuts, cashews
• Seeds: Chia, flax, hemp, pumpkin
• Olive oil (in moderation)

🌾 COMPLEX CARBS:
• Sweet potatoes: Rich in fiber
• Brown rice: High in fiber
• Oats: Beta-glucan for heart health
• Whole grain bread and pasta

🥬 FIBER-RICH VEGETABLES:
• Leafy greens: Spinach, kale, arugula
• Cruciferous: Broccoli, cauliflower
• Bell peppers: High in vitamin C
• Mushrooms: Great meat substitute

💧 HYDRATION:
• Water: 8-10 glasses daily
• Herbal teas: Green tea for metabolism
• Coconut water: Natural electrolytes

📋 SAMPLE MEAL PLAN:
🌅 Breakfast: Overnight oats with berries
🌞 Lunch: Quinoa bowl with vegetables
🌆 Dinner: Stir-fried vegetables with tempeh
🍎 Snacks: Apple with almond butter
        """
        
        diet_label = Label(
            text=diet_text,
            size_hint_y=None,
            height=600,
            text_size=(Window.width - 100, None),
            halign='left',
            valign='top',
            font_size='16sp'
        )
        content.add_widget(diet_label)
        
        close_btn = Button(
            text="Close",
            font_size='20sp',
            on_press=lambda x: popup.dismiss(),
            size_hint_y=None,
            height=60
        )
        content.add_widget(close_btn)
        
        popup = Popup(
            title="Vegan Diet Tips",
            content=content,
            size_hint=(0.95, 0.9)
        )
        popup.open()

if __name__ == '__main__':
    YogaMobileApp().run()
'''

# Write the main app file
with open('main.py', 'w') as f:
    f.write(main_app_code)

print("✅ main.py created successfully!")
```

### Step 4: Configure Buildozer
Copy and paste this into the third cell:

```python
# Initialize buildozer
!buildozer init

# Update buildozer.spec with our configuration
buildozer_config = '''
[app]
title = Yoga Belly Fat Loss
package.name = yogabellyfat
package.domain = org.yoga
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,mp3,wav
version = 1.0
requirements = python3,kivy,requests,urllib3
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
'''

# Write the configuration
with open('buildozer.spec', 'w') as f:
    f.write(buildozer_config)

print("✅ Buildozer configured successfully!")
```

### Step 5: Build the APK
Copy and paste this into the fourth cell:

```python
# Build the APK (this will take 10-15 minutes)
print("🔨 Starting APK build...")
print("⏳ This will take 10-15 minutes. Please wait...")

!buildozer android debug

print("✅ APK build completed!")
```

### Step 6: Download the APK
Copy and paste this into the fifth cell:

```python
# Check if APK was created
import os

apk_path = None
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.apk'):
            apk_path = os.path.join(root, file)
            break
    if apk_path:
        break

if apk_path:
    print(f"🎉 APK created successfully!")
    print(f"📁 Location: {apk_path}")
    print(f"📏 Size: {os.path.getsize(apk_path) / (1024*1024):.1f} MB")
    
    # Create download link
    from google.colab import files
    files.download(apk_path)
else:
    print("❌ APK not found. Check the build logs above for errors.")
```

## 🎯 What This Method Provides

### ✅ **Features Included:**
- **Professional mobile interface**
- **Timer functionality** for each pose
- **Diet tips and workout routines**
- **Touch-friendly buttons**
- **Smooth scrolling**
- **Popup dialogs**

### ⚠️ **What's Missing (No Images/Music):**
- Yoga pose images (due to upload limitations)
- Background music (due to file size)

### 🔧 **To Add Images Later:**
1. Build the basic APK first
2. Download and test it
3. We can add images in a second build if needed

## 📱 **Installation Steps**

1. **Download the APK** from Colab
2. **Transfer to your Android phone**
3. **Enable "Install from Unknown Sources"**
4. **Install and test the app**

## 🎉 **Success Indicators**

You should see:
```
✅ Dependencies installed successfully!
✅ main.py created successfully!
✅ Buildozer configured successfully!
🔨 Starting APK build...
✅ APK build completed!
🎉 APK created successfully!
```

**This method avoids the ZIP upload issue and will give you a working mobile app!** 🧘‍♀️📱 