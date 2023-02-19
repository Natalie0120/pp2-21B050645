a=int(input())
b=int(input())
a=(i**2 for i in range(a, b+1)) 
for x in a:
    print(x)