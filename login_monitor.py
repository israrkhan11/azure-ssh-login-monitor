# login_monitor.py
# Description: Detects failed SSH login attempts on Linux

LOG_FILE = "/var/log/auth.log"

def monitor_failed_logins():
    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                if "Failed password" in line:
                    print("[ALERT] Failed SSH Login Attempt Detected!")
                    print(line.strip())
    except PermissionError:
        print("Permission denied. Run with sudo.")
    except FileNotFoundError:
        print("Log file not found.")

if __name__ == "__main__":
    monitor_failed_logins()
