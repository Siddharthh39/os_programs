import os

def ls(path='.'):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"{path}: No such file or directory")
    except PermissionError:
        print(f"{path}: Permission denied")
