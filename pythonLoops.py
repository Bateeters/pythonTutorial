"""
Remove docstrings around a specific program if wanting to run it.
Add docstrings around a program if wanting to skip it.
"""

# While Loops -------------------------------------------------------------------------------
# While loops - used when you don't know how many iterations are required.

from math import sqrt
import random
print("While Loops:")

# while loop counting to 9 --------------
count = 0  # counter for loop

while count < 9:  # while count is less than 9
    print("number:", count)  # print the count
    count += 1  # add 1 to the count
# restart loop til count = 9
print("Goodbye")  # exit loop once count = 9


"""
Docstring'd out to run rest of program

# guessing game ---------------------------
# import random to generate random number
n = 20
# will generate random number between 0 and 20 (without +1 it would be 0-19)
to_be_guessed = int(n*random.random())+1
guess = 0  # creating variable for user's guess
while guess != to_be_guessed:  # while uer's guess is not generated number
    guess = int(input("New number: "))  # ask for new guess
    if guess > 0:  # if guess is higher than 0
        if guess > to_be_guessed:  # if guess is higher than generated number
            print("Number too large")
        elif guess < to_be_guessed:  # if guess is lower than generated number
            print("Number too small")
    else:  # if guess is lower than 0
        print("sorry that you're giving up!")
        break  # exit loop
else:  # if guess is generated number
    print("Congratulations. You made it!")
"""


# For Loops --------------------------------------------------------------------------------------------------
# for loops - used when you know the number of iterations required

print("\n\n\nFor Loops:")

# for <variable> in <range>:
#   statement 1
#   statement 2
#   ...

# using for loop to print items in list ----------------------
fruits = ['Mango', 'Grapes', 'Apple']

for fruit in fruits:  # for items in "fruits" list
    print("current fruit:", fruit)  # print items line by line
# once end of "fruits" list is reached, loop ends
print("Goodbye")


"""
Docstring'd out to run rest of program

# using for loop to find factorial of a number ----------------------

num = int(input("Number:"))  # input number wanting to be factored
factorial = 1

if num < 0:  # if user input is less than 0
    print("must be positive")
elif num == 0:  # if user input is 0
    print("Factorial = 1")
else:  # if user input is greater than 0
    # for number in range of 1 to user input +1 (DOES NOT INCLUDE num+1, makes range 1-num)
    for i in range(1, num + 1):
        factorial = factorial*i
        # factorial = factorial*1
        # factorial = factorial*2
        # factorial = ...
        # factorial = factorial*num
        # loop ends
print(factorial)  # prints factorial
"""


# Nested Loops --------------------------------------------------------------------------------------------------
# nested loops - allows any combiniation of loops to be used inside other (parent) loops (i.e. a for loop inside a while loop)

print("\n\n\nNested Loops:")


"""
Docstring'd out to run rest of program


# nested while loops
# Bank ATM example -----------------------------------------
print('Welcome to the Bank ATM')
restart = ('Y')  # variable for a user option
chances = 3  # tries to enter pin
balance = 67.14  # balance in account
while chances >= 0:  # while user has pin attempts left
    pin = int(input('Please Enter 4 Digit Pin: '))
    if pin == (1234):  # if pin is entered correctly (1234)
        print('Correct Pin\n')
        while restart not in ('n', 'NO', 'no', 'N'):  # while 'restart' is not in list
            print('1 - For Balance\n')
            print('2 - To Withdrawl\n')
            print('3 - To Deposit\n')
            print('4 - To Close Account\n')
            # user input for desired action
            option = int(input('Please select an option from above: '))
            if option == 1:  # if user checks balance (enters '1')
                print('Your Balance is $', balance, '\n')
                # ask if they have any other tasks
                restart = input('Go Back? (Y/N): ')
                # if done (entered n, NO, no, N), exit loop/program
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 2:  # if user wants to withdrawl (enters '2')
                option2 = ('y')
                withdrawl = float(
                    input('How much are you withdrawling?\n 10/20/40/60/80/100'))  # user input for withdrawl amount
                if withdrawl in [10, 20, 40, 60, 80, 100]:  # if input is in list
                    balance = balance - withdrawl  # subtract withdrawl amount from balance
                    print('\nYour Balance is now $', balance)
                    # ask if they have any other tasks
                    restart = input('Go Back? (Y/N): ')
                    # if done (entered n, NO, no, N), exit loop/program
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank You')
                        break
                    elif withdrawl != [10, 20, 40, 60, 80, 100]:  # if input is NOT in list
                        print('Invalid Amount, Please Retry\n')
                        restart = ('y')
                    elif withdrawl == 1:  # if input is 1
                        withdrawl = float(
                            input('Please Enter desired amount: '))
            elif option == 3:  # if user wants to deposit (enters '3')
                # user input for deposit amount
                deposit = float(input('How much are you depositing? '))
                balance = balance+deposit  # add deposit amount to balance
                print('\nYour balance is now $', balance)
                # ask if they have any other tasks
                restart = input('Go Back? (Y/N): ')
                # if done (entered n, NO, no, N), exit loop/program
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 4:  # if user selects close account (enters '4')
                print('Please wait...\n')
                print("We're sorry to see you leave us.\n")
                print('Thank you for your business.')
                break
            else:  # if user does not select options 1-4
                print('Please enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):  # if user does not enter pin correctly
        print('Incorrect Pin')
        chances = chances - 1
        if chances == 0:  # if pin entered wrong too many times
            print('\nIf you forgot your Pin please contact support.')
            break
"""


"""
# nested for loops
# pythagorian numbers example ----------------------------

# import sqare root function from math (from math import sqrt)
n = int(input("Maximal Number? "))  # user input to get top number of range
for a in range(1, n+1):  # for numbers in range of 1 to user input+1 (+1 makes range include user input)
    for b in range(a, n):  # for numbers in range of a to user input
        c_square = a**2+b**2
        c = int(sqrt(c_square)) # find square root of c_square
        if ((c_square - c**2) == 0): 
            print(a, b, c)
"""


# for loop inside while loop
# bulk reservation example ----------------------------------------

travelling = input("yes or no: ")  # user input if they need to use program
while travelling == 'yes':  # if user input is yes
    # user input for how many people (i.e. user enters '4')
    num = int(input("number of travelers: "))
    for num in range(1, num+1):  # for each person (runs loop 4 times)
        name = input("Name: ")  # input name
        age = input("Age: ")  # age
        sex = input("Male, Female, N/A")  # and sex
        print(name, age, sex)  # print info of each person as entered
    # once it finishes (runs 4 times) ask if they need to add another person.
    # if not yes, end program.
    travelling = input("Oops! forgot someone? (yes/no): ")
