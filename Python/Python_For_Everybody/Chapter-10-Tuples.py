# t = ('a', 'b', 'c', 'd', 'e')
# t1 = ('a',)
# print(type(t1))

# t = tuple('lupins')
# print(t)
# print(t[0])
# print(t[1:3])

# t[0] = 'A'

# t = ('A',) + t[1:]
# print(t)

# c1 = (0, 1, 2) < (0, 3, 4)
# print(c1)

# c2 = (0, 1, 2000000) < (0, 3, 4)
# print(c2)

# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))
    
# t.sort(reverse=True)

# res = list()
# for length, word in t:
#     res.append(word)

# print(res)

# m = ['have', 'fun']
# x, y = m
# (x, y) = m
# print(x)
# print(y)

# m = ['have', 'fun']
# x = m[0]
# y = m[1]
# print(x)
# print(y)

# a = 5
# b = 10
# a, b = b, a
# print(b)
# print(a)

# addr = 'monty@python.org'
# uname, domain = addr.split('@')
# print(uname)
# print(domain)

# d = {'a':10, 'b':1, 'c':22}
# t = list(d.items())
# t.sort()
# print(t)

# for key, val in t:
#     print(val, key)

# d = {'a':10, 'b':1, 'c':22}
# l = list()
# for key, val in d.items():
#     l.append((val, key))
    
# l.sort(reverse=True)
# print(l)

# import string
# fhand = open('romeo-full.txt')
# counts = dict()
# for line in fhand:
#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
            
# # Sort the dictionary by value.
# lst = list()
# for key, val in list(counts.items()):
#     lst.append(( val, key))
    
# lst.sort(reverse=True)
# for key, val in lst[:10]:
#     print(key, val)

# We would encounter a composite key if we wanted to create a telephone directory
# that maps from last-name, first-name pairs to telephone numbers. Assuming that 
# we have defined the variables last, first, and number, we could write a 
# dictionary assignment statement as follows:
# directory = dict()

# last1 = "Daahir"
# first1 = "Is'haaq"
# number1 = "08148394765"

# last4 = "Abdurrahmaan"
# first4 = "Maryam"
# number4 = "08148394765"

# last2 = "Abubakar"
# first2 = "Is'haaq"
# number2 = "08148394700"

# last3 = "Abubakar"
# first3 = "Anas"
# number3 = "08148394700"

# directory[last1, first1] = number1
# directory[last2, first2] = number2
# directory[last3, first3] = number3
# directory[last4, first4] = number4

# # for last, first in directory:
# #     print(first, last, directory[last, first])

# list_of_ints_in_strings = ['42', '65', '12']
# list_of_ints = []
# for x in list_of_ints_in_strings:
#     list_of_ints.append(int(x))

# # print(sum(list_of_ints))

# With list comprehension, the above code can be written in a more compact manner:
# list_of_ints_in_strings = ['42', '65', '12']
# list_of_ints = [int(x) for x in list_of_ints_in_strings]

# print(sum(list_of_ints))

# Revise a previous program as follows: Read and parse the “From” lines and pull 
# out the addresses from the line. Count the number of messages from each person 
# using a dictionary. After all the data has been read, print the person with 
# the most commits by creating a list of (count, email) tuples from the 
# dictionary. Then sort the list in reverse order and print out the person who 
# # has the most commits.
# fname = input('Enter a file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File can not be opened:', fname)
#     exit()
    
# msg_counts = dict()
# for line in fhand:
#     if line.startswith('From '):
#         words = line.split()
#         addresses = words[1]
#         msg_counts[addresses] = msg_counts.get(addresses, 0) + 1
        
# lst = list()
# for count, email in list(msg_counts.items()):            
#     lst.append((count, email))
    
# lst.sort(reverse=True)

# for count, email in lst[:1]:
#     print(count, email)    

# This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the 
# “From” line by finding the time string and then splitting that string into parts using the colon character. Once you 
# have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

""" fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File can not be opened:', fname)
    exit()
    
hour_counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time_str = words[5]
        time_str = time_str.split(':')
        hour_str = time_str[0]
        hour_counts[hour_str] = hour_counts.get(hour_str, 0) + 1
        
lst = list()
for count, hour in list(hour_counts.items()):            
    lst.append((count, hour))
    
lst.sort()

for count, hour in lst:
    print(count, hour) """ 
    
# Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should 
# convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, 
# punctuation, or anything other than the letters a-z.

import string
fname = input("Enter file name: ")
fhand = open(fname)
inp = fhand.read()

counts = dict()
for letter in inp:
    # if letter == "": continue
    letter = letter.translate(str.maketrans('', '', string.punctuation))
    letter = letter.strip().lower()
    if letter not in counts:
        counts[letter] = counts.get(letter, 0) + 1

# Sort the dictionary by value.
lst = list()
for key, val in list(counts.items()):
    lst.append(( val, key))
    
lst.sort(reverse=True)
for key, val in lst:
    print(val, key) 




























