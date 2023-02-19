n=int(input())
a=(i**2 for i in range(n)) 
for x in a:
    if(x%3==0 and x%4==0):
       print(x)