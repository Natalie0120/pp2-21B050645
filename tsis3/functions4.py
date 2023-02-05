# def isPrime(n): 
#     if n <= 1: return False
#     for i in range(2, n): 
#         if n % i == 0: 
#             return False; 
  
#     return True

# def returnPrime(list):
#     primes = []
#     for l in list:
#        for p in l:
#            if isPrime(p):
#               primes += p
#     return primes


# print(returnPrime([2,5,11,8,4,6,9,12]))


# import math

# def return_primes(arr):
#     return list(filter(lambda x : is_prime(x), arr))

# def is_prime(n):
#     for i in range(2, int(math.sqrt(n))):
#         if n % i == 0:
#             return False
#     return True

# print(return_primes([10,21,3,8,9,11,44,62,100,19]))