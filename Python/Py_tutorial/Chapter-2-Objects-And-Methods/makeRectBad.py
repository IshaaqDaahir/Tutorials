"""Program: makeRectBad.py
Attempt a function makeRect (incorrectly), which takes a corner Point and directions
to construct a rectangle."""

from graphics import *

# def makeRect(corner, width, height):    # Incorrect!
#     '''Return a new Rectangle given one corner Point and the dimensions.'''
#     corner2 = corner
#     corner2.move(width, height)
#     return Rectangle(corner, corner2)

def makeRect(corner, width, height):    
    '''Return a new Rectangle given one corner Point and the dimensions.'''
    corner2 = corner.clone()
    corner2.move(width, height)
    return Rectangle(corner, corner2)

def main():
    winWidth = 300
    winHeight = 300
    win = GraphWin('Draw a Rectangle (NOT!)', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    rect = makeRect(Point(20, 50), 250, 200)
    rect.draw(win)

    # Wait for another click to exit 
    msg = Text(Point(winWidth/2, 20), 'Click anywhere to quit.')
    msg.draw(win)
    win.getMouse()
    win.close()

main()

