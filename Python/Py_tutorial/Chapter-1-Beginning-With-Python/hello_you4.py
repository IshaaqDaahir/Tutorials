# The example program hello_you4.py does the same thing as the earlier hello_you 
# versions, but with a dictionary reference:
person = input("Enter your name: ")
greeting = 'Hello {person}!'.format(**locals())
print(greeting)




















