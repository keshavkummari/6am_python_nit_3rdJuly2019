#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]

oneMoreList = [22, 34, 56,34, 34, 78, 98]

#print(aCoolList,list(enumerate(aCoolList)))
print("")
aCoolList.insert(0,"Guido Van Rossum")
print(aCoolList,list(enumerate(aCoolList)))
#print (oneMoreList,list(enumerate(oneMoreList)))
print("")

'''
3. list.insert(i, x) :in
Insert an item at a given position. 
The first argument is the index of the element before which to insert, 
so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to
a.append(x).
'''