def calcWeeklyWages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage. Include overtime for hours over 40.
    '''

    if totalHours <= 40:
        regularHours = totalHours
        overtime = 0
    else:
        regularHours = 40
        overtime = totalHours - 40
    return hourlyWage*regularHours + (1.5 * hourlyWage)*overtime  

def main():
    hours = float(input('Enter hours worked:\n'))
    wage = float(input('Enter dollars paid per hour:\n'))
    total = calcWeeklyWages(hours, wage)

    # print(f'Wages are ${total:.2f}.')
    print('Wages are ${total:.2f}.'.format(**locals()))

main()