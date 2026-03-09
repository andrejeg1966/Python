"""
Created on 13.03.2025

@author: goran
"""

import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
print(socket.gethostname())
