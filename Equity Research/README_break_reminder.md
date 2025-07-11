# Break Reminder Application

A simple Python GUI application that reminds you to take breaks every 30 minutes to promote healthy work habits.

## Features

- **Automatic 30-minute reminders** - Popup notifications every 30 minutes
- **Sound notifications** - Audio alerts with new mail sound effect
- **Modern GUI** - Clean, user-friendly interface
- **Stay on top** - Window remains visible
- **Manual trigger** - "Take Break Now" button for immediate reminders
- **Start/Stop control** - Toggle the reminder system on/off
- **Sound toggle** - Enable/disable audio notifications
- **Next reminder display** - Shows when the next reminder will occur
- **Helpful break suggestions** - Includes tips for healthy breaks

## Requirements

- Python 3.x
- tkinter (usually comes with Python)

## How to Run

1. Open a terminal/command prompt
2. Navigate to the directory containing `break_reminder.py`
3. Run the command:
   ```
   python break_reminder.py
   ```

## How to Use

1. **Start the application** - The reminder will automatically start running
2. **Automatic reminders** - Every 30 minutes, a popup will appear with break suggestions and sound alert
3. **Manual reminder** - Click "Take Break Now" for an immediate reminder with sound
4. **Stop/Start** - Use the "Stop Reminder" button to pause/resume the system
5. **Sound control** - Use the "Sound: ON/OFF" button to toggle audio notifications
6. **Close** - Simply close the window to exit the application

## Sound Features

- **MP3 notification sound** - Uses `the-notification-email-143029.mp3` from Downloads folder
- **Custom WAV fallback** - Falls back to generated `notification.wav` file if MP3 is missing
- **System sound fallback** - Falls back to Windows system sounds if custom files are missing
- **Beep fallback** - Uses simple beep if system sounds are unavailable
- **Sound toggle** - Easily enable/disable audio notifications
- **Test sound** - Clicking the sound toggle button plays a test sound when enabling
- **Sound status display** - Shows which sound file is currently being used

## Break Suggestions

The app suggests taking breaks to:
- Stretch your legs
- Look away from the screen
- Get some water
- Take a few deep breaths

## Technical Details

- Uses `tkinter` for the GUI
- Uses `threading` for the timer functionality
- Uses `winsound` for audio notifications (Windows)
- Window stays on top for visibility
- Daemon threads ensure the app closes properly
- Custom WAV file generation for notification sounds

## Tips for Healthy Work Habits

- Take a 5-10 minute break every 30 minutes
- Stand up and move around during breaks
- Look at something 20 feet away for 20 seconds to reduce eye strain
- Stay hydrated throughout the day
- Consider using the 20-20-20 rule: every 20 minutes, look at something 20 feet away for 20 seconds 