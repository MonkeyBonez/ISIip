import socket
import re
import sys
s = socket.socket()
address = '136.243.94.106'
port = 53
print ("Attempting to connect to %s on port %s" % (address, port))
try:
    s.connect((address, port))
    print ("Connected to %s on port %s" % (address, port))
except socket.error:
        print ("Connection to %s on port %s failed" % (address, port))
