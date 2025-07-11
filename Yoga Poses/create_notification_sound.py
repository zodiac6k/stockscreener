import wave
import struct
import math

def create_notification_sound(filename="notification.wav", duration=1.0, frequency=800):
    """
    Create a simple notification sound file
    
    Args:
        filename (str): Output WAV file name
        duration (float): Duration in seconds
        frequency (int): Frequency in Hz
    """
    
    # Audio parameters
    sample_rate = 44100  # 44.1 kHz
    num_samples = int(sample_rate * duration)
    
    # Create audio data
    audio_data = []
    for i in range(num_samples):
        # Create a simple sine wave with fade in/out
        t = i / sample_rate
        fade_in = min(1.0, t / 0.1)  # Fade in over 0.1 seconds
        fade_out = min(1.0, (duration - t) / 0.1)  # Fade out over 0.1 seconds
        amplitude = fade_in * fade_out * 0.3  # Reduce volume to 30%
        
        # Generate sine wave
        sample = amplitude * math.sin(2 * math.pi * frequency * t)
        
        # Convert to 16-bit integer
        audio_data.append(int(sample * 32767))
    
    # Write WAV file
    with wave.open(filename, 'w') as wav_file:
        # Set parameters
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        # Write audio data
        for sample in audio_data:
            wav_file.writeframes(struct.pack('<h', sample))
    
    print(f"Notification sound created: {filename}")
    print(f"Duration: {duration} seconds")
    print(f"Frequency: {frequency} Hz")

if __name__ == "__main__":
    # Create a notification sound
    create_notification_sound()
    
    # You can also create different variations
    # create_notification_sound("notification_short.wav", 0.5, 1000)  # Short, higher pitch
    # create_notification_sound("notification_long.wav", 2.0, 600)   # Longer, lower pitch 