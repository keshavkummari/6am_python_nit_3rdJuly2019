# Search Function
# Syntax : re.match(pattern,string,flags)
import re

data = '''
Welcome 
to 
Python 
World 
by 
Guido Van Rossum
'''

searchObject = re.search(r"(.*)GUIDO(.*)",data,re.M|re.I)

if searchObject:
    
    print(searchObject.group())
    print(searchObject.groups())

else:
    print("There is no Match Found!")