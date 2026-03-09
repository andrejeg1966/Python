"""
udp socket client
Silver Moon
"""

import socket  # for sockets
import sys  # for exit
import time

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print("Failed to create socket")
    sys.exit()

host = "localhost"
port = 8888

i = 5
while i > 0:
    # msg = raw_input('Enter message to send : ')

    try:
        # Set the whole string
        # s.sendto("Hello", (host, port))
        ts = time.time()
        # ts = ""
        time.sleep(0.1)
        if i == 3:
            ts = ""
        s.sendto(str(ts), (host, port))

        # receive data from server (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print("Server reply : " + reply)

    except socket.error, msg:
        print("Error Code : " + str(msg[0]) + " Message " + msg[1])
        sys.exit()

    i = i - 1
