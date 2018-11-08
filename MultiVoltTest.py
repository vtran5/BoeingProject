
import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# AD5669 address, 0x56(86)
# Select DAC and input register, 0x2F(47)
#		0x8000(32768)	Selected all DAC channels

# Data input from user into command line
decA=int(raw_input("Leg Voltage 1: "))
decB=int(raw_input("Leg Voltage 2: "))
decC=int(raw_input("Leg Voltage 3: "))
decD=int(raw_input("Leg Voltage 4: "))
decE=int(raw_input("Leg Voltage 5: "))
decF=int(raw_input("Leg Voltage 6: "))

# Conversion from integer input into hex
hexA=hex(decA*51)
hexB=hex(decB*51)
hexC=hex(decC*51)
hexD=hex(decD*51)
hexE=hex(decE*51)
hexF=hex(decF*51)

# Commands for Leg 1
dataA= [int(hexA,16), 0x00]
bus.write_i2c_block_data(0x56, 0x20, dataA)
voltA=dataA[0]/51

# Commands for Leg 2
dataB = [int(hexB,16), 0x00]
bus.write_i2c_block_data(0x56, 0x21, dataB)
voltB=dataB[0]/51

# Commands for Leg 3
dataC= [int(hexC,16), 0x00]
bus.write_i2c_block_data(0x56, 0x22, dataC)
voltC=dataC[0]/51

# Commands for Leg 4
dataD = [int(hexD,16), 0x00]
bus.write_i2c_block_data(0x56, 0x23, dataD)
voltD=dataD[0]/51

# Commands for Leg 5
dataE = [int(hexE,16), 0x00]
bus.write_i2c_block_data(0x56, 0x24, dataE)
voltE=dataE[0]/51

# Commands for Leg 6
dataF= [int(hexF,16), 0x00]
bus.write_i2c_block_data(0x56, 0x25, dataF)
voltF=dataF[0]/51

# Print statements
print "Leg 1 : %.2f V" %voltA
print "Leg 2 : %.2f V" %voltB
print "Leg 3 : %.2f V" %voltC
print "Leg 4 : %.2f V" %voltD
print "Leg 5 : %.2f V" %voltE
print "Leg 6 : %.2f V" %voltF

time.sleep(0.5)
