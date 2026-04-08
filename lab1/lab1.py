# Przykład 1
'''
from math import pi

print("Witaj w programie do obliczania pola koła")

r = float(input("Podaj promień koła: "))

pole = round(pi * r ** 2, 2)

print(f"Pole koła o promieniu {r} wynosi: {pole}")
'''

# Przykład 2
'''Sprawdzamy, czy zmienna jest dodatnia czy ujemna

a = 10
if a > 0:
    print("Zmienna jest dodatnia")
elif a < 0:
    print("Zmienna jest ujemna")
else:
    print("Zmienna jest równa zero")
'''

# Przykład 2a
'''Typy wyliczeniowe'''

lista = [2, 4, 1, 9]
krotka = (1, 2, 3)
string = "Jakiś tekst"
słowinik = {1:"poniedziałek", 2:"wtorek", 3:"środa"}

# Przykład 3
'''Demo pętli for'''
for i in range(5, 25, 3):
    print(i)

for item in lista:
    print(item)

for item in enumerate(lista):
    print(item)