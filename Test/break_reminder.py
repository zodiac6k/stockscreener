import tkinter as tk
from tkinter import messagebox
import threading
import time
from datetime import datetime
import winsound
import os
import subprocess

class BreakReminder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Break Reminder")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f0f0')
        
        # Center the window
        self.root.eval('tk::PlaceWindow . center')
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
        # Variables
        self.is_running = False
        self.reminder_thread = None
        self.sound_enabled = True
        
        # Sound file path
        self.mp3_path = os.path.expanduser("~/Downloads/the-notification-email-143029.mp3")
        
        # Create GUI elements
        self.create_widgets()
        
        # Start the reminder system
        self.start_reminder()
        
    def create_widgets(self):
        # Main title
        title_label = tk.Label(
            self.root,
            text="Break Reminder",
            font=("Arial", 18, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Reminder is running...",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#006600'
        )
        self.status_label.pack(pady=10)
        
        # Next reminder time label
        self.next_reminder_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#666666'
        )
        self.next_reminder_label.pack(pady=5)
        
        # Sound file status label
        self.sound_status_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 8),
            bg='#f0f0f0',
            fg='#888888'
        )
        self.sound_status_label.pack(pady=2)
        self.update_sound_status()
        
        # Control buttons frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        # Start/Stop button
        self.control_button = tk.Button(
            button_frame,
            text="Stop Reminder",
            command=self.toggle_reminder,
            font=("Arial", 12),
            bg='#ff4444',
            fg='white',
            relief=tk.RAISED,
            padx=20,
            pady=10
        )
        self.control_button.pack(side=tk.LEFT, padx=10)
        
        # Manual reminder button
        manual_button = tk.Button(
            button_frame,
            text="Take Break Now",
            command=self.show_break_message,
            font=("Arial", 12),
            bg='#44aa44',
            fg='white',
            relief=tk.RAISED,
            padx=20,
            pady=10
        )
        manual_button.pack(side=tk.LEFT, padx=10)
        
        # Sound toggle button
        self.sound_button = tk.Button(
            button_frame,
            text="🔊 Sound: ON",
            command=self.toggle_sound,
            font=("Arial", 10),
            bg='#4444ff',
            fg='white',
            relief=tk.RAISED,
            padx=15,
            pady=8
        )
        self.sound_button.pack(side=tk.LEFT, padx=5)
        
        # Instructions
        instruction_label = tk.Label(
            self.root,
            text="This app will remind you to take a break every 30 minutes.\nClick 'Take Break Now' for an immediate reminder.\nSound notifications can be toggled on/off.",
            font=("Arial", 9),
            bg='#f0f0f0',
            fg='#666666',
            justify=tk.CENTER
        )
        instruction_label.pack(pady=20)
        
    def start_reminder(self):
        """Start the reminder system"""
        self.is_running = True
        self.reminder_thread = threading.Thread(target=self.reminder_loop, daemon=True)
        self.reminder_thread.start()
        self.update_next_reminder_time()
        
    def reminder_loop(self):
        """Main reminder loop that runs every 30 minutes"""
        while self.is_running:
            time.sleep(30 * 60)  # Sleep for 30 minutes
            if self.is_running:
                self.root.after(0, self.show_break_message)
                
    def play_alert_sound(self):
        """Play the new mail alert sound"""
        if self.sound_enabled:
            try:
                # Try to play MP3 file from downloads folder
                if os.path.exists(self.mp3_path):
                    # Use Windows Media Player to play MP3
                    subprocess.Popen(['wmplayer', self.mp3_path], shell=True)
                elif os.path.exists("notification.wav"):
                    winsound.PlaySound("notification.wav", winsound.SND_FILENAME)
                else:
                    # Play Windows system sound for new mail notification
                    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
            except:
                # Fallback to simple beep if system sound fails
                try:
                    winsound.Beep(800, 500)  # 800Hz for 500ms
                except:
                    pass  # Silently fail if sound is not available
    
    def show_break_message(self):
        """Show the break reminder message"""
        # Play alert sound
        self.play_alert_sound()
        
        # Bring window to front
        self.root.lift()
        self.root.focus_force()
        
        # Show message box
        result = messagebox.showinfo(
            "Time for a Break!",
            "It's been 30 minutes!\n\nTake a short break to:\n• Stretch your legs\n• Look away from the screen\n• Get some water\n• Take a few deep breaths\n\nYour eyes and body will thank you!",
            parent=self.root
        )
        
        # Update next reminder time
        self.update_next_reminder_time()
        
    def update_next_reminder_time(self):
        """Update the display showing when the next reminder will occur"""
        if self.is_running:
            now = datetime.now()
            # Calculate next 30-minute interval
            current_minute = now.minute
            if current_minute < 30:
                next_minute = 30
                next_hour = now.hour
            else:
                next_minute = 0
                next_hour = now.hour + 1
                if next_hour >= 24:
                    next_hour = 0
            
            next_time = now.replace(hour=next_hour, minute=next_minute, second=0, microsecond=0)
            
            self.next_reminder_label.config(
                text=f"Next reminder at: {next_time.strftime('%I:%M %p')}"
            )
        
    def update_sound_status(self):
        """Update the sound file status display"""
        if os.path.exists(self.mp3_path):
            self.sound_status_label.config(text="Using: MP3 notification sound")
        elif os.path.exists("notification.wav"):
            self.sound_status_label.config(text="Using: WAV notification sound")
        else:
            self.sound_status_label.config(text="Using: System notification sound")
    
    def toggle_sound(self):
        """Toggle sound notifications on/off"""
        self.sound_enabled = not self.sound_enabled
        if self.sound_enabled:
            self.sound_button.config(text="🔊 Sound: ON", bg='#4444ff')
            # Play a test sound
            self.play_alert_sound()
        else:
            self.sound_button.config(text="🔇 Sound: OFF", bg='#888888')
    
    def toggle_reminder(self):
        """Toggle the reminder on/off"""
        if self.is_running:
            self.is_running = False
            self.control_button.config(text="Start Reminder", bg='#44aa44')
            self.status_label.config(text="Reminder is stopped", fg='#cc0000')
            self.next_reminder_label.config(text="")
        else:
            self.is_running = True
            self.control_button.config(text="Stop Reminder", bg='#ff4444')
            self.status_label.config(text="Reminder is running...", fg='#006600')
            self.reminder_thread = threading.Thread(target=self.reminder_loop, daemon=True)
            self.reminder_thread.start()
            self.update_next_reminder_time()
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = BreakReminder()
    app.run() 