import socket
import time
from struct import*

UDP_IP = "192.168.1.3"
UDP_PORT = 11000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    TestData = unpack('h',data)
    print ("received message:", data)
