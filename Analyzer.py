from collections import OrderedDict
from operator import itemgetter
from ipwhois import IPWhois
from ipwhois.net import Net
from ipwhois.asn import ASNOrigin

inputfile = open("list.txt", "r")
countryFrequency = {}
countryRequestFrequency = {}
asnFrequency = {}
asnRequestFrequency={}
count = 0
next(inputfile)

for line in inputfile:
    ip = line.split()[0]
    country = line.split()[1]
    asn = line.split()[2]
    requests = int(line.split()[3])
    count += 1

    # obj = IPWhois(ip)
    # res = obj.lookup_whois()
    # print res

    if country not in countryFrequency:
        countryFrequency[country] = 0
    countryFrequency[country] += 1

    if country not in countryRequestFrequency:
        countryRequestFrequency[country] = requests
    countryRequestFrequency[country] += requests

    if asn not in asnFrequency:
        asnFrequency[asn] = 0
    asnFrequency[asn] += 1

    if asn not in asnRequestFrequency:
        asnRequestFrequency[asn] = requests
    asnRequestFrequency[asn] += requests


countryFrequency = OrderedDict(sorted(countryFrequency.items(), key=itemgetter(1)))
countryRequestFrequency = OrderedDict(sorted(countryRequestFrequency.items(), key=itemgetter(1)))
asnFrequency = OrderedDict(sorted(asnFrequency.items(), key=itemgetter(1)))
asnRequestFrequency = OrderedDict(sorted(asnRequestFrequency.items(), key=itemgetter(1)))

print "\n\t% Country IP in top 10000"
for country in countryFrequency:
    print country + " " , float(countryFrequency[country])/count

print "\n\t% Top country requests in top 10000"
for country in countryRequestFrequency:
    print country + " " , float(countryRequestFrequency[country])/sum(countryRequestFrequency.values())

print "\n\t% Top ASN in top 10000"
for asn in asnFrequency:
    print asn + " " , float(asnFrequency[asn])/count

net = Net('2001:43f8:7b0::')
obj = ASNOrigin(net)

count = 0
print "\n\t% Top ASN requests in top 10000"
for asn in asnRequestFrequency:
    if count > len(asnRequestFrequency) - 20:
        results = obj.lookup(asn)
        try:
            print results['nets'][0]['description']
        except (ValueError,IndexError):
            print 'N/A'
    print asn + " " , float(asnRequestFrequency[asn])/sum(asnRequestFrequency.values())
    count += 1