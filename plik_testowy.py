c = "Kiedyś ktoś to przeczyta i będzie śmiesznie"
b = "Twój stary"


if b == "Twój stary":
    print(c)
else: print(b)

for i in range(-3,24,4):  #wybór co czwartej liczby z przedziału (-3;24)
    print(i)

cities = ["Pecs", "Budapest", "Debrecen", "Sopron", "Szolnok", "Miszkolc", "Eger"]

for i, city in enumerate(cities):  #wybór 4 pierwszych miast z listy za pomocą pętli for które nie są stolicą
    if city == "Budapest":
        continue
    if i == 4:
        break
    print(i)
    print("{} spełnia wymagania".format(city))

print(2.2 * 3.0 == 6.6) ## co tu sie odpierdala XDXDXD
print(float(2.2 * 3.0))

print(3.3 * 2.0 == 6.6) ## no a tu juz jest git
print(float(3.3 * 2.0))

while True:  ## kalkulator w pętli while [który już się kończy po jednej operacji i wydaje błąd]
        try:
            x = (input("Wybierz liczbę by uzyskać jej sześcian: "))
            a = float(x)
            print(a * a * a)
            break
        except ValueError:
            print("Oops! Kalkulator nie przyjmuje tekstu i/lub dat.")
            break

