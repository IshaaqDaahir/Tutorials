# REWRITE YOUR PAY COMPUTATION TO GIVE THE EMPLOYEE 1.5 TIMES THE HOURLY RATE FOR
# HOURS WORKED ABOVE 40 HOURS.

# =============================================================================
# hours = input('Enter hours?\n')
# 
# rate = input('Enter rate?\n')
# 
# if float(hours) > 40:
#     over_time = float(rate) * 1.5
#     pay = ((float(hours) - 40) * over_time) + (40 * float(rate))
#     print('Pay = ', pay)
# else:
#     pay = float(hours) * float(rate)
#     print('Pay = ', pay)
# =============================================================================
    
# REWRITE YOUR PAY PROGRAM USING TRY AND EXCEPT SO THAT YOUR PROGRAM HANDLES 
# NON-NUMERIC INPUT GRACEFULLY BY PRINTING A MESSAGE AND EXITING THE PROGRAM.

try:
    hours = float(input('Enter hours?\n'))
 
    rate = float(input('Enter rate?\n'))
     
    if (hours) > 40:
        over_time = (rate) * 1.5
        pay = (((hours) - 40) * over_time) + (40 * (rate))
        print('Pay = ', pay)
    else:
        pay = (hours) * (rate)
        print('Pay = ', pay)
except:
     print('Error, please enter numeric input!')
    
# WRITE A PROGRAM TO PROMPT FOA A SCORE BETWEEN 0.0 AND 1.0. IF THE SCORE IS OUT 
# OF RANGE, PRINT AN ERROR MESSAGE.

# =============================================================================
# try:
#     score = float(input('Enter score between 0.0 and 1.0:\n'))
#     
#     if score > 1.0:
#         print('Bad score!')
#         
#     elif score >= 0.9:
#         print('Your grade is: A')
#         
#     elif score >= 0.8:
#         print('Your grade is: B')
#         
#     elif score >= 0.7:
#         print('Your grade is: C')
#         
#     elif score >= 0.6:
#         print('Your grade is: D')
#         
#     elif score < 0.6:
#         print('Your grade is: F')
#         
#     else:
#         print('Bad score!')
#         
# except:
#     print('Bad score!')
# =============================================================================
    










