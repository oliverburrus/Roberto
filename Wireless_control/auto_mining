import rospy
from std_msgs import Float64
from std_srvs import SetBool

#Step 1: Raise augur
def raise_augur_client(x, y):
    rospy.wait_for_service('actuator_extend')
    try:
        actuator_extend = rospy.ServiceProxy('actuator_extend', SetBool)
        resp1 = actuator_extend("True")
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
        
        
qq
