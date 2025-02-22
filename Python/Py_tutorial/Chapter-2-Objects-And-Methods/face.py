"""A simple graphics example construct a face from basic shapes."""

from graphics import *

def main():
    winWidth = 200 # give a name to the window width
    winHeight = 150 # and height
    win = GraphWin('Face', winWidth, winHeight) # give title and dimensions
    win.setCoords(0, 0, winWidth, winHeight) # make right side up coordinates!

    head = Circle(Point(40, 100), 25) # set center and radius
    head.setFill('yellow')
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    # eye2 = Circle(Point(50, 105), 5)
    # eye2.setFill('blue')
    # eye2.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill('red')
    mouth.draw(win)

    rect = Rectangle(Point(30, 90), Point(50, 85))
    rect.draw(win)

    # These lines can be used to terminate any graphics program
    message = Text(Point(winWidth/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()

# input()






