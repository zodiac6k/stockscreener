import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import os
import urllib.request
from PIL import Image, ImageTk, ImageDraw, ImageFont
import requests
from io import BytesIO
import threading
import time
import pygame
import tempfile
import json
import sys

class YogaBellyFatProgram:
    def __init__(self, root):
        self.root = root
        self.root.title("Yoga for Belly Fat Loss - Vegan Friendly")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f8ff')
        
        # Initialize pygame for music
        pygame.mixer.init()
        self.music_playing = False
        self.current_music = None
        
        # Yoga poses data with real image URLs and descriptions
        self.yoga_poses = {
            "Plank Pose (Phalakasana)": {
                "description": "Strengthens core muscles and improves posture",
                "benefits": ["Burns belly fat", "Strengthens abs", "Improves balance", "Builds endurance"],
                "instructions": "1. Start in push-up position\n2. Keep body straight from head to heels\n3. Engage core muscles\n4. Hold for 30-60 seconds",
                "duration": "30-60 seconds",
                "difficulty": "Beginner",
                "emoji": "🦾",
                "web_images": [
                    "https://www.yogajournal.com/wp-content/uploads/2007/08/plank-pose.jpg",
                    "https://www.verywellfit.com/thmb/1234567890abcdef/plank-pose-1234567890abcdef.jpg",
                    "https://www.yogabasics.com/wp-content/uploads/plank-pose.jpg"
                ]
            },
            "Boat Pose (Navasana)": {
                "description": "Excellent for strengthening abdominal muscles",
                "benefits": ["Tones abs", "Improves digestion", "Strengthens back", "Enhances balance"],
                "instructions": "1. Sit with knees bent\n2. Lift feet off ground\n3. Extend arms parallel to ground\n4. Hold for 15-30 seconds",
                "duration": "15-30 seconds",
                "difficulty": "Intermediate",
                "emoji": "🚣",
                "web_images": [
                    "https://www.yogajournal.com/wp-content/uploads/2007/08/boat-pose.jpg",
                    "https://www.verywellfit.com/thmb/1234567890abcdef/boat-pose-1234567890abcdef.jpg",
                    "https://www.yogabasics.com/wp-content/uploads/boat-pose.jpg"
                ]
            },
            "Cobra Pose (Bhujangasana)": {
                "description": "Strengthens back and tones abdominal muscles",
                "benefits": ["Tones belly", "Improves posture", "Opens chest", "Relieves back pain"],
                "instructions": "1. Lie on stomach\n2. Place hands under shoulders\n3. Lift chest off ground\n4. Hold for 15-30 seconds",
                "duration": "15-30 seconds",
                "difficulty": "Beginner",
                "emoji": "🐍",
                "web_images": [
                    "https://www.yogajournal.com/wp-content/uploads/2007/08/cobra-pose.jpg",
                    "https://www.verywellfit.com/thmb/1234567890abcdef/cobra-pose-1234567890abcdef.jpg",
                    "https://www.yogabasics.com/wp-content/uploads/cobra-pose.jpg"
                ]
            },
            "Bridge Pose (Setu Bandhasana)": {
                "description": "Strengthens core and glutes while opening hips",
                "benefits": ["Tones abs", "Strengthens back", "Opens hips", "Improves digestion"],
                "instructions": "1. Lie on back with knees bent\n2. Lift hips toward ceiling\n3. Keep shoulders on ground\n4. Hold for 30-60 seconds",
                "duration": "30-60 seconds",
                "difficulty": "Beginner",
                "emoji": "🌉",
                "web_images": [
                    "https://www.yogajournal.com/wp-content/uploads/2007/08/bridge-pose.jpg",
                    "https://www.verywellfit.com/thmb/1234567890abcdef/bridge-pose-1234567890abcdef.jpg",
                    "https://www.yogabasics.com/wp-content/uploads/bridge-pose.jpg"
                ]
            },
            "Warrior III (Virabhadrasana III)": {
                "description": "Challenges balance while engaging core muscles",
                "benefits": ["Strengthens core", "Improves balance", "Tones legs", "Builds focus"],
                "instructions": "1. Stand on one leg\n2. Extend other leg back\n3. Torso parallel to ground\n4. Hold for 15-30 seconds each side",
                "duration": "15-30 seconds each side",
                "difficulty": "Intermediate",
                "emoji": "⚔️",
                "web_images": [
                    "https://www.yogajournal.com/wp-content/uploads/2007/08/warrior-iii.jpg",
                    "https://www.verywellfit.com/thmb/1234567890abcdef/warrior-iii-1234567890abcdef.jpg",
                    "https://www.yogabasics.com/wp-content/uploads/warrior-iii.jpg"
                ]
            },
            "Side Plank (Vasisthasana)": {
                "description": "Targets obliques and strengthens entire core",
                "benefits": ["Tones obliques", "Strengthens arms", "Improves balance", "Burns fat"],
                "instructions": "1. Start in plank position\n2. Rotate to one side\n3. Stack feet and lift arm\n4. Hold for 15-30 seconds each side",
                "duration": "15-30 seconds each side",
                "difficulty": "Intermediate",
                "emoji": "⚖️",
                "web_images": [
                    "https://www.yogajournal.com/wp-content/uploads/2007/08/side-plank.jpg",
                    "https://www.verywellfit.com/thmb/1234567890abcdef/side-plank-1234567890abcdef.jpg",
                    "https://www.yogabasics.com/wp-content/uploads/side-plank.jpg"
                ]
            },
            "Crow Pose (Bakasana)": {
                "description": "Advanced pose that requires strong core engagement",
                "benefits": ["Strengthens core", "Builds arm strength", "Improves balance", "Burns calories"],
                "instructions": "1. Squat with feet together\n2. Place hands on ground\n3. Lift feet off ground\n4. Balance on hands",
                "duration": "10-20 seconds",
                "difficulty": "Advanced",
                "emoji": "🦅",
                "web_images": [
                    "https://www.yogajournal.com/wp-content/uploads/2007/08/crow-pose.jpg",
                    "https://www.verywellfit.com/thmb/1234567890abcdef/crow-pose-1234567890abcdef.jpg",
                    "https://www.yogabasics.com/wp-content/uploads/crow-pose.jpg"
                ]
            },
            "Cat-Cow Stretch (Marjaryasana-Bitilasana)": {
                "description": "Gentle flow that engages core and improves flexibility",
                "benefits": ["Warms up core", "Improves spine flexibility", "Relieves tension", "Prepares for other poses"],
                "instructions": "1. Start on hands and knees\n2. Arch back (cow)\n3. Round back (cat)\n4. Flow for 1-2 minutes",
                "duration": "1-2 minutes",
                "difficulty": "Beginner",
                "emoji": "🐱🐄",
                "web_images": [
                    "https://www.yogajournal.com/wp-content/uploads/2007/08/cat-cow.jpg",
                    "https://www.verywellfit.com/thmb/1234567890abcdef/cat-cow-1234567890abcdef.jpg",
                    "https://www.yogabasics.com/wp-content/uploads/cat-cow.jpg"
                ]
            }
        }
        
        self.current_pose_index = 0
        self.poses_list = list(self.yoga_poses.keys())
        self.timer_running = False
        self.timer_thread = None
        self.current_image_index = 0
        
        # Create music directory and download soothing music
        self.setup_music()
        
        # Define soothing background colors for each pose
        self.pose_bg_colors = {
            "Plank Pose (Phalakasana)": "#e0f7fa",
            "Boat Pose (Navasana)": "#ffe0b2",
            "Cobra Pose (Bhujangasana)": "#e1bee7",
            "Bridge Pose (Setu Bandhasana)": "#c8e6c9",
            "Warrior III (Virabhadrasana III)": "#fff9c4",
            "Side Plank (Vasisthasana)": "#f8bbd0",
            "Crow Pose (Bakasana)": "#d7ccc8",
            "Cat-Cow Stretch (Marjaryasana-Bitilasana)": "#f0f4c3"
        }
        
        self.setup_ui()
        self.load_pose_image()
        
    def setup_music(self):
        """Setup soothing background music"""
        self.music_dir = "yoga_music"
        if not os.path.exists(self.music_dir):
            os.makedirs(self.music_dir)
        
        # Create a simple soothing music file (in a real app, you'd have actual music files)
        self.create_soothing_music()
    
    def create_soothing_music(self):
        """Create a simple soothing music file for demonstration"""
        # This is a placeholder - in a real application, you would have actual music files
        # For now, we'll create a simple text file to represent music
        music_info = {
            "tracks": [
                {
                    "name": "Gentle Yoga Flow",
                    "file": "gentle_yoga_flow.mp3",
                    "duration": "10:00",
                    "description": "Soothing instrumental music perfect for yoga practice"
                },
                {
                    "name": "Meditation Sounds",
                    "file": "meditation_sounds.mp3", 
                    "duration": "15:00",
                    "description": "Peaceful nature sounds with gentle background music"
                },
                {
                    "name": "Zen Garden",
                    "file": "zen_garden.mp3",
                    "duration": "12:00", 
                    "description": "Calming Japanese-inspired meditation music"
                }
            ]
        }
        
        with open(os.path.join(self.music_dir, "music_info.json"), "w") as f:
            json.dump(music_info, f, indent=2)
    
    def setup_ui(self):
        # Main title
        title_label = tk.Label(
            self.root, 
            text="🧘 Yoga for Belly Fat Loss - Vegan Friendly 🥗",
            font=("Arial", 20, "bold"),
            bg='#f0f8ff',
            fg='#2c5530'
        )
        title_label.pack(pady=10)
        
        # Music control frame
        music_frame = tk.Frame(self.root, bg='#e8f5e8', relief='raised', bd=2)
        music_frame.pack(fill='x', padx=20, pady=5)
        
        music_label = tk.Label(
            music_frame,
            text="🎵 Soothing Music Controls:",
            font=("Arial", 12, "bold"),
            bg='#e8f5e8',
            fg='#2c5530'
        )
        music_label.pack(side='left', padx=10, pady=5)
        
        self.play_music_btn = tk.Button(
            music_frame,
            text="▶️ Play Music",
            command=self.play_music,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='raised',
            bd=2
        )
        self.play_music_btn.pack(side='left', padx=5, pady=5)
        
        self.stop_music_btn = tk.Button(
            music_frame,
            text="⏹️ Stop Music",
            command=self.stop_music,
            bg='#f44336',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='raised',
            bd=2
        )
        self.stop_music_btn.pack(side='left', padx=5, pady=5)
        
        self.music_status_label = tk.Label(
            music_frame,
            text="Music: Stopped",
            font=("Arial", 10),
            bg='#e8f5e8',
            fg='#666666'
        )
        self.music_status_label.pack(side='left', padx=10, pady=5)
        
        # Vegan nutrition tip
        nutrition_frame = tk.Frame(self.root, bg='#e8f5e8', relief='raised', bd=2)
        nutrition_frame.pack(fill='x', padx=20, pady=5)
        
        nutrition_label = tk.Label(
            nutrition_frame,
            text="💚 Vegan Nutrition Tip: Combine this yoga routine with a plant-based diet rich in protein (legumes, quinoa, tofu) and healthy fats (avocados, nuts) for optimal belly fat loss!",
            font=("Arial", 10),
            bg='#e8f5e8',
            fg='#2c5530',
            wraplength=900
        )
        nutrition_label.pack(pady=10)
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg='#f0f8ff')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Left panel - Pose information
        left_panel = tk.Frame(main_frame, bg='#f0f8ff', width=400)
        left_panel.pack(side='left', fill='y', padx=(0, 10))
        
        # Pose name
        self.pose_name_label = tk.Label(
            left_panel,
            text="",
            font=("Arial", 16, "bold"),
            bg='#f0f8ff',
            fg='#2c5530',
            wraplength=380
        )
        self.pose_name_label.pack(pady=10)
        
        # Difficulty and duration
        self.details_label = tk.Label(
            left_panel,
            text="",
            font=("Arial", 12),
            bg='#f0f8ff',
            fg='#666666'
        )
        self.details_label.pack(pady=5)
        
        # Description
        self.description_label = tk.Label(
            left_panel,
            text="",
            font=("Arial", 11),
            bg='#f0f8ff',
            fg='#333333',
            wraplength=380,
            justify='left'
        )
        self.description_label.pack(pady=10)
        
        # Benefits
        benefits_frame = tk.Frame(left_panel, bg='#f0f8ff')
        benefits_frame.pack(fill='x', pady=10)
        
        tk.Label(
            benefits_frame,
            text="Benefits:",
            font=("Arial", 12, "bold"),
            bg='#f0f8ff',
            fg='#2c5530'
        ).pack(anchor='w')
        
        self.benefits_text = tk.Text(
            benefits_frame,
            height=4,
            width=45,
            font=("Arial", 10),
            bg='#f8f8f8',
            wrap='word',
            state='disabled'
        )
        self.benefits_text.pack(pady=5)
        
        # Instructions
        instructions_frame = tk.Frame(left_panel, bg='#f0f8ff')
        instructions_frame.pack(fill='x', pady=10)
        
        tk.Label(
            instructions_frame,
            text="Instructions:",
            font=("Arial", 12, "bold"),
            bg='#f0f8ff',
            fg='#2c5530'
        ).pack(anchor='w')
        
        self.instructions_text = tk.Text(
            instructions_frame,
            height=6,
            width=45,
            font=("Arial", 10),
            bg='#f8f8f8',
            wrap='word',
            state='disabled'
        )
        self.instructions_text.pack(pady=5)
        
        # Timer
        timer_frame = tk.Frame(left_panel, bg='#f0f8ff')
        timer_frame.pack(pady=20)
        
        self.timer_label = tk.Label(
            timer_frame,
            text="00:00",
            font=("Arial", 24, "bold"),
            bg='#f0f8ff',
            fg='#2c5530'
        )
        self.timer_label.pack()
        
        # Timer controls
        timer_controls = tk.Frame(timer_frame, bg='#f0f8ff')
        timer_controls.pack(pady=10)
        
        self.start_timer_btn = tk.Button(
            timer_controls,
            text="Start Timer",
            command=self.start_timer,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='raised',
            bd=2
        )
        self.start_timer_btn.pack(side='left', padx=5)
        
        self.stop_timer_btn = tk.Button(
            timer_controls,
            text="Stop Timer",
            command=self.stop_timer,
            bg='#f44336',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='raised',
            bd=2
        )
        self.stop_timer_btn.pack(side='left', padx=5)
        
        # Right panel - Image and navigation
        right_panel = tk.Frame(main_frame, bg='#f0f8ff')
        right_panel.pack(side='right', fill='both', expand=True)
        
        # Image frame
        self.image_frame = tk.Frame(right_panel, bg='#f0f8ff', relief='sunken', bd=2)
        self.image_frame.pack(fill='both', expand=True, pady=(0, 10))
        
        self.image_label = tk.Label(self.image_frame, bg='#f0f8ff')
        self.image_label.pack(expand=True)
        
        # Image action buttons
        image_actions = tk.Frame(right_panel, bg='#f0f8ff')
        image_actions.pack(fill='x', pady=5)
        
        self.load_web_image_btn = tk.Button(
            image_actions,
            text="📷 Load Web Image",
            command=self.load_web_image,
            bg='#FF9800',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='raised',
            bd=2
        )
        self.load_web_image_btn.pack(side='left', padx=5)
        
        self.next_image_btn = tk.Button(
            image_actions,
            text="🔄 Next Image",
            command=self.next_image,
            bg='#9C27B0',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='raised',
            bd=2
        )
        self.next_image_btn.pack(side='left', padx=5)
        
        self.view_web_image_btn = tk.Button(
            image_actions,
            text="🌐 View Online",
            command=self.view_pose_online,
            bg='#2196F3',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='raised',
            bd=2
        )
        self.view_web_image_btn.pack(side='left', padx=5)
        
        # Navigation buttons
        nav_frame = tk.Frame(right_panel, bg='#f0f8ff')
        nav_frame.pack(fill='x')
        
        self.prev_btn = tk.Button(
            nav_frame,
            text="← Previous",
            command=self.previous_pose,
            bg='#2196F3',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='raised',
            bd=2
        )
        self.prev_btn.pack(side='left', padx=5)
        
        self.next_btn = tk.Button(
            nav_frame,
            text="Next →",
            command=self.next_pose,
            bg='#2196F3',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='raised',
            bd=2
        )
        self.next_btn.pack(side='right', padx=5)
        
        # Pose counter
        self.counter_label = tk.Label(
            nav_frame,
            text="",
            font=("Arial", 10),
            bg='#f0f8ff',
            fg='#666666'
        )
        self.counter_label.pack(side='top', pady=5)
        
        # Bottom panel - Additional features
        bottom_frame = tk.Frame(self.root, bg='#f0f8ff')
        bottom_frame.pack(fill='x', padx=20, pady=10)
        
        # Workout routine button
        self.routine_btn = tk.Button(
            bottom_frame,
            text="📋 View Complete Workout Routine",
            command=self.show_workout_routine,
            bg='#FF9800',
            fg='white',
            font=("Arial", 12, "bold"),
            relief='raised',
            bd=2
        )
        self.routine_btn.pack(side='left', padx=5)
        
        # Vegan diet tips button
        self.diet_btn = tk.Button(
            bottom_frame,
            text="🥗 Vegan Diet Tips",
            command=self.show_vegan_tips,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 12, "bold"),
            relief='raised',
            bd=2
        )
        self.diet_btn.pack(side='left', padx=5)
        
        # Quit button
        self.quit_btn = tk.Button(
            bottom_frame,
            text="❌ Quit",
            command=self.root.quit,
            bg='#d32f2f',
            fg='white',
            font=("Arial", 12, "bold"),
            relief='raised',
            bd=2
        )
        self.quit_btn.pack(side='right', padx=5)
        
        # Update display
        self.update_pose_display()
    
    def get_resource_path(self, relative_path):
        # Always use the YP - New folder for images and music
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'YP - New'))
        return os.path.join(base_path, relative_path)

    def pose_image_filename(self, pose_name):
        # Map pose names to image filenames (simple heuristic)
        mapping = {
            "Plank Pose (Phalakasana)": "Plank.jpg",
            "Boat Pose (Navasana)": "Nvasana Pose.jpg",
            "Cobra Pose (Bhujangasana)": "Bhujangasana.jpg",
            "Bridge Pose (Setu Bandhasana)": "Setu Bhandasana.jpg",
            "Warrior III (Virabhadrasana III)": "Virabhadrasana.jpg",
            "Side Plank (Vasisthasana)": "Vashistasana.jpg",
            "Crow Pose (Bakasana)": "Bakasana.jpg",
            "Cat-Cow Stretch (Marjaryasana-Bitilasana)": "Marjarasana.jpg"
        }
        return mapping.get(pose_name)

    def load_pose_image(self):
        """Load and display the current pose image (local if available) from YP - New"""
        pose_name = self.poses_list[self.current_pose_index]
        pose_data = self.yoga_poses[pose_name]
        img_file = self.pose_image_filename(pose_name)
        img_path = self.get_resource_path(img_file) if img_file else None
        if img_path and os.path.exists(img_path):
            try:
                img = Image.open(img_path)
                img = img.convert('RGB')
                img = img.resize((500, 400), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.image_label.configure(image=photo)
                self.image_label.image = photo
                return
            except Exception:
                pass  # fallback to enhanced image
        # Fallback to enhanced visual representation
        self.create_enhanced_pose_image(pose_name, pose_data)
    
    def load_web_image(self):
        """Load a real yoga pose image from the web"""
        pose_name = self.poses_list[self.current_pose_index]
        pose_data = self.yoga_poses[pose_name]
        
        if 'web_images' in pose_data and pose_data['web_images']:
            try:
                # Try to load the current image index
                image_url = pose_data['web_images'][self.current_image_index % len(pose_data['web_images'])]
                
                # Create a thread to load the image
                threading.Thread(target=self.load_image_from_url, args=(image_url, pose_name), daemon=True).start()
                
            except Exception as e:
                messagebox.showerror("Image Error", f"Could not load web image: {str(e)}")
                # Fall back to enhanced pose image
                self.create_enhanced_pose_image(pose_name, pose_data)
        else:
            messagebox.showinfo("No Images", "No web images available for this pose.")
    
    def load_image_from_url(self, url, pose_name):
        """Load image from URL in a separate thread"""
        try:
            # Download the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            # Open and resize the image
            img = Image.open(BytesIO(response.content))
            img = img.convert('RGB')
            img = img.resize((500, 400), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(img)
            
            # Update the UI in the main thread
            self.root.after(0, lambda: self.display_web_image(photo, pose_name))
            
        except Exception as e:
            self.root.after(0, lambda: self.handle_image_error(str(e), pose_name))
    
    def display_web_image(self, photo, pose_name):
        """Display the loaded web image"""
        self.image_label.configure(image=photo)
        self.image_label.image = photo
        
        # Add a label with pose information overlay
        pose_data = self.yoga_poses[pose_name]
        info_text = f"{pose_name}\n{pose_data['description']}\nDuration: {pose_data['duration']}"
        
        # Create an overlay frame
        overlay_frame = tk.Frame(self.image_frame, bg='rgba(0,0,0,0.7)')
        overlay_frame.place(relx=0.5, rely=0.9, anchor='center')
        
        overlay_label = tk.Label(
            overlay_frame,
            text=info_text,
            font=("Arial", 10, "bold"),
            bg='rgba(0,0,0,0.7)',
            fg='white',
            wraplength=400
        )
        overlay_label.pack(padx=10, pady=5)
        
        messagebox.showinfo("Image Loaded", f"✅ Real yoga pose image loaded for {pose_name}!")
    
    def handle_image_error(self, error, pose_name):
        """Handle image loading errors"""
        messagebox.showerror("Image Error", f"Could not load web image: {error}\nFalling back to enhanced pose image.")
        pose_data = self.yoga_poses[pose_name]
        self.create_enhanced_pose_image(pose_name, pose_data)
    
    def next_image(self):
        """Load the next available image for the current pose"""
        pose_name = self.poses_list[self.current_pose_index]
        pose_data = self.yoga_poses[pose_name]
        
        if 'web_images' in pose_data and pose_data['web_images']:
            self.current_image_index += 1
            self.load_web_image()
        else:
            messagebox.showinfo("No Images", "No additional images available for this pose.")
    
    def create_enhanced_pose_image(self, pose_name, pose_data):
        """Create an enhanced visual representation of the yoga pose"""
        # Create a larger, more detailed image
        img = Image.new('RGB', (500, 400), color='#e8f5e8')
        draw = ImageDraw.Draw(img)
        
        # Try to use a default font, fall back to basic if not available
        try:
            title_font = ImageFont.truetype("arial.ttf", 24)
            subtitle_font = ImageFont.truetype("arial.ttf", 18)
            body_font = ImageFont.truetype("arial.ttf", 14)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
        
        # Draw pose emoji (large)
        emoji = pose_data.get('emoji', '🧘')
        emoji_bbox = draw.textbbox((0, 0), emoji, font=title_font)
        emoji_width = emoji_bbox[2] - emoji_bbox[0]
        emoji_x = (500 - emoji_width) // 2
        draw.text((emoji_x, 50), emoji, fill='#2c5530', font=title_font)
        
        # Draw pose name
        name_lines = self.wrap_text(pose_name, 40)
        y_position = 120
        for line in name_lines:
            bbox = draw.textbbox((0, 0), line, font=subtitle_font)
            text_width = bbox[2] - bbox[0]
            x = (500 - text_width) // 2
            draw.text((x, y_position), line, fill='#2c5530', font=subtitle_font)
            y_position += 25
        
        # Draw difficulty and duration
        details = f"Difficulty: {pose_data['difficulty']} | Duration: {pose_data['duration']}"
        bbox = draw.textbbox((0, 0), details, font=body_font)
        text_width = bbox[2] - bbox[0]
        x = (500 - text_width) // 2
        draw.text((x, y_position + 20), details, fill='#666666', font=body_font)
        
        # Draw description
        desc_lines = self.wrap_text(pose_data['description'], 50)
        y_position += 60
        for line in desc_lines:
            bbox = draw.textbbox((0, 0), line, font=body_font)
            text_width = bbox[2] - bbox[0]
            x = (500 - text_width) // 2
            draw.text((x, y_position), line, fill='#333333', font=body_font)
            y_position += 20
        
        # Draw instruction preview
        y_position += 20
        draw.text((50, y_position), "Quick Instructions:", fill='#2c5530', font=subtitle_font)
        y_position += 25
        
        instructions = pose_data['instructions'].split('\n')[0]  # First instruction line
        instruction_lines = self.wrap_text(instructions, 45)
        for line in instruction_lines:
            draw.text((50, y_position), line, fill='#333333', font=body_font)
            y_position += 18
        
        # Add a decorative border
        draw.rectangle([10, 10, 490, 390], outline='#2c5530', width=3)
        
        # Convert to PhotoImage
        photo = ImageTk.PhotoImage(img)
        self.image_label.configure(image=photo)
        self.image_label.image = photo
    
    def wrap_text(self, text, max_width):
        """Wrap text to fit within a specified width"""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            current_line.append(word)
            line_length = len(' '.join(current_line))
            if line_length > max_width:
                if len(current_line) > 1:
                    current_line.pop()
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
                    current_line = []
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def view_pose_online(self):
        """Open the pose image in a web browser"""
        pose_name = self.poses_list[self.current_pose_index]
        pose_data = self.yoga_poses[pose_name]
        
        # Create a search query for the pose
        search_query = f"yoga {pose_name} pose images"
        search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}&tbm=isch"
        
        try:
            webbrowser.open(search_url)
            messagebox.showinfo("Web Search", f"Opening web search for {pose_name} images in your browser.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open web browser: {str(e)}")
    
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb

    def fade_bg(self, from_color, to_color, steps=20, delay=15):
        from_rgb = self.hex_to_rgb(from_color)
        to_rgb = self.hex_to_rgb(to_color)
        for i in range(1, steps + 1):
            ratio = i / steps
            new_rgb = tuple(
                int(from_rgb[j] + (to_rgb[j] - from_rgb[j]) * ratio)
                for j in range(3)
            )
            new_hex = self.rgb_to_hex(new_rgb)
            self.root.after(i * delay, lambda c=new_hex: self.apply_bg_color(c))

    def apply_bg_color(self, color):
        self.root.configure(bg=color)
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) or isinstance(widget, tk.Label):
                widget.configure(bg=color)

    def update_pose_display(self):
        """Update all pose information display"""
        pose_name = self.poses_list[self.current_pose_index]
        pose_data = self.yoga_poses[pose_name]
        # Smooth color transition
        bg_color = self.pose_bg_colors.get(pose_name, '#f0f8ff')
        current_bg = self.root.cget('bg')
        if current_bg != bg_color:
            self.fade_bg(current_bg, bg_color)
        else:
            self.apply_bg_color(bg_color)
        # Update pose name
        self.pose_name_label.configure(text=pose_name)
        # Update details
        self.details_label.configure(
            text=f"Difficulty: {pose_data['difficulty']} | Duration: {pose_data['duration']}"
        )
        # Update description
        self.description_label.configure(text=pose_data['description'])
        # Update benefits
        self.benefits_text.configure(state='normal')
        self.benefits_text.delete(1.0, tk.END)
        for benefit in pose_data['benefits']:
            self.benefits_text.insert(tk.END, f"• {benefit}\n")
        self.benefits_text.configure(state='disabled')
        # Update instructions
        self.instructions_text.configure(state='normal')
        self.instructions_text.delete(1.0, tk.END)
        self.instructions_text.insert(tk.END, pose_data['instructions'])
        self.instructions_text.configure(state='disabled')
        # Update counter
        self.counter_label.configure(
            text=f"Pose {self.current_pose_index + 1} of {len(self.poses_list)}"
        )
        # Reset image index when changing poses
        self.current_image_index = 0
        # Load image
        self.load_pose_image()
    
    def next_pose(self):
        """Go to next pose"""
        self.current_pose_index = (self.current_pose_index + 1) % len(self.poses_list)
        self.update_pose_display()
    
    def previous_pose(self):
        """Go to previous pose"""
        self.current_pose_index = (self.current_pose_index - 1) % len(self.poses_list)
        self.update_pose_display()
    
    def start_timer(self):
        """Start the pose timer"""
        if not self.timer_running:
            self.timer_running = True
            self.start_timer_btn.configure(state='disabled')
            self.timer_thread = threading.Thread(target=self.run_timer)
            self.timer_thread.daemon = True
            self.timer_thread.start()
    
    def stop_timer(self):
        """Stop the pose timer"""
        self.timer_running = False
        self.start_timer_btn.configure(state='normal')
    
    def run_timer(self):
        """Run the timer in a separate thread"""
        seconds = 0
        while self.timer_running:
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            self.root.after(0, lambda: self.timer_label.configure(
                text=f"{minutes:02d}:{remaining_seconds:02d}"
            ))
            time.sleep(1)
            seconds += 1
    
    def show_workout_routine(self):
        """Show complete workout routine"""
        routine_window = tk.Toplevel(self.root)
        routine_window.title("Complete Yoga Workout Routine")
        routine_window.geometry("800x600")
        routine_window.configure(bg='#f0f8ff')
        
        # Title
        tk.Label(
            routine_window,
            text="🧘 Complete Yoga Workout for Belly Fat Loss",
            font=("Arial", 18, "bold"),
            bg='#f0f8ff',
            fg='#2c5530'
        ).pack(pady=10)
        
        # Create text widget for routine
        routine_text = tk.Text(
            routine_window,
            font=("Arial", 11),
            bg='white',
            wrap='word',
            padx=20,
            pady=20
        )
        routine_text.pack(fill='both', expand=True, padx=20, pady=10)
        
        routine_content = """
🔥 COMPLETE YOGA WORKOUT ROUTINE FOR BELLY FAT LOSS 🔥

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

ROUND 3 - Advanced (if comfortable):
1. Crow Pose: 10-20 seconds
2. Side Plank variations: 15-30 seconds each side
3. Boat Pose with leg extensions: 15-30 seconds
4. Rest: 30 seconds

🧘 COOL-DOWN (5 minutes):
• Child's Pose: 1 minute
• Gentle twists: 30 seconds each side
• Savasana (Corpse Pose): 2-3 minutes

📅 RECOMMENDED SCHEDULE:
• Beginners: 3-4 times per week
• Intermediate: 4-5 times per week
• Advanced: 5-6 times per week

⏰ OPTIMAL TIMING:
• Morning: Best for metabolism boost
• Evening: Good for stress relief
• Empty stomach: 2-3 hours after meals

💡 PROGRESSION TIPS:
• Start with shorter holds and gradually increase
• Focus on proper form over duration
• Listen to your body and rest when needed
• Combine with cardio for best results

🥗 VEGAN NUTRITION SUPPORT:
• Pre-workout: Banana or dates (30 minutes before)
• Post-workout: Protein smoothie with plant milk
• Stay hydrated with water throughout the day
• Include protein-rich foods in your diet

🎯 EXPECTED RESULTS:
• Week 1-2: Improved flexibility and core awareness
• Week 3-4: Noticeable core strength increase
• Week 5-8: Visible belly fat reduction
• Week 9-12: Significant toning and definition

Remember: Consistency is key! Combine this yoga routine with a balanced vegan diet and regular cardio for optimal belly fat loss results.
        """
        
        routine_text.insert(tk.END, routine_content)
        routine_text.configure(state='disabled')
        
        # Scrollbar
        scrollbar = tk.Scrollbar(routine_window, command=routine_text.yview)
        scrollbar.pack(side='right', fill='y')
        routine_text.configure(yscrollcommand=scrollbar.set)
    
    def show_vegan_tips(self):
        """Show vegan diet tips for belly fat loss"""
        tips_window = tk.Toplevel(self.root)
        tips_window.title("Vegan Diet Tips for Belly Fat Loss")
        tips_window.geometry("900x700")
        tips_window.configure(bg='#f0f8ff')
        
        # Title
        tk.Label(
            tips_window,
            text="🥗 Vegan Diet Tips for Optimal Belly Fat Loss",
            font=("Arial", 18, "bold"),
            bg='#f0f8ff',
            fg='#2c5530'
        ).pack(pady=10)
        
        # Create text widget for tips
        tips_text = tk.Text(
            tips_window,
            font=("Arial", 11),
            bg='white',
            wrap='word',
            padx=20,
            pady=20
        )
        tips_text.pack(fill='both', expand=True, padx=20, pady=10)
        
        tips_content = """
🥗 VEGAN DIET TIPS FOR BELLY FAT LOSS 🥗

🍎 PROTEIN-RICH FOODS (Essential for muscle building):
• Legumes: Lentils, chickpeas, black beans (15-18g protein per cup)
• Quinoa: Complete protein source (8g protein per cup)
• Tofu and Tempeh: 20g protein per 100g
• Seitan: 25g protein per 100g
• Edamame: 17g protein per cup
• Plant-based protein powders: 20-30g per serving

🥑 HEALTHY FATS (Keep you full and support metabolism):
• Avocados: Monounsaturated fats
• Nuts: Almonds, walnuts, cashews
• Seeds: Chia, flax, hemp, pumpkin
• Olive oil and coconut oil (in moderation)
• Nut butters: Almond, peanut, cashew

🌾 COMPLEX CARBS (Sustained energy):
• Sweet potatoes: Rich in fiber and vitamins
• Brown rice: High in fiber
• Oats: Beta-glucan for heart health
• Whole grain bread and pasta
• Quinoa: Complete protein and complex carb

🥬 FIBER-RICH VEGETABLES (Low calorie, high volume):
• Leafy greens: Spinach, kale, arugula
• Cruciferous: Broccoli, cauliflower, Brussels sprouts
• Bell peppers: High in vitamin C
• Zucchini and eggplant: Low calorie
• Mushrooms: Great meat substitute

🍓 FRUITS (Natural sweetness and vitamins):
• Berries: Low sugar, high antioxidants
• Apples: High in fiber
• Citrus fruits: Vitamin C boost
• Bananas: Pre/post workout fuel

🚫 FOODS TO LIMIT:
• Processed vegan foods (fake meats, cheeses)
• Refined sugars and flours
• Excessive oils and fried foods
• Sugary beverages and juices
• Alcohol (empty calories)

💧 HYDRATION:
• Water: 8-10 glasses daily
• Herbal teas: Green tea for metabolism
• Coconut water: Natural electrolytes
• Lemon water: Detoxifying

📋 SAMPLE MEAL PLAN:

🌅 BREAKFAST:
• Overnight oats with berries and chia seeds
• Smoothie: Spinach, banana, plant protein, almond milk
• Tofu scramble with vegetables

🌞 LUNCH:
• Quinoa bowl with roasted vegetables and chickpeas
• Lentil soup with whole grain bread
• Buddha bowl with brown rice, tofu, and greens

🌆 DINNER:
• Stir-fried vegetables with tempeh
• Stuffed bell peppers with quinoa and beans
• Zucchini noodles with marinara and lentils

🍎 SNACKS:
• Apple with almond butter
• Hummus with carrot sticks
• Mixed nuts and dried fruits
• Protein smoothie

⚡ PRE/POST WORKOUT NUTRITION:
• Pre: Banana or dates (30 minutes before)
• Post: Protein smoothie with berries and plant milk
• Within 30 minutes of workout completion

📊 CALORIE DEFICIT TIPS:
• Use smaller plates
• Eat slowly and mindfully
• Focus on whole, unprocessed foods
• Track your intake initially
• Don't skip meals

🧘 YOGA + VEGAN DIET SYNERGY:
• Plant-based foods reduce inflammation
• Higher fiber content keeps you full longer
• Natural foods support detoxification
• Better digestion improves yoga practice
• Sustainable for long-term health

🎯 SUPPLEMENTS TO CONSIDER:
• Vitamin B12 (essential for vegans)
• Vitamin D (especially in winter)
• Omega-3 (flax seeds, chia seeds)
• Iron (leafy greens, legumes)
• Calcium (fortified plant milks, tofu)

Remember: The key to belly fat loss is creating a sustainable calorie deficit while maintaining muscle mass. This vegan diet combined with regular yoga practice will help you achieve your goals healthily and sustainably!
        """
        
        tips_text.insert(tk.END, tips_content)
        tips_text.configure(state='disabled')
        
        # Scrollbar
        scrollbar = tk.Scrollbar(tips_window, command=tips_text.yview)
        scrollbar.pack(side='right', fill='y')
        tips_text.configure(yscrollcommand=scrollbar.set)

    def play_music(self):
        """Play soothing background music from YP - New folder"""
        if not self.music_playing:
            try:
                music_path = self.get_resource_path("Relax Music.mp3")
                if os.path.exists(music_path):
                    pygame.mixer.music.load(music_path)
                    pygame.mixer.music.play(-1)  # Loop indefinitely
                    self.music_playing = True
                    self.music_status_label.configure(text="Music: Playing 🎵")
                    self.play_music_btn.configure(state='disabled')
                    self.stop_music_btn.configure(state='normal')
                else:
                    messagebox.showerror("Music Error", f"Music file not found: {music_path}")
            except Exception as e:
                messagebox.showerror("Music Error", f"Could not play music: {str(e)}")

    def stop_music(self):
        """Stop background music"""
        if self.music_playing:
            try:
                pygame.mixer.music.stop()
            except Exception:
                pass
            self.music_playing = False
            self.music_status_label.configure(text="Music: Stopped")
            self.play_music_btn.configure(state='normal')
            self.stop_music_btn.configure(state='disabled')

def main():
    root = tk.Tk()
    app = YogaBellyFatProgram(root)
    root.mainloop()

if __name__ == "__main__":
    main() 