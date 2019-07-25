'''
When you want to check for another condition after a condition resolves to true.

In such a situation, you can use the nested if construct.

In a nested if construct, you can have an "if...elif...else" construct inside another
if...elif...else construct.

Syntax:

The syntax of the nested if...elif...else construct:

if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else:
      statement(s)
elif expression4:
   statement(s)
else:
   statement(s)

'''

"""
x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))
 # 6 > 4
if x > y:
    #  6 > 8 
    if x > z:
        maximum = x
    else:
        maximum = z
else:
    if y > z:
        maximum = y 
    else:
        maximum = z

print("The Maximum Value is : ", maximum)
"""


#!/usr/bin/python

x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))
  #8 < 10
if x < y:
    #  8 < 6
    if x < z:
        minimum = x
    else:
        minimum = z
else:
    if y < z:
        minimum = y
    else:
        minimum = z

print("The minimum value is: " + str(minimum))