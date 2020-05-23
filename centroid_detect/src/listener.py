#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def coordtopic_callback(coord_info):
	rospy.loginfo(rospy.get_caller_id()+"%s", coord_info.data)

def listener():
	rospy.init_node('listener', anonymous = True)
	rospy.Subscriber('coordtopic', String, coordtopic_callback)
	
	rospy.spin()
	
if __name__ == '__main__':
	listener()
