'''Test animation and depth.'''

from graphics import *
import time

def main():
    winWidth = 300
    winHeight = 300
    win = GraphWin('Back and Forth', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)

    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill('blue')
    rect.draw(win)

    cir1 = Circle(Point(40, 100), 25)
    cir1.setFill('yellow')
    cir1.draw(win)

    cir2 = Circle(Point(150, 125), 25)
    cir2.setFill('red')
    cir2.draw(win)

    for i in range(46):    # animate cir1 to the right
        cir1.move(5, 0)
        time.sleep(0.1)

    for i in range(46):    # animate cir1 to the left
        cir1.move(-5, 0)
        time.sleep(0.1)

    for i in range(46):    # animate cir1 to the right
        cir1.move(5, 0)
        time.sleep(0.1)

    for i in range(46):    # animate cir1 to the left
        cir1.move(-5, 0)
        time.sleep(0.1)

    # Wait for a final click to exit
    Text(Point(winWidth/2, 20), 'Click anywhere to quit.').draw(win)
    win.getMouse()
    win.close()

main()

