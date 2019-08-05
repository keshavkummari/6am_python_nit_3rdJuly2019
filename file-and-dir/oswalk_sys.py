import os
import sys
import fnmatch 

# Find all .mp3 files on my operating system

rootpath = '/Users/keshavkummari/'

pattern = "*.mp3"

for varExpression1,varExpression2,varExpression3 in os.walk(rootpath):
    for var in fnmatch.filter(varExpression3,pattern):
        print(os.path.join(varExpression1, var))