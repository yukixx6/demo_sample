#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from raspimouse_ros_2.msg import LightSensorValues

def callback_vel(date):
    vel = Twist()
    try:
	if date.sum_all >= 2000:
	    vel.linear.x = 0.0
	else:
	    vel.linear.x = 0.35
	rospy.loginfo(vel)
	pub.publish(vel)
    except:
	rospy.loginfo("can't watch LightSensorValue")

if __name__ == '__main__':
    rospy.init_node('vel_pub')
    sub = rospy.Subscriber('/lightsensors', LightSensorValues, callback_vel)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.spin()
