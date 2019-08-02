# Match Function
# Syntax : re.match(pattern,string,flags)
import re

data = "Welcome to Python World by Guido Van Rossum"

matchObject = re.match(r"(.*)GUIDO(.*)",data,re.M|re.I)

if matchObject:
    
    print(matchObject.group())
    print(matchObject.groups())

else:
    print("There is no Match Found!")