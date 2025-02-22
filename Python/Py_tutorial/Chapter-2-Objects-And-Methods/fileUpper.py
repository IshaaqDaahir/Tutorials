fname = input("Enter a file name: ")
upperContents = open(fname).read().upper()
print(upperContents)