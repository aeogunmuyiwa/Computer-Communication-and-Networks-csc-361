import socket
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("IP",help="IP Addr",type=str)
parser.add_argument("Port",help="IP Addr",type=int)
parser.add_argument("file",help="IP Addr",type=str)
args=parser.parse_args()

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host =args.IP
port =args.Port
#remoteip=socket.gethostbyname(host)
s.connect((host,port))
s.send("GET /%s"%args.file+" HTTP/1.1 \n\n")
data=s.recvfrom(1024)
#print data
#data=data.replace("> ","\n")
for i in range(0, len(data)):
  print (data[i].encode())
print("\r\n".encode())
s.close()



