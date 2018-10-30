import socket
import time
from struct import*

UDP_IP_PC = "192.168.1.2"
UDP_PORT_send = 11001

UDP_IP = "192.168.1.4"
UDP_PORT_receive = 11000
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
#sock2 = socket.socket(socket.AF_INET, # Internet
                     #socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT_receive))
#sock.bind((UDP_IP, UDP_PORT))

while True:
    position = [10, 11, 12, 13, 14, 15]
    data = pack('%sd' % len(position), *position)
    #data = pack('d', 15)
    sock.sendto(data, (UDP_IP_PC, UDP_PORT_send))
    #data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #TestData = unpack('!6d',data)
    #print ("received message:", TestData[0])
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    TestData = unpack('6d',data) # 6d stands for 6 doubles (8 bytes float),
                                 # use !6d if data is bid endian
    leg_length = []
    leg_length = TestData
    print ("received message:", leg_length)
