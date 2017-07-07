outputfile = open("split.txt", "w")
inputfile = open("Analysis.txt", "r")
for line in inputfile:
    reqs = line.split()[1]
    print (reqs)
