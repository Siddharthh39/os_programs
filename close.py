#close: Close a file descriptor.
import os

fd = os.open("test.txt", os.O_CREAT | os.O_RDWR)
print("File descriptor:", fd)
os.close(fd)
print("File descriptor closed")

