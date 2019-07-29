import sys
import os

f = open("/Users/keshav/6am_python_nit_3rdJuly2019/ExceptionHandling/test.sh")

for var in f:
    try:
        f = open(var, 'r')
    except IOError:
        print("Can Not Open", var)
    else:
        print(var, "has", len(f.readlines()), 'lines')
        f.close()