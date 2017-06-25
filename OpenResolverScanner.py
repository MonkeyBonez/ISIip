# import subprocess
#
# # inputfile = open("list.txt", "r")
# # for line in inputfile:
# #     ip = line.split()[0]
# ip = ["213.111.4.90"]
# process = subprocess.Popen("dig +short test.openresolver.com TXT @", ip , stdout=subprocess.PIPE, shell=True)
# out, err = process.communicate()
# print (out)
#
import subprocess

inputfile = open("list.txt", "r")
next(inputfile)
count = 0
openCnt = 0
openResolver = []
for line in inputfile:
    if count >= 1000:
        break
    ip = line.split()[0]
    program_name = "dig +short test.openresolver.com TXT @" + ip
    print (program_name)
    command = [program_name]
    output = subprocess.Popen(command, stdout=subprocess.PIPE,shell=True).communicate()[0]
    if(output == "open-resolver-detected"):
        openCnt += 1
        openResolver.insert(ip)
    print (output)
    count += 1



print("open resolver count of top 1000: " + len(openResolver))
for ip in openResolver:
    print (ip)