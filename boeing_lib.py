import socket
import time
from struct import*
import numpy as np
import smbus
import serial
t = np.arange(0,201,4)
bus = smbus.SMBus(1)
rest = 2.5
#ser = serial.Serial('/dev/ttyACM1',9600)
def get_leg_length(yaw,roll,pitch,x,y,z):
    "This take the orientation as input, send them to simulink and get the leg lengths back"
    position = [yaw, roll, pitch, x, y,z]
    UDP_IP_PC = "192.168.1.4"
    UDP_PORT_send = 11001

    UDP_IP = "192.168.1.3"
    UDP_PORT_receive = 11000
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT_receive))
    data = pack('%sd' % len(position), *position)
    #data = pack('d', 15)
    sock.sendto(data, (UDP_IP_PC, UDP_PORT_send))
    time.sleep(0.1)
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    TestData = unpack('6d',data) # 6d stands for 6 doubles (8 bytes float),
                                 # use !6d if data is bid endian
    #leg_length = []
    #leg_length = TestData
    return TestData;
    
def turn_off():
    for i in range(0,51):	
        time.sleep(0.05)
        # Commands for Leg 1
        dataA= [int(round(rest*t[50-i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x20, dataA)
        voltA=float(dataA[0])/51.0

        # Commands for Leg 2
        dataB = [int(round(rest*t[50-i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x21, dataB)
        voltB=float(dataB[0])/51.0

        # Commands for Leg 3
        dataC= [int(round(rest*t[50-i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x22, dataC)
        voltC=float(dataC[0])/51.0

        # Commands for Leg 4
        dataD = [int(round(rest*t[50-i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x23, dataD)
        voltD=float(dataD[0])/51.0

        # Commands for Leg 5
        dataE = [int(round(rest*t[50-i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x24, dataE)
        voltE=float(dataE[0])/51.0

        # Commands for Leg 6
        dataF= [int(round(rest*t[50-i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x25, dataF)
        voltF=float(dataF[0])/51.0

        i+=1

        # Print statements
        #print ("V1 = %.2f V, V2 = %.2f V, V3 = %.2f V, V4 = %.2f V, V5 = %.2f V, V6 = %.2f V" %(voltA,voltB,voltC,voltD,voltE,voltF))
    return;

def turn_on(): 
    for i in range(0,51):	
        time.sleep(0.05)


        # Commands for Leg 1
        dataA= [int(round(rest*t[i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x20, dataA)
        voltA=float(dataA[0])/51.0

        # Commands for Leg 2
        dataB = [int(round(rest*t[i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x21, dataB)
        voltB=float(dataB[0])/51.0

        # Commands for Leg 3
        dataC= [int(round(rest*t[i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x22, dataC)
        voltC=float(dataC[0])/51.0

        # Commands for Leg 4
        dataD = [int(round(rest*t[i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x23, dataD)
        voltD=float(dataD[0])/51.0

        # Commands for Leg 5
        dataE = [int(round(rest*t[i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x24, dataE)
        voltE=float(dataE[0])/51.0

        # Commands for Leg 6
        dataF= [int(round(rest*t[i]/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x25, dataF)
        voltF=float(dataF[0])/51.0

        i+=1

        # Print statements
        #print ("V1 = %.2f V, V2 = %.2f V, V3 = %.2f V, V4 = %.2f V, V5 = %.2f V, V6 = %.2f V" %(voltA,voltB,voltC,voltD,voltE,voltF))
    return;

def kill_platform():
    time.sleep(0.5)
    data = [0x00, 0x00]
    bus.write_i2c_block_data(0x56, 0x2F, data)
    return;

def to_position(dec):
    for i in range(0,51):	
        time.sleep(0.05)	
        # Commands for Leg 1
        dataA= [int(round((dec[0]*t[i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x20, dataA)
        voltA=float(dataA[0])/51.0

        # Commands for Leg 2
        dataB = [int(round((dec[1]*t[i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x21, dataB)
        voltB=float(dataB[0])/51.0

        # Commands for Leg 3
        dataC= [int(round((dec[2]*t[i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x22, dataC)
        voltC=float(dataC[0])/51.0

        # Commands for Leg 4
        dataD = [int(round((dec[3]*t[i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x23, dataD)
        voltD=float(dataD[0])/51.0

        # Commands for Leg 5
        dataE = [int(round((dec[4]*t[i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x24, dataE)
        voltE=float(dataE[0])/51.0

        # Commands for Leg 6
        dataF= [int(round((dec[5]*t[i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x25, dataF)
        voltF=float(dataF[0])/51.0

        i+=1
        # Print statements
        #print ("V1 = %.2f V, V2 = %.2f V, V3 = %.2f V, V4 = %.2f V, V5 = %.2f V, V6 = %.2f V" %(voltA,voltB,voltC,voltD,voltE,voltF))
    return;

def to_rest(dec):
    for i in range(0,51):	
        time.sleep(0.05)

        # Commands for Leg 1
        dataA= [int(round((dec[0]*t[50-i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x20, dataA)
        voltA=float(dataA[0])/51.0

        # Commands for Leg 2
        dataB = [int(round((dec[1]*t[50-i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x21, dataB)
        voltB=float(dataB[0])/51.0

        # Commands for Leg 3
        dataC= [int(round((dec[2]*t[50-i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x22, dataC)
        voltC=float(dataC[0])/51.0

        # Commands for Leg 4
        dataD = [int(round((dec[3]*t[50-i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x23, dataD)
        voltD=float(dataD[0])/51.0

        # Commands for Leg 5
        dataE = [int(round((dec[4]*t[50-i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x24, dataE)
        voltE=float(dataE[0])/51.0

        # Commands for Leg 6
        dataF= [int(round((dec[5]*t[50-i]+rest*200)/4)), 0x00]
        bus.write_i2c_block_data(0x56, 0x25, dataF)
        voltF=float(dataF[0])/51.0

        i+=1
        # Print statements
        #print ("V1 = %.2f V, V2 = %.2f V, V3 = %.2f V, V4 = %.2f V, V5 = %.2f V, V6 = %.2f V" %(voltA,voltB,voltC,voltD,voltE,voltF))
    return;

class Error(Exception):
    """Base class for other exceptions"""
    pass

class VoltageOutOfRange(Error):
    """When the voltages are greater than 10V"""
    pass

def get_IMU():
    while true:
        x1 = ser.readline()
        if x1 == done:
            break
        
    yaw = ser.readline()
    pitch = ser.readline()
    roll = ser.readline()
    orientation = [yaw, pitch, roll]
    return orientation;
        
    
