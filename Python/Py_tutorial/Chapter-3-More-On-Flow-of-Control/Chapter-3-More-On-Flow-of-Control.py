# Exercise 3.1.4.1. Write a program, graduate.py, that prompts students for how many credits they
# have. Print whether of not they have enough credits for graduation. (At Loyola University Chicago 128
# credits are needed for graduation.)

# Exercise 3.1.5.1. In Idle, load grade1.py and save it as grade2.py Modify grade2.py so it has an
# equivalent version of the letterGrade function that tests in the opposite order, first for F, then D, C, ....
# Hint: How many tests do you need to do? 2 Be sure to run your new version and test with different inputs
# that test all the different paths through the program.

# Exercise 3.1.5.2. Write a program sign.py to ask the user for a number. Print out which category
# the number is in: ’positive’, ’negative’, or ’zero’.

# Exercise 3.1.5.3. Modify the wages.py or the wages1.py example to create a program wages2.py that
# assumes people are paid double time for hours over 60. Hence they get paid for at most 20 hours overtime
# at 1.5 times the normal rate. For example, a person working 65 hours with a regular wage of $10 per hour
# would work at $10 per hour for 40 hours, at 1.5*$10 for 20 hours of overtime, and 2*$10 for 5 hours of double
# time, for a total of 10*40 + (1.5*10)*20 + (2*10)*5 = $800. You may find wages1.py easier to adapt than
# wages.py.

# Exercise 3.1.7.1. A person is eligible to be a US Senator who is at least 30 years old and has been
# a US citizen for at least 9 years. Write a version of a program congress.py to obtain age and length of
# citizenship from the user and print out if a person is eligible to be a Senator or not. A person is eligible to
# be a US Representative who is at least 25 years old and has been a US citizen for at least 7 years. Elaborate
# your program congress.py so it obtains age and length of citizenship and prints whether a person is eligible
# to be a US Representative only, or is eligible for both offices, or is eligible for neither.

# Exercise 3.2.0.2. a. Write a program chooseButton3.py, modifying chooseButton2.py. Look at the
# format of the list buttonSetup, and extend it so there is a larger choice of buttons and colors. Add at least
# one button and color.
# b. Further extend the program chooseButton3.py by adding some further graphical object shape to
# the picture, and extend the list shapePairs, so they can all be interactively colored.
# c. (Optional) If you would like to carry this further, also add a prompt to change the outline color of
# each shape, and then carry out the changes the user desires.
# d. (Optional Challenge) Look at the pattern within the list buttonSetup. It has a consistent x coordinate, and 
# there is a regular pattern to the change in the y coordinate (a consistent decrease each time). The
# only data that is arbitrary each time is the sequence of colors. Write a further version chooseButton4.py
# with a function makeButtonSetup, that takes a list of color names as a parameter and uses a loop to create
# the list used as buttonSetup. End by returning this list. Use the function to initialize buttonSetup. If you
# like, make the function more general and include parameters for the x coordinate, the starting y coordinate
# and the regular y coordinate change.

# Exercise 3.3.3.1. a. Write a program sumAll.py that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers. At the end (only) print out the
# sum. You should not need to create a list! You can immediately increase the sum with each number entered.

# Exercise 3.3.4.1. ** As discussed above, the basic loop logic works whether the poly.undraw() call is
# at the beginning or end of the loop. Write a variation makePoly2.py that makes the code work the other
# way, with the poly.undraw() at the beginning of the loop. The new place to cut the loop does affect the
# code before and after the loop. In particular, the extra statement drawing poly is not needed after the loop
# is completed. Make other changes to the surrounding code to make this work.

# Exercise 3.3.4.2. Write a program very similar to makePoly.py, and call it makePath.py, with a
# function pathHere. The only outward difference between polyHere and pathHere is that while the first
# creates a closed polygon, and returns it, and the new one creates a polygonal path, without the final point
# being automatically connected to the first point, and a list of the lines in the path is returned. Internally
# the functions are quite different. The change simplifies some things: no need to undraw anything in the
# main loop - just draw the latest segment each time going from the previous point to the just clicked point.
# There is a complication however, you do need deal specially with the first point. It has no previous point to
# connect to. I suggest you handle this before the main loop, and draw the point so it is a visible guide for
# the next point. After your main loop is finished undraw this initial point. (The place on the screen will still
# be visible if an initial segment is drawn. If no more points were added, the screen is left blank, which is the
# way it should be.) You also need to remember the previous point each time through the main loop.
# In your main program, test the makePath function several times. Use the list of lines returned to loop
# and change the color in one path and the width of the lines in another path.

# Exercise 3.3.4.3. ** (Optional) I chose to have the ball start motionless, by making the initial value
# of pt (which determines the initial (dx, dy) ) be the center of the ball. Write a variation startRandom.py
# so pt is randomly chosen. Also make the initial location of the ball be random. You can copy the function
# getRandomPoint from bounce1.py.

# Exercise 3.3.4.4. ** Write a program madlib4.py that modifies the getKeys method of madlib2.py
# to use a while loop. (This is not an animation program, but this section is where you have had the most
# experience with while loops!) Hint: 6
# 6 This is actually the most natural approach. I avoided while loops initially, when only for loops had been discussed. It
# is redundant in the original approach, however, to find every instance of ’{’ to count the number of repetitions and then find
# them all again when extracting the cue keys. A more natural way to control the loop is a while loop stopping when there are
# no further occurrences of ’{’. This involves some further adjustments. You must cut the loop in a different place (to end after
# searching for ’{’) . As discussed before, cutting a loop in a different place may require changes before and after the loop, too.



