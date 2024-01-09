#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def run(val):
   if val.data == "Hello World":
      rospy.loginfo("node2: "+"Hello World Too!!")
   else:
      rospy.loginfo("node2: "+str(val.data))

if __name__ == "__main__":
   sub = rospy.Subscriber("chatter",String,callback=run)
   rospy.init_node("Listener")
   rospy.spin()

