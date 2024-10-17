#cat: concatenates and displays the content of files.
def cat(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"{filename}: No such file")

if __name__=='__main__':
	cat("rm.py")
