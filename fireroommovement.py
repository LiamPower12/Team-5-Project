import robot
r = robot.RobotController()
r.connect()

#movement starting from the middle block at the door

#room 2

r.left(385)
r.forward(150)

while r.scan_for_fire() == True:
     r.extinguish_fire()

r.backward(150)
r.right(385)

#room 4

r.forward(250)
r.rotate_counterclockwise(90)
r.forward(450)

while r.scan_for_fire() == True:
     r.extinguish_fire()

r.rotate_counterclockwise(180)
r.forward(450)
r.rotate_clockwise(90)
r.forward(250)



































































