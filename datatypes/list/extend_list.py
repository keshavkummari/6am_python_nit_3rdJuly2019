#!/usr/bin/python
aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]

# Before:
print (aCoolList)
print (oneMoreList)

aCoolList.extend(oneMoreList)
# After:
print (aCoolList)