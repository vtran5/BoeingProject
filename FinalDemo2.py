
import smbus
import time
import numpy as np

# Get I2C bus
bus = smbus.SMBus(1)

# AD5669 address, 0x56(86)
# Select DAC and input register, 0x2F(47)
#		0x8000(32768)	Selected all DAC channels

# Data input from user into command line
print "Round One"
decA=5
decB=4
decC=1
decD=1
decE=4
decF=5
print "Round Two"
decG=3.5
decH=5
decI=5
decJ=3.5
decK=1
decL=1
print "Round Three"
decM=2
decN=2.75
decO=2
decP=2.75
decQ=2
decR=2.75

t = np.arange(0,201,1)
for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataA= [int(round(decA*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataA)
	voltA=float(dataA[0])/51.0

# Commands for Leg 2
	dataB = [int(round(decB*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataB)
	voltB=float(dataB[0])/51.0

# Commands for Leg 3
	dataC= [int(round(decC*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataC)
	voltC=float(dataC[0])/51.0

# Commands for Leg 4
	dataD = [int(round(decD*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataD)
	voltD=float(dataD[0])/51.0

# Commands for Leg 5
	dataE = [int(round(decE*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataE)
	voltE=float(dataE[0])/51.0

# Commands for Leg 6
	dataF= [int(round(decF*t[i]/4)), 0x00]
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

time.sleep(0.5)

for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataA= [int(round(decA*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataA)
	voltA=float(dataA[0])/51.0

# Commands for Leg 2
	dataB = [int(round(decB*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataB)
	voltB=float(dataB[0])/51.0

# Commands for Leg 3
	dataC= [int(round(decC*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataC)
	voltC=float(dataC[0])/51.0

# Commands for Leg 4
	dataD = [int(round(decD*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataD)
	voltD=float(dataD[0])/51.0

# Commands for Leg 5
	dataE = [int(round(decE*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataE)
	voltE=float(dataE[0])/51.0

# Commands for Leg 6
	dataF= [int(round(decF*t[200-i]/4)), 0x00]
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

for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataG= [int(round(decG*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataG)
	voltA=float(dataG[0])/51.0

# Commands for Leg 2
	dataH = [int(round(decH*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataH)
	voltB=float(dataH[0])/51.0

# Commands for Leg 3
	dataI= [int(round(decI*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataI)
	voltC=float(dataI[0])/51.0

# Commands for Leg 4
	dataJ = [int(round(decJ*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataJ)
	voltD=float(dataJ[0])/51.0

# Commands for Leg 5
	dataK = [int(round(decK*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataK)
	voltE=float(dataK[0])/51.0

# Commands for Leg 6
	dataL= [int(round(decL*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataL)
	voltF=float(dataL[0])/51.0
	
	i+=1

# Print statements
	print "Leg 1 : %.2f V" %voltA
	print "Leg 2 : %.2f V" %voltB
	print "Leg 3 : %.2f V" %voltC
	print "Leg 4 : %.2f V" %voltD
	print "Leg 5 : %.2f V" %voltE
	print "Leg 6 : %.2f V" %voltF

time.sleep(0.5)

for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataG= [int(round(decG*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataG)
	voltA=float(dataG[0])/51.0

# Commands for Leg 2
	dataH = [int(round(decH*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataH)
	voltB=float(dataH[0])/51.0

# Commands for Leg 3
	dataI= [int(round(decI*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataI)
	voltC=float(dataI[0])/51.0

# Commands for Leg 4
	dataJ = [int(round(decJ*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataJ)
	voltD=float(dataJ[0])/51.0

# Commands for Leg 5
	dataK = [int(round(decK*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataK)
	voltE=float(dataK[0])/51.0

# Commands for Leg 6
	dataL= [int(round(decL*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataL)
	voltF=float(dataL[0])/51.0
	
	i+=1

# Print statements
	print "Leg 1 : %.2f V" %voltA
	print "Leg 2 : %.2f V" %voltB
	print "Leg 3 : %.2f V" %voltC
	print "Leg 4 : %.2f V" %voltD
	print "Leg 5 : %.2f V" %voltE
	print "Leg 6 : %.2f V" %voltF

for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataM= [int(round(decM*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataM)
	voltA=float(dataM[0])/51.0

# Commands for Leg 2
	dataN = [int(round(decN*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataN)
	voltB=float(dataN[0])/51.0

# Commands for Leg 3
	dataO= [int(round(decO*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataO)
	voltC=float(dataO[0])/51.0

# Commands for Leg 4
	dataP = [int(round(decP*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataP)
	voltD=float(dataP[0])/51.0

# Commands for Leg 5
	dataQ = [int(round(decQ*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataQ)
	voltE=float(dataQ[0])/51.0

# Commands for Leg 6
	dataR= [int(round(decR*t[i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataR)
	voltF=float(dataR[0])/51.0
	
	i+=1

# Print statements
	print "Leg 1 : %.2f V" %voltA
	print "Leg 2 : %.2f V" %voltB
	print "Leg 3 : %.2f V" %voltC
	print "Leg 4 : %.2f V" %voltD
	print "Leg 5 : %.2f V" %voltE
	print "Leg 6 : %.2f V" %voltF

time.sleep(0.5)

for i in range(0,201):	
	time.sleep(0.02)
	
# Commands for Leg 1
	dataM= [int(round(decM*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x20, dataM)
	voltA=float(dataM[0])/51.0

# Commands for Leg 2
	dataN = [int(round(decN*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x21, dataN)
	voltB=float(dataN[0])/51.0

# Commands for Leg 3
	dataO= [int(round(decO*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x22, dataO)
	voltC=float(dataO[0])/51.0

# Commands for Leg 4
	dataP = [int(round(decP*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x23, dataP)
	voltD=float(dataP[0])/51.0

# Commands for Leg 5
	dataQ = [int(round(decQ*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x24, dataQ)
	voltE=float(dataQ[0])/51.0

# Commands for Leg 6
	dataR= [int(round(decR*t[200-i]/4)), 0x00]
	bus.write_i2c_block_data(0x56, 0x25, dataR)
	voltF=float(dataR[0])/51.0
	
	i+=1

# Print statements
	print "Leg 1 : %.2f V" %voltA
	print "Leg 2 : %.2f V" %voltB
	print "Leg 3 : %.2f V" %voltC
	print "Leg 4 : %.2f V" %voltD
	print "Leg 5 : %.2f V" %voltE
	print "Leg 6 : %.2f V" %voltF
