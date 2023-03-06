#Write a Python program to write a list to a file.

list=[]
k=int(input())
for i in range(k):
    x=input()
    list.append(x)
f=open('myt.txt','r')
print('Old text:')
print(f.read())
f.close


with open('myt.txt','w+') as f:
    for items in list:
        f.write('%s\n' %items)
f.close
print("New text:")
f=open('myt.txt','r')
print(f.read())
f.close