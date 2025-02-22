'''Make a choice of colors via mouse clicks in Rectangles --
Demonstrate loops using lists of tuples of data.'''

from graphics import *

def isBetween(x, end1, end2):
    """Return True if x is between the ends or equal to either.
    The ends do not need to be in increasing order."""

    return end1 <= x <= end2 or end2 <= x <= end1

def isInside(point, rect):
    '''Return True if point is inside the Rectangle rect.'''

    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return isBetween(point.getX(), pt1.getX(), pt2.getX()) and \
           isBetween(point.getY(), pt1.getY(), pt2.getY())

def polyHere(rect, win):
    '''Draw a polygon interactively in Rectangle rect, in GraphWin win.
    Collect mouse clicks inside rect into a Polygon.
    When a click goes outside rect, stop and return the final Polygon.
    The polygon ends up drawn. The method draws and undraws rect.'''

    rect.setOutline('red')
    rect.draw(win)
    
    lines = []
    Text(Point(200, 380),'Click your first point inside the shape.').draw(win)
    
    firstPoint = win.getMouse()
    prevPoint = firstPoint
    while isInside(prevPoint, rect):
        nextPoint = win.getMouse()
        line = Line(prevPoint, nextPoint)
        line.draw(win)
        lines.append(line)

        prevPoint = nextPoint

    rect.undraw()
    return lines

def main():
    winWidth = 400
    winHeight = 400
    win = GraphWin('Draw and Color Polygon', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)

    rect1 = Rectangle(Point(5, 55), Point(200, 120))
    line1 = polyHere(rect1, win)
    for line in line1:
        line.setWidth('5')

    rect2 = Rectangle(Point(210, 50), Point(350, 350))
    line2 = polyHere(rect2, win)
    for line in line2:
        line.setFill('green')
        line.setWidth('3')

    win.getMouse()
    win.close()

main()



