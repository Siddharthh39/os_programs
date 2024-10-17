#wait: Wait for a child process to complete.
import os

pid = os.fork()

if pid == 0:
    print("Child process with PID:", os.getpid())
    os._exit(0)
else:
    finished_pid, status = os.wait()
    print(f"Parent process, child {finished_pid} has finished with status {status}")
