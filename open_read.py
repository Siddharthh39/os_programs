#opendir and readdir: Open a directory and read its contents.
import os

directory = os.opendir(".")
print("Directory contents:")
for entry in os.listdir("."):
    print(entry)
