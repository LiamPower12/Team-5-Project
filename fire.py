import robot

r = robot.RobotController()
r.connect()

while r.scan_for_fire() == True:
     r.extinguish_fire()





































































