#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from subprocess import call

frame = Tk()
frame.title("REMOTE")
frame.geometry("400x250")

rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)

def fw():
	print("fw")
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def bw():
	print("bw")
	cmd = Twist()
	cmd.linear.x = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def sl():
	print("sl")
	cmd = Twist()
	cmd.linear.y = 1.0
	cmd.angular.z= 0.0
	pub.publish(cmd)
	
def sr():
	print("sr")
	cmd = Twist()
	cmd.linear.y = -1.0
	cmd.angular.z= 0.0
	pub.publish(cmd)

def rtl(event):
	print("rtl")
	cmd = Twist()
	cmd.linear.x = 0.0
	cmd.angular.z= 1.0
	pub.publish(cmd)
	
def rtr(event):
	print("rtr")
	cmd = Twist()
	cmd.linear.x = 0.0
	cmd.angular.z= -1.0
	pub.publish(cmd)

def rest(event):
	print("reset")
	call(["rosservice", "call", "/reset"])

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=60)
	
B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=170)
	
B3 = Button(text = "SL", command=sl)
B3.place(x=20, y=120)
	
B4 = Button(text = "SR", command=sr)
B4.place(x=128, y=120)

# Create a Canvas for B5
canvas_b5 = Canvas(frame, width=40, height=40)
canvas_b5.place(x=236, y=150)
canvas_b5.create_oval(0, 0, 40, 40,fill="#C0C0C0")
canvas_b5.create_text(20, 20, text="RTL", fill="black")
canvas_b5.bind("<Button-1>", rtl)

# Create a Canvas for B6
canvas_b6 = Canvas(frame, width=40, height=40)
canvas_b6.place(x=300, y=80)
canvas_b6.create_oval(0, 0, 40, 40,fill="#C0C0C0")
canvas_b6.create_text(20, 20, text="RTR", fill="black")
canvas_b6.bind("<Button-1>", rtr)

canvas_b7 = Canvas(frame, width=60, height=40)
canvas_b7.place(x=170, y=10)
canvas_b7.create_oval(0, 0, 60, 40,fill="#C0C0C0")
canvas_b7.create_text(30, 20, text="Reset", fill="black")
canvas_b7.bind("<Button-1>", rest)
	
frame.mainloop()
