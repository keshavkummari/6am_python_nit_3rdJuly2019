#!/usr/bin/python

class JustCounter:
    __secretCount = 5
   
    def count(self):
       self.__secretCount += 1
       print (self.__secretCount)
 
counter = JustCounter()
counter.count()  # 6
counter.count()  # 7
counter.count()  # 8
#print(counter.__secretCount)
print(counter._JustCounter__secretCount)