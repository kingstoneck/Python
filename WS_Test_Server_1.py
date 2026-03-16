#!/usr/bin/env python3

import socket
import time

host = '127.0.0.1'  # Standard loopback interface address (localhost)
port = 65432        # Port to listen on (non-privileged ports are > 1023)

#num = int(input("Enter a natural number "))
#num = int(10)
#i=1
#print("The numbers are as follows:")
#while i<=num:
#	print("i=",i)
#	time.sleep(1)
#	i=i+1
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ws:
    ws.bind((host, port))
    ws.listen()
    conn, addr = ws.accept()
    with conn:
        print('Connected by', addr)
		#print('Testing')
		#print('Testing 2')
		#num = int(10)
		#i=1
		#while i<=num:
		#	print("i=",i)
		#	time.sleep(1)
		#	i=i+1
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

			
