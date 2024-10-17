import os

pid = os.fork()

if pid == 0:
    print("This is the child process, executing 'ls' command")
    os.execlp("ls", "ls", "-l")
else:
    os.wait() 
    print("This is the parent process")
