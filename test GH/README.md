# Yoga Belly Fat Loss App

A mobile yoga application built with Kivy for Android, designed to help users lose belly fat through targeted yoga poses and vegan-friendly nutrition guidance.

## 🧘 Features

- **6 Yoga Poses**: Plank, Boat, Cobra, Bridge, Warrior III, Side Plank
- **Timer Functionality**: Built-in timer for each pose
- **Vegan Diet Tips**: Comprehensive nutrition guidance
- **Complete Workout Routine**: Full 30-minute workout program
- **Mobile Optimized**: Designed for portrait orientation on mobile devices

## 📱 App Information

- **App Name**: Yoga Belly Fat Loss
- **Package**: com.yoga.bellyfat
- **Version**: 1.0
- **Target**: Android API 21+ (Android 5.0+)

## 🚀 Building the APK

This repository uses GitHub Actions to automatically build the APK when you push to the main branch.

### Automatic Build (Recommended)

1. Push your code to the main branch
2. Go to the "Actions" tab in your GitHub repository
3. Wait for the build to complete (10-15 minutes)
4. Download the APK from the "Artifacts" section

### Manual Build

If you want to build locally:

```bash
# Install dependencies
pip install buildozer
pip install cython==0.29.33

# Initialize buildozer
buildozer init

# Build APK
buildozer android debug
```

## 📁 Repository Structure

```
├── main.py                 # Main Kivy application
├── requirements.txt        # Python dependencies
├── app_config.json        # App configuration
├── .github/
│   └── workflows/
│       └── build.yml      # GitHub Actions workflow
└── README.md              # This file
```

## 🎯 Yoga Poses Included

1. **Plank Pose** - Strengthens core muscles (30-60 seconds)
2. **Boat Pose** - Excellent for abs (15-30 seconds)
3. **Cobra Pose** - Tones abdominal muscles (15-30 seconds)
4. **Bridge Pose** - Strengthens core and glutes (30-60 seconds)
5. **Warrior III** - Challenges balance (15-30 seconds)
6. **Side Plank** - Targets obliques (15-30 seconds)

## 🥗 Vegan Nutrition Features

- Protein-rich food recommendations
- Healthy fat sources
- Complex carbohydrate options
- Fiber-rich vegetables
- Hydration guidelines

## 📋 Workout Routine

- **Warm-up**: 5 minutes
- **Main workout**: 20-30 minutes (3 rounds)
- **Cool-down**: 5 minutes
- **Frequency**: 3-5 times per week

## 🔧 Technical Details

- **Framework**: Kivy 2.1.0+
- **Python**: 3.9+
- **Build Tool**: Buildozer
- **Target Architecture**: arm64-v8a
- **Minimum Android**: API 21 (Android 5.0)

## 📞 Support

If you encounter any issues:

1. Check the build logs in the Actions tab
2. Ensure all files are properly uploaded
3. Verify the workflow file is in the correct location

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ for healthy living and vegan-friendly fitness** 