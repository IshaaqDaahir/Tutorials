"""
String Substitution for a Mad Lib
Adapted from code by Kirby Urner
"""

storyFormat = """
Once upon a time, deep in an ancient jungle, there lived a {animal}. This {animal} 
liked to eat {food}, but the jungle had very little {food} to offer. One day an 
explorer found the {animal} and discovered it liked {food}. The explorer took the 
{animal} back to {city}, where it could eat as much {food} as it wanted. However, 
the {animal} became homesick, so the explorer brought it back to the jungle, 
leaving a large supply of {food}.

The End
"""

def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt)
    dictionary[cue] = response

def tellStory():
    userPicks = dict()
    for cue in ['animal', 'food', 'city']:
        addPick(cue, userPicks)
    story = storyFormat.format(**userPicks)
    print(story)
    
tellStory()

# This line is only here to accommodate running the program in Windows by double 
# clicking on its file icon. Without this line, the story would be displayed and 
# then the program would end, and Windows would make it immediately disappear from 
# the screen! This line forces the program to continue being displayed until there 
# is another response from the user, and meanwhile the user may look at the output 
# from tellStory
input('Press Enter to end the program.')