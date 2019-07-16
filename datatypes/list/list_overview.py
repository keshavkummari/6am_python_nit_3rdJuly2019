'''
A list is a mutable sequence of values of any type.

A list with zero elements is called an empty list.

List elements are indexed by sequential integers, starting with zero.
'''

list()

cloud_providers = ["aws",'azure',"gcp"]

print(cloud_providers,type(cloud_providers),len(cloud_providers))

print(list(enumerate(cloud_providers)))