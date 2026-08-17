import winshell
import ctypes
import sys
import time
from datetime import datetime

LOG_FILE = "recycle_bin_log.txt"  # Change path if needed

def log_message(message):
    """Append a timestamped message to the log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {message}\n")

def empty_recycle_bin():
    try:
        winshell.recycle_bin().empty(
            confirm=False,
            show_progress=False,
            sound=False
        )
        log_message("Recycle Bin emptied successfully.")
        exit(0)
    except winshell.x_winshell as e:
        log_message(f"Error accessing Recycle Bin: {e}")
        exit(1)
    except Exception as e:
        log_message(f"Unexpected error: {e}")
        exit(1)

if __name__ == "__main__":
    if sys.platform != "win32":
        log_message("This script only works on Windows.")
        sys.exit(1)

    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        is_admin = False

    if not is_admin:
        log_message("Warning: Not running as administrator. Some items may not be deleted.")

    # Delay to ensure shell is ready
    time.sleep(10)

    empty_recycle_bin()