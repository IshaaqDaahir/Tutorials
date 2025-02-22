from graphics import *

winWidth = 500 # give a name to the window width
winHeight = 500 # and height
win = GraphWin('Scene', winWidth, winHeight) # give title and dimensions
win.setCoords(0, 0, winWidth, winHeight) # make right side up coordinates!
win.setBackground('gray')

def person_1():
    person_one_head = Circle(Point(100, 450), 40) # set center and radius
    person_one_head.setFill('brown')
    person_one_head.draw(win)

    person_one_eye_1 = Circle(Point(85, 460), 7)
    person_one_eye_1.setFill('black')
    person_one_eye_1.draw(win)

    person_one_nose = Circle(Point(100, 448), 5)
    person_one_nose.setFill('blue')
    person_one_nose.draw(win)

    person_one_eye_2 = Circle(Point(117, 460), 7)
    person_one_eye_2.setFill('black')
    person_one_eye_2.draw(win)

    person_one_mouth = Oval(Point(80, 425), Point(120, 440)) # set corners of bounding box
    person_one_mouth.setFill('orange')
    person_one_mouth.setWidth(2)
    person_one_mouth.draw(win)

    person_one_neck = Line(Point(100, 410), Point(100, 390))
    person_one_neck.setWidth(7)
    person_one_neck.draw(win)
    person_one_neck.setFill('brown')

    person_one_hand_1 = Line(Point(98, 393), Point(5, 300))
    person_one_hand_1.setWidth(7)
    person_one_hand_1.draw(win)
    person_one_hand_1.setFill('brown')

    person_one_hand_2 = Line(Point(102, 393), Point(270, 350))
    person_one_hand_2.setWidth(7)
    person_one_hand_2.draw(win)
    person_one_hand_2.setFill('brown')

    person_one_body = Line(Point(100, 410), Point(100, 230))
    person_one_body.setWidth(10)
    person_one_body.draw(win)
    person_one_body.setFill('brown')

    person_one_leg_1 = Line(Point(100, 240), Point(5, 50))
    person_one_leg_1.setWidth(10)
    person_one_leg_1.draw(win)
    person_one_leg_1.setFill('brown')

    person_one_leg_2 = Line(Point(100, 240), Point(195, 50))
    person_one_leg_2.setWidth(10)
    person_one_leg_2.draw(win)
    person_one_leg_2.setFill('brown')

def person_2():
    person_two_head = Circle(Point(400, 450), 40) # set center and radius
    person_two_head.setFill('purple')
    person_two_head.draw(win)

    person_two_eye_1 = Circle(Point(415, 460), 7)
    person_two_eye_1.setFill('black')
    person_two_eye_1.draw(win)

    person_two_nose = Circle(Point(399, 448), 5)
    person_two_nose.setFill('orange')
    person_two_nose.draw(win)

    person_two_eye_2 = Circle(Point(383, 460), 7)
    person_two_eye_2.setFill('black')
    person_two_eye_2.draw(win)

    person_two_mouth = Oval(Point(380, 425), Point(420, 440)) # set corners of bounding box
    person_two_mouth.setFill('green')
    person_two_mouth.setWidth(2)
    person_two_mouth.draw(win)

    person_two_neck = Line(Point(400, 410), Point(400, 390))
    person_two_neck.setWidth(10)
    person_two_neck.draw(win)
    person_two_neck.setFill('purple')

    person_two_hand_1 = Line(Point(403, 393), Point(495, 300))
    person_two_hand_1.setWidth(7)
    person_two_hand_1.draw(win)
    person_two_hand_1.setFill('purple')

    person_two_hand_2 = Line(Point(400, 395), Point(200, 350))
    person_two_hand_2.setWidth(7)
    person_two_hand_2.draw(win)
    person_two_hand_2.setFill('purple')

    person_two_body = Line(Point(400, 410), Point(400, 230))
    person_two_body.setWidth(10)
    person_two_body.draw(win)
    person_two_body.setFill('purple')

    person_two_leg_1 = Line(Point(400, 230), Point(495, 50))
    person_two_leg_1.setWidth(10)
    person_two_leg_1.draw(win)
    person_two_leg_1.setFill('purple')

    person_two_leg_2 = Line(Point(400, 230), Point(300, 50))
    person_two_leg_2.setWidth(10)
    person_two_leg_2.draw(win)
    person_two_leg_2.setFill('purple')

def food():
    message = Text(Point(winWidth/2, 20), 'Click on six points between catoons')
    message.draw(win)

    # Get and draw six vertices of polygon
    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)

    p4 = win.getMouse()
    p4.draw(win)

    p5 = win.getMouse()
    p5.draw(win)

    p6 = win.getMouse()
    p6.draw(win)

    vertices = [p1, p2, p3, p4, p5, p6]
    food_bowl = Polygon(vertices)
    food_bowl.setFill('indigo')
    food_bowl.setOutline('white')
    food_bowl.setWidth(4)    # width of boundary line
    food_bowl.draw(win)

    # These lines can be used to terminate any graphics program
    message.setText('Click anywhere to quit.')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    
    win.getMouse()
    win.close()

def main():
    win.getMouse()
    person_1()

    win.getMouse()
    person_2()

    win.getMouse()
    food()

main()

# input()