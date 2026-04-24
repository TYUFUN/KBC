import sys
from commands import autostart, bind, help, ls, create, remove, treat
from additional import log_error
print("""Welcome to KBC!\nType 'help' for information.""")
while True:
    try:
        inputt = input(">>> ").strip()
        if inputt.startswith("create "):
            parts = inputt.split(" ", 2)  # ["create", "c+5", "C:\Program Files\..."]
        else:
            parts = inputt.split()
        match parts:
            case ["help", page]:
                help(page=page)
            case ["help"]:
                help(page="1")
            case ["ls"]:
                ls()
            case ["exit"]:
                sys.exit(0)
            case ["create", keys, action]:
                action = action.strip()
                create(keys, action)
            case ["rm", keys]:
                remove(keys)
            case ["rm", "all"]:
                remove("all")
            case ["bind", do, keys]:
                bind(do, keys)
            case ["autostart", do]:
                autostart(do)
            case ["treat", sygnal, option, action]:
                treat(sygnal, option, action)
            case _:
                print("Unknown command. Use help for information.")
    except Exception:
        log_error()
