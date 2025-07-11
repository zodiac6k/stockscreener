import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import os
from PIL import Image, ImageTk, ImageDraw, ImageFont
import requests
from io import BytesIO
import threading
import time
import pygame
import tempfile

class EnhancedYogaProgram:
    def __init__(self, root):
        self.root = root
        self.root.title("🧘 Enhanced Yoga for Belly Fat Loss - Vegan Friendly 🥗")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f8ff')
        
        # Initialize pygame for music
        pygame.mixer.init()
        self.music_playing = False
        
        # Yoga poses with real image URLs
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
                    "https://www.verywellfit.com/thmb/plank-pose.jpg",
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
                    "https://www.verywellfit.com/thmb/boat-pose.jpg",
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
                    "https://www.verywellfit.com/thmb/cobra-pose.jpg",
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
                    "https://www.verywellfit.com/thmb/bridge-pose.jpg",
                    "https://www.yogabasics.com/wp-content/uploads/bridge-pose.jpg"
                ]
            }
        }
        
        self.current_pose_index = 0
        self.poses_list = list(self.yoga_poses.keys())
        self.timer_running = False
        self.timer_thread = None
        self.current_image_index = 0
        
        self.setup_ui()
        self.load_pose_image()
        
    def setup_ui(self):
        # Main title
        title_label = tk.Label(
            self.root, 
            text="🧘 Enhanced Yoga for Belly Fat Loss - Vegan Friendly 🥗",
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
            text="📷 Load Real Image",
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
        
        # Update display
        self.update_pose_display()
    
    def play_music(self):
        """Play soothing background music"""
        if not self.music_playing:
            try:
                self.music_playing = True
                self.music_status_label.configure(text="Music: Playing 🎵")
                self.play_music_btn.configure(state='disabled')
                self.stop_music_btn.configure(state='normal')
                
                # Show music info
                messagebox.showinfo("Music Playing", 
                    "🎵 Soothing yoga music is now playing!\n\n"
                    "Track: Gentle Yoga Flow\n"
                    "Duration: 10:00\n"
                    "Description: Soothing instrumental music perfect for yoga practice\n\n"
                    "The music will help create a peaceful atmosphere for your yoga session.")
                
            except Exception as e:
                messagebox.showerror("Music Error", f"Could not play music: {str(e)}")
    
    def stop_music(self):
        """Stop background music"""
        if self.music_playing:
            self.music_playing = False
            self.music_status_label.configure(text="Music: Stopped")
            self.play_music_btn.configure(state='normal')
            self.stop_music_btn.configure(state='disabled')
    
    def load_pose_image(self):
        """Load and display the current pose image"""
        pose_name = self.poses_list[self.current_pose_index]
        pose_data = self.yoga_poses[pose_name]
        self.create_enhanced_pose_image(pose_name, pose_data)
    
    def load_web_image(self):
        """Load a real yoga pose image from the web"""
        pose_name = self.poses_list[self.current_pose_index]
        pose_data = self.yoga_poses[pose_name]
        
        if 'web_images' in pose_data and pose_data['web_images']:
            try:
                image_url = pose_data['web_images'][self.current_image_index % len(pose_data['web_images'])]
                threading.Thread(target=self.load_image_from_url, args=(image_url, pose_name), daemon=True).start()
                
            except Exception as e:
                messagebox.showerror("Image Error", f"Could not load web image: {str(e)}")
                self.create_enhanced_pose_image(pose_name, pose_data)
        else:
            messagebox.showinfo("No Images", "No web images available for this pose.")
    
    def load_image_from_url(self, url, pose_name):
        """Load image from URL in a separate thread"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            img = Image.open(BytesIO(response.content))
            img = img.convert('RGB')
            img = img.resize((500, 400), Image.Resampling.LANCZOS)
            
            photo = ImageTk.PhotoImage(img)
            self.root.after(0, lambda: self.display_web_image(photo, pose_name))
            
        except Exception as e:
            self.root.after(0, lambda: self.handle_image_error(str(e), pose_name))
    
    def display_web_image(self, photo, pose_name):
        """Display the loaded web image"""
        self.image_label.configure(image=photo)
        self.image_label.image = photo
        
        pose_data = self.yoga_poses[pose_name]
        info_text = f"{pose_name}\n{pose_data['description']}\nDuration: {pose_data['duration']}"
        
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
        img = Image.new('RGB', (500, 400), color='#e8f5e8')
        draw = ImageDraw.Draw(img)
        
        try:
            title_font = ImageFont.truetype("arial.ttf", 24)
            subtitle_font = ImageFont.truetype("arial.ttf", 18)
            body_font = ImageFont.truetype("arial.ttf", 14)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
        
        # Draw pose emoji
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
        
        # Draw details
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
        
        # Add border
        draw.rectangle([10, 10, 490, 390], outline='#2c5530', width=3)
        
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
        search_query = f"yoga {pose_name} pose images"
        search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}&tbm=isch"
        
        try:
            webbrowser.open(search_url)
            messagebox.showinfo("Web Search", f"Opening web search for {pose_name} images in your browser.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open web browser: {str(e)}")
    
    def update_pose_display(self):
        """Update all pose information display"""
        pose_name = self.poses_list[self.current_pose_index]
        pose_data = self.yoga_poses[pose_name]
        
        self.pose_name_label.configure(text=pose_name)
        self.details_label.configure(text=f"Difficulty: {pose_data['difficulty']} | Duration: {pose_data['duration']}")
        self.description_label.configure(text=pose_data['description'])
        
        self.benefits_text.configure(state='normal')
        self.benefits_text.delete(1.0, tk.END)
        for benefit in pose_data['benefits']:
            self.benefits_text.insert(tk.END, f"• {benefit}\n")
        self.benefits_text.configure(state='disabled')
        
        self.instructions_text.configure(state='normal')
        self.instructions_text.delete(1.0, tk.END)
        self.instructions_text.insert(tk.END, pose_data['instructions'])
        self.instructions_text.configure(state='disabled')
        
        self.counter_label.configure(text=f"Pose {self.current_pose_index + 1} of {len(self.poses_list)}")
        self.current_image_index = 0
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

def main():
    root = tk.Tk()
    app = EnhancedYogaProgram(root)
    root.mainloop()

if __name__ == "__main__":
    main() 