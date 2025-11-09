import os
import subprocess
import venv
import shutil
import time
from data.paths import BASE_DIR, VENV_DIR, REQUIREMENTS, CSV_PATH, RAW_PATH
from data.paths import TEMPLATE_PATH, EXCEL_PATH #will be obsolete

# 1️⃣ Create venv if not exists
if not os.path.exists(VENV_DIR):
    print("📦 Creating virtual environment...")
    venv.create(VENV_DIR, with_pip=True)
else:
    print("✅ Virtual environment already exists.")

# 2️⃣ Define paths
if os.name == "nt":
    python_executable = os.path.join(VENV_DIR, "Scripts", "python.exe")
    pip_executable = os.path.join(VENV_DIR, "Scripts", "pip.exe")
else:
    python_executable = os.path.join(VENV_DIR, "bin", "python")
    pip_executable = os.path.join(VENV_DIR, "bin", "pip")

# Wait until pip exists (Windows can delay creation a bit)
for i in range(5):
    if os.path.exists(pip_executable):
        break
    time.sleep(1)
else:
    raise FileNotFoundError(f"❌ pip not found in venv: {pip_executable}")

# 3️⃣ Install requirements inside the venv
if os.path.exists(REQUIREMENTS):
    print("📄 Installing requirements...")
    subprocess.check_call([python_executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])
    subprocess.check_call([python_executable, "-m", "pip", "install", "-r", REQUIREMENTS])
else:
    print("⚠️ requirements.txt not found.")

# 5️⃣ Prepare app files
os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)
os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)

#-----------------
# Will be obsolete
#-----------------

# 4️⃣ Install kernel for Jupyter (optional)
print("⚙️ Setting up Jupyter kernel...")
subprocess.check_call([python_executable, "-m", "pip", "install", "ipykernel"])
subprocess.check_call([
    python_executable, "-m", "ipykernel", "install",
    "--user", "--name", "cvapp_env", "--display-name", "Python (CVapp)"
])

# this excel part will be obsolete
if not os.path.exists(EXCEL_PATH):
    shutil.copyfile(TEMPLATE_PATH, EXCEL_PATH)
    print(f"✅ Created new training plan from template: {EXCEL_PATH}")
else:
    print(f"✅ Using existing training plan: {EXCEL_PATH}")
