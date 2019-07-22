'''--------------------------------------------------------------'''
# 6. Membership Operators :
'''--------------------------------------------------------------'''

'''
in and not in are the membership operators in Python. 

They are used to test whether a value or variable is found in a sequence
(string, list, tuple, set and dictionary).
'''
# Membership operators test for membership in a sequence, such as
# strings, lists, or tuples.

# 1. in	    = x in y, here in results in a 1 if x is a member of sequence y.
# 2. not in   = x not in y, here not in results in a 1 if x is not a member of sequence y.

x = 'Hello world'
y = {1:'a',2:'b'}

print('h'.swapcase() in x)

print(1 in y)

print('hello' not in x)