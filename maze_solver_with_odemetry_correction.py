from robot_control_class import RobotControl

from math import degrees, copysign, sqrt, pow, pi

robotcontrol = RobotControl()

front=robotcontrol.get_front_laser()
right=robotcontrol.get_laser(0)
left=robotcontrol.get_laser(719)
correct=0
acc=0
while(left+right!=front):
    front=robotcontrol.get_front_laser()
    right=robotcontrol.get_laser(0)
    left=robotcontrol.get_laser(719)
    (position, rotation) = robotcontrol.get_odom()
    correct=degrees(rotation)
    if(correct>0):
        correct-=acc
    else:
        correct+=acc
       
    robotcontrol.rotate(correct)    
    
    if(front>0.8):
        robotcontrol.move_straight_time("forward",0.6,0.5)
    elif(right>left):
        robotcontrol.rotate(90)
        acc+=90
    elif(left>right):
        acc-=90
        robotcontrol.rotate(-90)

robotcontrol.stop_robot()

