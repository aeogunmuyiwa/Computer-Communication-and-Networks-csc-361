from socket import *
from datetime import datetime
import time 
import sys
#create a client side socket
#ADDRESS FAMILY, DTAGRAM FOT UDP, TCP:STREAM
clientsocket = socket(AF_INET,SOCK_DGRAM)

# Assign IP address and port number to socket , serverport given in sever code
HOST = '127.0.0.1'
serverPort = 12000

#set waiting time for one seconf for repsonse from the server
clientsocket.settimeout(1)
sequence_number = 1
last_ping = 11 

#declare the socket address
remote_address = (HOST,serverPort)

while sequence_number < last_ping :
  start_time = time.time()
  message = 'ping '+str(sequence_number)+ " " + time.ctime(start_time)
  sequence_number+=1
  try:
    sent = clientsocket.sendto(message,remote_address)
    print("sent " + message)
    #recieve messgae from the sever
    data, serverAddress = clientsocket.recvfrom(1024)
    print("recieved " + data)
    recieved_time= time.time()
    RTT = recieved_time -start_time
    print("RTT: " + str(RTT) + " seconds\n" )
    
  except timeout:
    print('Request timed out\n')


#Close client socket
clientsocket.close()

