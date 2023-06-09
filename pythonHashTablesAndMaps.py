"""
A Hash Table or Hashmap is a type of data structure that maps keys to its value pairs.
It implements the abstract array data type.
Basically makes use of a function that computes an index value that in turn holds the elements to be searched, inserted, removed, etc...
Makes data fast and easy to access.
Hash tables store key value pairs and the key is generated using a has function.

Hash tables or hashmaps in python are implemented through the built-in dictionary data type.
The keys of a dictionary in python are generated by a hashing function.
The elements of a dictionary are not ordered and can be changed.
"""

import pandas as pd
print("Create a starting dictionary")
my_dict = {'Dave': '001', 'Ava': '002', 'Joe': '003'}
# show that dictionary is created
print(my_dict)
# show the type of the dictionary
print(type(my_dict))

print("\nCreating Blank dictionary:")
new_dict = dict()
print(new_dict)
print(type(new_dict))

# adding values to blank dictionary
new_dict = dict(Dave='001', Ava='002')
print(new_dict)

# nested Dictionaries
print("\n\nNested Dictionaries:")
# nested dictionaries are dictionaries that lie within other dictionaries

# dictionary with employees
emp_details = {'Employee':
               {'Dave':
                # dictionary with Dave's information
                {'ID': '001', 'Salary': '2000', 'Designation': 'Team Lead'},
                'Ava':
                # dictionary with Ava's information
                {'ID': '002', 'Salary': '1000', 'Designation': 'Associate'}
                }
               }
print(emp_details)

# Hash Table Operations
print("\n\n\nHash Table Operations:")

print("\nAccessing Items:")
# Starting dictionary
print(my_dict)

# Get value associated with the key 'Dave'
print(my_dict['Dave'])

# show all the keys present in my_dict
print(my_dict.keys())

# show all the values present in my_dict
print(my_dict.values())

# get value associated with requested key, 'Ava'
print(my_dict.get('Ava'))

print("\nUsing loops to print dictionaries:")
# using a loop to print each key in my_dict
for x in my_dict:
    print(x)

# using a loop to print each value in my_dict
print("\nvalues instead of keys")
for x in my_dict.values():
    print(x)

# using loop to print each key WITH their value in my_dict
print("\nBoth key and value")
# x,y because you are returning two elements rather than just a key or value
for x, y in my_dict.items():
    print(x, y)


# Updating Values
print("\n\nUpdating:")
# starting dictionary
print(my_dict)

# update Dave's id to 004 from 001
my_dict['Dave'] = '004'

# add new value
my_dict['Chris'] = '003'

print(my_dict)


# Deleting Values
print("\n\nDeleting:")
# starting dictionary
print(my_dict)

# pop function - returns value and delete's both value and key associated with specified key
print(my_dict.pop('Ava'))
print(my_dict)

# popitem function - same functionality as pop but targets last added item (key AND value).
print(my_dict.popitem())
print(my_dict)

# del function - removes key and value specified WITHOUT returning it
del my_dict['Dave']
print(my_dict)


# Converting a dictionary into a Dataframe
"""
A dataframe is a 2D data structure that consists of colums of various types.
It is very similar to a Python dictionary and you can even convert a dictionary into a pandas dataframe.
"""

print("\n\n\nDictionary to Dataframe:")
# import pandas

# changing 'emp_details' nested dictionary to pandas dataframe
df = pd.DataFrame(emp_details['Employee'])
print(df)
