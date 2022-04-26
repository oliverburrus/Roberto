#!/usr/bin/env python

#LAST THING TO DO!!!
#Figure out how to orient robot 90 degrees



#Import required packages
import rospy 
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
import math
import message_filters


#The width of your robot in meters
robot_width = .5
#How far the lidar is set back on the robot in meters
lidar_y_position = .1
#How far you want your robot to stay away from obstacles in meters
clearence = .2

wall_width_right = 2
wall_width_left = 2

dist_to_mining_area = 3.616

#Max radius of LIDAR scan
R_value = (robot_width/2)/math.sin(math.radians(22.5))+lidar_y_position+clearence

#Now, we define the movement functions (eg. move_right, move_left, move_straight)
def move_right(data, pose_data):
	#Set the publisher and the initial state
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	msg = Twist()
    	linear_x = 0
    	angular_z = 0
    	state_description = ''
	
	#Get Pose data
	position_x = pose_data.pose.position.x
	orientation_x = pose_data.pose.orientation.x
	
	#Orient robot 90deg (in development)
	#while orientation_x < -math.pi/2:
	#	angular_z = 0.3
		
	#Get LIDAR data for the left quadrant
	a = data.ranges[147:233]
	
	#Set Left values
	if min(a) <= R_value+clearence:
		#If obstacle is still in robots' path
		Left = 2
	#elif position_x <= -(wall_width_right/2)-clearence: 
		#Needs proof of value
		# lighthouse detects robot is too close to wall
	#	Left = 1
	else:
		#Path clear
		Left = 0

	#Set twist messages according to Left values
	if Left == 2:
		state_description = 'Obstacle Detected_right'
		linear_x = 0.6
		angular_z = 0
	elif Left == 1:
		state_description = 'Too Close to Wall'
		#Turn straight, then run "move_right"
		#Needs proof of value
		#while orientation_x < 0:
		angular_z = -0.3
		#Below is causing bug (probably because of orientation)
		#move_left(data, pose_data)
	elif Left == 0:
		state_description = 'Clear'
		#while orientation_x < 0:
		angular_z = -0.3
		linear_x = 0
	
	#Publish Twist_msg
	rospy.loginfo(state_description)
    	msg.linear.x = linear_x
    	msg.angular.z = angular_z
    	pub.publish(msg)

def move_left(data, pose_data):
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	msg = Twist()
    	linear_x = 0
    	angular_z = 0
    	state_description = ''
	position_x = pose_data.pose.position.x
	orientation_x = pose_data.pose.orientation.x
	
	#Orient robot 90deg (in development)
	#while orientation_x < math.pi/2:
	#	angular_z = 0.3
	a = data.ranges[522:617]
	if min(a) <= R_value+clearence:
		Right = 2
	#elif position_x >= (wall_width_left/2)-clearence: 
		# lighthouse detects robot is too close to wall
	#	Right = 1
	else:
		Right = 0

	if Right == 2:
		state_description = 'Obstacle Detected_left'
		linear_x = 0.6
		angular_z = 0
	elif Right == 1:
		state_description = 'Too Close to Wall'
		#Turn straight, then run "move_right"
		#while orientation_x > 0:
		angular_z = 0.3
		move_right(data, pose_data)
	elif Right == 0:
		#while orientation_x > 0:
		state_description = 'Clear'
		angular_z = 0.3
	rospy.loginfo(state_description)
    	msg.linear.x = linear_x
    	msg.angular.z = angular_z
    	pub.publish(msg)

def move_straight():
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	msg = Twist()
    	linear_x = 0.6
    	angular_z = 0
    	state_description = 'Clear_straight'
	rospy.loginfo(state_description)
    	msg.linear.x = linear_x
    	msg.angular.z = angular_z
    	pub.publish(msg)

def callback(scan, pose_msg):
	position_x = pose_msg.pose.position.x
   	a = scan.ranges[48:95]
    	if min(a) <= R_value:
        	Left = 1
    	else:
        	Left = 0
    	b = scan.ranges[0:47]
    	if min(b) <= R_value:
        	Front_left = 1
    	else:
        	Front_left = 0
    	c = scan.ranges[713:760]
    	if min(c) <= R_value:
        	Front_right = 1
    	else:
        	Front_right = 0
    	d = scan.ranges[665:713]
    	if min(d) <= R_value:
        	Right = 1
    	else:
        	Right = 0


	if Left == 0 and Front_left == 0 and Front_right == 0 and Right == 0:
        	state_description = 'case 1 - clear'
       		move_straight()
        elif Left == 1 and Front_left == 0 and Front_right == 0 and Right == 0:
        	state_description = 'case 2 - far_left'
		move_right(scan, pose_msg)
    	elif Left == 0 and Front_left == 1 and Front_right == 0 and Right == 0:
        	state_description = 'case 3 - front_left'
        	move_right(scan, pose_msg)
        elif Left == 1 and Front_left == 1 and Front_right == 0 and Right == 0:
        	state_description = 'case 4 - left'
        	move_right(scan, pose_msg)
        elif Left == 0 and Front_left == 0 and Front_right == 0 and Right == 1:
        	state_description = 'case 5 - far_right'
        	move_left(scan, pose_msg)
    	elif Left == 0 and Front_left == 0 and Front_right == 1 and Right == 0:
        	state_description = 'case 6 - front_right'
        	move_left(scan, pose_msg)
        elif Left == 0 and Front_left == 0 and Front_right == 1 and Right == 1:
        	state_description = 'case 7 - right'
        	move_left(scan, pose_msg)
        elif Left == 0 and Front_left == 1 and Front_right == 1 and Right == 0:
        	state_description = 'case 8 - front'
        	move_right(scan, pose_msg)
        elif Left == 1 and Front_left == 0 and Front_right == 0 and Right == 1:
        	state_description = 'case 9 - far_left/far_right'
        	move_left(scan, pose_msg)
    	elif Left == 1 and Front_left == 0 and Front_right == 1 and Right == 0:
        	state_description = 'case 10 - far_left/front_right'
        	move_left(scan, pose_msg)
        elif Left == 0 and Front_left == 1 and Front_right == 0 and Right == 1:
        	state_description = 'case 11 - front_left/far_right'
        	move_left(scan, pose_msg)
        elif Left == 0 and Front_left == 1 and Front_right == 1 and Right == 1:
        	state_description = 'case 12 - front_left/right'
        	move_left(scan, pose_msg)
        elif Left == 1 and Front_left == 1 and Front_right == 1 and Right == 0:
        	state_description = 'case 13 - left/front_right'
        	move_right(scan, pose_msg)
        elif Left == 1 and Front_left == 0 and Front_right == 1 and Right == 1:
        	state_description = 'case 14 - far_left/right'
        	move_left(scan, pose_msg)
    	elif Left == 1 and Front_left == 1 and Front_right == 0 and Right == 1:
        	state_description = 'case 15 - left/far_right'
        	move_left(scan, pose_msg)
        elif Left == 1 and Front_left == 1 and Front_right == 1 and Right == 1:
        	state_description = 'case 16 - all_directions'
        	move_left(scan, pose_msg)
        else:
        	state_description = 'unknown case'
	rospy.loginfo(state_description)

rospy.init_node('check_obstacle')


laser_sub = message_filters.Subscriber('/scan', LaserScan)
pose_sub = message_filters.Subscriber('/pose_msg1', PoseStamped)

ts = message_filters.ApproximateTimeSynchronizer([laser_sub, pose_sub], queue_size=10, slop = 1)
ts.registerCallback(callback)

rospy.spin()
