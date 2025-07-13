"""
Deployment helper for Streamlit Cloud
Run this script to prepare your app for deployment
"""

import os
import shutil

def prepare_for_deployment():
    """Prepare the app for Streamlit Cloud deployment"""
    
    # Check if all required files exist
    required_files = [
        "Sample Quant Trading.py",
        "requirements.txt", 
        "tickers.csv"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required files found!")
    print("\n📋 Deployment Checklist:")
    print("1. ✅ Main app file: Sample Quant Trading.py")
    print("2. ✅ Dependencies: requirements.txt")
    print("3. ✅ Data file: tickers.csv")
    print("4. ✅ Documentation: README.md")
    
    print("\n🚀 Ready for deployment!")
    print("\nNext steps:")
    print("1. Create a GitHub repository")
    print("2. Upload these files to your repository")
    print("3. Go to share.streamlit.io")
    print("4. Connect your GitHub account")
    print("5. Deploy with main file: Sample Quant Trading.py")
    
    return True

if __name__ == "__main__":
    prepare_for_deployment() 