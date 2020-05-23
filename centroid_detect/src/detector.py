#!/usr/bin/env python
<<<<<<< HEAD
# coding=utf-8
=======
>>>>>>> 513c0938f85815884d01c90394148ed7bb15fdd9
import numpy as np
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

bridge = CvBridge()

<<<<<<< HEAD
def talker(cX, cY):
	pub = rospy.Publisher('coordtopic', String, queue_size = 10)
	
	rate = rospy.Rate(0.3)
	
	x_ = str(cX)
	y_ = str(cY)
	output_str = "Centroid Coordinates are: "+x_+" "+y_
	pub.publish(output_str)
	#rate.sleep()
	

def fun(ros_image):
	print '.'
	global bridge
	# Convert ROS image to cv2 image using bridge object
=======
def fun(ros_image):
	print 'Got an Image'
	global bridge
>>>>>>> 513c0938f85815884d01c90394148ed7bb15fdd9
	try:
		cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
	except CvBridgeError as e:
		print(e)
	# Detection code
	# Convert to grayscale image
	gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
#	hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
	gray_image = cv2.medianBlur(gray_image, 5)
	gray_image = cv2.medianBlur(gray_image, 7)
	gray_image = cv2.medianBlur(gray_image, 5)
	gray_image = cv2.medianBlur(gray_image, 3)
	gray_image = cv2.medianBlur(gray_image, 3)
	# Convert to Binary Image
	ret, thresh = cv2.threshold(gray_image,48, 255, cv2.THRESH_BINARY)
	# erosion dilation to remove white noise
	thresh = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations = 6)
	thresh = cv2.dilate(thresh, np.ones((3, 3), np.uint8), iterations = 6)
#	thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
#	lower = np.array([110, 95, 60])
#	higher = np.array([255, 255, 180])
#	mask = cv2.inRange(hsv, lower, higher)

	# Calculate moments of Binary Image
	M = cv2.moments(thresh)
	# Calculate X,Y coordinates of center
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	# Put circle at the centroid
	cv2.circle(cv_image, (cX, cY), 2, (255, 255, 255), -1)

	cv2.imshow("Centroid", cv_image)
<<<<<<< HEAD
	
	cv2.waitKey(1)
	talker(cX, cY)
	"""
	if cv2.waitKey(1) & 0xFF == ord('q'):
		#cv2.destroyAllWindows()
		return 0
	"""	

def main(args):
	rospy.init_node('centroid_detector', anonymous=True)
	image = rospy.Subscriber("/magnus/camera/image_raw", Image, fun) 
		
=======
	cv2.waitKey(0)



def main(args):
	rospy.init_node('centroid_detector', anonymous=True)
	image_sub = rospy.Subscriber("/magnus/camera/image_raw", Image, fun) 
>>>>>>> 513c0938f85815884d01c90394148ed7bb15fdd9
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting Down")
<<<<<<< HEAD
		cv2.destroyAllWindows()
=======
	cv2.destroyAllWindows()
>>>>>>> 513c0938f85815884d01c90394148ed7bb15fdd9

if __name__ == '__main__':
	main(sys.argv)


