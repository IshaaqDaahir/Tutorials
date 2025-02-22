"""
String Substitution for a Mad Lib
Adapted from code by Kirby Urner
"""

storyFormat = """
Once upon a time, deep in an ancient jungle, there lived a {animal}. This {animal} 
liked to eat {food}, but the jungle had very little {food} to offer. One day an 
explorer found the {animal} and discovered it liked {food}. The explorer took the 
{animal} back to {city}, where it could eat as much {food} as it wanted. However, 
the {animal} became homesick, so the explorer brought it back to the jungle, 
leaving a large supply of {food}.

The End
"""

""" def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt)
    dictionary[cue] = response

def tellStory():
    userPicks = dict()
    addPick('animal', userPicks)
    addPick('food', userPicks)
    addPick('city', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)
    
tellStory()

# This line is only here to accommodate running the program in Windows by double 
# clicking on its file icon. Without this line, the story would be displayed and 
# then the program would end, and Windows would make it immediately disappear from 
# the screen! This line forces the program to continue being displayed until there 
# is another response from the user, and meanwhile the user may look at the output 
# from tellStory
input('Press Enter to end the program.') """

'''A very simple program,
showing how short a Python program can be!
Authors: ___, ___
'''
# person = input('Enter your name: ')
# print('Hello', person + '!') # This is a stupid comment after the # mark
# print("Hello ", person, '!', sep='')
 
"""Illustrate input and print."""
# applicant = input("Enter the applicant's name: ")
# interviewer = input("Enter the interviewer's name: ")
# time = input("Enter the appointment time: ")
# print(interviewer, "will interview", applicant, "at", time)

# x = input('Enter an integer: ')
# y = input('Enter another integer: ')
# print('The sum of ', x, ' and ', y, ' is ', int(x) + int(y), '.', sep='')

'''Conversion of strings to int before addition'''
# xString = input('Enter an integer: ')
# x = int(xString)
# yString = input('Enter another integer: ')
# y = int(yString)
# print('The sum of ', x, ' and ', y, ' is ', x+y, '.', sep='')

'''Two numeric inputs'''
# x = int(input('Enter an integer: '))
# y = int(input('Enter another integer: '))
# print('The sum of ', x, ' and ', y, ' is ', x+y, '.', sep='')

# x = int(input('Enter an integer: '))
# y = int(input('Enter another integer: '))
# sum = x + y
# print('The sum of ', x, ' and ', y, ' is ', sum, '.', sep='')

# Exercise 1.10.3.1. * Write a version, add3.py, that asks for three numbers, and 
# lists all three, and their sum, in similar format to the example above.

# x = int(input('Enter an integer: '))
# y = int(input('Enter another integer: '))
# z = int(input('Enter another integer: '))
# summation = x + y + z
# print('The sum of ', x, ' ', y, ' and ', z, ' is ', summation, '.', sep='')

# Exercise 1.10.3.2. * a. Write a program, quotient.py, that prompts the user for 
# two integers, and then prints them out in a sentence with an integer division 
# problem like "The quotient of 14 and 3 is 4 with a remainder of 2".

# x = int(input('Enter an integer: '))
# y = int(input('Enter another integer: '))
# quotient = x // y
# remainder = x % y
# print(f"The quotient of {x} and {y} is {quotient} with a remainder of {remainder}")

# person = input('Enter your name: ')
# # greeting = 'Hello {}!'.format(person)
# # print(greeting)
# print('Hello {}!'.format(person))

'''Compare different approaches to printing with embedded values.'''
# applicant = input("Enter the applicant's name: ")
# interviewer = input("Enter the interviewer's name: ")
# time = input("Enter the appointment time: ")
# # print(interviewer + ' will interview ' + applicant + ' at ' + time + '.')
# # print(interviewer, ' will interview ', applicant, ' at ', time, '.', sep='')
# # print('{} will interview {} at {}.'.format(interviewer, applicant, time))
# print('{0} will interview {1} at {2}.'.format(interviewer, applicant, time))

# a = 5
# b = 9

# formatStr = "The set is {{{}, {}}}."
# setStr = formatStr.format(a, b)
# print(setStr)

'''Fancier format string example.'''
# x = 20
# y = 30
# formatStr = '{0} + {1} = {2}; {0} * {1} = {3}.'
# equations = formatStr.format(x, y, x+y, x*y)
# print(equations)

# Exercise 1.10.4.1. * Write a version of Exercise 1.10.3.1, add3f.py, that uses 
# the string format method to construct the final string.
# x = int(input("Enter an integer: "))
# y = int(input("Enter another integer: "))
# z = int(input("Enter another integer: "))
# summation = x + y + z
# # formattedSummation = "The sum of {} {} and {} is {}.".format(x, y, z, summation)
# formattedSummation = "The sum of {0} {1} and {2} is {3}.".format(x, y, z, summation)
# print(formattedSummation)

# Exercise 1.10.4.2. * Write a version of Exercise 1.10.3.2, quotientformat.py, that 
# uses the string format method to construct the final string.
# x = int(input("Enter an integer: "))
# y = int(input("Enter another integer: "))
# quotient = x // y
# remainder = x % y
# formattedStr = "The quotient of {0} and {1} is {2} with a remainder of {3}.".format(x, y, quotient, remainder)
# print(formattedStr)

def happyBirthdayEmily():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Emily.")
    print('Happy Birthday to you!')

def happyBirthdayAndre():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Andre.")
    print('Happy Birthday to you!')

# happyBirthdayEmily()
# happyBirthdayAndre()

# def main():
#     happyBirthdayAndre()
#     happyBirthdayEmily()

# main()
# main()

# def f():
#     print('In function f')
#     print('When does this print?')

# f()

# def f():
#     print('In function f')    
# print('When does this print?')
# f()

# Exercise 1.11.3.1. * Write a program, poem.py, that defines a function that 
# prints a short poem or song verse. Give a meaningful name to the function. Have 
# the program end by calling the function three times, so the poem or verse is 
# repeated three times.

def mySoulmate():
    print('I can only think about you!')
    print('Your voice always brings peace to my heart!')
    print('Your beauty always makes me blush!')
    print('I only see you in my mind!')

# mySoulmate()
# mySoulmate()
# mySoulmate()

# def happyBirthday(person):
#     print('Happy Birthday to you!')
#     print('Happy Birthday to you!')
#     print('Happy Birthday, dear ' + person + '.')
#     print('Happy Birthday to you!')
    
# # happyBirthday('Emily')
# # happyBirthday('Andre')

# def main():
#     happyBirthday('Emily')
#     happyBirthday('Andre')
#     happyBirthday('Maria')
    
# main()    

# Exercise 1.11.4.1. * Make your own further change to the file and save it as 
# birthdayMany.py: Add a function call, so Maria gets a verse, in addition to Emily 
# and Andre. Also print a blank line between verses. (You may either do this by 
# adding a print line to the function definition, or by adding a print line between 
# all calls to the function.)
# def happyBirthday(person):
#     print('Happy Birthday to you!')
#     print('Happy Birthday to you!')
#     print('Happy Birthday, dear ' + person + '.')
#     print('Happy Birthday to you!')
#     print()
    
# # happyBirthday('Emily')
# # happyBirthday('Andre')

# def main():
#     happyBirthday('Emily')
#     # print()
#     happyBirthday('Andre')
#     # print()
#     happyBirthday('Maria')
    
# main()    

# We can combine function parameters with user input, and have the program be able 
# to print Happy Birthday for anyone.
def happyBirthday(person):
    print('Happy Birthday to you!')
    print('Happy Birthday to you!')
    print('Happy Birthday, dear ' + person + '.')
    print('Happy Birthday to you!')

# def main():
#     userName = input("Enter the Birthday person's name: ")
#     happyBirthday(userName)

# main()

def sumProblem(x, y):
    sum = x + y
    print('The sum of ', x, ' and ', y, ' is ', sum, '.', sep='')
    print()
    
# def main():
#     sumProblem(2, 3)
#     sumProblem(1234567890123, 535790269358)
#     a = int(input('Enter an integer: '))
#     b = int(input('Enter another integer: '))
#     # print(sumProblem(a, b))
#     sumProblem(a, b)

# main()

# Exercise 1.11.5.1. ’* Modify the program above and save it as quotientProb.py. The 
# new program should have a quotientProblem function, printing as in the Exercise 
# 1.10.3.2. The main method should test the function on several sets of literal 
# values, and also test the function with input from the user.
# def quotientProblem(x, y):
#     quotient = x // y
#     remainder = x % y
#     print(f"The quotient of {x} and {y} is {quotient} with a remainder of {remainder}.\n")

# def main():
#     quotientProblem(14, 3)
#     quotientProblem(124, 90)
#     a = int(input("Enter an integer: "))
#     b = int(input("Enter another integer: "))
#     quotientProblem(a, b)
    
# main() 

# 1.11.6. Returned Function Values.
# def f(x):
#     return x * x

# print(f(3))
# print(f(3) + f(4))

def lastFirst(firstName, lastName):
    separator = ', '
    result = lastName + separator + firstName
    return result

# print(lastFirst('Benjamin', 'Franklin'))
# print(lastFirst('Andrew', 'Harrington'))

# Exercise 1.11.6.1. Create quotientReturn.py by modifying quotientProb.py from 
# Exercise 1.11.5.1 so that the program accomplishes the same thing, but everywhere 
# change the quotientProblem function into one called quotientString that merely 
# returns the string rather than printing the string directly. Have the main 
# function print the result of each call to the quotientString function.

def quotientString(x, y):
    quotient = x // y
    remainder = x % y
    return f"The quotient of {x} and {y} is {quotient} with a remainder of {remainder}.\n"

# def main():
#     print(quotientString(14, 3))
#     print(quotientString(124, 90))
#     a = int(input("Enter an integer: "))
#     b = int(input("Enter another integer: "))
#     print(quotientString(a, b))

# main()

# 1.11.8. Local Scope.
# Bad Scope
# def main():
#     x = 3
#     f()
    
# def f():
#     print(x) # f does not know the x defined in main
    
# main()

# Good Scope
# def main():
#     x = 3
#     f(x)

# def f(z):
#     print(z)    

# main()

# Global Constants.
PI =  3.14159265358979  # global constant -- only place the value of PI is set

def circleArea(radius):
    return PI * radius * radius  # use value of global constant PI

def circleCircumference(radius):
    return 2 * PI * radius       # use value of global constant PI

# print(f'circle area with radius 5: {circleArea(5)}\n')
# print('circumference with radius 5:', circleCircumference(5))

# 1.12. Dictionaries
"""A tiny English to Spanish dictionary is created,
using the Python dictionarytype 'dict'.
The the dictionary is used, briefly."""

def createDictionary():
    '''Returns a tiny Spanish dictionary'''
    spanish = dict()    # creates an empty dictionary

    spanish['hello'] = 'hola'
    spanish['yes'] = 'si'
    spanish['one'] = 'uno'
    spanish['two'] = 'dos'
    spanish['three'] = 'tres'
    spanish['red'] = 'rojo'
    spanish['black'] = 'negro'
    spanish['green'] = 'verde'
    spanish['blue'] = 'azul'
    return spanish
   
# def main():
#     dictionary = createDictionary()    
#     """ print(dictionary['two'])
#     print(dictionary['red'])
#     print(dictionary)
#     print(createDictionary()['hello'])
#     print(createDictionary()) """
    
#     # dictionary['one'] = 'Daya'
#     print('Count in Spanish: ' + dictionary['one'] + ', ' + 
#           dictionary['two'] + ', ' + dictionary['three'] + ',...\n')
    
#     print('Spanish colors: ' + dictionary['red'] + ', ' + 
#           dictionary['blue'] + ', ' + dictionary['green'] + ',...')

# main()

# Exercise 1.12.1.1. * Write a tiny Python program numDict.py that makes a dictionary whose keys are 
# the words ’one’, ’two’, ’three’, and ’four’, and whose corresponding values are the numerical 
# equivalents, 1, 2, 3, and 4 (ints, not strings). Include code to test the resulting dictionary by 
# referencing several of the definitions and printing the results.
def numbers():
    nums = {}
    nums['one'] = 1
    nums['two'] = 2
    nums['three'] = 3
    nums['four'] = 4
    return nums    

# def main():
#     dictionary = numbers()
#     print(dictionary['one'], '\n')
#     print(dictionary['two'], '\n')
#     print(dictionary['three'], '\n')
#     print(dictionary['four'])

# main()

# 1.12.2. Dictionaries and String Formatting.
# def main():
#     dictionary = createDictionary()
#     numberFormat = "Count in Spanish: {one}, {two}, {three}, ...\n"
#     # withSubstitutions = numberFormat.format(one='uno', two='dos', three='tres')
#     # print(withSubstitutions)
#     withSubstitutions = numberFormat.format(**dictionary)
#     print(withSubstitutions)
#     print("Spanish colors: {red}, {blue}, {green}, ...".format(**dictionary))

# main()

# print(list(range(6))) 
# print(range(8))

# 1.13.4. Basic for Loops.
# for count in [1, 2, 3]:
#     print(count)
#     print('Yes' * count)

# items = ['red', 'orange', 'yellow', 'green']
# for item in items:
#     print(item)

# 1.13.7. Accumulation Loops.
def sumList(nums):
    '''Return the sum of the numbers in nums.'''
    sum = 0
    for num in nums:
        # nextSum = sum + num
        # sum = nextSum
        
        sum = sum + num
    return sum

# Exercise 1.13.7.2. * Write a program testSumList.py which includes a main function 
# to test the sumList function several times. Include a test for the extreme case, 
# with an empty list.

# Exercise 1.13.7.3. ** Complete the following function. This starting code is in 
# joinAllStub.py. Save it to the new name joinAll.py. Note the way an example is 
# given in the documentation string. It simulates the use of the function in the 
# Shell. This is a common convention:

# Functions can also return values. Consider the Python for this mathematical 
# sequence: define the!function m(x) = 5x, let y = 3; find m(y) + m(2y-1).
def m(x):
    return 5 * x

y = 3
# print(m(y) + m(2 * y - 1))

# Exercise 1.13.8.1. ** Play computer on the following code. Reality check: 31 is 
# printed when line 6 finally executes.
x = 0
y = 1
for n in [5, 4, 6]:
    x = x + y * n
    y = y + 1
    
# print(x)
# print(y)

# Exercise 1.13.8.2. ** The following code is supposed to compute the product of the 
# numbers in a list.For instance product([5, 4, 6]) should calculate and return 
# 5*4*6=120 in steps, calculating 5, 5*4=20and 20*6=120 . Play computer on a call to 
# product([5, 4, 6]) until you see that it makes a mistake. This code appears in the 
# example file numProductWrong.py. Save it as numProduct.py and fix the error 
# (and save again!). 

# Exercise 1.13.8.3. ** Play computer on the following code. Table headings are 
# shown for you. Reality check: 70 is printed.
# def f(x):
#     return x + 4

# print(f(3) * f(6))

# 1.13.9. The print function end keyword.
# print('all', 'on', 'same', 'line')
# print('different line')

# print('all', 'on', end=' ')
# print('same', end=' ')
# print('line')
# print('different line')

# 1.14.3. String Formats for Float Precision.
# x = 23.457413902458498
# print(format(x, '.5f'))
# print(format(x, '.2f'))

x = 2.876543
# colonStr = 'longer: {:.5f}, shorter: {:.3f}.'.format(x, x)
colonStr = 'longer: {x:.5f}, shorter: {x:.3f}.'.format(**locals())
# print(colonStr)

noDict = 'No dictionary: {:.5f}.'.format(x)
# print(noDict)

onePoint = format(.1, '.20f') 
# print(onePoint)
twoPoint = format(.2, '.20f')
# print(twoPoint)
totalPoint = format(.1 + .2, '.20f')
# print(totalPoint)
threePoint = format(.3, '.20f')
# print(threePoint)

# Exercise 1.14.3.1. * Write a program, discount.py, that prompts the user for an 
# original price and for a discount percentage and prints out the new price to the 
# nearest cent. For example if the user enters 2.89 for the price and 20 for the 
# discount percentage, the value would be (1- 20/100)*2.89, rounded to two decimal 
# places, 2.31. For price .65 with a 25 percent discount, the value would be 
# (1- 25/100)*.65, rounded to two decimal places, .49.10 Write the general calculation 
# code following the pattern of the calculations  illustrated in the two concrete 
# examples.

# string = 'A word: {}, a number: {}, a formatted number: {:.3f}.'
# formString = string.format('Joe', 23, 2.13579)
# print(formString)

defs = {}
defs['name'] = 'Joe'
defs['num'] = 23
defs['dec'] = 2.13579

String = 'A word: {name}, a number {num}, a formatted number: {dec:.3f}.'
formString = String.format(**defs)
# print(formString)

for i in range(5):
    print(i)
































































































































































































































































































































































































































































































































