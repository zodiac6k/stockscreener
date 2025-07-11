#!/usr/bin/env python3
"""
Prepare Yoga App for GitHub Repository
This script creates all necessary files for GitHub Actions APK build.
"""

import os
import shutil
import zipfile

def create_github_directory():
    """Create the .github/workflows directory structure"""
    github_dir = ".github/workflows"
    os.makedirs(github_dir, exist_ok=True)
    print(f"Created directory: {github_dir}")

def copy_workflow_file():
    """Copy the GitHub Actions workflow file"""
    if os.path.exists('github_workflow.yml'):
        github_dir = ".github/workflows"
        shutil.copy2('github_workflow.yml', os.path.join(github_dir, 'build.yml'))
        print("Copied workflow file to .github/workflows/build.yml")
    else:
        print("Warning: github_workflow.yml not found")

def create_github_package():
    """Create a ZIP package for GitHub upload"""
    # Create package directory
    package_dir = "github_repository_files"
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    os.makedirs(package_dir)
    
    # Create .github/workflows directory in package
    github_dir = os.path.join(package_dir, ".github", "workflows")
    os.makedirs(github_dir, exist_ok=True)
    
    # Files to copy
    files_to_copy = [
        'main.py',
        'requirements.txt',
        'app_config.json',
        'README.md'
    ]
    
    # Copy main files
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, package_dir)
            print(f"Copied {file}")
    
    # Copy workflow file
    if os.path.exists('github_workflow.yml'):
        shutil.copy2('github_workflow.yml', os.path.join(github_dir, 'build.yml'))
        print("Copied workflow file")
    
    # Create ZIP file
    zip_filename = "github_repository_files.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, package_dir)
                zipf.write(file_path, arcname)
    
    print(f"Created {zip_filename}")
    print(f"Package size: {os.path.getsize(zip_filename) / 1024:.1f} KB")
    
    # Clean up
    shutil.rmtree(package_dir)
    
    return zip_filename

def create_upload_instructions():
    """Create instructions for GitHub upload"""
    instructions = """# GitHub Repository Upload Instructions

## 📁 Files to Upload to GitHub

Upload these files to your GitHub repository:

### Required Files:
1. `main.py` - Main Kivy application
2. `requirements.txt` - Python dependencies
3. `app_config.json` - App configuration
4. `README.md` - Repository documentation

### GitHub Actions Setup:
1. Create folder: `.github/workflows/`
2. Upload `build.yml` to `.github/workflows/`

## 🚀 Step-by-Step Process:

### 1. Create GitHub Repository
1. Go to https://github.com/new
2. Name: `yoga-belly-fat-app` (or your preferred name)
3. Make it Public or Private
4. Don't initialize with README (we'll upload our own)

### 2. Upload Files
**Option A: Using GitHub Web Interface**
1. Go to your new repository
2. Click "Add file" → "Upload files"
3. Drag and drop all files from the package
4. Commit with message: "Initial commit - Yoga app files"

**Option B: Using Git Commands**
```bash
git clone https://github.com/YOUR_USERNAME/yoga-belly-fat-app.git
cd yoga-belly-fat-app
# Copy all files from the package here
git add .
git commit -m "Initial commit - Yoga app files"
git push origin main
```

### 3. Verify GitHub Actions
1. Go to your repository
2. Click "Actions" tab
3. You should see the workflow running
4. Wait 10-15 minutes for build to complete

### 4. Download APK
1. In Actions tab, click on the completed workflow
2. Scroll down to "Artifacts"
3. Click "yoga-app-apk" to download
4. Install APK on your phone

## 📋 File Structure in Repository:
```
yoga-belly-fat-app/
├── main.py
├── requirements.txt
├── app_config.json
├── README.md
└── .github/
    └── workflows/
        └── build.yml
```

## 🔧 Troubleshooting:
- If build fails, check the Actions logs
- Ensure all files are uploaded correctly
- Verify the workflow file is in the right location
- Check that the repository is public (for free GitHub Actions)

## 📞 Need Help?
- Check the build logs in Actions tab
- Verify all files are present in repository
- Ensure workflow file is properly named and located
"""
    
    with open('github_upload_instructions.md', 'w') as f:
        f.write(instructions)
    
    print("Created github_upload_instructions.md")

def main():
    """Main function to prepare GitHub files"""
    print("Preparing Yoga App for GitHub Repository")
    print("=" * 50)
    
    # Create GitHub directory structure
    create_github_directory()
    copy_workflow_file()
    
    # Create package
    zip_file = create_github_package()
    
    # Create instructions
    create_upload_instructions()
    
    print("\nGitHub Preparation Complete!")
    print("=" * 50)
    print(f"Package created: {zip_file}")
    print("\nNext Steps:")
    print("1. Create a new GitHub repository")
    print("2. Upload files from the package to your repository")
    print("3. Ensure the workflow file is in .github/workflows/")
    print("4. Push to trigger the build")
    print("5. Download APK from Actions tab")
    print("\nSee github_upload_instructions.md for detailed steps")

if __name__ == "__main__":
    main() 