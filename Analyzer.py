import requests as reqs
from bs4 import BeautifulSoup
from collections import OrderedDict
from operator import itemgetter



def ASNOwnerLookup(asn):
    url = "https://www.ultratools.com/tools/asnInfoResult?domainName=" + asn
    page = reqs.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    html = list(soup.children)[23] #gets tag with ASN owner data
    data = list(html.children)[3]
    # print data
    spans = data.find_all('span', {'class' : 'value'})
    return spans[3].text #gets owner



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

print ("\n\t% Country IP in top 10000")
for country in countryFrequency:
    print (country + " " , float(countryFrequency[country])/count)

print ("\n\t% Top country requests in top 10000")
for country in countryRequestFrequency:
    print (country + " " , float(countryRequestFrequency[country])/sum(countryRequestFrequency.values()))

print ("\n\t% Top ASN in top 10000")
for asn in asnFrequency:
    print (asn + " " , float(asnFrequency[asn])/count)


count = 0
print ("\n\t% Top ASN requests in top 10000")
for asn in asnRequestFrequency:
    print (asn + " ", float(asnRequestFrequency[asn]) / sum(asnRequestFrequency.values()))
    if count > len(asnRequestFrequency) - 20:
        print "Owner: " + ASNOwnerLookup(asn)
    count += 1