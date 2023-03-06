#Write a Python program that invoke square root function after specific milliseconds.

from time import sleep
from math import sqrt
def mil(x, ms):
    fun=sqrt(x)
    sleep(ms/1000)
    return fun

x=int(input())
ms=int(input())
print(mil(x,ms))