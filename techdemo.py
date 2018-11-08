import smbus
import time
import numpy as np
from boeing_lib import *

# Get I2C bus
bus = smbus.SMBus(1)

# Data input from user into command line
print ("Rest Position")
#rest = 2.5
dec = [0]*6
str = "yes"
while str == "yes":
        print ("Input leg lengths for desired position")
        dec[0] = float(input ("Leg length 1: "))*.56 - 2.5
        dec[1] = float(input ("Leg length 2: "))*.56 - 2.5
        dec[2] = float(input ("Leg length 3: "))*.56 - 2.5
        dec[3] = float(input ("Leg length 4: "))*.56 - 2.5
        dec[4] = float(input ("Leg length 5: "))*.56 - 2.5
        dec[5] = float(input ("Leg length 6: "))*.56 - 2.5
        ##
        t = np.arange(0,201,4)
        # Go to rest position
        turn_on();
        time.sleep(3)
        # Go to "dec" position
        to_position(dec)
        time.sleep(3)
        # Go back to rest position from "dec" position
        to_rest(dec)
        time.sleep(0.5)
        str = input("Do you want to continue (yes/no): ")

# Go to zero position
turn_off()
