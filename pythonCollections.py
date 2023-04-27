"""
collections in python are basically container data types:
- lists
- tuples
- sets
- dictionaries

They have different characteristics based on declaration type and usage.
"""

"""
Lists:
- declared using []
- mutable (you can change the values)
- stores duplicate values
- allows get by index values
"""

"""
Tuples:
- ordered
- immutable (you cannot change the values inside once it is declared)
- can have duplicates of the same value
"""

"""
Sets:
- unordered
- declared using {}
- not indexed (cannot access elements inside using index values)
- no duplicates
"""

"""
Dictionaries:
- "key: value" pairs
- mutable (able to change values)
- declared using {}
- not indexed (use "key" to get associated value)
"""


"""
Collection Module:
Collections have specialized data structures which cover the shortcomings of the above mentioned data types.
Do not need to install like other modules, just need to import it.

namedtuple()
Chainmap
deque
Counter
OrderedDict
defaultdict
UserDict
UserList
UserString
"""

# namedtuple() - returns a tuple with a named value for each element in the tuple.
# overcomes the problem of accessing the elements using the index values
# you do not need to remember the index values

# Namedtuple Examples:
# import namedtuple

from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import ChainMap
from collections import deque
from collections import namedtuple
print('Namedtuple Examples:')
#           (name of tuple,    values of tuple)
a = namedtuple('courses', 'name, technology')
s = a('data science', 'python')
print(s)

# How to get value or implement a tuple using a list
print('\nUsing a list to get values or implement a tuple:')
s = a._make(['artificial intelligence', 'python'])
print(s)


# deque (pronounced "deck") - an optimised list to perform insertion and deletion easily.
# Deque(['e','d','u','r','e','k','a'])

# Deque Examples:
# import deque
print('\n\nDeque Examples:')
print('starting deque:')
a = ['e', 'd', 'u', 'r', 'e', 'k', 'a']
d = deque(a)
print(d)

# Add element to deque
print('\nAdding "python" to deque:')
d.append('python')
print(d)

# Adding element to beginning of deque
print('\nAdding element to beginning of deque:')
d.appendleft('first')
print(d)

# Remove last value from deque
print('\nRemove last value from deque:')
d.pop()
print(d)

# Remove first value from deque
print('\nRemove first value from deque:')
d.popleft()
print(d)


# Chainmap - a dectionary like class for creating a single view of multiple mappings.
# A = {1:'edureka', 2:'python'}
# B = {3:'data science', 4:'AI'}
# [{1:'edureka', 2:'python},{3:'data science', 4:'AI'}]

# ChainMap Examples:
# import ChainMap
print('\n\nChainMap Examples:')
print('starting dictionaries:')
a = {1: 'edureka', 2: 'python'}
b = {3: 'ML', 4: 'AI'}
print(a)
print(b)

print('\nUsing ChainMap:')
a1 = ChainMap(a, b)
print(a1)


# Counter - a dictionary subclass for counting hashable objects.

# Counter Examples:
# import Counter
print('\n\nCounter Examples:')
print('\nStarting list:')
a = [1, 1, 2, 3, 2, 2, 4, 5, 4, 5, 4, 3, 6, 2, 2]
print(a)

print('\nUsing Counter:')
c = Counter(a)
print(c)
# Counter returns how many times each appears in the list using a dictionary.
# 2 appears 5 times "2: 5" and so on.

# Using elements function
print('\nElements function:')
print(list(c.elements()))
# returns a list of elements in the counter (ordered)

# Using most_common fuction
print('\nmost_common fuction:')
print(c.most_common())
# returns sorted list with the count of each element inside the counter

# Using subtract function
print('\nsubtract function:')
# subtract 2, 1 time and 6, 1 time
sub = {2: 1, 6: 1}
c.subtract(sub)
# checking to see if values were subtracted (removed)
print(c.most_common())


# OrderedDict - dictionary subclass which remembers the order in which the entries were done.
# Even if you change the value of the Key, the position will not be changed because of the order in which it was added.


# OrderedDict Example
# import OrderedDict
print('\n\nOrderedDict Examples:')
print('Starting OrderedDict:')
d = OrderedDict()
print(d)

# Adding to dictionary d
d[1] = 'e'
d[2] = 'd'
d[3] = 'u'
d[4] = 'r'
d[5] = 'e'
d[6] = 'k'
d[7] = 'a'
print('\ndictionary after adding values:')
print(d)

print('\nGet keys of the dictionary:')
print(d.keys())
# Only returns keys of dictionary

print('\nGet items of the dictionary:')
print(d.items())
# Returns the items of the dictionary and the keys associated with them

print('\nChanging a value of the OrderedDict:')
d[1] = 'python'
print(d)
# value 'e' changes to 'python' without moving it in the order of values in the dictionary


# defaultdict - a dictionary subclass which calls a factory function to supply missing values.
# does not throw errors when a missing key value is called in a dictionary.

# defaultdict example:
# import defaultdict
print('\n\ndefaultdict Examples:')
print('starting dictionary:')
d = defaultdict(int)
d[1] = 'python'
d[2] = 'edureka'
print(d)

print('\nGet value at key 3 (no value added there)')
print(d[3])
# returns "0" instead of "KeyError: 3" that would be returned from normal dictionary.


# UserDict - a wrapper around dictionary objects for easier dictionary sub-classing.
# UserList - a wrapper around list objects for easier List sub-classing.
# UserString - a wrapper around string objects for easier string sub-classing.
