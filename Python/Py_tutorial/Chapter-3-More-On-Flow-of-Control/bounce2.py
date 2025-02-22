'''Show a ball bouncing off the sides of the window.
'''
from graphics import *
import time, random

def bounceInBox(shape, dx, dy, xLow, xHigh, yLow, yHigh, win):
    '''Animate a shape moving in jumps (dx, dy), bouncing when its center reaches the
    low and high x and y coordinates.
    '''

    delay = .005
    
    msg = Text(Point(145, 20), 'Click to start.').draw(win)
    win.getMouse()
    while win.checkMouse() == None:
        shape.move(dx, dy)
        center = shape.getCenter()
        x = center.getX()
        y = center.getY()
        if x < xLow:
            dx = -dx
        elif x > xHigh:
            dx = -dx

        if y < yLow:
            dy = -dy
        elif y > yHigh:
            dy = -dy
        time.sleep(delay)
        msg.setText('Click to stop and end.')

def getRandomPoint(xLow, xHigh, yLow, yHigh):
    '''Return a random Point with coordinates in the range specified.'''
    x = random.randrange(xLow, xHigh + 1)
    y = random.randrange(yLow, yHigh + 1)
    return Point(x, y)

def makeDisk(center, radius, win):
    '''Return a red disk that is drawn in win with given center and radius.'''

    disk = Circle(center, radius)
    disk.setOutline('red')
    disk.setFill('red')
    disk.draw(win)
    return disk

def getShift(point1, point2):
    '''Returns a tuple (dx, dy) which is the shift from point1 to point2.'''
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    return (dx, dy)

def getUserShift(point, prompt, win):
    '''Return he change in position from the point toa mouse click in win.
    First display the prompt string under point.'''

    text = Text(Point(point.getX(), 60), prompt)
    text.draw(win)
    userPt = win.getMouse()
    text.undraw()
    return getShift(point, userPt)

def bounceBall(dx, dy):
    '''Make a ball bounce around the screen, initially moving by (dx, dy)
    at each jump.'''

    winWidth = 290
    winHeight = 290
    
    win = GraphWin('Ball Bounce', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)

    radius = 10
    xLow = radius # center is separated from the wall by the radius at a bounce
    xHigh = winWidth - radius
    yLow = radius 
    yHigh = winHeight - radius

    center = Point(winWidth/2, winHeight/2)
    ball = makeDisk(center, radius, win)

    # NEW interactive direction and speed setting
    prompt = '''Click to indicate the direction 
    and speed of the ball: The further 
    you click from the ball, the faster 
    it starts.'''
    
    (dx, dy) = getUserShift(center, prompt, win)
    scale = 0.01 # to reduce the size of animation steps

    bounceInBox(ball, dx*scale, dy*scale, xLow, xHigh, yLow, yHigh, win)
    Text(Point(145, 20), 'Click to quit.')
    win.getMouse()
    win.close()

# bounceBall(3, 5)
bounceBall(-3, -5)
