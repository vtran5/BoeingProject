import smbus
import time
import numpy as np

# Get I2C bus
bus = smbus.SMBus(1)

# Data input from user into command line
print ("Rest Position")
restA=2.5
restB=2.5
restC=2.5
restD=2.5
restE=2.5
restF=2.5
print ("Round One - X")
decA=2.5
decB=2.5
decC=2.5
decD=2.5
decE=-0.5
decF=-0.5
print ("Round Two - Y")
decG=2.5
decH=2.5
decI=-0.5
decJ=-0.5
decK=2.5
decL=2.5
print ("Round Three - Z")
decM=2.5
decN=2.5
decO=2.5
decP=2.5
decQ=2.5
decR=2.5
t = np.arange(0,201,1)
##
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
	print ("Leg 1 : %.2f V" %voltA)
	print ("Leg 2 : %.2f V" %voltB)
	print ("Leg 3 : %.2f V" %voltC)
	print ("Leg 4 : %.2f V" %voltD)
	print ("Leg 5 : %.2f V" %voltE)
	print ("Leg 6 : %.2f V" %voltF)

time.sleep(2)

# X-Motion 
for i in range(0,201):	
	time.sleep(0.02)
  
	
# Commands for Leg 1
	dataA= [int(round((decA*t[i]+restA*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataA)
	voltA=float(dataA[0])/51.0

# Commands for Leg 2
	dataB = [int(round((decB*t[i]+restB*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataB)
	voltB=float(dataB[0])/51.0

# Commands for Leg 3
	dataC= [int(round((decC*t[i]+restC*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataC)
	voltC=float(dataC[0])/51.0

# Commands for Leg 4
	dataD = [int(round((decD*t[i]+restD*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataD)
	voltD=float(dataD[0])/51.0

# Commands for Leg 5
	dataE = [int(round((decE*t[i]+restE*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataE)
	voltE=float(dataE[0])/51.0

# Commands for Leg 6
	dataF= [int(round((decF*t[i]+restF*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataF)
	voltF=float(dataF[0])/51.0
	
	i+=1

# Print statements
	print ("Leg 1 : %.2f V" %voltA)
	print ("Leg 2 : %.2f V" %voltB)
	print ("Leg 3 : %.2f V" %voltC)
	print ("Leg 4 : %.2f V" %voltD)
	print ("Leg 5 : %.2f V" %voltE)
	print ("Leg 6 : %.2f V" %voltF)

time.sleep(0.5)

for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataA= [int(round((decA*t[200-i]+restA*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataA)
	voltA=float(dataA[0])/51.0

# Commands for Leg 2
	dataB = [int(round((decB*t[200-i]+restB*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataB)
	voltB=float(dataB[0])/51.0

# Commands for Leg 3
	dataC= [int(round((decC*t[200-i]+restC*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataC)
	voltC=float(dataC[0])/51.0

# Commands for Leg 4
	dataD = [int(round((decD*t[200-i]+restD*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataD)
	voltD=float(dataD[0])/51.0

# Commands for Leg 5
	dataE = [int(round((decE*t[200-i]+restE*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataE)
	voltE=float(dataE[0])/51.0

# Commands for Leg 6
	dataF= [int(round((decF*t[200-i]+restF*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataF)
	voltF=float(dataF[0])/51.0
	
	i+=1

# Print statements
	print ("Leg 1 : %.2f V" %voltA)
	print ("Leg 2 : %.2f V" %voltB)
	print ("Leg 3 : %.2f V" %voltC)
	print ("Leg 4 : %.2f V" %voltD)
	print ("Leg 5 : %.2f V" %voltE)
	print ("Leg 6 : %.2f V" %voltF)
time.sleep(0.5)
# Y-Motion

for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataG= [int(round((decG*t[i]+restA*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataG)
	voltA=float(dataG[0])/51.0

# Commands for Leg 2
	dataH = [int(round((decH*t[i]+restB*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataH)
	voltB=float(dataH[0])/51.0

# Commands for Leg 3
	dataI= [int(round((decI*t[i]+restC*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataI)
	voltC=float(dataI[0])/51.0

# Commands for Leg 4
	dataJ = [int(round((decJ*t[i]+restD*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataJ)
	voltD=float(dataJ[0])/51.0

# Commands for Leg 5
	dataK = [int(round((decK*t[i]+restE*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataK)
	voltE=float(dataK[0])/51.0

# Commands for Leg 6
	dataL= [int(round((decL*t[i]+restF*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataL)
	voltF=float(dataL[0])/51.0
	
	i+=1

# Print statements
	print ("Leg 1 : %.2f V" %voltA)
	print ("Leg 2 : %.2f V" %voltB)
	print ("Leg 3 : %.2f V" %voltC)
	print ("Leg 4 : %.2f V" %voltD)
	print ("Leg 5 : %.2f V" %voltE)
	print ("Leg 6 : %.2f V" %voltF)

time.sleep(0.5)

for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataG= [int(round((decG*t[200-i]+restA*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataG)
	voltA=float(dataG[0])/51.0

# Commands for Leg 2
	dataH = [int(round((decH*t[200-i]+restB*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataH)
	voltB=float(dataH[0])/51.0

# Commands for Leg 3
	dataI= [int(round((decI*t[200-i]+restC*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataI)
	voltC=float(dataI[0])/51.0

# Commands for Leg 4
	dataJ = [int(round((decJ*t[200-i]+restD*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataJ)
	voltD=float(dataJ[0])/51.0

# Commands for Leg 5
	dataK = [int(round((decK*t[200-i]+restE*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataK)
	voltE=float(dataK[0])/51.0

# Commands for Leg 6
	dataL= [int(round((decL*t[200-i]+restF*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataL)
	voltF=float(dataL[0])/51.0
	
	i+=1

# Print statements
	print ("Leg 1 : %.2f V" %voltA)
	print ("Leg 2 : %.2f V" %voltB)
	print ("Leg 3 : %.2f V" %voltC)
	print ("Leg 4 : %.2f V" %voltD)
	print ("Leg 5 : %.2f V" %voltE)
	print ("Leg 6 : %.2f V" %voltF)
time.sleep(0.5)

# Z-Motion

for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataM= [int(round((decM*t[i]+restA*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataM)
	voltA=float(dataM[0])/51.0

# Commands for Leg 2
	dataN = [int(round((decN*t[i]+restB*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataN)
	voltB=float(dataN[0])/51.0

# Commands for Leg 3
	dataO= [int(round((decO*t[i]+restC*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataO)
	voltC=float(dataO[0])/51.0

# Commands for Leg 4
	dataP = [int(round((decP*t[i]+restD*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataP)
	voltD=float(dataP[0])/51.0

# Commands for Leg 5
	dataQ = [int(round((decQ*t[i]+restE*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataQ)
	voltE=float(dataQ[0])/51.0

# Commands for Leg 6
	dataR= [int(round((decR*t[i]+restF*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataR)
	voltF=float(dataR[0])/51.0
	
	i+=1

# Print statements
	print ("Leg 1 : %.2f V" %voltA)
	print ("Leg 2 : %.2f V" %voltB)
	print ("Leg 3 : %.2f V" %voltC)
	print ("Leg 4 : %.2f V" %voltD)
	print ("Leg 5 : %.2f V" %voltE)
	print ("Leg 6 : %.2f V" %voltF)

time.sleep(0.5)

for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataM= [int(round((decM*t[200-i]+restA*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataM)
	voltA=float(dataM[0])/51.0

# Commands for Leg 2
	dataN = [int(round((decN*t[200-i]+restB*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataN)
	voltB=float(dataN[0])/51.0

# Commands for Leg 3
	dataO= [int(round((decO*t[200-i]+restC*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataO)
	voltC=float(dataO[0])/51.0

# Commands for Leg 4
	dataP = [int(round((decP*t[200-i]+restD*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataP)
	voltD=float(dataP[0])/51.0

# Commands for Leg 5
	dataQ = [int(round((decQ*t[200-i]+restE*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataQ)
	voltE=float(dataQ[0])/51.0

# Commands for Leg 6
	dataR= [int(round((decR*t[200-i]+restF*200)/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataR)
	voltF=float(dataR[0])/51.0
	
	i+=1

# Print statements
	print ("Leg 1 : %.2f V" %voltA)
	print ("Leg 2 : %.2f V" %voltB)
	print ("Leg 3 : %.2f V" %voltC)
	print ("Leg 4 : %.2f V" %voltD)
	print ("Leg 5 : %.2f V" %voltE)
	print ("Leg 6 : %.2f V" %voltF)

#execfile("FinalDemo2.py") # automatically executes the second half of the flight profile, the roll, pitch, and yaw demonstration
time.sleep(2)
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
	print ("Leg 1 : %.2f V" %voltA)
	print ("Leg 2 : %.2f V" %voltB)
	print ("Leg 3 : %.2f V" %voltC)
	print ("Leg 4 : %.2f V" %voltD)
	print ("Leg 5 : %.2f V" %voltE)
	print ("Leg 6 : %.2f V" %voltF)
