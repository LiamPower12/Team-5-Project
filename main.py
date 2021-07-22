import robot
r = robot.RobotController()
r.connect()


#if r.read_marker() == 1:

#else:


#functions for how the robot will move depending if there is a person in room 1
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

#moving from starting position to room 1
import moving
moving.room_num_1()

#add marker scanning function when it is made
r.left(675)
r.forward(100)

r.scan_for_people()

if r.scan_for_people() == False:
    no_person1()
elif r.scan_for_people()== True:
    person1()



