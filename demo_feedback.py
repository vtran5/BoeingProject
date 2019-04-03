import smbus
import time
import numpy as np
from boeing_lib import *

# Get I2C bus
bus = smbus.SMBus(1)

# Data input from user into command line
print ("Welcome to Boeing Flight Simulator project")
#rest = 2.5
dec = [0]*6
str = "yes"
leg_length = []
zero_orientation = []
orientation = []
positions = read_file('Book1.xls')
# Go to rest position
turn_on()
zero_orientation = get_IMU()
start= rest
print("The platform is now at rest position")
while str == "yes":
        print ("Input desired position:")
        try:
                x = float(input("X: "))
                y = float(input("Y: "))
                z = float(input("Z: "))
                pitch = float(input("pitch: "))
                roll = float(input("roll: "))
                yaw = float(input("yaw: "))
        except ValueError:
                print ("You need to input a number")
        else:
                leg_length = get_leg_length(yaw,roll,pitch,x,y,z)
                print("The computed leg lengths are:")
                print(leg_length)
                volt = [i*0.56 for i in leg_length]
                #dec = [i*0.56 - rest for i in leg_length]
                print("The computed voltages are:")
                print("%.2f V, %.2f V, %.2f V, %.2f V, %.2f V, %.2f V" % (volt[0],volt[1], volt[2], volt[3],volt[4],volt[5]) )
                try:
                        for i in volt:
                                if i>5 or i<0:
                                        raise VoltageOutOfRange
                except VoltageOutOfRange:
                        print("This position is out of range of the platform (the voltages need to be between 0V and 10V), try again!")
                else:
                        ##
                        t = np.arange(0,201,4)
                        # Go to rest position
                        #turn_on();
                        #print("The platform is now at rest position")
                        
                        time.sleep(1)
                        # Go to "dec" position
                        to_position(volt,start)
                        print("The platform is now at the desired position")
                        start = volt
                        #Get IMU values
                        orientation = get_IMU()
                        orientation = [orientation[i] - zero_orientation[i] for i in [0,1,2]]
                        print("The orientation is: ")
                        print("%.2f %.2f %.2f" % (orientation[0], orientation[1], orientation[2]))
                        time.sleep(2)
                        str = input("Do you want to continue (yes/no): ")
# Go back to rest position from "dec" position
to_position(rest,volt)
print("The platform is now at rest position")
time.sleep(2)
# Go to zero position
turn_off()
print("Now you can turn off the platform")
