import subprocess
from pynput import keyboard
import threading
import time
import os
from additional import log_error, CONFIG, loading, window
keybind = {}
clear_timer = None
def reload_listener():
    while True:
        time.sleep(3)
        config = loading()
        keybind.clear()
        for a in config:
            keybind[a["keys"]] = a["action"]
def listener(): 
    config = loading()
    for a in config:
        keybind[a["keys"]] = a["action"]
    pressed = set()
    def on_press(key):
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
        clear_timer = threading.Timer(0.3, pressed.clear)
        clear_timer.start()
        for keys in list(keybind):
            ass = set(keys.split("+"))
            if ass == pressed:
                action = keybind[keys]
                pressed.clear()
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
                break

    def on_release(key):
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