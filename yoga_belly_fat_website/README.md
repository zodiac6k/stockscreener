# Yoga Transformation for Wellness and Health Program Website

This website presents a yoga program for reducing belly fat, with each pose on its own page, using images and content from the YP - New folder. The site also includes a feedback page to collect user input.

## Features
- Each yoga pose has its own page with instructions, benefits, and an image.
- Background music can be played on each page.
- A feedback form at the end collects name, email, and message.

## Local Development
1. Install [Node.js](https://nodejs.org/) if you want to use a static site generator or React.
2. Run a local server (e.g., `npx serve` or `python -m http.server`).
3. Open `index.html` in your browser.

## Deployment
- You can deploy this site using GitHub Pages, Vercel, Netlify, or any static hosting provider.
- For GitHub Pages: push the contents of this folder to your repository and enable Pages in the repo settings.
- For Vercel/Netlify: drag and drop the folder or connect your repo.

# Yoga Transformation for Wellness and Health Mobile App (Kivy)

This is a ready-to-use Kivy app for Android that displays yoga poses, their descriptions, and plays relaxing music. Images and music are loaded from the `YP - New/images` folder.

## How to Use

1. Copy all `.jpg` and `Relax Music.mp3` from `YP - New/images` into an `assets` folder in your app directory.
2. Save the following code as `main.py` in your app directory.
3. Install Kivy: `pip install kivy`
4. Run the app: `python main.py`
5. To build for Android, use [Buildozer](https://buildozer.readthedocs.io/en/latest/).

---

## main.py
```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader

POSES = [
    {"name": "Plank Pose", "image": "assets/Plank.jpg"},
    {"name": "Boat Pose", "image": "assets/Nvasana Pose.jpg"},
    {"name": "Cobra Pose", "image": "assets/Bhujangasana.jpg"},
    {"name": "Bridge Pose", "image": "assets/Setu Bhandasana.jpg"},
    {"name": "Warrior III", "image": "assets/Virabhadrasana.jpg"},
    {"name": "Side Plank", "image": "assets/Vashistasana.jpg"},
    {"name": "Crow Pose", "image": "assets/Bakasana.jpg"},
    {"name": "Cat-Cow Stretch", "image": "assets/Marjarasana.jpg"},
]

class YogaApp(App):
    def build(self):
        self.music = SoundLoader.load('assets/Relax Music.mp3')
        layout = BoxLayout(orientation='vertical')
        for pose in POSES:
            btn = Button(text=pose["name"], size_hint_y=None, height=50)
            btn.bind(on_release=lambda btn, p=pose: self.show_pose(p))
            layout.add_widget(btn)
        music_btn = Button(text="Play Music", size_hint_y=None, height=50)
        music_btn.bind(on_release=self.play_music)
        layout.add_widget(music_btn)
        return layout

    def show_pose(self, pose):
        self.root.clear_widgets()
        self.root.add_widget(Image(source=pose["image"]))
        self.root.add_widget(Label(text=pose["name"]))
        back_btn = Button(text="Back")
        back_btn.bind(on_release=lambda x: self.restart())
        self.root.add_widget(back_btn)

    def restart(self):
        self.root.clear_widgets()
        self.build()

    def play_music(self, instance):
        if self.music:
            self.music.play()

if __name__ == '__main__':
    YogaApp().run()

---

## assets/
- Place all pose images (`.jpg`) and `Relax Music.mp3` here.

---

## Credits
- Yoga content adapted from [Yoga for Transformation and Healthy Living](https://zodiac6k.github.io/YFT/index.html) 