def volumeSphere(radius: float): 
   fp = (4/3) * 3.142 
   sp = radius ** 3 
   volume = fp * sp 
   return volume 

# The formula was splitted into two part as "fp(first part)" and "sp(second part)" 
# In line 2, 3.142 represents the value of π as it is a mathematical constant. 
# Line 3 stores the value of the radius to power of 3 ( the '**' is like calling pow(...) function in C language.

radius = int(input("Enter a radius of a sphere : "))

volume = volumeSphere(radius)

print("The volumn of sphere is ", volume)