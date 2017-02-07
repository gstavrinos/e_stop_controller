#!/usr/bin/env python
import rospy
import tf
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist

pitch_threshold = 0
twist_publisher = None

def imu_callback(msg):
    global pitch_threshold, twist_publisher, cnt
    (roll, pitch, yaw) = tf.transformations.euler_from_quaternion([msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w])
    if pitch < -abs(pitch_threshold) or pitch > abs(pitch_threshold):
        twist = Twist()
	if pitch < -abs(pitch_threshold) - 0.05:
            twist.linear.x = -0.15
            print 'GO BACK!'
        elif pitch > abs(pitch_threshold) + 0.05:
            twist.linear.x = 0.15
        twist_publisher.publish(twist)

def init():
    global pitch_threshold, twist_publisher
    rospy.init_node('safety_controller')
    imu_topic = rospy.get_param('~imu_topic','/imu/data')
    pitch_threshold = rospy.get_param('~pitch_threshold', -0.7)
    twist_topic = rospy.get_param('~twist_topic','/safety_controller/cmd_vel')
    rospy.Subscriber(imu_topic, Imu, imu_callback)
    twist_publisher = rospy.Publisher(twist_topic, Twist, queue_size=10);
    rospy.spin()



if __name__ == '__main__':
    init()
