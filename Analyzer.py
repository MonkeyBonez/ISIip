from collections import OrderedDict
from operator import itemgetter

inputfile = open("list.txt", "r")
countryFrequency = {}
countryRequestFrequency = {}
asnFrequency = {}
count = 0
next(inputfile)
for line in inputfile:
    ip = line.split()[0]
    country = line.split()[1]
    asn = line.split()[2]
    requests = int(line.split()[3])
    count += 1

    if country not in countryFrequency:
        countryFrequency[country] = 0
    countryFrequency[country] += 1

    if country not in countryRequestFrequency:
        countryRequestFrequency[country] = requests
    countryRequestFrequency[country] += requests

    if asn not in asnFrequency:
        asnFrequency[asn] = 0
    asnFrequency[asn] += 1


countryFrequency = OrderedDict(sorted(countryFrequency.items(), key=itemgetter(1)))
countryRequestFrequency = OrderedDict(sorted(countryRequestFrequency.items(), key=itemgetter(1)))
asnFrequency = OrderedDict(sorted(asnFrequency.items(), key=itemgetter(1)))

print "\n\t% Country IP in top 1000"
for country in countryFrequency:
    print country + " " , float(countryFrequency[country])/count

print "\n\t% Top country requests in top 1000"
for country in countryRequestFrequency:
    print country + " " , float(countryRequestFrequency[country])/sum(countryRequestFrequency.values())

print "\n\t% Top ASN in top 1000"
for asn in asnFrequency:
    print asn + " " , float(asnFrequency[asn])/count