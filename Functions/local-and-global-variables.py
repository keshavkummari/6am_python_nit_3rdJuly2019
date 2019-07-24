#!/usr/bin/python

# Global Variables
global0 = 100
global1 = 200

abc = "Syed"

def multiply(numberOne, numberTwo):
    'This function multiplies'
    abc1 = numberOne*numberTwo  # Local Variable
    print ("Local Variable : ",abc1)
    print("Global Variable :  , abc")
    print ("Global Variable : ",global0)
    print ("Global Variable : ",global1)
    return

#multiply(_global0,_global1)

multiply(10,20)

# print(abc1) # Local Variable
#print(multiply(5,6))