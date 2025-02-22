'''Program: triangle.py or triangle.pyw (best name for Windows).
Interactive graphics program to draw a triangle, with prompts in a Text object and 
feedback via mouse clicks. Illustrates all of the most common GraphWin methods, 
plus some of the ways to change the appearance of the graphics.'''

from graphics import *

def main():
    winHeight = 300
    winWidth = 300
    win = GraphWin('Draw a Triangle', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)    # make right-side-up coordinates!
    win.setBackground('yellow')

    message = Text(Point(winWidth/2, 20), 'Click on three points')
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)

    # p4 = win.getMouse()
    # p4.draw(win)

    # p5 = win.getMouse()
    # p5.draw(win)

    # p6 = win.getMouse()
    # p6.draw(win)

    # vertices = [p1, p2, p3, p4, p5, p6]
    vertices = [p1, p2, p3]
    triangle = Polygon(vertices)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4)    # width of boundary line
    triangle.draw(win)

    # Wait for a final click to exit
    message.setText('Click anywhere to quit.')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)

    win.getMouse()
    win.close()

main()

input()