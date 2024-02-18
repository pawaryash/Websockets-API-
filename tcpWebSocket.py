#TCP client program to connect to the server 

import socket
import sys

try: 
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create socket")
    print("Reason"+str(err))
    sys.exit()

print("socket created")

target_host = input("Enter the target_host name to connect: ")
target_port = input("ENter the target port: ")

try:
    sock.connect((target_host, int(target_port)))
    print("Socket connected to: "+target_host + ":" +str(target_port))
    sock.shutdown(2)
except socket.error as err:
    print("Failed to connect to socket.")
    print("reason"+str(err))
    sys.exit()
