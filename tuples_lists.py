cities = ["pecs", "budapest", "debrecen", "sopron", "szolnok", "miszkolc", "eger"]

for i, city in enumerate(cities):  #wybór 4 pierwszych miast z listy za pomocą pętli for które nie są stolicą
    if city == "budapest":
        continue
    if i == 4:
        break
    print(i)
    print("{} spełnia wymagania".format(city))

print()
population_2008 = { 'belgium': 10666866, 'bulgaria': 7518002, 'czechia': 10343422, 'denmark': 5475791, 'germany': 82217837, 'estonia': 1338440, 'ireland': 4457765, 'greece': 11060937, 'spain': 45668939, 'france': 64007193, 'croatia': 4311967, 'italy': 58652875, 'cyprus': 776333, 'latvia': 2191810, 'lithuania': 3212605, 'luxembourg': 483799, 'hungary': 10045401, 'malta': 407832, 'netherlands': 16405399, 'austria': 8307989, 'poland': 38115641, 'portugal': 10553339, 'romania': 20635460, 'slovenia': 2010269, 'slovakia': 5376064, 'finland': 5300484, 'sweden': 9182927, 'united kingdom': 61571647, 'iceland': 315459, 'liechtenstein': 35356, 'norway': 4737171, 'switzerland': 7593494, 'montenegro': 615543, 'north macedonia': 2045177, 'albania': 2958266, 'serbia': 7365507, 'turkey': 70586256, 'andorra': 83137, 'belarus': 9689770, 'bosnia and herzegovina': 3843846, 'kosovo': 2153139, 'moldova': 3572703, 'san marino': 32054, 'ukraine': 46192309, 'armenia': 3230086, 'azerbaijan': 8629900, 'georgia': 4382070 }
population_2018 = { 'belgium': 11398589, 'bulgaria': 7050034, 'czechia': 10610055, 'denmark': 5781190, 'germany': 82792351, 'estonia': 1319133, 'ireland': 4830392, 'greece': 10741165, 'spain': 46658447, 'france': 66926166, 'croatia': 4105493, 'italy': 60483973, 'cyprus': 864236, 'latvia': 1934379, 'lithuania': 2808901, 'luxembourg': 602005, 'hungary': 9778371, 'malta': 475701, 'netherlands': 17181084, 'austria': 8822267, 'poland': 37976687, 'portugal': 10291027, 'romania': 19530631, 'slovenia': 2066880, 'slovakia': 5443120, 'finland': 5513130, 'sweden': 10120242, 'united kingdom': 66273576, 'iceland': 348450, 'liechtenstein': 38114, 'norway': 5295619, 'switzerland': 8484130, 'montenegro': 622359, 'north macedonia': 2075301, 'albania': 2870324, 'serbia': 7001444, 'turkey': 80810525, 'andorra': 74794, 'belarus': 9491823, 'bosnia and herzegovina': 3502550, 'kosovo': 1798506, 'moldova': 3547539, 'san marino': 34453, 'ukraine': 42386403, 'armenia': 2972732, 'azerbaijan': 9898085, 'georgia': 3729633 }

pophun_08 = population_2008["hungary"]
pophun_18 = population_2018["hungary"]
print(("the pop in 2008 is %d") % pophun_08)
print(("the pop in 2018 is %d") % population_2018["hungary"])

print()
change = pophun_18 - pophun_08
print(("the differnece was %d") % change)


print()

#max min value search
max_diff = population_2018['hungary'] - population_2008['hungary']
min_diff = population_2018['poland'] - population_2008['poland'] #nie ma znaczenia jaki klucz się wybierze tip
max_country = 'hungary'
min_country = 'poland'

for key, value in population_2008.items():
    pop_2018 = population_2018[key]
    print("%s, 2008: %d, 2018: %d" % (key, value, pop_2018))
    diff = pop_2018 - value
    print("difference: %d" % diff)

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

#collatz sequence

collatz = []
num = int(input("wybierz liczbę startową: "))

while num != 1:
    collatz.append(num)
    if num % 2 == 0:
        num = int(num / 2)
    else:
        num = int(3 * num + 1)


print(collatz)
