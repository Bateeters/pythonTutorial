# single line comment

# comments in python
# multi-line comments shortcut method
# Hold alt and click at the begining of each line

"""
Docstring comments
they are not omitted by the interpreter
comments are omitted
"""

x = 100

print(x)

# datatypes:

# numbers
# integer:
# x = 10

# float:
# x = 10.234

# Complex:
# x = 25j

# string
# list
# dictionary
# tuple
# set

# number data type------------------------------------------------------------
print("\nNumber data types")
print(type(x))
x = 10.25
print(x)
print(type(x))

x = 10j
print(x)
print(type(x))

num = 10 > 9
print(num)
print(type(num))

# string data type--------------------------------------------------------------------
print("\nString data types")
name = 'edureka'
print(name)
print("\nlength of name variable:")
print(len(name))

# get letter associated with index supplied
print(name[2])
# negative numbers start at end of string and move left
print(name[-1])
print(name[-2])

# showing only specified section of string
print(name[2:8])
print(name[2:7])
print(name[2:6])

# changing letter case
print(name.upper())
print(name.lower())
print(name.capitalize())

# list data type-----------------------------------------------------------------------
print("\nList Data:")
mylist = [10, 20, 30, 30, 'edureka', 'courses']
print(mylist)

# printing values at index 2,3,and 4.
# Stop at 5 but does not print it
print(mylist[2:5])

# changing value in list at index 2
mylist[2] = 35
print(mylist)

# adding value to list using .append()
# append ads value to end of list.
mylist.append(10)
print(mylist)

# adding values to list at specified index using .insert()
# it does not override other values, just pushes them back in list
# .insert(x,y)
# x = index to place it at,
# y = value being inserted
mylist.insert(5, 100)
print(mylist)

# reverse list order
mylist.reverse()
print(mylist)

# dictionary data type---------------------------------------------------------------
print("\nDictionaries:")

# create dictionary named courses
# dictionaries are set up with "key: value" layout

courses = {1: 'python',
           2: 'data science',
           'third': 'machine learning'}

# showing dictionary is created
print(courses)

# different ways to get value at "third" key
print(courses['third'])
print(courses.get('third'))

# dictionaries are not indexed which means you cannot get values based on index number/order
# this means you need to use the key in order to return associated value
# below function will bring back an error instead of 'python'
# print(courses[0])

# changing value at a given key
courses['third'] = 'hadoop'
print(courses)

# adding value to end of dictionary
courses['fourth'] = 'machine learning'
print(courses)

# tuple data type---------------------------------------------------------------
# tuples cannot be changed once written
# allows duplicates
print("\nTuples:")

# creating tuple named animals
animals = (10, 10, 20, 'tiger', 'lion', 'giraffe', 'tiger')

# showing tuple is created
print(animals)

# get value at specified index
print(animals[2])

# you can check how many times something is in the tuple
print(animals.count('tiger'))

# set data type---------------------------------------------------------------
# sets cannot be changed once written
# no duplicates
print('\nSets:')

# creating set named myset
myset = {10, 20, 30, 40, 40, 30, 'edureka', 'courses'}

# showing set is created
print(myset)

# set objects do not support indexing
# you cannot get value from inputing an index number
# below function will give error
# print(myset[2])

# range function ----------------------------------------------------------------------
print('\nrange function:')

print(range(10))

# printing numbers 0-10
# you create a list with the range function
# range(11) will count from 0 to, but not inclue, 11
# as it counts, it will add each number to list
print(list(range(11)))

# you can also make a list with other data types ----------------------------------------------
print('\nList with multiple data types:')

# create list a
a = [1, 2, 3, 4]
# create dictionary b
b = {4, 5, 6, 4, 6}

# showing a and b are created
print(a)
print(b)

# merge list a and dictionary b into a new list together
c = [a, b]
print(c)

# a and b are counted as their own index rather than each element indexed
print(c[1])

# data type conversion--------------------------------------------------------------------
print('\nData type conversion:')

# number variable (int)
x = 10

# string variable (str)
name = 'name'

print(x)
print(name)

# you cannot add an int and str together
# below function will give an error
# print(x+name)

# str() changes passed value to string
# when strings are added together, they will be combined with no space between them
print(str(x) + name)

# converting dictionary b to a list
print(b)
print(list(b))
