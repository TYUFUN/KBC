import json
from additional import CONFIG, log_error, save_keybinds, loading


keys = {
    "ctrl": "<ctrl>",
    "alt": "<alt>",
    "shift": "<shift>",
    "space": "<space>",
    "win": "<win>",
}
def help():
    print("""
KBC - Keybind CUI
A simple program to create keybinds for opening websites, programs or executing commands.

Files:
  kbc.exe      - manage your keybinds via CUI
  listener.exe - listens keyboard and executes keybinds (can be added to autostart)
  
  To add listener.exe to autostart:
  1. Press Win+R and type: shell:startup
  2. Create a shortcut to listener.exe in that folder

Commands:
  create <keys> <action>  - add a new keybind (e.g. create ctrl+c https://google.com)
  list                    - list all keybinds
  remove <keys>           - remove a keybind
  remove all              - remove all keybinds
  help                    - show this message
  exit                    - exit the program
  bind taskkill <keys>          - kills the active window's process 
    """)
def list():
    try:
        with open(CONFIG, "r", encoding="utf-8") as f:
            config = json.load(f)
            if not config:
                print("No keybinds found.")
                return
            for bind in config:
                print(f"{bind['keys']} -> {bind['action']}")
    except Exception:
        log_error()
def create(key, action):
    try:
        for k in keys:
            key = key.replace(k, keys[k])
        bind = {
            "keys": key,
            "action": action
        }
        save_keybinds(bind)
        print(f"Keybind {key} -> {action} created")
    except Exception:
        log_error()
def remove(key):
    if key == "all":
        try:
            with open(CONFIG, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)
            print("All keybinds removed")
        except Exception:
            log_error()
        return
    for k in keys:
        key = key.replace(k, keys[k])
    config = loading()
    new_config = []
    for с in config:
        if с["keys"] != key:
            new_config.append(с)
    if new_config == config:
        print("keybind not found")
    else:
        print(f"Keybind {key} removed")
    try:
        with open(CONFIG, "w", encoding="utf-8") as f:
            json.dump(new_config, f, indent=4)
    except Exception:
        log_error()
def bind(do, key):
    try:
        for k in keys:
            key = key.replace(k, keys[k])
        bind = {
            "keys": key,
            "action": do
        }
        save_keybinds(bind)
        print(f"Keybind {key} -> {do} created")
    except Exception:
        log_error()
    