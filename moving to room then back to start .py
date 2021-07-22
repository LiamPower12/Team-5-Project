import robot_mac
r = robot_mac.RobotController()
r.connect()

def room_num_1():
    r.left(135)
    r.forward(360)

room_num_1()

def room_num_2():
    r.forward(560)

room_num_2()

while r.scan_for_fire() == True:
     r.extinguish_fire()

def room_num_3():
    r.forward(440)
    r.rotate_counterclockwise(90)
    r.forward(1550)

room_num_3()

def room_num_4():
    r.forward(560)
    r.rotate_counterclockwise(86)
    r.forward(835)
    r.rotate_counterclockwise(84)
    r.forward(690)
    r.rotate_clockwise(83)
    r.forward(700)

room_num_4()

while r.scan_for_fire() == True:
     r.extinguish_fire()

def room_num_5():
    r.left(1000)
    r.forward(210)
    r.rotate_counterclockwise(85)
    r.forward(450)

room_num_5()

def room_back():
    r.backward(450)
    r.left(200)
    r.backward(900)
    r.left(650)
    r.rotate_clockwise(1)
    r.backward(1000)
    r.left(900)
    r.rotate_counterclockwise(6)
    r.forward(2000)
    r.rotate_clockwise(45)
    r.forward(350)
    r.rotate_clockwise(42)
    r.forward(1270)
    r.rotate_counterclockwise(180)



room_back()
