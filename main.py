import winshell
import ctypes
import sys

def empty_recycle_bin(confirm=True):
    try:

        # Empty the Recycle Bin without showing progress or sound
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        print("Recycle Bin emptied successfully.")

    except winshell.x_winshell as e:
        print(f"Error accessing Recycle Bin: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Ensure script is running on Windows
    if sys.platform != "win32":
        print("This script only works on Windows.")
        sys.exit(1)

    # Check if running with admin privileges (optional but recommended)
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        is_admin = False

    if not is_admin:
        print("Warning: You are not running as administrator. Some items may not be deleted.")

    empty_recycle_bin(confirm=True)