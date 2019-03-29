from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.uvic.ca"
port = 25
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver,port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
email_from = raw_input("Mail From: ")
mail_command = "Mail From: <"+ email_from + ">\r\n"
clientSocket.send(mail_command.encode())
recv2 = clientSocket.recv(1024)
print("After Mail From Command: "+ recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')



# Send RCPT TO command and print server response. 
recipient = raw_input("RCPT TO: ")
rcpt_command = "RCPT TO: <"+ recipient + ">\r\n"
clientSocket.send(rcpt_command)
rcpt_recv = clientSocket.recv(1024)
print("After RCPT TO Command: "+ rcpt_recv)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send DATA command and print server response. 
data_command='DATA\r\n'
clientSocket.send(data_command)
datarecv = clientSocket.recv(1024)
print("After Data Command: "+ datarecv)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quit = 'quit\r\n'
clientSocket.send(quit.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '221':
    print('221 reply not received from server.')