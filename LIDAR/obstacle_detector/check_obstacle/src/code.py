#!/usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

def callback(msg):
	a = min(msg.ranges)
	if a <= .5:
		print("1")
	else:
		print("0")



rospy.init_node('check_obstacle')

sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
