#!/usr/bin/env python

import json
import rospy
import time
from std_msgs.msg import String
from robot_body.msg import motorSet
from robot_body.msg import motorStat
from robot_body.msg import servoSet
print "WORD_LISTENNER successful import"

pub = dict()
motorStatus = dict()
motor = motorSet()
RservoPub = rospy.Publisher('servo/Rcmd', servoSet, queue_size=10)
LservoPub = rospy.Publisher('servo/Lcmd', servoSet, queue_size=10)
Rcmd = servoSet()
Lcmd = servoSet()

def getMotorInfo(data, name):
    motorStatus[name] = data

def callback(data):
    try:
        with open("/home/odroid/catkin_ws/src/robot_body/recording/data_base/"+ data.data + ".json", "r") as sign:
            movement = json.load(sign)

        names = movement["actors_NAME"]
        freq = float(movement["freq"])
        frames = movement["frame_number"]
        seq = movement["position"]

        for frame in range(frames):
            id = 0
            for name in names:
                motor.compliant = False # motorStatus[name].compliant
                motor.direct = motorStatus[name].direction
                motor.goal_position = seq[str(frame)]['Robot'][id]
                motor.offset = motorStatus[name].offset
                motor.max_load = motorStatus[name].max_load
                pub[name].publish(motor)
                id += 1

            Rcmd = seq[str(frame)]['Right_hand']
            Lcmd = seq[str(frame)]['Left_hand']
            RservoPub.publish(Rcmd)
            LservoPub.publish(Lcmd)

            time.sleep(1/freq)


    except Exception, err:
        print err

def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('Word', String, callback)
    list = ['abs_z', 'bust_y', 'bust_x', 'head_z', 'head_y', 'l_shoulder_y', 'l_shoulder_x', 'l_arm_z', 'l_elbow_y',
            'l_forearm_z', 'r_shoulder_y', 'r_shoulder_x', 'r_arm_z', 'r_elbow_y', 'r_forearm_z']
    for name in list:
        pub[name] = rospy.Publisher('poppy/set/' + name, motorSet, queue_size=10)
        rospy.Subscriber('poppy/get/' + name, motorStat, callback=getMotorInfo, callback_args=name)
    print 'WORD_LISTENER publishers & subscribers successful Initial'
    rospy.spin()

if __name__ == '__main__':
    listener()
