"""
A dictionary is a mutable mapping from keys to values.

A dictionary with no keys is called an empty dictionary.

Dictionaries are also known in some programming languages as
associative memories,associative arrays, or hashmaps.

Unlike sequences, which are indexed by a range of integers,
dictionaries are indexed by keys, which can be of any immutable type.

Thus, dictionaries are also unordered.

When printed, iterated upon, or converted into a sequence,
its elements will appear in an arbitrary, implementation-dependent order.
"""

# Creating Dictionaries in Python

#!/usr/bin/python

dict1 = {'Name': 'minnu', 'Age': 7, 'Class': 'First'}

print(dict1)
#print(dict1,type(dict1),id(dict1),len(dict1),dict(enumerate(dict1)))


# Updating Dictionaries in Python
#dict1['Age'] = 10

#print(dict1)

# Deleting a Key from a Variable or Delete a Element
#del dict1['Class']
#del dict1

#print(dict1)

# Accessing of Keys from a Variable
"""
guido = {'Name':'Van', 'Age':60, 'Class':'First'}

print(guido,type(guido),id(guido),len(guido))

print(dict(enumerate(guido)))

print("guido['Name']: ", guido['Name'])
print("guido['Age']: ", guido['Age'])
print("guido['Class']: ", guido['Class'])
"""

# Methods
fileName = {'Course':'Python', 'type':'Video', 'boolean': 1 }

sample = {1: "one", 2 : "two"}

print(fileName.get('type'))

print(fileName.keys())

print(fileName.values())

print(fileName['Course'])

print(fileName.items())