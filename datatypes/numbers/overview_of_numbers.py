
# Integers : int()
# Floating Point Numbers : float()
# Complex Numbers : complex()

"""
a = 5 
print(a, "is of type", type(a))

a = 2.0
print(a, 'is of type', type(a))

a = 1-2J 
print(a, "is complex numbers?", isinstance(1-2J, complex))

"""
import math
"""
a1 = 5
print(math.fabs(a1))
print(math.ceil(-10.1))
print(math.floor(-10.7))
print(math.modf(22.67))
print(math.exp(6.1))
print(math.sqrt(45))
"""

import random

"""
print("Random-Choice",random.choice([1,2,3,4,5,9]))

print(random.randrange(0,10,2))

print(random.random())
random.seed(5)
print(random.random())
random.seed(5)
print(random.random())
"""
#print(random.shuffle())

aList = [20,16,30,40,5,9]
print("Before",aList)
random.shuffle(aList)
print("After",aList)
