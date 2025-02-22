def letterGrade(score):
    if score >= 90:
        letter = 'F'
    elif score >= 80:
        letter = 'D'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'B' 
    else:
        letter = 'A'
    return letter

grade = int(input('Enter your score here:\n'))
print(f'Your grade is {letterGrade(grade)}!')

