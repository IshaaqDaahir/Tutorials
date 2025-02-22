"""Simple example with Entry objects.
Enter your name, click the mouse, and see greetings."""

from graphics import *

def main():
    winWidth = 300
    winHeight = 300
    infoHeight = 15
    win = GraphWin("Greeting", winWidth, winHeight)
    win.setCoords(0,0, winWidth, winHeight)

    instructions = Text(Point(winWidth/2, 40), 
                        "Enter your name.\nThen click the mouse.")
    instructions.draw(win)

    entry1= Entry(Point(winWidth/2, 200), 15)
    entry1.draw(win)
    Text(Point(winWidth/2, 230), "Name:").draw(win) # label for the Entry

    win.getMouse()  # To know the user is finished with the text.
    name = entry1.getText()

    greeting1 = "Hello, " + name + "!"
    Text(Point(winWidth/3, 150), greeting1).draw(win)

    greeting2 = "Bonjour, " + name + "!"
    Text(Point(2*winWidth/3, 100), greeting2).draw(win)

    instructions.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()