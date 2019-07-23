"""
# Python Operators:

# There are 7 types of Operators :

1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

"""

'''--------------------------------------------------------------'''
# 1. Arithmetic Operators:
'''--------------------------------------------------------------

1. +   =	Addition
2. -   =	Subtraction
3. *   =	Multiplication
4. /   =	Division  
5. %   =	Modulus
6. **  =	Exponent
7. //  =	Floor Division

'''

# Python3 code to demonstrate
# each occurrence frequency using
# naive method

# initializing string
test_str = "Hyderabad"

# using naive method to get count
# of each element in string
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print("Count of all characters in Hyderabad is :\n " + str(all_freq))



