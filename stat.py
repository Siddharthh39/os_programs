#stat: Get file status.import os
stat_info = os.stat("test.txt")
print("File size:", stat_info.st_size)
print("File inode:", stat_info.st_ino)
print("File mode:", stat_info.st_mode)
