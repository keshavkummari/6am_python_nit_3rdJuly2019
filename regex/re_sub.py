import re

data = "9908-823-070 # This is Phone Number"

print(data)

num = re.sub(r'#.*$',"",data)

print(num)

#num = "9908-823-070"

num = re.sub(r'\D',"",data) # 9908823070

print(num)