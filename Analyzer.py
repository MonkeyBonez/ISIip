
inputfile = open("list.txt", "r")
countryFrequency = {}
countryRequestFrequency = {}
next(inputfile)
for line in inputfile:
    ip = line.split()[0]
    country = line.split()[1]
    address = line.split()[2]
    requests = int(line.split()[3])

    if country not in countryFrequency:
        countryFrequency[country] = 0
    countryFrequency[country] += 1

    if country not in countryRequestFrequency:
        countryRequestFrequency[country] = requests
    countryRequestFrequency[country] += requests



print "\n\tCountry IP frequencies in top 1000"
for country in countryFrequency:
    print country + " " , countryFrequency[country]

print "\n\tTop country requests in top 1000"
for country in countryRequestFrequency:
    print country + " " , float(countryRequestFrequency[country])/sum(countryRequestFrequency.values())