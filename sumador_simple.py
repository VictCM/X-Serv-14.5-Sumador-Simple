#!/usr/bin/python3

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

mySocket.bind(('localhost', 1234))

#Lo convierto en servidor y digo que solo escuche a 5 clientes como maximo
mySocket.listen(5)

rndm_num=random.randint(1,999999999)

while True:
    print("Waiting for connections")
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received: ')
    bytes_receive = recvSocket.recv(2048)
    request = str(bytes_receive, 'utf-8')
    #proceso peticion y veo que me piden
    print(request)
    resource = request.split()[1]
    print("Resource: ", resource)
    _, op1, operacion, op2 = resource.split('/')
    print(op1, operacion, op2)
    #hago lo que me dicen
    respuesta1 = "Calculando: "
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + respuesta1, 'utf-8'))
    recvSocket.close()
