"""
Data Structures: Sets

A set is an unordered collection without duplicates.

When printed, iterated upon, or converted into a sequence,
its elements will appear in an arbitrary, implementation-dependent order.

"""
# String Example 
a = "a b c a b c"
print(a, type(a))
print(set(a))

# List Example 
alist = ['aws',10,20.75,'azure','gcp','python','aws','azure',10,20.75]
print(set(alist))

# Tuple Example 
aTuple = 'aws',10,20.75,'azure','gcp','python','aws','azure',10,20.75
print(set(aTuple))

# Dictionaries Example 
aDict = {'CloudVendor':'AWS','Programming':"Python",'CloudVendor':'AWS','Programming':"Python"}
print(set(aDict))

# Numbers Example 
aNumber = '1020304050'
print(set(aNumber))