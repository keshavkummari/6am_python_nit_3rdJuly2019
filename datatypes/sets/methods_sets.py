
# Union Method
aList = [1,2,3,4,5]
bList = [5,6,7]
#print(set(aList).union(set(bList)))

# Intersection Method 
#print(set(aList).intersection(set(bList)))

# Difference Method
#print(set(aList).difference(set(bList)))

# Update Method
#s = set([1,2,3,4,5])
#s.update(set([5,6,7]))
#print(s)

# Add Method
#s = set([1,2,3,4,5])
#s.add(6)
#print(s)

# Discard & Remove Methods
#s = set([1,2,3,4,5])
#s.discard(5)
#print(s)
#s.remove(6)
#print(s)


# Copy Method
"""
s = set([1,2,3,4,5])
t = s.copy()
print(s)
print(t)

print(s == t)
print(id(s))
print(id(t))
print(s is t)
"""

# POP Method :
"""
s = set([1,2,3,4,5])
print(s)
print(s.pop())
print(s)
"""

# issubset and issuperset Methods
s = set([2,9,7,1])
s1 = set([2,9,7,1])
t = set([1,7])
t1 = set([1,2,3,4])
t2 = set([1,2,3,4,5,6,7,8,9])

#print(s.issubset(s1))
#print(set(s).issubset(t))
#print(set(s).issubset(t1))
#print(set(s).issubset(t2))

print(set(s).issuperset(t))
print(set(s).issuperset(t1))
print(set(s).issuperset(t2))
