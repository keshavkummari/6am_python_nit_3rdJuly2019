import os 

# Present Working Directory
print(os.getcwd())

# List the Present Working Directory Content
print(os.listdir(os.getcwd()))
#OR
print(os.listdir("/Users/keshavkummari/6am_python_nit_3rdJuly2019/file-and-dir"))

# UID
print(os.getuid())

# GID 
print(os.getgid())
# cat /etc/passwd | grep 'keshav' 

# To return information about OS
print(os.uname())

# Create a Directory
#print(os.mkdir("aws_azure"))

# Rename a Directory
#print(os.rename("aws_azure","aws_test"))

print(os.chdir("/Users/keshavkummari/6am_python_nit_3rdJuly2019/"))

print(os.getcwd())