def getKeys(formatString):
    '''formatString is a format string with embedded dictionary keys. Return a list 
    containing all the keys from the format string.'''
    
    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        # find the start and end of the next key
        # We search for the start of the next key using/going from the end of the last 
        # one:
        start = formatString.find('{', end) + 1
        
        # We search for the end of the key using the start value here
        end = formatString.find('}', start)
        
        key = formatString[start : end] 
        keyList.append(key)

    return keyList

originalStory = """
Once upon a time, deep in an ancient jungle, there lived a 
{animal}. This {animal} liked to eat {food}, but the jungle 
had very little {food} to offer. One day, an explorer found 
the {animal} and discovered it liked {food}. The explorer 
took the {animal} back to {city}, where it could it as much
{food} as it wanted. However, the {animal} became homesick,
so the explorer brought it back to the jungle, leaving a 
large supply of {food}.

The End
"""

print(getKeys(originalStory))




