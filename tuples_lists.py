cities = ["Pecs", "Budapest", "Debrecen", "Sopron", "Szolnok", "Miszkolc", "Eger"]

for i, city in enumerate(cities):  #wybór 4 pierwszych miast z listy za pomocą pętli for które nie są stolicą
    if city == "Budapest":
        continue
    if i == 4:
        break
    print(i)
    print("{} spełnia wymagania".format(city))

print()
population_2008 = { 'Belgium': 10666866, 'Bulgaria': 7518002, 'Czechia': 10343422, 'Denmark': 5475791, 'Germany': 82217837, 'Estonia': 1338440, 'Ireland': 4457765, 'Greece': 11060937, 'Spain': 45668939, 'France': 64007193, 'Croatia': 4311967, 'Italy': 58652875, 'Cyprus': 776333, 'Latvia': 2191810, 'Lithuania': 3212605, 'Luxembourg': 483799, 'Hungary': 10045401, 'Malta': 407832, 'Netherlands': 16405399, 'Austria': 8307989, 'Poland': 38115641, 'Portugal': 10553339, 'Romania': 20635460, 'Slovenia': 2010269, 'Slovakia': 5376064, 'Finland': 5300484, 'Sweden': 9182927, 'United Kingdom': 61571647, 'Iceland': 315459, 'Liechtenstein': 35356, 'Norway': 4737171, 'Switzerland': 7593494, 'Montenegro': 615543, 'North Macedonia': 2045177, 'Albania': 2958266, 'Serbia': 7365507, 'Turkey': 70586256, 'Andorra': 83137, 'Belarus': 9689770, 'Bosnia and Herzegovina': 3843846, 'Kosovo': 2153139, 'Moldova': 3572703, 'San Marino': 32054, 'Ukraine': 46192309, 'Armenia': 3230086, 'Azerbaijan': 8629900, 'Georgia': 4382070 }
population_2018 = { 'Belgium': 11398589, 'Bulgaria': 7050034, 'Czechia': 10610055, 'Denmark': 5781190, 'Germany': 82792351, 'Estonia': 1319133, 'Ireland': 4830392, 'Greece': 10741165, 'Spain': 46658447, 'France': 66926166, 'Croatia': 4105493, 'Italy': 60483973, 'Cyprus': 864236, 'Latvia': 1934379, 'Lithuania': 2808901, 'Luxembourg': 602005, 'Hungary': 9778371, 'Malta': 475701, 'Netherlands': 17181084, 'Austria': 8822267, 'Poland': 37976687, 'Portugal': 10291027, 'Romania': 19530631, 'Slovenia': 2066880, 'Slovakia': 5443120, 'Finland': 5513130, 'Sweden': 10120242, 'United Kingdom': 66273576, 'Iceland': 348450, 'Liechtenstein': 38114, 'Norway': 5295619, 'Switzerland': 8484130, 'Montenegro': 622359, 'North Macedonia': 2075301, 'Albania': 2870324, 'Serbia': 7001444, 'Turkey': 80810525, 'Andorra': 74794, 'Belarus': 9491823, 'Bosnia and Herzegovina': 3502550, 'Kosovo': 1798506, 'Moldova': 3547539, 'San Marino': 34453, 'Ukraine': 42386403, 'Armenia': 2972732, 'Azerbaijan': 9898085, 'Georgia': 3729633 }

pophun_08 = population_2008["Hungary"]
pophun_18 = population_2018["Hungary"]
print(("The pop in 2008 is %d") % pophun_08)
print(("The pop in 2018 is %d") % population_2018["Hungary"])

print()
change = pophun_18 - pophun_08
print(("The differnece was %d") % change)


print()

#max min value search
max_diff = population_2018['Hungary'] - population_2008['Hungary']
min_diff = population_2018['Poland'] - population_2008['Poland'] #nie ma znaczenia jaki klucz się wybierze tip
max_country = 'Hungary'
min_country = 'Poland'

for key, value in population_2008.items():
    pop_2018 = population_2018[key]
    print("%s, 2008: %d, 2018: %d" % (key, value, pop_2018))
    diff = pop_2018 - value
    print("Difference: %d" % diff)

    if diff > max_diff:
        max_diff = diff
        max_country = key
    if diff < min_diff:
        min_diff = diff
        min_country = key

print()
print(max_country)
print(max_diff)
print()
print(min_country)
print(min_diff)

import random

#2.1

numbers = []
odds = []
evens = []
for i in range(20):
    numbers.append(random.randint(1, 100))
print(numbers)

for number in numbers:
    if number % 2 == 0:
        odds.append(number)
    else:
        evens.append(number)

print(odds)
print(evens)
