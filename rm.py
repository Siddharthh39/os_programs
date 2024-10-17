#rm: removes a file.
import os

def rm(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' removed")
    except FileNotFoundError:
        print(f"{filename}: No such file")
    except IsADirectoryError:
        print(f"{filename}: Is a directory")

if __name__=='__main__':
	rm("/home/siddharth/Pictures/Screenshots/Screenshot_20240817_115916-1.png")
