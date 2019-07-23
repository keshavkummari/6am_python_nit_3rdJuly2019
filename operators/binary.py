"""
#ipaddress = "192.168.0.3"

a = 192
b = 168
c = 0
d = 3

print(bin(a),bin(b),bin(c),bin(d))
"""

# True : 1
# False: 0

a = 15
b = 10

print(bin(a)) # 0b1111

print(bin(b)) # 0b1010

'''
1 = True and 0 = False : False 0
1 = True and 1 = True  : True  1 
1 = True and 0 = False : False 0
1 = True and 1 = True  : True  1 
'''

print(f"Results of {bin(a)} AND {bin(b)} = {bin(a&b)}")
# Results of 0b1111 AND 0b1010 = 0b1010

# Bitwise OR Operator
print(f"Results of {a} : {bin(a)} {b} : {bin(b)} = {bin(a|b)}")

# Results of 15 : 0b1111 10 : 0b1010 = 0b1111
'''
1 = True and 1 = True  : True  1 
1 = True and 1 = True  : True  1 
1 = True and 1 = True  : True  1 
1 = True and 1 = True  : True  1 
'''

# XOR ^ Operator

print(bin(a^b))

'''
0b1111
0b1010
-------
0b0101
'''

#!/usr/bin/python3

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

#c = a & b        # 12 = 0000 1100
#print ("result of AND is ", c,':',bin(c))

#c = a | b        # 61 = 0011 1101
#print ("result of OR is ", c,':',bin(c))

#c = a ^ b        # 49 = 0011 0001
#print ("result of EXOR is ", c,':',bin(c))

c = ~a           # -61 = 1100 0011
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2      # 240 = 1111 0000
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2       # 15 = 0000 1111
print ("result of RIGHT SHIFT is ", c,':',bin(c))

