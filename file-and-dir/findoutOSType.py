import os sys

if sys.platform == "win32":
    print("We are on Windows",os.uname())
    command = "C:\\winnt\\system32\\cmd.exe"
    params = ["uname -a"]
    print(command)

elif sys.platform == "darwin":
    print("We are on MacOS", os.uname())
    print("%s" %(sys.platform))
    command = "/usr/bin/uname"
    params = ['uname','-a']
    print(command)