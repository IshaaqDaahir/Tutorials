import re
# Search for lines that contain "From:"
""" hand = open('romeo.txt')
for line in hand:
    line = line .rstrip()
    # if re.search('From:', line):
    if re.search('[aeiou]', line):
        print(line) """

# The caret character is used in regular expressions to match “the beginning” of a line. We could change our program 
# to only match lines where “From:” was at the beginning of the line as follows:

# Search for line that start with "From"
""" hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line) """
        
# The most commonly used special character is the period or full stop, which matches any character.
# Search for lines that start with "F", followed by 2 characters, followed by "m:"
""" hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # if re.search("^F..m:", line):
    if re.search("\D", line):
        print(line) """  

# We can further narrow down the lines that we match using a repeated wild card character in the following example:
# Search for lines that start with From and have an "at" sign
""" hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line) """
        
# This following program uses findall() to find the lines with email addresses in them and extract one or more addresses 
# from each of those lines.
""" s = "A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM"
d = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 Return-Path: <postmaster@collab.sakaiproject.org> for <source@collab.sakaiproject.org>; Received: (from apache@localhost) Author: stephen.marquard@uct.ac.za"
lst = re.findall('\S+@\S+', d)
print(lst) """
    
# Search for lines that have an "at" sign between characters
""" hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x) """ 
    
# Search for lines that have an "at" sign between characters. The characters must be a letter or number.
""" hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x) """
    
# Search for lines that start with "X" followed by any non-whitespace characters and ":" followed by a space and any 
# number. The number can include a decimal.
""" hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search("^X\S*: [0-9.]+", line):
        print(line) """
        
# Search for lines that start with "X" followed by any non-whitespace characters and ":" followed by a space and any
# number. The number can include a decimal. Then print the number if it is greater than zero. 
""" hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall("^X\S*: ([0-9.]+)", line)
    # x = re.findall("\d", line)
    if len(x) > 0:
        for f in x:
            print(float(f)) """
            
# Search for lines that start with "Details: rev=" followed by numbers. Then print the numbers if one is found.
""" hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall("^Details:.*rev=([0-9]+)", line)
    if len(x) > 0:
        for i in x:
            print(int(i)) """
            
# Search for lines that start with "From" and a character followed by a "two digit number between 00 and 99" followed by 
# ':'. Then print the number if one is found.
""" hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall("^From .* ([0-9][0-9]):", line)
    if len(x) > 0:
        for i in x:
            print(int(i)) """
            
""" x = "We just received $10.00 for cookies."
y = re.findall("\$[0-9.]+", x)
# y = re.findall("\B", x)
# y = re.findall("\b", x)
for f in y:
    print(f) """    
    
# Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular 
# expression and count the number of lines that matched the regular expression: 
""" pattern = input('Enter a regular expression: ')
hand = open('mbox.txt')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search(f"{pattern}", line):
        count += 1

print(f"mbox.txt had {count} lines that matched {pattern}") """
    
# Write a program to look for lines of the form: New Revision: 39772. Extract the number from each of the lines using a 
# regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.
fname = input('Enter file: ')
hand = open(fname)

count = 0
lst = []
sum_numbers = 0
for line in hand:
       line = line.rstrip()
       x = re.findall("^New Revision: ([0-9][0-9][0-9][0-9][0-9]+?)", line)
       if len(x) > 0:
#            val = float(x[0])
#            lst.append(val)
# print(int(sum(lst)/len(lst)))
           
           for i in x:
               count += 1
               sum_numbers += int(i)
           
average = (sum_numbers/count)
print(int(average))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    