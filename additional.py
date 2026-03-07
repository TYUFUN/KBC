import traceback
import json
import os
import sys
import win32gui
import win32process
import psutil
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(BASE_DIR, "config.json")
LOGS="latest_logs.txt"
def log_error():
    with open(LOGS, "w", encoding="utf-8") as f:
        f.write(traceback.format_exc())
        print("An error occurred! Check latest_logs.txt")
def loading():
    if not os.path.exists(CONFIG):
        return []
    try:
        with open(CONFIG, "r", encoding="utf-8") as f:
            config = json.load(f)
            return config
    except Exception:
        log_error()
        
        return []
def save_keybinds(bind):
    a = loading()
    a.append(bind)
    try:
        with open(CONFIG, "w", encoding="utf-8") as f:
            json.dump(a, f, indent=4)
    except Exception:
        log_error()
def window():
    hwnd = win32gui.GetForegroundWindow()
    pid = win32process.GetWindowThreadProcessId(hwnd)[1]
    return psutil.Process(pid).name()
