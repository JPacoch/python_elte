import random

#guess a number
print("Hello! Welcome to the 'Guess a number' game! What is your name? ")
name = input()
name = str(name)
print("Hello %s" % name)
num = random.randint(1,100)

guess = str(input("Ready? "))


while guess != num:
    print("Guess a number between 1 and 100.")
    guess = input()
    guess = int(guess)

    if guess < num:
        print("The number is too low")

    if guess > num:
        print("The number is too large")

    if guess == num:
        print("Nice! You are correct!")
        break


#kamien papier nozyczki
l = ['Rock', 'Paper', 'Scissors' ]
AI = l[random.randint(0,2)]

num_of_games = 0

while num_of_games < 5:
    human = input("1, 2, 3... ")

    num_of_games = num_of_games + 1
    try:
        if human == AI:
            print("That's a draw.")
        elif human  == "Paper":
            if AI == "Rock":
                print("You won!")
            else:
                print("You lost.")
        elif human == "Rock":
            if AI == "Paper":
                print("You lost.")
            else:
                print("You won!")
        elif human == "Scissors":
            if AI == "Paper":
                print("You won!")
            else:
                print("You lost.")
    except ValueError:
        print("Pick from 'Rock', 'Paper' or 'Scissors'!")
        break

countries = ['Albania', 'Andorra', 'Austria', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Czech Republic', 'Denmark', 'United Kingdom', 'Estonia', 'Belarus', 'Finland', 'France', 'Greece', 'Netherlands', 'Croatia', 'Ireland', 'Iceland', 'Kosovo', 'Poland', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Hungary', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Germany', 'Norway', 'Italy', 'Portugal', 'Romania', 'San Marino', 'Spain', 'Switzerland', 'Sweden', 'Serbia', 'Slovakia', 'Slovenia', 'Ukraine']
capitals = ['Tirana', 'Andorra la Vella', 'Vienna', 'Brussels', 'Sarajevo', 'Sofia', 'Prague', 'Copenhagen', 'London', 'Tallin', 'Minsk', 'Helsinki', 'Paris', 'Athens', 'Hague', 'Zagreb', 'Dublin', 'Reykjavik', 'Prishtina', 'Warsaw', 'Riga', 'Vaduz', 'Vilnius', 'luxembourg', 'Skopje', 'Budapest', 'Valletta', 'Chisinau', 'Monaco', 'Podgorica', 'Berlin', 'Oslo', 'Rome', 'Lisbon', 'Bucharest', 'San Marino', 'Madrid', 'Berne', 'Stockholm', 'Belgrade', 'Bratislava', 'Ljubljana', 'Kiev']
areas = [28748, 468, 83857, 30519, 51130, 110912, 78864, 43077, 244100, 45100, 207600, 338145, 543965, 131957, 33933, 56500, 70283, 103000, 10887, 312683, 63700, 160, 65200, 2586, 25713, 93036, 316, 33700, 2, 13812, 357042, 323877, 301277, 92389, 237500, 61, 504782, 41293, 449964, 66577, 49035, 20250, 603700]
populations = [3.2, 0.07, 7.6, 10.0, 4.5, 9.0, 10.4, 5.1, 57.2, 1.6, 10.3, 4.9, 56.2, 10.0, 14.8, 4.7, 3.5, 0.3, 2.2, 37.8, 2.6, 0.03, 3.6, 0.4, 2.1, 10.4, 0.3, 4.4, 0.03, 0.6, 78.6, 4.2, 57.5, 10.5, 23.2, 0.03, 38.8, 6.7, 8.5, 7.2, 5.3, 2.0, 51.8]

lista = []
dicc = {}

for idx in range(0,len(countries)):
    dicc = {
        "country": countries[idx],
        "capital": capitals[idx],
        "area": areas[idx],
        "population": populations[idx]
    }
    lista.append(dicc)
    idx + 1

print(lista)

for idx in range(0,len(countries)):
    dicc = {
        "country": countries[idx],
        "capital": capitals[idx],
        "area": areas[idx],
        "population": populations[idx],
        "density": populations[idx] / areas[idx]
    }
    lista.append(dicc)
    idx + 1

print(lista)

max_dens = max(item['density'] for item in lista)
print(max_dens)

class Country():
    name = 'Country'

    def card(self, idxx):
        name = countries[idxx]
        caps = capitals[idxx]
        pops = populations[idxx]
        area = areas[idxx]
        return print("Country name: %s. Capital: %s. Population: %f mln. Area: %f km2. " % (name, caps, pops, area))

    def density(self, idxx):
        name = countries[idxx]
        dens = populations[idxx] / areas[idxx] * 1000000
        return print("z/km2" % (name, dens))

state = Country()
state.card(12)
state.density(12)

listt = []

for i in range(len(countries)):
    state.card(i)
    state.density(i)


class BMI():

    def __str__(self):
        return "To jest kalkulator Body Mass Index."

    def bmi_ind(self, wzrost, waga):
        return waga / ((wzrost / 100) ** 2)

    def bmi(self, wzrost, waga):
        if waga / ((wzrost / 100) ** 2) < 18.5:
            print("You are underweight.")
        elif waga / ((wzrost / 100) ** 2) < 25:
            print("You are normal weight.")
        elif waga / ((wzrost / 100) ** 2) < 30:
            print("You are overweight.")
        else:
            print("You are obese.")

#Kalkulator fahnrenheit - > celsjusz

def fahr2cels(fahrenheit):
    c = 5/9 * (fahrenheit - 32)
    return c

for fahr in range(0,101,10):
    cels = fahr2cels(fahr)
    print('Fahr = %d, Cels = %.2f' % (fahr, cels))

import math


#Test liczb pierwszych

def isPrime(number):
    if number < 2: #special case od 1 and 0
        return False

    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False

    return True

try:
    num = int(input("Number to check: "))
    if isPrime(num):
        print("%d is a prime" % num)
    else:
        print("%d is not a prime" % num)
except:
    print("Not a number")

#anagram check
def anagram(word1, word2):

    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

#pyramid
def pyramid(height):
    height = int(height)
    for up in range(1, height + 1):
        for width in range(1, up + 1):
            print("*")
        print()
