import json
import os
import win32com.client
from additional import BASE_DIR, CONFIG, SYGNALS, log_error, save_keybinds, loading, save_sygnals, shortcut_path


keys = {
    "ctrl": "<ctrl>",
    "alt": "<alt>",
    "shift": "<shift>",
    "win": "<win>",
    "space": "<space>",
    "f1": "<f1>",
    "f2": "<f2>",
    "f3": "<f3>",
    "f4": "<f4>",
    "f5": "<f5>",
    "f6": "<f6>",
    "f7": "<f7>",
    "f8": "<f8>",
    "f9": "<f9>",
    "f10": "<f10>",
    "f11": "<f11>",
    "f12": "<f12>",
}

def help(page: str):
    if page == "1":
        print("""
KBC - Keybind CUI
A simple program to create keybinds for opening websites, programs or executing commands.

Files:
  kbc.exe      - manage your keybinds via CUI
  listener.exe - listens keyboard and executes keybinds (can be added to autostart)
  
 Notes:
  listener.exe must be in the same folder as kbc.exe
  keys like <ctrl> in list output are correct, this is how program reads them
  you can create keybinds using "create" for opening websites, programs (.exe) or executing commands
  
  !important: you must write keys with "+" without spaces (e.g. ctrl+c, alt+f4, win+shift+s)
  
Commands:
  create <keys> <action>    - add a new keybind (e.g. create ctrl+c https://google.com)
  ls                        - list all keybinds
  rm <keys>                 - remove a keybind
  rm all                    - remove all keybinds
  help <page>               - show this message or another help messages (default page=0)
  exit                      - exit the program
  bind taskkill <keys>      - kills the active window's process 
  bind shutdown <keys>      - shutdown the computer
  bind restart <keys>       - restart the computer
  autostart on|off             - enable or disable autostart keybind listener
    """)
    elif page == "2":
        print("""
KBC Help - Page 2: Signal Handling (treat)
This command allows you to bind Bluetooth signals (like media buttons) to specific actions.

Commands:
  treat <signal> -a <action>  - bind a signal to open a website, program or command
                                (e.g. treat media_play_pause -a https://spotify.com)                              
  treat <signal> -k <keys>    - bind a signal to simulate keyboard keys (up to 4 keys)
                                (e.g. treat media_next -k ctrl+shift+n)

Flags:
  -a (action) - executes a standard KBC action (web, path, or system command)
  -k (keys)   - simulates physical key presses on your keyboard

example of Bluetooth Signals (pynput standard):
  media_play_pause    - Play/Pause button
  media_volume_up     - Volume Up button
  media_volume_down   - Volume Down button
  media_next          - Next Track button
  media_previous      - Previous Track button

Notes:
  - You can find the exact signal name by asking AI or search in the internet.
  - Signal names must be written exactly as shown (all lowercase).
  - Like in "create", keys for the -k flag must be separated by "+" without spaces.
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
    except FileNotFoundError:
        print("Config file not found. No keybinds created yet.")
    except Exception:
        log_error()
    try:
        with open(SYGNALS, "r", encoding="utf-8") as c:
            sygnals = json.load(c)
            if not sygnals:
                return
            for bind in sygnals:
                print(f"{bind['sygnals']} -> {bind['action']}")
    except FileNotFoundError:
        pass
def create(key:str, action:str) -> dict:
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
def remove(key:str):
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
def bind(do:str, key:str) -> dict:
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
def autostart(do:str):
    if do == "off":
        try:
            if os.path.exists(shortcut_path):
                os.remove(shortcut_path)
                print("Autostart disabled")
            else:
                print("Autostart is not enabled.")
        except Exception:
            log_error()
    elif do == "on":
        try:
            
            target_path = os.path.join(BASE_DIR, "listener.exe")
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortcut(shortcut_path)
            shortcut.Targetpath = target_path
            shortcut.Save()
            print("Autostart enabled")
        except Exception:
            log_error()
def treat(sygnal:str, option:str, action:str) -> dict:
    try:
        if option == "-k":
            for k in keys:
                action = action.replace(k, keys[k])
        bind = {
            "sygnals": sygnal,
            "action": action,
            "option": option
        }
        save_sygnals(bind)
        print(f"sygnal treat {sygnal} -> {action} created")
    except Exception:
        log_error()