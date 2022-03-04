#!/usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

def callback(msg):
	A = msg.ranges[]
	if A <= .5:
		print("1")
	else:
		print("0")
	B = msg.ranges[]
	if B <= .5:
		print("1")
	else:
		print("0")
	C = msg.ranges[]
	if C <= .5:
		print("1")
	else:
		print("0")
	D = msg.ranges[]
	if D <= .5:
		print("1")
	else:
		print("0")



rospy.init_node('check_obstacle')

sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
