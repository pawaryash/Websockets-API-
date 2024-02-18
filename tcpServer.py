import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
server_socket.bind(('192.168.1.9',12345)) #port no. should be in this range: 1 to 65535
server_socket.listen(5) #if the server is busy upto 5 connections are kept waiting. If a 6th connection tries to connect then it is refused.

while True:
    print("Server is waiting for connection")
    client_socket,addr=server_socket.accept() #connect to a client
    print("client conected from: ",addr)

    while True:
        data = client_socket.recv(1024)
        if not data or data.decode('utf-8')=='END':
            break
        print("Received data from client: %s", data.decode("utf-8"))
        try:
            client_socket.send(bytes('Hey client',"utf-8"))
        except: 
            print("Exited by the user.")
        
    client_socket.close()