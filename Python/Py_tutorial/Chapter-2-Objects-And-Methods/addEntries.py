"""Example with two Entry objects and type Conversion.
Do addition."""

from graphics import *
from addEntries2 import makeLabeledEntry

def main():
    winWidth = 300
    winHeight = 300

    win = GraphWin("Addition", winWidth, winHeight)
    win.setCoords(0,0, winWidth, winHeight)
    instructions = Text(Point(winWidth/2, 30), 
                        "Enter two numbers.\nThen click the mouse.")
    instructions.draw(win)

    """ entry1 = Entry(Point(winWidth/2, 250), 25)
    entry1.setText("0")
    entry1.draw(win)
    Text(Point(winWidth/2, 280), "First Number:").draw(win)
    
    entry2 = Entry(Point(winWidth/2, 180), 25)
    entry2.setText('0')
    entry2.draw(win)
    Text(Point(winWidth/2, 210), "Second Number").draw(win)

    win.getMouse()  # To know the user is finished with the text.
    
    numStr1 = entry1.getText()
    num1 = int(numStr1)
    numStr2 = entry2.getText()
    num2 = int(numStr2) 

    sum = num1 + num2
    result = "The sum of\n{num1}\nplus\n{num2}\nis {sum}.".format(**locals())

    # result = f"The sum of\n{num1}\nplus\n{num2}\nis {sum}."
    Text(Point(winWidth/2, 110), result).draw(win)

    instructions.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()
    """

    entry1 = makeLabeledEntry(Point(winWidth/2, 250), 25,
                              '0', 'First Number:', win)
    entry2 = makeLabeledEntry(Point(winWidth/2, 180), 25,
                              '0', 'Second Number:', win)
    
    win.getMouse()  # To know the user is finished with the text.

    num1 = int(entry1.getText())
    num2 = int(entry2.getText())

    sum = num1 + num2
    result = "The sum of\n{num1}\nplus\n{num2}\nis {sum}.".format(**locals())

    # result = f"The sum of\n{num1}\nplus\n{num2}\nis {sum}."
    Text(Point(winWidth/2, 110), result).draw(win)

    instructions.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()