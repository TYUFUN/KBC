import traceback
import json
import os
import sys
import win32gui
import win32process
import psutil
startup = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup") # type: ignore
shortcut_path = os.path.join(startup, "listener.lnk")
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(BASE_DIR, "config.json")
SYGNALS = os.path.join(BASE_DIR, "sygnals.json")
LOGS="latest_logs.txt"
def log_error():
    with open(LOGS, "w", encoding="utf-8") as f:
        f.write(traceback.format_exc())
        print("An error occurred! Check latest_logs.txt")
def loading() -> list:
    if not os.path.exists(CONFIG):
        return []
    try:
        with open(CONFIG, "r", encoding="utf-8") as f:
            return json.load(f)     
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
def load_sygnals() -> list:
    if not os.path.exists(SYGNALS):
        return []
    try:
        with open(SYGNALS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        log_error()
        return []
def save_sygnals(bind):
    a = load_sygnals()
    a.append(bind)
    try:
        with open(SYGNALS, "w", encoding="utf-8") as f:
            json.dump(a, f, indent=4)
    except Exception:
        log_error()

        