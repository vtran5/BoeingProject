import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
#while True:
    #print(1)
    #read_serial=ser.readline()
time.sleep(2)
while True:
    x1 = str(ser.readline(), 'utf-8')
    print(x1)
    #print("done1\n")
    if x1 == "done\n":
        #print('break')
        break
    
yaw = float(ser.readline())
pitch = float(ser.readline())
roll = float(ser.readline())
orientation = [yaw, pitch, roll]
#x = float (ser.readline())
#y = float (ser.readline())
#z = float (ser.readline())
#print ("roll: %.2f, pitch: %.2f, yaw: %.2f" %(x, y, z))
print(orientation)
