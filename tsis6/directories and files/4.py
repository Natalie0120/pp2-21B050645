#Write a Python program to count the number of lines in a text file.

import os
file=open('myt.txt','r')
line_counter=0
Content=file.read()
CoList = Content.split("\n")
  
for i in CoList:
    if i:
        line_counter += 1
          
print("Thr quantity lines in the file:", end=' ')
print(line_counter)