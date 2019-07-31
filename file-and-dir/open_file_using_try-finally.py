
"""
try:
    varable_name = open("file.txt","rt")
    perform file operations
finally:
    varable_name.close()
"""

import os

try:
    file = open("/Users/keshavkummari/6am_python_nit_3rdJuly2019/file-and-dir/test.txt","rt")
    print(file.tell())
    #print(file.seek())
    print(file.readline())
    print(file.tell())
    print(file.seek(0))
    print(file.tell())
    print(file.read())
    print(file.tell())
finally:
    file.close()