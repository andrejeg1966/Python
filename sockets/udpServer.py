'''
    Simple udp socket server
'''
 
import socket
import sys
import time
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
    
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
    print 'Socket bind complete'
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
logOff = True
i = 5
#now keep talking with the client
while (i > 0):
    # receive data from client (data, addr)
    print("host name: " + str (socket.gethostname()))
    time.sleep(.1)
    ts = time.time()
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
   
    if(data):
        print("data received.: " + data)
     
    if not data:
        print("no data") 
        break
     
    reply = 'OK...' + str(ts) + "/" + data
    #time.sleep(5)
    
    s.sendto(reply , addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
    
    i = i - 1
s.close()

