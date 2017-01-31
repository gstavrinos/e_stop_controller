#!/usr/bin/env python
import rospy
import tf
from sensor_msgs.msg import Imu

pitch_threshold = 0

def imu_callback(msg):
    global pitch_threshold
    #print msg
    (roll, pitch, yaw) = tf.transformations.euler_from_quaternion([msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w])
    if pitch < pitch_threshold and abs(pitch_threshold-pitch) >= 0.01:
        print 'D A N G E R ! ! !'
    else:
        print 'SAFE :)'
    #print 'PITCH = ' + str(pitch)

def init():
    global pitch_threshold
    rospy.init_node('assisted_teleoperation')
    imu_topic = rospy.get_param('~imu_topic','/imu/data')
    pitch_threshold = rospy.get_param('~pitch_threshold', -1.16)
    rospy.Subscriber(imu_topic, Imu, imu_callback)
    while not rospy.is_shutdown():
        x = 1



if __name__ == '__main__':
    init()