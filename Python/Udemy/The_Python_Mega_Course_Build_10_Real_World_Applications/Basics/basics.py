# def sentence_maker(phrase):
#     interrogatives = ('how', 'what', 'why', 'when', 'which')
#     capitalized = phrase.capitalize()
#     if phrase.startswith(interrogatives):
#         return '{}?'.format(capitalized)
#     else:
#         return '{}.'.format(capitalized)

# results = []
# while True:
#     user_input = input('Say something: ')
#     if user_input == '/end':
#         break
#     else:
#         results.append(sentence_maker(user_input))

# print(' '.join(results))

# LIST COMPREHENSION
# temps = [221, 234, 340, 230]

# new_temps = [temp / 10 for temp in temps]

# print(new_temps)

# # LIST COMPREHENSION WITH CONDITIONALS
# temps = [221, 234, 340, -9999, 230]

# new_temps = [temp / 10 if temp != -9999 else 0  for temp in temps]

# print(new_temps)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Zero division is meaningless'
    
print(divide(1, 0))
print('End of program')

