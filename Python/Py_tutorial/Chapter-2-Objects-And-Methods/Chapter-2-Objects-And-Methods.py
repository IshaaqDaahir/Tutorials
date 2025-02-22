tale = 'This is the best of times.'
# print(tale.count('i'))
# print(tale.count('is'))
# print(tale.count('That'))
# print(tale.count(' '))
# print(tale.count('t'))
# print(tale.count('T'))

# print(3 * 'X'.count('XXX'))
# print((3 * 'X').count('XXX'))

# print(dir(''))

# In a slice, if you give an index past a limit of where it could be, Python assumes you 
# mean the actual end.
word = 'program'
# print(word[:9])
# print(word[8:10])
# print(word[3:6])

# A useful string method that uses the ideas of indices and slices is find.
s = 'Mississippi'
# print(s.find('i'))
# print(s.find('si'))
# print(s.find('sa'))
# print(s.find('si', 4))

# line = 'Hello, there!'
# print(line.find('e'))
# print(line.find('he'))
# print(line.find('e', 10))
# print(line.find('he', 10))

# print(help(line.find))
# print(dir(str))
# print(help(str.capitalize))

# print(tale.split())
# print(s.split('i'))
# print(s.split())    # no whitespace

# line = 'Go: Tear some strings apart!'
# seq = line.split()
# print(seq)
# print(line.split(':'))
# print(line.split('ar'))

lines = 'This includes\nsome new\nlines.'
# print(lines.split())

# 2.1.6. join. Join is roughly the reverse of split. It joins together a sequence of 
# strings. The syntax is rather different. The separator sep comes first, since it has 
# the right type (a string).
# print(" ".join(seq))
# print("".join(seq))
# print("//".join(seq))
# print("##".join(seq))
# print(":".join(seq))

# Exercise 2.1.6.1. * Write a program underscores.py that would input a phrase from the 
# user and print out the phrase with the white space between words replaced by an 
# underscore. For instance if the input is "the best one", then it would print 
# "the_best_one". The conversion can be done in one or two statements using the recent 
# string methods.

# Exercise 2.1.6.2. ** An acronym is a string of capital letters formed by taking the 
# first letters from a phrase. For example, SADD is an acronym for ’students against 
# drunk driving’. Note that the acronym should be composed of all capital letters even 
# if the original words are not. Write a program acronym.py that has the user input a 
# phrase and then prints the corresponding acronym.

# 2.2.1. Appending to a List.
words = list()

words.append('animal')
words.append('food')
words.append('city')
# print(words)

def multipleAll(numList, multiplier):
    '''Return a new list containing all of the elements of numList, each multiplied by
    multiplier.'''
    
    newList = []
    for i in numList:
        multiplied = i * multiplier
        newList.append(multiplied)
        
    print(newList)
    
# multipleAll([3, 1, 7], 5)

# 2.2.2. Sets.
# Python has a type set. Like many type names, it can be used to convert other types. 
# In this case it makes sense to convert any collection, and the process removes 
# duplicates.
numberList = [2, 1, 3, 2, 5, 5, 2]
aSet = set(numberList)

# for item in aSet:
#     print(item)
#     print()

itemSet = set(['animal', 'food', 'animal', 'food', 'food', 'city'])
# print(itemSet)

# 2.3.1. A Function to Ease the Creation of Mad Libs.
def getKeys(formatString):
    '''formatString is a format string with embedded dictionary keys. Return a list 
    containing all the keys from the format string.'''
    
    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        # find the start and end of the next key
        # We search for the start of the next key using/going from the end of the last 
        # one:
        start = formatString.find('{', end) + 1
        
        # We search for the end of the key using the start value here
        end = formatString.find('}', start)
        
        key = formatString[start : end] 
        keyList.append(key)

    return keyList

from graphics import *

win = GraphWin()
win = GraphWin("Test window", 1000, 600)

pt = Point(500, 300)
pt.draw(win)

cir = Circle(pt, 25)
cir.draw(win)
cir.setOutline('red')
cir.setFill('blue')

line = Line(pt, Point(150, 100))
line.draw(win)

rect = Rectangle(Point(50, 50), pt)
rect.draw(win)
rect.setOutline('brown')
rect.setFill('green')

line.move(10, 40)

# win.close()

print(line)
print(cir)

input()           

# Exercise 2.4.5.1. * Make a program scene.py creating a scene with the graphics 
# methods. You are likely to need to adjust the positions of objects by trial and error 
# until you get the positions you want. Make sure you have graphics.py in the same 
# directory as your program.

# Exercise 2.4.5.2. * Elaborate your scene program so it becomes changeScene.py, and 
# changes one or more times when you click the mouse (and use win.getMouse()). You may 
# use the position of the mouse click to affect the result, or it may just indicate you 
# are ready to go on to the next view.

# Exercise 2.4.8.1. ** Save backAndForth3.py to the new name backAndForth4.py. Add a 
# triangular nose in the middle of the face in the makeFace function. Like the other 
# features of the face, make sure the position of the nose is relative to the center 
# parameter. Make sure the nose is included in the final list of elements of the face 
# that get returned.

# Exercise 2.4.12.1. * Write a program ranges.py that uses the range function to 
# produce the sequnce 1, 2, 3, 4, and then print it. Also prompt the user for an 
# integer n and print the sequnce 1, 2, 3, ... , n – including n. Hint: 8 Finally use 
# a simple repeat loop to find and print five randomly chosen numbers from the range 
# 1, 2, 3, ... , n.

# Exercise 2.5.0.2. Make the following programs in sequence. Be sure to save the 
# programs in the same directory as where you start the idle shortcut and where you 
# have all the sample text files: 
# a. printUpper.py: read the contents of the sample2.txt file and print the contents 
# out in upper case. (This should use file operations and should work no matter what 
# the contents are in sample2.txt. Do not assume the particular string written by 
# nextFile.py!) 

# b. fileUpper.py: prompt the user for a file name, read and print the contents of 
# the requested file in upper case.

# c. copyFileUpper: modify fileUpper.py to write the upper case string to a new file 
# rather than printing it. Have the name of the new file be dynamically derived from 
# the old name by prepending ’UPPER’ to the name. For example, if the user specified 
# the file sample.txt (from above), the program would create a file UPPERsample.txt, 
# containing ’MY FIRST OUTPUT FILE!’. When the user specifies the file name 
# stuff.txt, the resulting file would be named UPPERstuff.txt.

# Exercise 2.5.0.3. Write madlib3.py, a small modification of madlib2.py, requiring only a modification
# to the main function of madlib2.py. Your madlib3.py should prompt the user for the name of a file that
# should contain a madlib format string as text (with no quotes around it). Read in this file and use it as the
# format string in the tellStory function. This is unlike in madlib2.py, where the story is a literal string
# coded directly into the program called originalStory. The tellstory function and particularly the getKeys
# function were developed and described in detail in this tutorial, but for this exercise there is no need to
# follow their inner workings - you are just a user of the tellstory function (and the functions that it calls).
# You do not need to mess with the code for the definition of tellStory or any of the earlier supporting
# functions. The original madlib string is already placed in a file jungle.txt, that is in this format as an
# example. With the Idle editor, write another madlib format string into a file myMadlib.txt. If you earlier
# created a file myMadlib.py, then you can easily extract the story from there (without the quotes around it).
# Test your program both with jungle.txt and your new madlib story file.


























