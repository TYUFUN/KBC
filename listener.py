import subprocess
from pynput import keyboard
from pynput.keyboard import Key, Controller
import threading
import time
import os
from additional import log_error, CONFIG, loading, window, load_sygnals
keybind = {}
sygnals = None
clear_timer = None
controller = Controller()
def reload_listener():
    while True:
        global sygnals
        time.sleep(3)
        config = loading()
        keybind.clear()
        sygnals = load_sygnals()
        for a in config:
            keybind[a["keys"]] = a["action"]
def run(action:str):
    if action.startswith("http"):
        subprocess.Popen(["cmd", "/c", "start", action],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW)
    elif action.endswith(".exe"):
            subprocess.Popen([action], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif action == "taskkill":
        task = window()
        subprocess.Popen(["taskkill", "/F", "/IM", task],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW)
    elif action == "shutdown":
        os.system("shutdown /s /t 0")
    elif action == "restart":
        os.system("shutdown /r /t 0")
    else:
        subprocess.Popen(["powershell", "-Command", action], creationflags=subprocess.CREATE_NEW_CONSOLE)
def listener():
    global sygnals 
    config = loading()
    sygnals = load_sygnals()
    for a in config:
        keybind[a["keys"]] = a["action"]
    pressed = set()
    def on_press(key: str):
        try:
            for b in sygnals:
                target_key = getattr(keyboard.Key, b["sygnals"])
                if key == target_key:
                    if b["option"] == "-a":
                        run(b["action"])
                    elif b["option"] == "-k":
                        keys_sg = b["action"].split("+")
                        with controller.pressed(*keys_sg):
                            pass
        except Exception:
            log_error              
        global clear_timer
        if clear_timer:
            clear_timer.cancel()
        try:
            char = key.char
            if char:
                if not char.isprintable():
                    char = chr(ord(char) + 96)   
                pressed.add(char)
        except AttributeError:
            name = key.name
            name = name.replace("_l", "").replace("_r", "")
            pressed.add(f"<{name}>")
        clear_timer = threading.Timer(0.5, pressed.clear)
        clear_timer.start()
        for keys in list(keybind):
            ass = set(keys.split("+"))
            if ass == pressed:
                action = keybind[keys]
                pressed.clear()
                run(action)
                break
    def on_release(key: str):
        try:
            char = key.char
            if char:
                if not char.isprintable():
                    char = chr(ord(char) + 96)
                pressed.discard(char)
        except AttributeError:
            name = key.name.replace("_l", "").replace("_r", "")
            pressed.discard(f"<{name}>")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
t = threading.Thread(target=reload_listener, daemon=True)
t.start()
listener()