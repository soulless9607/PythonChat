#!/usr/lib/python2.7
#encoding: utf-8
import socket
import sys
mi_socket = socket.socket() #nuevo socket por default
host = socket.gethostname()
port= 1996
mi_socket.bind((host,port))  #establecemos conexion y puerto
mi_socket.listen(5) #cantidad de peticiones en cola
print 'waiting for connections (2)'
#client = 0
client1, address = mi_socket.accept() #aceptamos el cliente y su dirección
print 'Client 1 has connected '
client1.send("Welcome to the server, client 1".encode())
print 'Waiting for connections (1)'
client2, adress1 = mi_socket.accept()
print 'client 2 has connected '
client2.send("Welcome to the server, client 2".encode())
while 1:
    message = raw_input('>>')
    message = message.encode()
    client1.send(message)
    client2.send(message)
    print 'Message sent'
    message_recive1 = client1.recv(1024)
    print ('client 1: ', message_recive1.decode())
    client2.send(message_recive1)

    message_recive1 = client2.recv(1024)
    print ('client 1: ', message_recive1.decode())
    client1.send(message_recive1)


    #print ('client 2: ', message_recive2)
    #client2.send(message_recive2.decode())





""" while True: #ciclo infinito
    if client == 0:

        print 'Connected'
        client.send("Welcome")
        client1, address1 = mi_socket.accept()
    else:
        request = client.recv(1024) #recuperamos los datos enviados desde el cliente
        print request
        client.send(request)
        request = client1.recv(1024)
        print request
        client1.send(request)
        """
