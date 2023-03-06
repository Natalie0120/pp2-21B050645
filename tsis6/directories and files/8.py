# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

import os
filepath='C:\\Users\\pdash\\OneDrive\\Документы\\GitHub\\PP2\\Lab6\\D.txt'
if os.path.exists(filepath):
    os.remove(filepath)
else:
    print("Can not delete the file as it doesn't exists")