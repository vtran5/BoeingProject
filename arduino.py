import serial
import time

ser = serial.Serial('/dev/ttyACM1',9600)
#while True:
    #print(1)
    #read_serial=ser.readline()
time.sleep(2)
while True:
    print('try')
    try:
        while True:
            print('read')
            x1 = str(ser.readline(), 'utf-8')
            print(x1)
            if x1 == "done\n":
                break
            
        yaw = float(ser.readline())
        pitch = float(ser.readline())
        roll = float(ser.readline())
        orientation = [yaw, pitch, roll]
    except ValueError:
        continue
    break
print(orientation)
