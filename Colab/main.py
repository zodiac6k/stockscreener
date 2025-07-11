from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

class YogaApp(App):
    def build(self):
        # Set window size for mobile
        Window.size = (400, 800)
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title = Label(
            text="Yoga for Belly Fat Loss",
            font_size='24sp',
            bold=True,
            size_hint_y=None,
            height=80,
            color=(0.2, 0.3, 0.2, 1)
        )
        main_layout.add_widget(title)
        
        # Subtitle
        subtitle = Label(
            text="Vegan-Friendly Workout Program",
            font_size='14sp',
            size_hint_y=None,
            height=40,
            color=(0.4, 0.4, 0.4, 1)
        )
        main_layout.add_widget(subtitle)
        
        # Scrollable content
        scroll = ScrollView()
        grid = GridLayout(
            cols=1,
            spacing=15,
            size_hint_y=None,
            padding=[10, 10]
        )
        grid.bind(minimum_height=grid.setter('height'))
        
        # Add yoga poses
        poses = [
            ("Plank Pose", "30-60 seconds", "Beginner", "Strengthens core muscles"),
            ("Boat Pose", "15-30 seconds", "Intermediate", "Excellent for abs"),
            ("Cobra Pose", "15-30 seconds", "Beginner", "Tones abdominal muscles"),
            ("Bridge Pose", "30-60 seconds", "Beginner", "Strengthens core and glutes"),
            ("Warrior III", "15-30 seconds", "Intermediate", "Challenges balance"),
            ("Side Plank", "15-30 seconds", "Intermediate", "Targets obliques")
        ]
        
        for pose_name, duration, difficulty, description in poses:
            pose_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=180)
            
            # Pose header
            header = BoxLayout(size_hint_y=None, height=50)
            header.add_widget(Label(text="*", font_size='28sp'))
            header.add_widget(Label(text=pose_name, font_size='18sp', bold=True))
            pose_layout.add_widget(header)
            
            # Pose description
            pose_layout.add_widget(Label(
                text=description,
                size_hint_y=None,
                height=30,
                color=(0.3, 0.3, 0.3, 1)
            ))
            
            # Pose details
            pose_layout.add_widget(Label(
                text=f"Duration: {duration} | Difficulty: {difficulty}",
                size_hint_y=None,
                height=30,
                color=(0.5, 0.5, 0.5, 1)
            ))
            
            # Timer button
            timer_btn = Button(
                text="Start Timer",
                size_hint_y=None,
                height=50,
                background_color=(0.3, 0.7, 0.3, 1),
                on_press=lambda x, name=pose_name: self.show_timer(name)
            )
            pose_layout.add_widget(timer_btn)
            
            grid.add_widget(pose_layout)
        
        scroll.add_widget(grid)
        main_layout.add_widget(scroll)
        
        # Bottom buttons
        bottom_layout = BoxLayout(size_hint_y=None, height=60, spacing=10)
        
        diet_btn = Button(
            text="Diet Tips",
            background_color=(0.2, 0.6, 0.2, 1),
            on_press=self.show_diet_tips
        )
        bottom_layout.add_widget(diet_btn)
        
        routine_btn = Button(
            text="Full Routine",
            background_color=(0.8, 0.4, 0.0, 1),
            on_press=self.show_routine
        )
        bottom_layout.add_widget(routine_btn)
        
        main_layout.add_widget(bottom_layout)
        
        return main_layout
    
    def show_timer(self, pose_name):
        """Show timer popup for a pose"""
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Timer display
        timer_label = Label(
            text="30",
            font_size='48sp',
            bold=True,
            color=(0.2, 0.7, 0.2, 1)
        )
        content.add_widget(timer_label)
        
        # Pose name
        content.add_widget(Label(
            text=f"Timer for {pose_name}",
            font_size='18sp',
            color=(0.3, 0.3, 0.3, 1)
        ))
        
        # Instructions
        content.add_widget(Label(
            text="Hold the pose for the full duration",
            font_size='14sp',
            color=(0.5, 0.5, 0.5, 1)
        ))
        
        # Close button
        close_btn = Button(
            text="Close",
            size_hint_y=None,
            height=50,
            background_color=(0.7, 0.3, 0.3, 1),
            on_press=lambda x: popup.dismiss()
        )
        content.add_widget(close_btn)
        
        popup = Popup(
            title="Timer",
            content=content,
            size_hint=(0.8, 0.6),
            background_color=(0.95, 0.95, 0.95, 1)
        )
        popup.open()
    
    def show_diet_tips(self, instance):
        """Show vegan diet tips"""
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        tips_text = """Vegan Diet Tips for Belly Fat Loss

Protein-Rich Foods:
- Legumes (lentils, chickpeas)
- Quinoa and tofu
- Nuts and seeds

Healthy Fats:
- Avocados and olive oil
- Nuts and nut butters
- Chia and flax seeds

Complex Carbs:
- Sweet potatoes
- Brown rice and oats
- Whole grain bread

Fiber-Rich Vegetables:
- Leafy greens
- Broccoli and cauliflower
- Bell peppers

Stay Hydrated:
- 8-10 glasses of water daily
- Herbal teas
- Coconut water

Remember: Combine with regular yoga practice for best results!"""
        
        content.add_widget(Label(
            text=tips_text,
            font_size='14sp',
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=400
        ))
        
        close_btn = Button(
            text="Close",
            size_hint_y=None,
            height=50,
            background_color=(0.7, 0.3, 0.3, 1),
            on_press=lambda x: popup.dismiss()
        )
        content.add_widget(close_btn)
        
        popup = Popup(
            title="Vegan Diet Tips",
            content=content,
            size_hint=(0.9, 0.8),
            background_color=(0.95, 0.95, 0.95, 1)
        )
        popup.open()
    
    def show_routine(self, instance):
        """Show complete workout routine"""
        content = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        routine_text = """Complete Yoga Workout Routine

WARM-UP (5 minutes):
- Cat-Cow Stretch: 1-2 minutes
- Gentle spinal twists: 1 minute each side
- Deep breathing: 1 minute

MAIN WORKOUT (20-30 minutes):

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

COOL-DOWN (5 minutes):
- Child's Pose: 1 minute
- Gentle twists: 30 seconds each side
- Savasana: 2-3 minutes

Schedule: 3-5 times per week
Best time: Morning or evening
Results: Visible in 4-8 weeks"""
        
        content.add_widget(Label(
            text=routine_text,
            font_size='14sp',
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=500
        ))
        
        close_btn = Button(
            text="Close",
            size_hint_y=None,
            height=50,
            background_color=(0.7, 0.3, 0.3, 1),
            on_press=lambda x: popup.dismiss()
        )
        content.add_widget(close_btn)
        
        popup = Popup(
            title="Complete Workout Routine",
            content=content,
            size_hint=(0.9, 0.8),
            background_color=(0.95, 0.95, 0.95, 1)
        )
        popup.open()

if __name__ == '__main__':
    YogaApp().run()
