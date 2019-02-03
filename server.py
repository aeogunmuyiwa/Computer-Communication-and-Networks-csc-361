#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
host = ''
port = 34832

# we could also have bind it to speicfic address or local host  & we tell the operating system to
serverSocket.bind ((host, port))#associate the socket with the local address,


# accept upto 5 accepting cleint , waiting queue
serverSocket.listen(1)


while True:
    #Establish the connection
    print('Ready to serve...')
    #we accept a new client address,
    #s.accept() blocks until connection is recieved , sever sleeps if nothing is happening
    #returns a pair(client_Socket , address) and we save it in a new socket used for data
    # accept blocks until there are connection from client
    connectionSocket, addr =  serverSocket.accept()

    try:
      #recieve the message from the client
        message = serverSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f.read()
        message_to_send = 'HTTP/1.1 200 OK\r\n\r\n'
        #Send one HTTP header line into socket
        connectionSocket.send(message)

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
