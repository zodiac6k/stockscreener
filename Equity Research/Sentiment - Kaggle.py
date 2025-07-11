import os
import subprocess
import zipfile

os.environ['KAGGLE_CONFIG_DIR'] = r'C:\Users\zodia\.kaggle'

# Download the dataset using subprocess
subprocess.run([
    'kaggle', 'datasets', 'download',
    '-d', 'aaron7sun/stocknews',
    '-p', 'C:/Py Test/'
], check=True)

# Unzip the file
with zipfile.ZipFile("C:/Py Test/stocknews.zip", 'r') as zip_ref:
    zip_ref.extractall("C:/Py Test/")