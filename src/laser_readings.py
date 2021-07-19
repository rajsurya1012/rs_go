#! /usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

def callback_laser(msg):
    regions=[
        min(min(msg.ranges[0:143]),10),
        min(min(msg.ranges[144:287]),10),
        min(min(msg.ranges[288:431]),10),
        min(min(msg.ranges[432:575]),10),
        min(min(msg.ranges[576:713]),10),
    ]
    rospy.loginfo(regions)

def main():
    rospy.init_node('laser_readings')
    sub=rospy.Subscriber("/rs_go/laser/scan", LaserScan, callback_laser)
    rospy.spin()

if __name__=='__main__':
    main()