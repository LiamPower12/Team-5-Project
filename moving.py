import robot
r = robot.RobotController()
r.connect()

l = []

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
    r.backward(250)
    r.forward(850)

def room_num_1():
    r.left(100)
    r.forward(360)
    r.read_marker()
    if r.read_marker() == 1:
        r.left(675)
        r.take_temperature()
        l.append(r.take_temperature())
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
    r.read_marker()
    if r.read_marker() == 1:
        r.left(675)
        r.take_temperature
        l.append(r.take_temperature())
        r.forward(150)
        r.scan_for_fire()
        while r.scan_for_fire() == True:
            r.extinguish_fire()
        r.backward(150)
        r.right(675)


room_num_2()

def room_num_3():
    r.forward(450)
    r.rotate_counterclockwise(90)
    r.forward(1660)
    r.read_marker()
    while r.read_marker() == 2:
        r.left(150)
        r.take_temperature
        l.append(r.take_temperature())
        r.right(250)


room_num_3()


def room_num_4():
    r.forward(600)
    r.rotate_counterclockwise(90)
    r.forward(900)
    r.left(800)
    r.forward(850)
    r.read_marker()
    if r.read_marker() == 1:
        r.forward(300)
        r.take_temperature
        l.append(r.take_temperature())
        r.left(600)
        r.scan_for_fire()
        while r.scan_for_fire() == True:
            r.extinguish_fire()
        r.right(600)
        r.backward(325)

room_num_4()

def room_num_5():
    r.left(1475)
    r.forward(150)
    r.read_marker()
    if r.read_marker() == 1:
        r.forward(300)
        r.take_temperature()
        l.append(r.take_temperature())
        r.left(300)
        r.scan_for_people()
        if r.scan_for_people() == True:
            r.rescue_person()
        r.right(300)
        r.backward(450)



room_num_5()


def room_back():
    r.right(1475)
    r.backward(800)
    r.right(800)
    r.backward(850)
    r.left(2300)
    r.forward(1400)


room_back()

print(l)

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [l[0], l[1], l[2], l[3], l[4]]
plt.plot(x, y)
plt.show()