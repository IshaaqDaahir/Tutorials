# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     count += 1
#     # print(line)
# print('Line Count: ', count)

# If you know the file is relatively small compared to the size of your main 
# memory, you can read the whole file into one string using the read method on 
# the file handle.

# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# # print(inp[:20])

# It is a good idea to store the output of read as a variable because each call 
# to read exhausts the resource:

# fhand = open('mbox-short.txt')
# print(len(fhand.read()))
# print(len(fhand.read()))

# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:'):
#         print(line)

# We could use line slicing to print all but the last character, but a simpler 
# approach is to use the rstrip method which strips whitespaces from the right 
# side of a string as follows:
    
# fhand = open('mbox-short.txt')
# for line in fhand:
#     # line = line[:-1]
    
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)
        
# We can structure the loop to follow the pattern of skipping uninteresting lines
# as follows:

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip() 
#     # Skip 'uninterested lines'
#     if not line.startswith('From:'):
#         continue
#     # Process our 'interesting' line  
#     print(line)

# we can write the following loop to show lines which contain the string 
# “@uct.ac.za” (i.e., they come from the University of Cape Town in South Africa):

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.find('@uct.ac.za') == -1: continue
#     print(line)

# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0 
# for line in fhand:
#     if line.startswith('Subject:'):
#         count += 1
# print(f'There were {count} subject lines in {fname}')

# We need to assume that the open call might fail and add recovery code when the 
# open fails as follows:
 
# while True:
#     fname = input('Enter the file name: ')
#     try:
#         fhand = open(fname)
    
#         count = 0
#         for line in fhand:
#             if line.startswith('Subject:'):
#                 count += 1
#         print(f'There were {count} subject lines in {fname}')
#         break
    
#     except:
#         print(f'File can not be opened: {fname}')
#         continue
        
# Writing files

# fout = open('mbox-short.txt', 'w')
practice = open('practice3.txt', 'w')
line1 = "This here's the wattle,\n"
practice.write(line1)

line2 = 'the emblem of our land.\n'
practice.write(line2)
practice.close()

# The built-in function "repr" can help. It takes any object as an argument and 
# returns a string representation of the object. For strings, it represents 
# whitespace characters with backslash sequences:

# s = '1 2\t 3\n 4'
# print((s))

# Write a program to read through a file and print the contents of the file 
# (line by line) all in upper case.

# while True:
#     try:
#         fname = input('Enter the file name: ')
#         fhand = open(fname)
#         result = fhand.read()
        
#         for line in result:
#             convert = result.upper()
#         print(convert)
#         break
#     except:
#         print(f'File can not be opened: {fname}')
#         continue
   
# Write a program to prompt for a file name, and then read through the file and 
# look for lines of the form: X-DSPAM-Confidence: 0.8475 
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart 
# the line to extract the floating-point number on the line. Count these lines 
# and then compute the total of the spam confidence values from these lines. 
# When you reach the end of the file, print out the average spam confidence.

# while True:
#     try:
#         fname = input('Enter the file name: ')
#         fhand = open(fname)
        
#         count = 0
#         total = 0
#         for line in fhand:
#             if not line.startswith('X-DSPAM-Confidence:'): 
#                 continue
#             if line.startswith('X-DSPAM-Confidence:'):
#                 colon_pos = line.find(':')
#                 extract = line[colon_pos + 1 : ]
                
#                 count += 1
#                 total = total + float(extract) 
#                 average = total/count
#         print(f'Average spam confidence: {average}')
#         break
    
#     except:
#         print(f'File can not be opened: {fname}')
#         continue
    
# Modify the program that prompts the user for the file name so that it prints a 
# funny message when the user types in the exact file name “na na boo boo”. 
# The program should behave normally for all other files which exist and don’t 
# exist. 

# while True:
#     try:
#         fname = input('Enter the file name: ')
        
#         if fname == 'na na boo boo':
#             print("NA NA BOO BOO TO YOU - You have been punk'd!")
#             break
        
#         fhand = open(fname)
        
#         count = 0
#         total = 0
#         for line in fhand:
#             if not line.startswith('X-DSPAM-Confidence:'): 
#                 continue
#             if line.startswith('X-DSPAM-Confidence:'):
#                 colon_pos = line.find(':')
#                 extract = line[colon_pos + 1 : ]
                
#                 count += 1
#                 total = total + float(extract) 
#                 average = total/count
#         print(f'Average spam confidence: {average}')
#         break
    
#     except:
#         print(f'File can not be opened: {fname}')
#         continue




