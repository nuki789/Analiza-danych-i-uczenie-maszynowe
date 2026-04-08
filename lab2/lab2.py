"""for i in range (1, 10):
    print(i)

lista = [10, 20, 30, 40, 50]

for item in lista:
    print(item**2)"""

'''a = 0
while a<10:
    
    if a==3:
        #a = a+1
        #continue
        break
    
    print(a, "abc")
    
    a = a + 1'''

'''
def suma_listy(lista = [0]):
    """Tutaj jest dokumentacja naszego kodu"""
    suma = 0
    for item in lista:
        suma = suma + item
    return suma
    '''


class Ulamek:
    def __init__(self, l, m):
        self.licznik = l
        self.mianownik = m
    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"
    def __add__(u1, u2):
            
        licznik = u1.licznik * u2.mianownik + u1.mianownik * u2.licznik
        mianownik = u1.mianownik * u2.mianownik
            
        wynik = Ulamek(licznik, mianownik)
            
        return wynik
    
    def zw(self, k):
        self.licznik = self.licznik + k
        self.mianownik = self.mianownik + k














