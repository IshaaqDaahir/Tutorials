"""Test animation of a group of objects making a face. Combine the face elements in 
a function, and use it twice. Have an extra level of repetition in the animation."""

from graphics import *
import time

def moveAll(shapeList, dx, dy):
    """Move all shapes in shapeList by (dx, dy)."""
    for shape in shapeList:
        shape.move(dx, dy)

def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    """Animate the shapes in shapeList along a line. Move by dx, dy, each time. Repeat
    the specified number of repetitions. Have the specified delay in seconds after 
    each repeat."""

    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)

def makeFace(center, win):  # NEW
    """Display face centered at center in window win. Return a list of the shapes in 
    the face."""

    head = Circle(center, 25)
    head.setFill('yellow')
    head.draw(win)

    eye1Center = center.clone() # face positions are relative to the center
    eye1Center.move(-10, 5)     # locate further points in relation to others
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)
    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)

    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill('red')
    mouth.draw(win)

    return [head, eye1, eye2, mouth]

def main():
    winWidth = 300
    winHeight = 300
    win = GraphWin('Back and Forth', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)    # make right side up coordinates!

    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill('blue')
    rect.draw(win)

    faceList = makeFace(Point(40, 100), win)    # NEW
    faceList2 = makeFace(Point(150, 125), win)

    stepsAccross = 46   #New section
    dx = 5
    dy =3
    wait = 0.1
    for i in range(1):
        moveAllOnLine(faceList, dx, 0, stepsAccross, wait)
        moveAllOnLine(faceList, -dx, 8, stepsAccross//2, wait)
        moveAllOnLine(faceList, -dx, -11, stepsAccross//2, wait)
        moveAllOnLine(faceList, dx, 0, stepsAccross, wait)

        # moveAllOnLine(faceList2, dx, 0, stepsAccross, wait)
        # moveAllOnLine(faceList2, -dx, 8, stepsAccross//2, wait)
        # moveAllOnLine(faceList2, -dx, -11, stepsAccross//2, wait)
        # moveAllOnLine(faceList2, dx, 0, stepsAccross, wait)

    Text(Point(winWidth/2, 20), 'Click anywhere to quit.').draw(win)
    win.getMouse()
    win.close()
        
main()
