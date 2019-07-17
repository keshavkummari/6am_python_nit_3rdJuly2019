'''
A tuple is an immutable sequence of values of any type.
Tuple elements are indexed by sequential integers, starting with zero.

Tuples are constructed by the comma operator,
with or without enclosing parentheses.

An empty tuple must have the enclosing parentheses.

A single item tuple must have a trailing comma.
'''
#!/usr/bin/python

tup1 = ('python', 'linux', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "A", "B", "C", "E",5,"$"
tup4 = """A""","""B""","""C""","""E"""
tup5 = 'a', 'b', 'c', 'd'
tup6 = '''a''', '''b''', '''c''', '''d'''

print (tup1,type(tup1),id(tup1),len(tup1))

print (tup2,type(tup2),id(tup1),len(tup2))

print (tup3,type(tup3),id(tup1),len(tup3))

print (tup4,type(tup4),id(tup1),len(tup4))

print (tup5,type(tup5),id(tup5),len(tup5))

print (tup6,type(tup6),id(tup6),len(tup6))

# Call the tuple using index:
print (tup3[1])

print(tuple(enumerate(tup1)))
