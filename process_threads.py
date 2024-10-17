#4. Write a program to create processes and threads. 
import os
import threading
import multiprocessing
import time

# Function for the process
def process_task(num):
    print(f"Process {num} started with PID: {os.getpid()}")
    time.sleep(2)
    print(f"Process {num} ended")

# Function for the thread
def thread_task(num):
    print(f"Thread {num} started with TID: {threading.get_ident()}")
    time.sleep(2)
    print(f"Thread {num} ended")

def main():
    # Create processes
    print("Creating processes...")
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=process_task, args=(i,))
        processes.append(p)
        p.start()

    # Wait for processes to complete
    for p in processes:
        p.join()

    # Create threads
    print("Creating threads...")
    threads = []
    for i in range(3):
        t = threading.Thread(target=thread_task, args=(i,))
        threads.append(t)
        t.start()

    # Wait for threads to complete
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

