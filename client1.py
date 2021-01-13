#!/usr/lib/python2.7
#encoding: utf-8
import socket
import sys
mi_socket = socket.socket()
host = socket.gethostname()
port = 1996
mi_socket.connect((host, port))
print '---Connected to the server--- '
message = mi_socket.recv(1024)
message = message.decode()
print 'server message: ', message
while 1:
    message = mi_socket.recv(1024)
    message = message.decode()
    print("Server", message)
    message = mi_socket.recv(1024)
    message = message.decode()
    print("Server", message)

    new_message = input(str("Client 1: "))
    new_message = new_message.encode()
    mi_socket.send(new_message)
    print 'message sent'
