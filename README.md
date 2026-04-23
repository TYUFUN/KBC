# KBC --- Keybind CUI (v2.0)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Version](https://img.shields.io/badge/Version-2.0-green)

**KBC** is a Windows console utility that allows you to create custom
keybinds for: - opening websites - launching programs - executing system
commands - handling media / Bluetooth signals (Play, Next, Volume, etc.)

It works together with a background keyboard listener.

------------------------------------------------------------------------

## Files

  -----------------------------------------------------------------------
  File                      Purpose
  ------------------------- ---------------------------------------------
  `kbc.exe`                 Manage keybinds via CUI

  `listener.exe`            Background process that listens for key
                            presses and signals
  -----------------------------------------------------------------------

> Both files **must** be placed in the same folder.

------------------------------------------------------------------------

## Installation

1.  Download the latest version from the [Releases](../../releases) page
2.  Place `kbc.exe` and `listener.exe` in the same folder
3.  Run `listener.exe`

**Autostart** can be enabled directly from `kbc.exe` using the `autostart on` command — no need to manually create shortcuts.

<details>
<summary>Why should I enable autostart?</summary>

So that the listener starts automatically when Windows boots — you won't have to manually launch it every time you restart your PC, and all your keybinds will work right away.

</details>

------------------------------------------------------------------------

## Important Notes

-   `listener.exe` must be in the same folder as `kbc.exe`
-   Keys shown like `<ctrl>` in output are correct --- this is how the
    program reads them
-   Keys must always be written using `+` **without spaces**\
    Examples: `ctrl+c`, `alt+f4`, `win+shift+s`
-   You can create keybinds for:
    -   websites
    -   `.exe` files
    -   any Windows command

------------------------------------------------------------------------

## Commands

  Command                    Description
  -------------------------- ---------------------------------------
  `create <keys> <action>`   Create a new keybind
  `ls`                       List all keybinds
  `rm <keys>`                Remove a keybind
  `rm all`                   Remove all keybinds
  `bind taskkill <keys>`     Kill the process of the active window
  `bind shutdown <keys>`     Shutdown the computer
  `bind restart <keys>`      Restart the computer
  `autostart on\|off`        Enable or disable listener autostart
  `help <page>`              Show help message
  `exit`                     Exit the program

------------------------------------------------------------------------

## New in 2.0 --- Media & Bluetooth signal handling (`treat`)

You can now bind actions not only to keyboard keys, but also to device
signals, for examle Bluetooth device

### Syntax

    treat <signal> -a <action>
    treat <signal> -k <keys>

### Flags

  -----------------------------------------------------------------------
  Flag                           Action
  ------------------------------ ----------------------------------------
  `-a`                           Execute a standard KBC action (website,
                                 path, or system command)

  `-k`                           Simulate keyboard key presses (up to 4
                                 keys)
  -----------------------------------------------------------------------

### Examples

    treat media_play_pause -a https://spotify.com
    treat media_next -k ctrl+shift+n

### Example signals (pynput standard)

  Signal                Button
  --------------------- ----------------
  `media_play_pause`    Play / Pause
  `media_next`          Next Track
  `media_previous`      Previous Track
  `media_volume_up`     Volume Up
  `media_volume_down`   Volume Down

> Signal names are case-sensitive and must be written in lowercase.

------------------------------------------------------------------------

## Usage Examples

    create alt+g https://google.com
    create ctrl+shift+n C:\Windows\System32\notepad.exe
    bind taskkill alt+f5
    autostart on
    ls

Output:

    <alt>+g -> https://google.com
    <ctrl>+<shift>+n -> C:\Windows\System32\notepad.exe
    <alt>+<f5> -> taskkill
