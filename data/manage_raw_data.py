from fitparse import FitFile
import pandas as pd
from paths import CONV_PATH, RAW_PATH
from pathlib import Path
import os

#-----------------------------------------------------------------------------------
# Functions to manage *.fit files extraction and save them to the folder as a backup
#-----------------------------------------------------------------------------------

folder = Path(RAW_PATH)

# Patterns to drop
DROP_PATTERNS = [
    "unknown_", "_position", "_phase", "_smoothness", "_torque", "_stroke", "_pedal",
    "pco", "power_", "pool_", "swim_", "left_", "right_", "nec_", "swc_", "stance_time_balance"
]

# Columns to keep
KEEP_COLS = [
    "start_time", "timestamp", "sport", "sub_sport",
    "total_distance", "total_ascent", "total_descent",
    "total_timer_time", "total_elapsed_time", "total_moving_time",
    "avg_speed", "enhanced_avg_speed", "max_speed", "enhanced_max_speed",
    "avg_heart_rate", "max_heart_rate",
    "avg_cadence", "max_cadence",
    "avg_step_length", "avg_stance_time", "avg_vertical_oscillation",
    "total_calories", "total_training_effect", "intensity_factor"
]

def extract_detail(folder):
    all_dfs = []

    for filename in os.listdir(folder):
        if not filename.lower().endswith(".fit"):
            continue  # skip non-FIT files

        file_path = os.path.join(folder, filename)
        fitfile = FitFile(file_path)

        # Extract all record messages
        records = [{d.name: d.value for d in record} for record in fitfile.get_messages("record")]

        # Convert to DataFrame
        df = pd.DataFrame(records)
        # Add an ID column derived from filename without .fit
        filename_core = os.path.splitext(filename)[0]
        df["activity_id"] = filename_core

        all_dfs.append(df)

    df_detail = pd.concat(all_dfs, ignore_index=True)
    return df_detail

def extract_session(folder):
    all_sessions = []

    for filename in os.listdir(folder):
        if not filename.lower().endswith(".fit"):
            continue

        fit_path = str(folder / filename)
        fitfile = FitFile(fit_path)
        filename_core = Path(filename).stem

        # Extract session messages
        session_data = [{d.name: d.value for d in msg} for msg in fitfile.get_messages("session")]
        df_session = pd.DataFrame(session_data)

        # Drop unwanted columns
        df_session = df_session[[c for c in df_session.columns if not any(p in c for p in DROP_PATTERNS)]]
        df_session = df_session[[c for c in df_session.columns if not df_session[c].apply(lambda x: isinstance(x, (list, tuple))).any()]]
        df_session = df_session.dropna(axis=1, how="all")

        # Keep key columns
        cols = [c for c in KEEP_COLS if c in df_session.columns]
        df_session = df_session[cols]

        # Add activity ID
        df_session["activity_id"] = filename_core

        all_sessions.append(df_session)

    # Combine all sessions
    df_session = pd.concat(all_sessions, ignore_index=True)
    return df_session

def save_df_by_activity(df, output_folder, suffix="session"):
    """
    Save a DataFrame grouped by 'activity_id' into CSVs, with a dynamic suffix.
    """
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    for activity_id, df_group in df.groupby("activity_id"):
        out_path = output_folder / f"{activity_id}_{suffix}.csv"
        df_group.to_csv(out_path, index=False)
        print(f"Saved {len(df_group)} rows -> {out_path}")


df_detail = extract_detail(folder)
df_session = extract_session(folder)

save_df_by_activity(df_detail, CONV_PATH, suffix="records")
save_df_by_activity(df_session, CONV_PATH, suffix="session")