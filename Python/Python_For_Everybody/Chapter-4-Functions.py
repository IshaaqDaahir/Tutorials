import math
import random

signal_power = 10
noise_power = 20.5

ratio = signal_power/noise_power
decibels = 10 * math.log10(ratio)

degrees = 45
radians = degrees / 360.0 * (2*math.pi)
result = math.sin(radians)

# =============================================================================
# for i in range(5):
#     x = random.random()
#     print(x)
# =============================================================================

rand_int = random.randint(5, 10)

t = [1, 2, 3]
select  = random.choice(t)

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
    
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
# repeat_lyrics()

power = math.pow(2, 4)
# print(power)

def print_twice(bruce):
    print(bruce)
    print(bruce)

michael = "Eric, the half a bee."
# result = print_twice('Bing')

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 15)
# print(x)

# REWRITE YOUR PAY COMPUTATION WITH TIME-AND-A-HALF FOR OVERTIME AND CREATE A 
# FUNCTION CALLED computepay WHICH TAKES TWO PARAMETERS (hours and rate).

def computepay(hours, rate):
    try:
        hours = float(input("Enter Hours:\n"))
        rate = float(input('Enter Rate:\n'))
        
        if (hours) > 40:
             over_time = (rate) * 1.5
             pay = (((hours) - 40) * over_time) + (40 * (rate))
             print('Pay = ', pay)
        else:
             pay = (hours) * (rate)
             print('Pay = ', pay)
    except:
         print('Error, please enter numeric input!')

computepay('hours', 'rate')
    
# REWRITE THE GRADE PROGRAM FROM THE PREVIOUS CHAPTER USING A FUNCTION CALLED 
# computegrade THAT TAKES A SCORE AS ITS PARAMETER AND RETURNS A GRADE AS A STRING.
    
def computegrade(score):
    try:
        score = float(input('Enter score between 0.0 and 1.0:\n'))
        
        if score > 1.0:
            print('Bad score!')
        elif score >= 0.9:
             print('Your grade is: A')
             
        elif score >= 0.8:
             print('Your grade is: B')
             
        elif score >= 0.7:
             print('Your grade is: C')
             
        elif score >= 0.6:
             print('Your grade is: D')
             
        elif score < 0.6:
             print('Your grade is: F')
             
        else:
             print('Bad score!')
             
    except:
         print('Bad score!')
         
# computegrade('score')