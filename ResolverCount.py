import socket
import pyasn
inputfile = open("reqs.out", "r")
aggressiveResolvers = 0
benignResolvers = 0
count = 0
for line in inputfile:
    count = count + 1
    req = int(line.split()[1])
    if req > 1248:
        aggressiveResolvers = aggressiveResolvers + 1
    elif req < 52:
        benignResolvers = benignResolvers + 1
aggressiveResolvers = str(aggressiveResolvers)
benignResolvers = str(benignResolvers)
print("Number of agressive resolvers: " + aggressiveResolvers +"\n Number of benign resolvers " + benignResolvers )