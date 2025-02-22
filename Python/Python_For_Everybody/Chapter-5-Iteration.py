# =============================================================================
# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Blastoff')
# =============================================================================

# INFINITE LOOP
# =============================================================================
# n = 10
# while True:
#     print(n, end=' ')
#     n = n - 1
# print("Done")
# =============================================================================

# FOR EXAMPLE, SUPPOSE YOU WANT TO TAKE INPUT FROM THE USER UNTIL THEY TYPE 
# "done". YOU COULD WRITE:

# =============================================================================
# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')
# =============================================================================

# =============================================================================
# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')
# =============================================================================

# =============================================================================
# friends = ['Josef', 'Glenn', 'Sally']
# for friend in friends:
#     print('Happy New Year: ', friend)
# print('Done!')
# =============================================================================

# =============================================================================
# count = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#     count = count + 1
# print('Count: ', count)
# =============================================================================

# =============================================================================
# total = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#     total = total + itervar
# print('Total: ', total)
# =============================================================================

nums = [3, 41, 12, 9, 74, 15]
# length = len(nums)
total = sum(nums)
# print(total)

# =============================================================================
# largest = None
# print('Before', largest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar > largest:
#         largest = itervar
#     print('Loop: ', itervar, largest)
# print('Largest: ', largest)
# =============================================================================

# smallest = None
# print('Before', smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#     print('Loop: ', itervar, smallest)
# print('Smallest: ', smallest)

nums = [3, 41, 12, 9, 74, 15]
maximum = max(nums)
minimum = min(nums)
# print(minimum)

# THE FOLLOWING IS A SIMPLE VERSION OF THE PYTHON BUILT-IN min() FUNCTION
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

# Write a program which repeatedly reads numbers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try
# and except and print an error message and skip to the next number.

# total = 0
# count = 0

# while True:
#         line = (input('Enter a number: '))
#         if line[0] == '#':
#             continue
#         if line == 'done':
#             break
#         try:
#             value = float(line)
#         except:
#             print('Invalid input!')
#             continue
#         total = total + value
#         count = count + 1
    
# print('Total: ', total)
# print('Count: ', count)
# print('Average = ', (total) / (count))
        
# Write another program that prompts for a list of numbers as above and at the 
# end prints out both the maximum and minimum of the numbers instead of the 
# average.

numbers = []
while True:
    try:
        line = (input('Enter numbers to find minimum and maximum: '))
        if line[0] == '#':
            continue
        if line == 'done':
            break
        
        value = int(line)    
    except:
        print('Invalid input!')
        continue
    numbers.append(value)
    minimum = min(numbers)
    maximum = max(numbers)
    
print('Minimum: ', minimum)        
print('Maximum: ', maximum)



        



















