# KBC - Keybind CUI
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Version](https://img.shields.io/badge/Version-1.2-green)

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
3. Run `listener.exe` to start listening for your keybinds

**Autostart** can be enabled directly from `kbc.exe` using the `autostart on` command — no need to manually create shortcuts.

<details>
<summary>Why should I enable autostart?</summary>

So that the listener starts automatically when Windows boots — you won't have to manually launch it every time you restart your PC, and all your keybinds will work right away.

</details>

---

## Notes

- `listener.exe` must be in the same folder as `kbc.exe`
- Keys like `<ctrl>` in list output are correct, this is how the program reads them
- You can create keybinds for websites, programs (`.exe`) or any command
- **Important:** write keys with `+` without spaces (e.g. `ctrl+c`, `alt+f4`, `ctrl+shift+n`)

---

## Commands

| Command | Description |
|---------|-------------|
| `create <keys> <action>` | Add a new keybind (e.g. `create alt+g https://google.com`) |
| `ls` | List all keybinds |
| `rm <keys>` | Remove a keybind |
| `rm all` | Remove all keybinds |
| `bind taskkill <keys>` | Kill the active window's process |
| `bind shutdown <keys>` | Shutdown the computer |
| `bind restart <keys>` | Restart the computer |
| `autostart on\|off` | Enable or disable autostart for listener.exe |
| `help` | Show help message |
| `exit` | Exit the program |

---

## Examples

```
>>> create alt+g https://google.com
>>> create ctrl+shift+n C:\Windows\System32\notepad.exe
>>> bind taskkill alt+f5
>>> autostart on
>>> ls
<alt>+g -> https://google.com
<ctrl>+<shift>+n -> C:\Windows\System32\notepad.exe
<alt>+<f5> -> taskkill
```
