#fork: Create a new process.
import os

pid = os.fork()

if pid < 0:
    print("Fork failed")
elif pid == 0:
    print("This is the child process with PID:", os.getpid())
else:
    print("This is the parent process with PID:", os.getpid())
