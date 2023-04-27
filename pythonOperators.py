"""
Python Operator types include:
arithmetic
assignment
comparison
logical
membership
identity
bitwise
"""

"""
Arithmetic Operators:
used to perform arithmetic operations between variables.
addition (+)
subtraction (-)
multiplication (*)
division (/)
modulus (%)
exponentiation (**)
flow division (//)
"""

# Arithmetic Operators:
print("Arithmetic Operators:")
x = 10
y = 20

# addition
print(x+y)

# subtraction
print(x-y)

# multiplication
print(x*y)

# exponentiation, x to the y power
print(x**y)

# division
print(x/y)

# flow division
print(x//y)

# modulus, gives the remainder of x/y
print(x % y)


"""
Assignment Operators:
used to assign values to a variable or any value.
=
+=
-=
*=
%=
**=
//=
|=
^=
&=
"""

# Assignment Operators
print("\n\n\nAssignment Operators:")


# the lines below are the same
x = 100
x += 10
print(x)

x = 100
x = x+10
print(x)

# equal to
print("\nEqual to:")
a = 5
print(a)

# plus is equal to
print("\nplus is equal to:")
# same as a = a+5
a += 5
print(a)

# exponentiation is equal to:
print("\nExponentiation is equal to:")
# same as a = a**5
a **= 5
print(a)


"""
Comparison Operators: (Boolean)
used to compare values.
equal (==)
not equal (!=)
greater than (>)
less than (<)
greater than or equal (>=)
less than or equal (<=)
"""

# Comparison Operators
print("\n\nComparison Operators:")
val = 10
num1 = 20
print(val)
print(num1)

# are they the same
print("\nvariables are equal to:")
compare = val == num1
print(compare)

"""
Logical Operators:
used to combine conditional statements. (conditional statements include: if, elif, else)
logical operators indlude:
and
or
not
"""

# Logical Operators:
print("\n\nConditional Statements:")
print(val, num1)

# if statement
if val == num1:  # are the numbers the same?
    print('equal')
elif val > num1:  # is val greater than num1?
    print('greater')
else:  # is val less than num1?
    print('smaller')

print("\nLogical Operators:")
x = 10

print("\nand:")
# is x greater than 10 AND 5?
print(x > 10 and x > 5)
# false, x is greater than 5 but equals 10

# is x greater than 8 and 5?
print(x > 8 and x > 5)
# true, x is greater than both

print("\nor:")
# is x greater than 10 or 5?
print(x > 10 or x > 5)
# true, x is greater than 5

# is x greater than 10 or 12?
print(x > 10 or x > 12)
# false, x is less than both

print("\nnot:")
# is x not greater than 10 and 5?
print(not (x > 10 and x > 5))
# true, not gives the opposite value that would be returned from the statement


"""
Identity Operators:
used to compare objects.
identity operators indlude:
is - true if both variables are same object
is not - true if variables are not same object
"""

# Identity Operators:
print("\n\nIdentity Operators:")
# creating 2 lists
list1 = [10, 20, 30]
list2 = [10, 20, 30]
print(list1)
print(list2)

# assigning x
x = list1

# compare x and list1
print(x is list1)
# true, x was assigned as list1

# compare list1 and list2
print(list1 is list2)
# false, list1 and list2 may have the same elements but they are two different lists.

print(list1 is not list2)
# true

"""
Membership Operators:
used to check if a sequence is present in an object.
membership operators indlude:
in - true if a sequence with the specified value is present in the object
not in - true if a sequence with the specified value is not present in the object
"""

# Membership Operators:
print("\n\nMembership Operators:")

print(10 in list1)
print(list1 in list2)
print(list1 == list2)

"""
Bitwise Operators:
used to compare binary numbers.
bitwise operators indlude:
bitwise AND (&) - sets each bit to 1 if both bits are 1.
bitwise OR (|) - sets each bit to 1 if one of the bits is 1.
bitwise XOR (^) - sets each bit to 1 if only one of the bits is 1.
bitwise NOT (~) - Inverts all bits.
Left Shift (<<) - shift left by pushing in zeroes from the right and let the leftmost bits fell off.
Right Shift (>>) - shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bit fall off
"""

# Bitwise Operators:
print("\n\nBitwise Operators:")
print("bitwise AND:")
print(10 & 12)  # prints 8
# 10 in binary = 1010
# 12 in binary = 1100
# & means if both bits are 1 then it sets the bit to 1.
# 10 & 12 = 1010 & 1100 = 1000 = 8 in binary

print("\nbitwise OR:")
print(10 | 12)  # prints 14
# 1010
# 1100
# -----
# 1110

print("\nright shift:")
print(10 >> 2)  # prints 2
# 1010
# shift 2 bits right = 10 = 2 in binary

print("\nleft shift:")
print(10 << 2)  # prints 40
# 1010
# shift 2 bits left = 101000 = 40 in binary
