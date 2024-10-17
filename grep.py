#grep: searches for a pattern in files.
import re

def grep(pattern, filename):
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                if re.search(pattern, line):
                    print(f"{line_num}: {line.strip()}")
    except FileNotFoundError:
        print(f"{filename}: No such file")


if __name__=='__main__':
	grep("for","/home/siddharth/shared vm/pattern/num.py")
