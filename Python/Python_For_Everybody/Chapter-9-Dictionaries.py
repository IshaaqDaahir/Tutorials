eng2sp = dict()

# eng2sp['one'] = 'uno'
# print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng2sp)

# print(eng2sp['two'])
# print(eng2sp['four'])

# print(len(eng2sp))

# print('one' in eng2sp)

# print('uno' in eng2sp)

# To see whether something appears as a value in a dictionary, you can use the
# method values, which returns the values as a type that can be converted to a list,
# and then use the in operator:

vals = list(eng2sp.values())
# print('uno' in vals)

# Write a program that reads the words in words.txt and stores them as keys in a 
# "dictionary". It doesn’t matter what the values are. Then you can use the "in" 
# operator as a fast way to check whether a string is in the dictionary.

# dictionary = dict()

# fhand = open('words.txt')
# for line in fhand:
#     word = line.strip()
    
#     dictionary[word] = None
# # print(dictionary)  
# search_word = input('Enter a string to serach: ').strip()

# if search_word in dictionary:
#     print(f'"{search_word}" is in the dictionary.')
# else:
#     print(f'"{search_word}" is not in the dictionary.')
    
# Suppose you are given a string and you want to count how many times each letter
# appears.
    
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
# print(d)    
    
# Dictionaries have a method called "get()" that takes a key and a default value. 
# If the key appears in the dictionary, get returns the corresponding value; 
# otherwise it returns the default value.
    
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
# print(counts.get('jan', None))
# print(counts.get('jan', 0)) 
# print(counts.get('tim', None)) 

# We can use get to write our histogram loop more concisely. Because the get 
# method automatically handles the case where a key is not in a dictionary, we 
# can reduce four lines down to one and eliminate the if statement.   
    
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
# print(d)
    
# One of the common uses of a dictionary is to count the occurrence of words in 
# a file with some written text.  

# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
    
#     counts = dict()
#     for line in fhand:
#         words = line.split()
#         for word in words:
#             if word not in counts:
#                 counts[word] = 1
#             else:
#                 counts[word] += 1

#     print(counts)
# except:
#     print('File cannot be opened:', fname)

# counts = {'ckuck': 1, 'annie': 42, 'jan': 100}
# for key in counts:
#     print(key, counts[key])

# For example if we wanted to find all the entries in a dictionary with a value
# above ten, we could write the following code:

# counts = {'ckuck': 1, 'annie': 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])

# If you want to print the keys in alphabetical order, you first make a list 
# of the keys in the dictionary using the keys method available in dictionary 
# objects, and then sort that list and loop through the sorted list, looking 
# up each key and printing out key-value pairs in sorted order as follows:

# counts = {'ckuck': 1, 'annie': 42, 'jan': 100}
# lst = list(counts.keys())
# print(lst)
# lst.sort()
# for key in lst:
#     print(key, counts[key])

# Counting and printing key-value pair after removing the punctuations.
# import string

# # print(string.punctuation)

# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File can not be opened:', fname)
#     exit()

# counts = dict()
# for line in fhand:
#     line = line.rstrip()
#     line = line.translate(line.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         # if word not in counts:
#         #     counts[word] = 1
#         # else:
#         #     counts[word] += 1
#         counts[word] = counts.get(word, 0) + 1
            
# print(counts)
    
# Write a program that categorizes each mail message by which day of the week 
# the commit was done. To do this look for lines that start with “From”, then 
# look for the third word and keep a running count of each of the days of the 
# week. At the end of the program print out the contents of your dictionary 
# (order does not matter).

# fname = input('Enter a file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File can not be opened:', fname)
#     exit()
    
# counts = dict()
# for line in fhand:
#     if line.startswith('From '):
#         words = line.split()
#         third_word = words[2]
#         counts[third_word] = counts.get(third_word, 0) + 1
        
# print(counts)

# Write a program to read through a mail log, build a histogram using a 
# dictionary to count how many messages have come from each email address, and 
# print the dictionary.

# fname = input('Enter a file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File can not be opened:', fname)
#     exit()
    
# counts = dict()
# for line in fhand:
#     if line.startswith('From '):
#         words = line.split()
#         mails = words[1]
#         counts[mails] = counts.get(mails, 0) + 1
        
# print(counts)

# Add code to the above program to figure out who has the most messages in the 
# file. After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and 
# minimum loops) to find who has the most messages and print how many messages 
# the person has.

# fname = input('Enter a file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File can not be opened:', fname)
#     exit()
    
# counts = dict()
# for line in fhand:
#     if line.startswith('From '):
#         words = line.split()
#         mails = words[1]
#         counts[mails] = counts.get(mails, 0) + 1
#         for most in counts:
#             most = max(counts)
        
# print(most, counts[most])

# This program records the domain name (instead of the address) where the message 
# was sent from instead of who the mail came from (i.e., the whole email address
# ). At the end of the program, print out the contents of your dictionary.

""" fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File can not be opened:', fname)
    exit()
    
counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        mails = words[1]
        
        at_pos = mails.find('@')
        domain_name = mails[at_pos + 1 : ]
        counts[domain_name] = counts.get(domain_name, 0) + 1

print(counts) """

# Counting and printing key-value pair after removing the punctuations and sorting in key-value pair.
import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)
















