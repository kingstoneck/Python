#!/usr/bin/env python3

import socket
import time

host = '127.0.0.1'  # The server's hostname or IP address
port = 65432        # The port used by the server

ws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False
print("Server not connected")
while True:
	if(not connected):
		try:
			ws.connect((host, port))
			print("Server Connected")
			connected = True
		except:
			pass
	else:
		#try:
		#	ws.sendall(b'Hello, world')
		#except:
			print("Server Not Connected")
			ws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			connected = False
			pass
		#time.sleep(5)
ws.close()

print('Received', repr(data))

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(b'Hello, world')
#    data = s.recv(1024)
#
#print('Received', repr(data))
