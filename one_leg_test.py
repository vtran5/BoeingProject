import smbus
import time
import numpy as np

# Get I2C bus
bus = smbus.SMBus(1)

# Data input from user into command line
print ("Rest Position")
restA=3
##
t = np.arange(0,201,1)
#Go to rest position

#for i in range(0,201):	
#	time.sleep(0.02)
    
	
# Commands for Leg 1
dataA= [int(round(restA*200/4)), 0x00]
bus.write_i2c_block_data(0x56, 0x2F, dataA)
voltA=float(dataA[0])/51.0
# Print statements
print ("Leg 1 : %.2f V" %voltA)
time.sleep(30)

# Go to zero position

for i in range(0,201):	
	time.sleep(0.02)
    
	
# Commands for Leg 1
	dataA= [int(round(restA*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x2F, dataA)
	voltA=float(dataA[0])/51.0
# Print statements
	print ("Leg 1 : %.2f V" %voltA)
