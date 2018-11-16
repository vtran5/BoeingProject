import smbus
import time
import numpy as np

# Get I2C bus
bus = smbus.SMBus(1)

# Data input from user into command line
print ("Rest Position")
rest=3
##
t = np.arange(0,201,4)
#Go to rest position

#for i in range(0,201):	
#	time.sleep(0.02)
    
	
# Commands for Leg 1
for i in range(0,51):	
        time.sleep(0.05)
        # Commands for Leg 1
        dataA= [int(round(rest*t[i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x2F, dataA)
        voltA=float(dataA[0])/51.0
        # Print statements
        print ("Leg 1 : %.2f V" %voltA)
time.sleep(5)

# Go to zero position

for i in range(0,51):	
	time.sleep(0.05)
    
	
# Commands for Leg 1
	dataD= [int(round(rest*t[50-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x2F, dataD)
	voltD=float(dataD[0])/51.0
# Print statements
	print ("Leg 1 : %.2f V" %voltD)
