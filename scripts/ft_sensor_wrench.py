#!/usr/bin/env python

"""
This node subscribes to wrench data from Rokubi FT sensor and publishes the calibrated wrench 
"""

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import WrenchStamped


class ftSensorNode():
    def __init__(self):
        self.initial_wrench = 0
        self.counter = 0
        self.pub = rospy.Publisher('calibrated_wrench', WrenchStamped, queue_size = 10)
        self.sub = rospy.Subscriber('/bus0/ft_sensor0/ft_sensor_readings/wrench', WrenchStamped, self.wrench_callback)


    def wrench_callback(self, msg):
        #print(msg.wrench.force.x)
        rospy.loginfo(msg)

        if self.counter < 100:
            self.initial_wrench = msg
            self.counter+=1
        else:
            cal_msg = self.calibrate_wrench(msg)
            self.pub.publish(cal_msg)

    def calibrate_wrench(self, msg):
        cal_msg = WrenchStamped()
        cal_msg.header = msg.header
        cal_msg.wrench.force.x = msg.wrench.force.x - self.initial_wrench.wrench.force.x
        cal_msg.wrench.force.y = msg.wrench.force.y - self.initial_wrench.wrench.force.y
        cal_msg.wrench.force.z = msg.wrench.force.z - self.initial_wrench.wrench.force.z
        cal_msg.wrench.torque.x = msg.wrench.torque.x - self.initial_wrench.wrench.torque.x
        cal_msg.wrench.torque.y = msg.wrench.torque.y - self.initial_wrench.wrench.torque.y
        cal_msg.wrench.torque.z = msg.wrench.torque.z - self.initial_wrench.wrench.torque.z
    
        return cal_msg


if __name__ == '__main__':
    try:
        rospy.init_node('ft_sensor_wrench', anonymous = True)
        ftSensorNode()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass

