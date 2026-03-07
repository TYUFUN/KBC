import sys
from commands import bind, help, list, create, remove
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
            case ["help"]:
                help()
            case ["list"]:
                list()
            case ["exit"]:
                sys.exit(0)
            case ["create", keys, action]:
                action = action.strip()
                create(keys, action)
            case ["remove", keys]:
                remove(keys)
            case ["remove", "all"]:
                remove("all")
            case ["bind", do, keys]:
                bind(do, keys)
            case _:
                print("Unknown command. Use help for information.")
    except Exception:
        log_error()
