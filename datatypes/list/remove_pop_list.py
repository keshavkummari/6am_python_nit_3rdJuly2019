#!/usr/bin/python
aCoolList = ["superman", "spiderman", 1947,1987,1947,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]

print (list(enumerate(aCoolList)))

#aCoolList.remove(1947)
#aCoolList.pop()
aCoolList.pop(3)
print("")
print(list(enumerate(aCoolList)))

