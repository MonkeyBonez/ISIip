import socket
import re
import sys
inputfile = open("reqs.out", "r")
count = 0
DNS_PORT = 53
s = socket.socket()

def ipPortConnector (address, port):
    print ("Attempting to connect to %s on port %s" % (address, port))
    try:
        s.connect((address, port))
        print ("Connected to %s on port %s" % (address, port))
    except socket.error:
        print ("Connection to %s on port %s failed" % (address, port))

for line in inputfile:
    count+= 1
    ip = line.split()[0]
    ipPortConnector(ip,DNS_PORT)
    if count > 20:
        break




