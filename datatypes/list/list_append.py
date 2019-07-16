#!/usr/bin/python
a_list = [1, 2, 3]

print(a_list,type(a_list),id(a_list),len(a_list))
print(list(enumerate(a_list)))

a_list.append(4)

print(a_list,type(a_list),id(a_list),len(a_list))
print(list(enumerate(a_list)))

a_list.append([5, 6, 7])
print(a_list,type(a_list),id(a_list),len(a_list))
print(list(enumerate(a_list)))

a_list.append("Guido")
print(a_list,type(a_list),id(a_list),len(a_list))
print(list(enumerate(a_list)))