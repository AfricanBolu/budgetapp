import os
import sys
import subprocess

def install_library(library_name):
    try:
        __import__(library_name)
        print(f"{library_name} is already installed.")
        return
    except ImportError:
        print(f"Installing {library_name}...")
        try:
            subprocess.check_call([os.sys.executable, "-m", "pip", "install", library_name])
            print(f"{library_name} installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {library_name}: {e}")
