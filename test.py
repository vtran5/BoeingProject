import smbus
import time
import numpy as np

# Get I2C bus
bus = smbus.SMBus(1)

# Data input from user into command line
print "Rest Position"
restA=3.79
restB=3.79
restC=3.79
restD=3.79
restE=3.79
restF=3.79
t = np.arange(0,201,1)
# Go to rest position

for i in range(0,201):	
	time.sleep(0.02)
    
	
# Commands for Leg 1
	dataA= [int(round(restA*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataA)
	voltA=float(dataA[0])/51.0

# Commands for Leg 2
	dataB = [int(round(restB*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataB)
	voltB=float(dataB[0])/51.0

# Commands for Leg 3
	dataC= [int(round(restC*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataC)
	voltC=float(dataC[0])/51.0

# Commands for Leg 4
	dataD = [int(round(restD*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataD)
	voltD=float(dataD[0])/51.0

# Commands for Leg 5
	dataE = [int(round(restE*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataE)
	voltE=float(dataE[0])/51.0

# Commands for Leg 6
	dataF= [int(round(restF*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataF)
	voltF=float(dataF[0])/51.0
	
	i+=1

# Print statements
	print "Leg 1 : %.2f V" %voltA
	print "Leg 2 : %.2f V" %voltB
	print "Leg 3 : %.2f V" %voltC
	print "Leg 4 : %.2f V" %voltD
	print "Leg 5 : %.2f V" %voltE
	print "Leg 6 : %.2f V" %voltF

time.sleep(15)

# Go to zero position

for i in range(0,201):	
	time.sleep(0.02)
    
	
# Commands for Leg 1
	dataA= [int(round(restA*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataA)
	voltA=float(dataA[0])/51.0

# Commands for Leg 2
	dataB = [int(round(restB*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataB)
	voltB=float(dataB[0])/51.0

# Commands for Leg 3
	dataC= [int(round(restC*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataC)
	voltC=float(dataC[0])/51.0

# Commands for Leg 4
	dataD = [int(round(restD*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataD)
	voltD=float(dataD[0])/51.0

# Commands for Leg 5
	dataE = [int(round(restE*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataE)
	voltE=float(dataE[0])/51.0

# Commands for Leg 6
	dataF= [int(round(restF*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataF)
	voltF=float(dataF[0])/51.0
	
	i+=1

# Print statements
	print "Leg 1 : %.2f V" %voltA
	print "Leg 2 : %.2f V" %voltB
	print "Leg 3 : %.2f V" %voltC
	print "Leg 4 : %.2f V" %voltD
	print "Leg 5 : %.2f V" %voltE
	print "Leg 6 : %.2f V" %voltF
