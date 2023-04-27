# Array - a data structure which can hold more than one value at a time.
# It is a collection or ordered series of elements of the same type.
# indexing always starts from 0


"""
Difference between lists and arrays:
Both store data the same way.
Arrays only take a single data type value, lists store any data type value.
This means the operations performed on them are different.
"""

# to use arrays in python, you need to import the module

# 3 different ways of importing array:
# import array (without alias)
# import array as arr (using alias)
# from array import * (using *)

import array as arr

# creating a base array
print("Starting Array:")
# array (of int values, [values])
a = arr.array('i', [1, 2, 3, 4, 5, 6])
print(a)

# Accessing elements example
print("\n\nAccessing Elements:")
# access value at index 2
print(a[2])


# Basic array operations
print("\n\nBasic Array operations:")
print("starting array:")
print(a)
# Arrays are mutable (changeable)

# find length of array
print("\n\nFind length of array:")
# len() function returns an integer value that is equal to the number of elements in the array.
print(len(a))

# adding/changing element of array
print("\n\nAdding/changing element of array:")
# append() - add a single element at the end of an array.
# extend() - add more than one element at the end of an arrary.
# insert() - add an element at a specific position in an array.

print(a)
print("\nappend:")
a.append(8)
print(a)

print("\nextend:")
a.extend([9, 8, 6, 5, 4])
print(a)

print("\ninsert:")
a.insert(2, 6)
print(a)


# remove/delete element of array
print("\n\nRemove/delete element of array:")
# pop - remove an element and return it
# remove - remove an element with a specific value (first occurance) without returning it.
print(a)

print("\npop:")
print(a.pop())
print(a)

print("\npop(index value):")
print(a.pop(2))
print(a)

print("\npop(negative index value):")
print(a.pop(-1))
print(a)

print("\nremove:")
print(a.remove(8))
print(a)

# Array concatenation
print("\n\nArray concatenation (combining arrays):")
b = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
c = arr.array('i', [3, 5, 7, 5, 3, 2, 1])
print("New Arrays:")
print(b)
print(c)

d = arr.array('i')
print("\nEmpty Array:")
print(d)

d = b+c
# concantenated b and c into array d
print(d)
# both arrays must be same data type or else will return error.

# Array Slicing
print("\n\nArray Slicing:")
print("\nOriginal array:")
print(d)

# print only values in indexes 0-4 (go to but do not include 5)
print("\n array sliced 0:5")
print(d[0:5])

# slicing using negative index values
print("\n using negative index values, 0:-2")
print(d[0:-2])


# Loop through an array
print("\n\nLoop through an array:")
# for loop - iterates over the itesm of an array specified number of times.
# while loop - iterates over the elements until a certain condition is met.

print("\nstarting array:")
print(d)

print("\nbasic for loop:")
# for every element in d: print the element
for x in d:
    print(x)

print("\nSlicing for loop:")
# for every element in d[0:3]: print element
for x in d[0:3]:
    print(x)

print("\nBasic while loop:")
# counter for while loop (used to make sure it does not run forever)
index = 0

# while index is less than d[5]: print d[index] AND add 1 to index
# this includes and prints value at d[5]
while index < d[5]:
    print(d[index])
    index += 1

print("\nWhile loop using len()")
print("starting array:")
print(a)

# counter for while loop
counter = 0
# loop to go through entire array a and print every element
while counter < len(a):
    print(a[counter])
    counter += 1
