import multiprocessing, time, random

def write_shared_memory(shared_data):
    print("Writer Process: Writing data to shared memory...")
    shared_data.value = random.randint(1, 100)
    print(f"Writer Process: Shared memory now contains {shared_data.value}")
    time.sleep(2)

def read_shared_memory(shared_data):
    time.sleep(1)  
    print("Reader Process: Reading data from shared memory...")
    print(f"Reader Process: Shared memory contains {shared_data.value}")

if __name__ == "__main__":
    shared_data = multiprocessing.Value('i', 0)
    writer = multiprocessing.Process(target=write_shared_memory, args=(shared_data,))
    reader = multiprocessing.Process(target=read_shared_memory, args=(shared_data,))
    
    writer.start(); reader.start()
    writer.join(); reader.join()

    print("Main Process: Both writer and reader processes have finished.")
    