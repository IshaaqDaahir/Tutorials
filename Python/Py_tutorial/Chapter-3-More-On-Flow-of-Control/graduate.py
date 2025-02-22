name = input('Enter your name here:\n')

creditsNum = int(input('How many credits do you have?\n'))
if creditsNum >= 128:
    print(f'Congratulations {name}, you have enough credits for graduation!')
else:
    print(f'Sorry {name}, you are not eligible for graduation!')