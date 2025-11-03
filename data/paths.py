import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VENV_DIR = os.path.join(BASE_DIR, "venv")
REQUIREMENTS = os.path.join(BASE_DIR, "requirements.txt")

DB_PATH = os.path.join(BASE_DIR, "data/training_db")
CSV_PATH = os.path.join(BASE_DIR, "src/garmin_connect_export")
EXCEL_PATH = os.path.join(BASE_DIR, "src/training_plan.xlsx")
TEMPLATE_PATH = os.path.join(BASE_DIR, "src/template.xlsx")

SRC_FOLDER = os.path.join(BASE_DIR, "src")

print(BASE_DIR)
print(DB_PATH)
print(CSV_PATH)

# To be later obsolete:
specific_csv = os.path.join(CSV_PATH, "Activities.csv")
