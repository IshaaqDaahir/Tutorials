"""Test animation of a group of objects making a face."""

from graphics import *
import time

def moveAll(shapeList, dx, dy):
    """Move all shapes in shapeList by (dx, dy)."""
    for shape in shapeList:
        shape.move(dx, dy)

def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    """Animate the shapes in shapeList along a line. Move by dx, dy, each time.
    Repeat the specified number of repetetions. Have the specified delay (in seconds)
    after each repeat."""

    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)

def main():
    winWidth = 300
    winHeight = 300
    win = GraphWin('Back and Forth', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)    # make right side up coordinates!

    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill('Blue')
    rect.draw(win)

    head = Circle(Point(40, 100), 25)
    head.setFill('yellow')
    head.draw(win)   

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill("blue")
    eye1.draw(win)
    
    eye2 = Line(Point(45, 105), Point(55, 105))
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85))
    mouth.setFill('red')
    mouth.draw(win)

    faceList = [head, eye1, eye2, mouth]

    cir2 = Circle(Point(150, 125), 25)
    cir2.setFill('red')
    cir2.draw(win)

    moveAllOnLine(faceList, 5, 0, 46, .1)
    moveAllOnLine(faceList, -5, 0, 46, 0.1)

    moveAllOnLine(faceList, 5, 0, 46, .1)
    moveAllOnLine(faceList, -5, 0, 46, 0.1)

    Text(Point(winWidth/2, 20), 'Click anywhere to quit.').draw(win)
    win.getMouse()
    win.close()

main()

# input()