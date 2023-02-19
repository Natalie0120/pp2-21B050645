from math import tan, pi
print('Input number of sides:',end='')
sides=int(input())
print('Input the length of a side:',end='')
lenth=int(input())
apothem=((lenth)/(2*(tan(pi/sides))))
area=(sides*apothem*lenth)/2
print('Area=',end='')
print(area)