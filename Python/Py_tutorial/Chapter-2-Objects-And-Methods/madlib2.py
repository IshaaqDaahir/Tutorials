"""
madlib2.py
Interactive display of a mad lib, which is provided as a 
Python format string, with all the cues being dictionary
formats, in the form {cue}. In this version, the cues are 
extracted from the story automatically, and the user is 
prompted for the replacements.

Original mad lib adapted form code of Kirby Urner

"""

def getKeys(formatString):  # change: returns a set
    """formatString is a format string with embedded 
    dictionary keys. Return a set containing all the keys
    from the format string."""
    keyList = list()
    
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key)    # may add duplicates
    return set(keyList)    # removes duplicates:
                           # no duplicates in a set
                           
def addPick(cue, dictionary):    # from madlib.py
    '''Prompt the user and add one cue to the dictionary.'''
    prompt = 'Enter an example for ' + cue + ': '
    dictionary[cue] = input(prompt)
    
def getUserPicks(cues):
    '''Loop through the collection of cue keys and get user choices. 
    Return the resulting dictionary.'''

    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks

def tellStory(story):
    '''story is a format string with Python dictionary references embedded, in the
    form {cue}. Prompt the user for the madlib substitutions and then print the 
    resulting story with the substitutions.'''

    cues = getKeys(story)
    userPicks = getUserPicks(cues)
    print(story.format(**userPicks))

def main():
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
    tellStory(originalStory)

main()



































