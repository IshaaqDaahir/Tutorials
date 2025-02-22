fname = input("Enter a file name: ")
upperContents = open(fname).read().upper()
newFile = open(f'UPPER{fname}', 'w')
newFile.write(upperContents)