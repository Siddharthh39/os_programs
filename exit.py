#exit: Exit the process
import os
import sys

pid = os.fork()

if pid == 0:
    print("This is the child process, it will exit now")
    sys.exit(0)
else:
    os.wait()  
    print("This is the parent process, child has exited")
