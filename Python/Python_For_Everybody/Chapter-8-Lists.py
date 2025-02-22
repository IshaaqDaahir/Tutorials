cheeses = ['Chedder', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []

numbers[1] = 5

# print('Edam' in cheeses)
# print('Brie' in cheeses)

# for cheese in cheeses:
#     print(cheese)

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
# print(numbers)

# for x in empty:
#     print('This never happens.')

nested_list = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
# print(len(nested_list))
# print(nested_list[3])

# Concatination
a = [1, 2, 3]
b =[4, 5, 6]
c = a + b
# print(c)
# print([0] * 4)
# print([1, 2, 3] * 3)

# Slicing
t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])
# print(t[:4])
# print(t[3:])
# print(t[:])

# Mutation
t[1:3] = ['x', 'y']
# print(t)

# "append()" Method
t = ['a', 'b', 'c']
t.append('d')
# print(t)

# "extend()" Method
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
# print(t1)

# "sort()" Method
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
# print(t)

# Deleting Element using "pop()" Method
t = ['a', 'b', 'c']
# x = t.pop()
# x = t.pop(1)
# print(t)
# print(x)

# If you don’t need the removed value, you can use the "del" statement:
t = ['a', 'b', 'c']
del t[1]
# print(t)

# If you know the element you want to remove (but not the index), you can use
# "remove" method:
t = ['a', 'b', 'c']
t.remove('b')
# print(t)

# To remove more than one element, you can use del with a "slice" index:
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
# print(t)

nums = [3, 41, 12, 9, 74, 15]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(sum(nums)/len(nums))

# In this program, we have "count" and "total" variables to keep the number and
# running "total" of the user’s numbers as we repeatedly prompt the user for a 
# number.

# total = 0
# count = 0
# while True:
#     inp = input("Enter a number: ")
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count += 1

# average = total / count
# print('Average: ', average)

# We could simply remember each number as the user entered it and use built-in
# functions to compute the "sum" and "count" at the end.
numlist = list()
# numlist = []
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average:', average)

# To convert from a string to a list of characters, you can use "list()" method:
s = 'spam'
t = list(s)
# print(t) 

# If you want to break a string into words, you can use the split method:
s = 'pining for the fjords'
t = s.split()
# print(t)
# print(t[2])

# You can call split with an optional argument called a "delimiter" that specifies
# which characters to use as word boundaries. The following example uses a hyphen
# as a delimiter:
s = 'spam-spam-spam'
delimeter = '-'
t = s.split(delimeter)
# print(t)

t = ['pining', 'for', 'the', 'fjords']
# delimeter = ''
delimeter = ' '
s = delimeter.join(t)
# print(s)

# What if we wanted to print out the day of the week from those lines that start
# with “From”?
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '): continue
#     words = line.split()
#     print(words[2])

# To check whether two variables refer to the same object, you can use the "is" 
# operator.
a = 'banana'
b = 'banana'
# print(a is b)

# But when you create two lists, you get two objects:
a = [1, 2, 3]
b = [1, 2, 3]
# print(a is b)

a = [1, 2, 3]
b = a
# print(b is a)
b[0] = 17
# print(b)
# print(a)

# For example, "delete_head()" removes the first element from a list:
def delete_head(t):
    del t[0]
    
letters = ['a', 'b', 'c']
delete_head(letters)
# print(letters)

# For example, the "append" method modifies a list, but the "+" operator creates 
# a new list:
t1 = [1, 2]
t2 = t1.append(3)
# print(t1)
# print(t2)

t3 = t1 + [3]
# print(t3)
# print(t1 is t3)

def tail(t):
    return t[1:]

letters = ['a', 'b', 'c']
rest = tail(letters)
# print(rest)
# print(letters)

# Write a function called "chop" that takes a list and modifies it, removing the 
# first and last elements, and returns "None". 
def chop(t):
    t[1:-1]

letters = ['a', 'b', 'c']
rest = chop(letters)
# print(rest)

# Then write a function called "middle" that takes a list and returns a new list 
# that contains all but the first and last elements.
def middle(t):
    return t[1:-1]

# letters = middle(['a', 'b', 'c', 'd'])
letters = ['a', 'b', 'c', 'd']
rest = middle(letters)
# print(rest)

# If you want to use a method like sort that modifies the argument, but you 
# need to keep the original list as well, you can make a copy.
t = [5, 1, 3, 2, 4]
orig = t[:]
# t.sort()
new = sorted(t)
# print(t)
# print(new)

# Let’s revisit our program that is looking for the day of the week on the 
# "from" lines of our file:
    
# This looks much simpler and we don’t even need to do the rstrip to remove the 
# newline at the end of the file. But is it better?
    
# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     print('Debug:', words)
#     if words[0] != 'From': continue
#     print(words[2])

# There are many ways to protect this code; we will choose to check the number 
# of words we have before we look at the first word:
# fhand = open('mbox.txt')
# for line in fhand:
#     words = line.split()
#     # print('Debug:', words)
#     if len(words) == 0: continue
#     if words[0] != 'From': continue
#     print(words[2])

# Rewrite the guardian code in the above example without two if statements. 
# Instead, use a compound logical expression using the "or" logical operator 
# with a single "if" statement.
# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     if len(words) == 0 or words[0] != 'From': continue
#     print(words[2])

# List all unique words, sorted in alphabetical order, that are stored in a file 
# "romeo.txt" containing a subset of Shakespeare’s work. Create a list of unique
# words, which will contain the final result. Write a program to open the file 
# "romeo.txt" and read it line by line. For each line, split the line into a 
# list of words using the "split" function. For each word, check to see if the 
# word is already in the list of unique words. If the word is not in the list of
# unique words, add it to the list. When the program completes, sort and print 
# the list of unique words in alphabetical order.

unique_words = list()

fname = input('Enter file: ')
fhand = open(fname)
for line in fhand:
    words = line.split()
    for word in words:
        if word in unique_words: continue
        unique_words.append(word)
        
unique_words.sort()
print(unique_words)            
            
# Write a program to read through the mail box data and when you find line that
# starts with “From”, you will split the line into words using the "split()" 
# function. We are interested in who sent the message, which is the second word
# on the From line. You will parse the From line and print out the second word 
# for each From line, then you will also count the number of From (not From:) 
# lines and print out a count at the end.     

# fname = input('Enter a file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if not line.startswith('From '): continue
#     words = line.split()
#     count += 1
#     print(f'{words[1]}')
# print(f'There were {count} lines in the file with "From" as the first word!')

# Rewrite the program that prompts the user for a list of numbers and prints 
# out the maximum and minimum of the numbers at the end when the user enters 
# “done”. Write the program to store the numbers the user enters in a list and 
# use the max() and min() functions to compute the maximum and minimum numbers 
# after the loop completes.

# numbers = []
# while True:
#     try:
#         line = (input('Enter a number: '))
#         if line[0] == '#':
#             continue
#         if line == 'done':
#             break
        
#         value = int(line)    
#     except:
#         print('Invalid input!')
#         continue
#     numbers.append(value)
#     minimum = min(numbers)
#     maximum = max(numbers)
    
# print('Minimum: ', minimum)        
# print('Maximum: ', maximum)
    




























