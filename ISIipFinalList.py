from geoip import geolite2
import socket
import win_inet_pton
outputfile = open("list.txt", "w")
inputfile = open("reqs.out", "r")
outputfile.write("ip           country      address              requests \n" )
count = 1
numOfIps = input('Enter how many abnormally-acting ips you would like to get the information of:')
if numOfIps > 0:
    while (count < numOfIps + 1 ):
        for line in inputfile:
            singleIp = line.split()[0]
            singleReq = line.split()[1]
            if singleReq > 1248 or singleReq < 52:
                match = geolite2.lookup(singleIp)
                if match is not None:
                    singleCountry = match.country
                else:
                        singleCountry = "unknown"

                try:
                        singleAddress = socket.gethostbyaddr(singleIp)[0]

                except socket.error:
                        singleAddress = "unknown"

                outputfile.write(singleIp + " " + singleCountry + " " + singleAddress + " " +singleReq + "\n")

            count = count + 1
            if count>numOfIps:
                break
else:
    for line in inputfile:
        singleIp = line.split()[0]
        singleReq = line.split()[1]
        if singleReq > 1248 or singleReq < 52:
            match = geolite2.lookup(singleIp)
            if match is not None:
                singleCountry = match.country
            else:
                singleCountry = "unknown"

            try:
                singleAddress = socket.gethostbyaddr(singleIp)[0]

            except socket.error:
                singleAddress = "unknown"

            outputfile.write(singleIp + " " + singleCountry + " " + singleAddress + " " + singleReq + "\n")

outputfile.close()
print ("Done")