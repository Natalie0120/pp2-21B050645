n=int(input())
a=(i**2 for i in range(n)) 
for x in a:
    if(x%2==0):
       print(x)
       