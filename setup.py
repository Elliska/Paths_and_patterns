import os
import subprocess
import sys
import venv
import ensurepip
import shutil
from data.paths import BASE_DIR,  VENV_DIR, REQUIREMENTS, DB_PATH, TEMPLATE_PATH, EXCEL_PATH 

ensurepip.bootstrap()

# Step 1: Create virtual environment if not exists
if not os.path.exists(VENV_DIR):
    print("📦 Creating virtual environment...")
    venv.create(VENV_DIR, with_pip=True)
else:
    print("✅ Virtual environment already exists.")

# Step 2: Install requirements
pip_executable = os.path.join(VENV_DIR, "Scripts", "pip.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "pip")

if os.path.exists(REQUIREMENTS):
    print("📄 Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS])
else:
    print("⚠️ requirements.txt not found.")


# os.makedirs(os.path.dirname(EXCEL_PATH), exist_ok=True)

# Check if the personal training file exists
if not os.path.exists(EXCEL_PATH):
    # Copy template to create a new training plan
    shutil.copyfile(TEMPLATE_PATH, EXCEL_PATH)
    print(f"Created new training plan from template: {EXCEL_PATH}")
else:
    print(f"Using existing training plan: {EXCEL_PATH}")


