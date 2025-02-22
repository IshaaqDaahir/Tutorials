"""Draw random circles."""

from graphics import *
import random, time

def main():
    win = GraphWin('Random Circles', 300, 300)
    msg = Text(Point(150, 20),'Click to start.').draw(win)
    win.getMouse()
    while win.checkMouse() == None:
        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        color = color_rgb(r, g, b)

        radius = random.randrange(3, 40)
        x = random.randrange(5, 295)
        y = random.randrange(5, 295)

        circle = Circle(Point(x, y), radius)
        circle.setFill(color)
        circle.draw(win)
        time.sleep(.05)
        msg.setText('Click to stop and end.')
    
    msg.setText('Click to close.')
    win.getMouse()
    win.close()

main()