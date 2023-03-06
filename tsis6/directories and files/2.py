# Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path

import os
print('Exist:', os.access('c:\\ programming library.docx', os.F_OK))
print('Readable:', os.access('c:\\ programming library.docx', os.R_OK))
print('Writable:', os.access('c:\\ programming library.docx', os.W_OK))
print('Executable:', os.access('c:\\ programming library.docx', os.X_OK))