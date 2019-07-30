#/usr/bin/python

def divide(x, y):
    try:
        result = x / y
    #except Exception as abc:
    #    print(abc)
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
# Else is going to define a block of code to be executed if no errors were raised
    finally:
        print("executing finally clause")
# The Finally block lets you execute code, regardless of the results of the try and except blocks

divide(2, 0)