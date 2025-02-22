# fruit = 'Mangos'

# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index + 1

# Write a while loop that starts at the last character in the string and works its 
# way backwards to the first character in the string, printing each letter on a 
# separate line, except backwards.

# fruit = 'Orange'
# index = len(fruit) - 1
# while index >= 0:
#     letter = fruit[index]
#     print(letter)
#     index -= 1

# fruit = 'Mangos'
# for char in fruit:
#     print(char)

# def count(word, char):
#     count = 0
#     for letter in word:
#         if letter == char:
#             count = count + 1
#     print(f'Count = {count}')

# count('banana', 'a')

# word = 'Pineapple'
# conv_word = word.upper()
# if word < 'banana':
#     print(f'Your word, {word}, comes before banana.')
# elif word > 'banana':
#     print(f'Your word, {word}, comes after banana.')
# else:
#     print('Alright, bananas.')

# Write an invocation that counts the number of times the letter "a" occurs in 
# “banana”.
name = 'banana'
occurs = name.count('a')
# print(occurs)

data = 'From stephen,marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
sppos = data.find(' ', atpos)
host = data[atpos + 1: sppos]
print(host)

years = 3
count = .1
species = 'camels'
seen = f'In {years} I have spotted {count} {species}.'
# print(seen)

# Exercise 5: Take the following Python code that stores a string:
string = 'X-DSPAM-Confidence:0.8475'
colon_pos = string.find(':')
extract = string[colon_pos + 1 : ]
conversion = float(extract)
# print(conversion)

data = "Write an invocation that counts the number of times the letter"
# print(data.replace("W", 'Abubakar'))















