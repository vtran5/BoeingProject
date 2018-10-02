import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
while True:
    #read_serial=ser.readline()
    x = float (ser.readline())
    y = float (ser.readline())
    z = float (ser.readline())
    print "roll: %.2f" %x
    print "pitch: %.2f" %y
    print "yaw: %.2f" %z
    #print read_serial
    #time.sleep(0.01)
