def filter_prime(x) :
    l=0
    for i in range(2,x) :
        if x%i==0 :
            l=l+1
    if l==0 :
        print(x, end=" ")

a=list(input().split())

for i in  a:
    filter_prime(int(i))