def joinStrings(stringList):
    '''Join all the strings in stringList into one string, and return the result.'''
    joined = ''
    for string in stringList:
        joined = joined + string
    return joined

def main():
    print(joinStrings(['very ', 'hot ', 'day!']))
    print()
    print(joinStrings(['I ', 'am ', 'very', ' happy', ' today!']))
    
main()
    