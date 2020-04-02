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
