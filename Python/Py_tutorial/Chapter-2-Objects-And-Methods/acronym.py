def acronym():
    phrase = input('Enter a phrase: ').upper().split()
    
    letters = []
    
    for word in phrase:
        letter = word[0]
        letters.append(letter)
        
    joinedLetters = "".join(letters)  
    print(joinedLetters)
    
acronym()  
    
# students against drunk driving  SADD
















