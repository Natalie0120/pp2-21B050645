#Write a Python program with builtin function that returns True if all elements of the tuple are true.

n=int(input())
l=list()
cnt=0
for i in range(n):
    x=str(input())
    l.append(x)
for x in l:
    if x=="True":
        cnt+=1
    elif x=="False":
        cnt-=1
print(cnt)
if cnt==n:
    print ("True")
else:
    print("False")