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
    #print "PITCH = " + str(pitch)
    if pitch < pitch_threshold and abs(pitch_threshold-pitch) >= 0.01:
        #print 'D A N G E R ! ! !'
        twist_publisher.publish(Twist())
    '''
    else:
        print 'SAFE :)'
    '''

def init():
    global pitch_threshold, twist_publisher
    rospy.init_node('e_stop_controller')
    imu_topic = rospy.get_param('~imu_topic','/imu/data')
    pitch_threshold = rospy.get_param('~pitch_threshold', -0.7)
    twist_topic = rospy.get_param('~twist_topic','/e_stop')
    rospy.Subscriber(imu_topic, Imu, imu_callback)
    pitch_threshold = -0.7
    twist_publisher = rospy.Publisher(twist_topic, Twist, queue_size=10);
    rospy.spin()



if __name__ == '__main__':
    init()
