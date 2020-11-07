##The purpose of this project is to create a simple calulator with basic operations using python in terminal (window).
##The project is divided into two parts. In the first part, basic separated operations are utilized in an instructional way.
##The final part will be a combined one that will be run as python projectonecalculator.py in terminal window as a user's desired frequency.

####################################################################
##ProjectOne: Part 1
####################################################################

##This step prompts users for any number inupt as they wish including words, symbols, or just the enter key.

number_1 = input('Enter your first number: ')
number_2 = input('Enter your second number: ')

##But the following inputs function to either an integer or a float. To suit whole number purpose, int() function is utilized to convert to integer data type.
##So, if we enter any symbols, letters, or non-integers it outputs error."
number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))


##This step adds four mathematical operators. We use + to add, - to subtract, * to multiply, and / to divide. 

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

print(number_1 + number_2)

##Now, lets add more context to run the program fully by using string formatters.
##User receives confirmation about numbers while entering alongside operator/s.

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)

##Now, lets add the remaining operators: add, subtract, multiply, and divide
##But at this time the program will execute all the operations.
number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

# Addition
print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)

# Subtraction
print('{} - {} = '.format(number_1, number_2))
print(number_1 - number_2)

# Multiplication
print('{} * {} = '.format(number_1, number_2))
print(number_1 * number_2)

# Division
print('{} / {} = '.format(number_1, number_2))
print(number_1 / number_2)

##To limit to perform only one operation at a time , we use conditional statements.

operation = input('''
Please type in the math operation you'd prefer to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('Lets run the program again, if a valid operator is not typed. ')


####################################################################
##ProjectOne: Part 2
####################################################################

## In this step, lets define some functions to perform the program as many times as the user wants.

## By using the again function, the users are given choice as to whether
## they want to recalculate or not. In this case, each conditional statement is used to handle errors.
##The function is named again() and added below to def calculate(): code block.


def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Lets run the program again, if a valid operator is not typed. ')

    # Add again() function to calculate() function
    again()
    ##Now lets add string function str.upper(): to do a little better
    ## to accept a lower case y and n. This is all done to handle errors with else statement above.
    ##if typed n or n, it's gonna say see you later
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()
