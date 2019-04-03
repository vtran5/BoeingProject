from struct import*
import socket
import time

UDP_IP ="192.168.1.3"
UDP_IP_PC ="192.168.1.7"
UDP_PORT = 11000
UDP_PORT_PC = 11001
position = [0,1,2,3,4,5]
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
#sock.bind((UDP_IP, UDP_PORT_PC))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock.bind((UDP_IP, UDP_PORT))


data = pack('%sd' % len(position), *position) #%s = len(position), in this case '6d'
#data = pack('d', 15)
sock.sendto(data, (UDP_IP_PC, UDP_PORT_PC))
