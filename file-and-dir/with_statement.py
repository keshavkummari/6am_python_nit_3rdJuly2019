
with open("/Users/keshavkummari/6am_python_nit_3rdJuly2019/file-and-dir/test.txt","r+a") as file:
    #print(file.read())
    print(file.tell())
    print(file.seek(0))
    #print(file.write("Our Next Topic is RegEx"))
    print(file.read())
