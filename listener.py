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
tryfix = {
    "<win>": Key.cmd,
    "<ctrl>": Key.ctrl,
    "<shift>": Key.shift,
    "<alt>": Key.alt,
    "<space>": Key.space,
    "<f1>": Key.f1,
    "<f2>": Key.f2,
    "<f3>": Key.f3,
    "<f4>": Key.f4,
    "<f5>": Key.f5,
    "<f6>": Key.f6,
    "<f7>": Key.f7,
    "<f8>": Key.f8,
    "<f9>": Key.f9,
    "<f10>": Key.f10,
    "<f11>": Key.f11,
    "<f12>": Key.f12,
}
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
def pressing(keys: str):
    key = keys.split("+")
    spisok = []
    for k in key:
        spisok.append(tryfix.get(k, k))
    num = len(spisok)
    match num:
        case  4:
            a, b, c, d = spisok
            with controller.pressed(a):
                with controller.pressed(b):
                    with controller.pressed(c):
                        controller.press(d)
                        controller.release(d)
        case  3:
            a, b, c, = spisok
            with controller.pressed(a):
                with controller.pressed(b):
                    controller.press(c)
                    controller.release(c)
        case  2:
            a, b = spisok
            with controller.pressed(a):
                controller.press(b)
                controller.release(b)
        case 1:
            a = spisok[0]
            controller.press(a)
            controller.release(a)
        case _:
            return []
def listener():
    config = loading()
    sygnals = load_sygnals()
    for a in config:
        keybind[a["keys"]] = a["action"]
    pressed = set()
    def on_press(key):
        try:
            for b in sygnals:
                target_key = getattr(keyboard.Key, b["sygnals"])
                if key == target_key:
                    if b["option"] == "-a":
                        run(b["action"])
                    elif b["option"] == "-k":
                        pressing(b["action"])
        except Exception:
            log_error()              
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