
"""
file = open("/Users/keshavkummari/6am_python_nit_3rdJuly2019/file-and-dir/test.txt","r")

#print(file)
#print(type(file))
#print(id(file))

print(file.read())
print(file.readline())
print(file.readlines())

file.close()
"""

"""
# Python File Modes:
------------------
Mode	Description
'r'		Open a file for reading. (default)
'w'		Open a file for writing. Creates a new file if it does not 
		exist or truncates the file if it exists.
'x'		Open a file for exclusive creation.
                If the file already exists, the operation fails.
'a'		Open for appending at the end of the file
                without truncating it. 
		Creates a new file if it does not exist.
't'		Open in text mode. (default)
'b'		Open in binary mode.
'+'		Open a file for updating (reading and writing)

"""