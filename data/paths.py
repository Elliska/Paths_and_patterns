import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VENV_DIR = os.path.join(BASE_DIR, "venv")
REQUIREMENTS = os.path.join(BASE_DIR, "requirements.txt")

DB_PATH = os.path.join(BASE_DIR, "data/training_db")
RAW_PATH = os.path.join(BASE_DIR, "src/watch_export_enduro3")
CONV_PATH = os.path.join(BASE_DIR, "src/fit_converted")

CSV_PATH = os.path.join(BASE_DIR, "src/garmin_connect_export")

SRC_FOLDER = os.path.join(BASE_DIR, "src")

print(BASE_DIR)
print(DB_PATH)
print(CSV_PATH)

# To be later obsolete:
specific_csv = os.path.join(CSV_PATH, "Activities.csv")
EXCEL_PATH = os.path.join(BASE_DIR, "src/training_plan.xlsx") #will be obsolete
TEMPLATE_PATH = os.path.join(BASE_DIR, "src/template.xlsx") #will be obsolete