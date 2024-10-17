#2.Write programs using the I/O system calls of LINUX operating system (open, read, write, etc)
#open: Open a file descriptor.
import os

# Open a file in read/write mode, create it if it doesn't exist
fd = os.open("example.txt", os.O_RDWR | os.O_CREAT)
print(f"File descriptor: {fd}")

# Write some data to the file
os.write(fd, b"Hello, world!\n")
print("Data written to file")

# Move the pointer to the beginning of the file
os.lseek(fd, 0, os.SEEK_SET)

# Read data from the file
data = os.read(fd, 100)
print(f"Data read from file: {data.decode()}")

# Close the file descriptor
os.close(fd)
print("File descriptor closed")
