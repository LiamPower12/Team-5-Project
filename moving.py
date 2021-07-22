import robot
r = robot.RobotController()
r.connect()

#person1/no_person1 will bring the robot to room two using different routes depending if there is a person
#to be saved in room 1

def no_person1():
    r.backward(150)
    r.right(700)
    r.forward(575)

def person1():
    r.rescue_person()
    r.backward(150)
    r.right(700)
    r.backward(350)
    r.forward(950)

def room_num_1():
    r.left(100)
    r.forward(360)
    if r.read_marker() == 1:
        #temp function
        r.left(675)
        r.forward(100)
        r.scan_for_people()
        if r.scan_for_people() == False:
            no_person1()
        elif r.scan_for_people() == True:
            person1()
    else:
        r.left(135)
        r.forward(360)

room_num_1()

def room_num_2():
    if r.read_marker() == 1:
        #temp function
        #put in movements to get robot from marker to fire
        while r.scan_for_fire() == True:
            r.extinguish_fire()
        #movements to leave fire room
    r.forward(560)


room_num_2()

def room_num_3():
    r.forward(440)
    r.rotate_counterclockwise(90)
    r.forward(1550)
    if r.read_marker() == 1:
        #move into room
        #temp function
        #move out of room
    r.forward(440)
    r.rotate_counterclockwise(90)
    r.forward(1550)

room_num_3()

def room_num_4():
    if r.read_marker() == 1:
        #temp function
        #move robot to fire
        while r.scan_for_fire() == True:
            r.extinguish_fire()
        #move robot out of room
    r.forward(560)
    r.rotate_counterclockwise(86)
    r.forward(835)
    r.rotate_counterclockwise(84)
    r.forward(690)
    r.rotate_clockwise(83)
    r.forward(700)

room_num_4()


def room_num_5():
    if r.read_marker() == 1:
        #temp function
        #move robot to person
        r.scan_for_people()
        if r.scan_for_people() == True:
            r.rescue_person()
        #leave room
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
