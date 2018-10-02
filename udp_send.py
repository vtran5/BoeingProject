from struct import*
import socket
import time

UDP_IP =""
UDP_TP_PC ="192.168.10.1"
UDP_PORT = 25000
UDP_PORT_PC = 25001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock.bind((UDP_IP, UDP_PORT_PC))

sock_PC = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock_PC.bind((UDP_IP, UDP_PORT_PC))

data,addr = sock .recvfrom(10)
TestData = unpack('h',data)
ReceivedTest = TestData[0] & 0x0003

for x in range (0,500):
    data, addr = sock.recvfrom(10)
    TestData = unpack('h',data)
    SendData=pack('h',TestData[0])
    sent = sock_PC.sendto(SentData, (UDP_IP_PC, UDP_PORT_PC))
