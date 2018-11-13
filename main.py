from boeing_lib import *

print("Please type the desired position: ")
x     =  float(input("x: "))
y     =  float(input("y: "))
z     =  float(input("z: "))
pitch =  float(input("pitch: "))
roll  =  float(input("roll: "))
yaw   =  float(input("yaw: "))
leg_length = []
leg_length = get_leg_length(pitch, roll, yaw,x,y,z)
print("received messages: ", leg_length)
