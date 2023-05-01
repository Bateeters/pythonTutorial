"""
Key function for working with files in Python is the open() function:

open(<filename>, <mode>)

different modes:
"r" Read - Default value. opens a file for reading. error if the file does not exist
"a" Append - Opens a file for appending. creates the file if it does not exist
"w" Write - Opens a file for writing. creates the file if it does not exist
"x" Create - Creates the specified file, returns an error if the file exist

You can also specify if the file should be handled as binary or text mode
"t" Text - Default value. text mode
"b" Binary - Binary mode (e.g images)
"""

# following 2 lines of code are the same because read mode is default.
# f = open("demofile.txt")
# f = open("demofile.txt", "r")


"""
Reading Text Files:
file.read()

The below code will open the file, read it and print it to the console.
file = open("testfile.txt", "r")
print(file.read())

below code will tell the code to only read the first 5 characters from the file.
print file.read(5)
"""

# Example 1:
# open file in write mode
import os
file = open("exampleFileHandling/demoFile.txt", 'w')
file.write("Hello World!")
file.close()
# if we left the write mode blank, it overwrites what was originally in the text document with a blank document when ran.

# Example 2:
# open file in read mode
file = open("exampleFileHandling/demoFile.txt", 'r')
print(file.read())
# close file
file.close()

# Example 3:
# open file in read mode
file = open("exampleFileHandling/demoFile.txt", 'r')
print(file.read(5))
# close file
file.close()


"""
print(file.readline()):     line by line output

print(file.readlines()):    read lines separately
"""

print("\n")


file = open("exampleFileHandling/demoFile.txt", 'w')
file.write("Hello World!")
file.write("\nWe love code!")
file.write("\nPython is fun.")
file.close()

# Example 4:
file = open("exampleFileHandling/demoFile.txt", 'r')
print(file.readline())
file.close()

# Example 5:
file = open("exampleFileHandling/demoFile.txt", 'r')
print(file.readlines())
file.close()


"""
Loop method to read all lines in file

file = open("testfile.txt", "r")
for line in file:
    print file.readline()

"""

print("\n")

# Example 6:
file = open("exampleFileHandling/demoFile.txt", 'r')
for line in file:
    print(file.readlines())
file.close()


"""
Writing to an existing file:

"a" or "w" mode when opening file.
"w" will overwrite entire file!

file = open("demofile.txt", "a")
f.write("text")

"""
print("\n")


file = open("exampleFileHandling/demoFile.txt", 'w')
file.write("Hello World!")
file.write("Hello World again!")
file.close()

# overwrite text originally in file
file = open("exampleFileHandling/demoFile.txt", 'w')
file.write("Overwritten!")
file.close()

file = open("exampleFileHandling/demoFile.txt", 'r')
print(file.readline())
file.close()


# Creating a file
# creates new .txt file in designated folder with designated name
file = open("exampleFileHandling/newfile.txt", "x")
file.write("New file")
file.close()


# Deleting a file:
# import os is needed for this.
# os.remove("<filename>")

# can also be used to remove a folder,
# os.rmdir("<folder>")
