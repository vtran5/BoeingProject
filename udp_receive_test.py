import socket
import time
from struct import*

UDP_IP = "192.168.1.4"
UDP_PORT = 11000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    TestData = unpack('6d',data) # 6d stands for 6 doubles (8 bytes float),
                                 # use !6d if data is bid endian
    leg_length = []
    leg_length = TestData
    print ("received message:", leg_length)
    #print (TestData)
    
