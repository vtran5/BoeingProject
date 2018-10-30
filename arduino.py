import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
while True:
    #read_serial=ser.readline()
    x = float (ser.readline())
    y = float (ser.readline())
    z = float (ser.readline())
    print ("roll: %.2f, pitch: %.2f, yaw: %.2f" %(x, y, z))

