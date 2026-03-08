# KBC - Keybind CUI
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Version](https://img.shields.io/badge/Version-1.1-green)

A simple Windows utility that lets you create custom keybinds for opening websites, launching programs or executing commands.

---

## Files

KBC consists of two executables that work together:

| File | Description |
|------|-------------|
| `kbc.exe` | CUI app for managing your keybinds |
| `listener.exe` | Runs in the background and listens for your keybinds |

> Both files must be in the same folder to work correctly.

---

## Installation

1. Download the latest release from the [Releases](../../releases) page
2. Place both `kbc.exe` and `listener.exe` in the same folder
3. Run `listener.exe` once to start listening for keybinds

**To add listener.exe to autostart:**
1. Press `Win+R` and type `shell:startup`
2. Create a shortcut to `listener.exe` in that folder

<details>
<summary>Why should I add it to autostart?</summary>

So that the listener starts automatically when Windows boots — you won't have to manually launch it every time you restart your PC, and all your keybinds will work right away.

</details>

---

## Usage

Run `kbc.exe` to open the CUI and manage your keybinds:

```
Welcome to KBC!
Type 'help' for information.
>>>
```

---

## Examples

```
>>> create alt+g https://google.com
>>> create ctrl+shift+n notepad.exe
>>> list
<alt>+g -> https://google.com
<ctrl>+<shift>+n -> notepad.exe
```
