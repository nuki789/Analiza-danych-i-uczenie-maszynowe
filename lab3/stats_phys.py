def srednia_listy(lista):
    """ Sumuje wszystkie elementy listy i dzieli przez ilość elementów w liście, zwraca średnią """
    suma = 0
    for item in lista:
        suma = suma + item
    srednia = suma / len(lista)
    return srednia

###################################################################################################################

def odchylenie_standardowe(lista):
    """ Oblicza odchylenie standardowe dla listy, zwraca odchylenie standardowe """
    licznik = 0
    srednia = srednia_listy(lista)
    for item in lista:
        licznik = licznik + (item - srednia) ** 2
    sigma = (licznik / len(lista)) ** 0.5
    return sigma

###################################################################################################################

def pearson_core(lista_x, lista_y):
    """ Oblicza współczynnik korelacji Pearsona dla dwóch list, zwraca współczynnik korelacji """
    srednia_x = srednia_listy(lista_x)
    srednia_y = srednia_listy(lista_y)
    licznik = 0
    mianownik_A = 0
    mianownik_B = 0
    for item in range(len(lista_x) - 1):
        licznik = licznik + (lista_x[item] - srednia_x) * (lista_y[item] - srednia_y)
        mianownik_A = mianownik_A + (lista_x[item] - srednia_x) ** 2
        mianownik_B = mianownik_B + (lista_y[item] - srednia_y) ** 2
    corr = licznik / ((mianownik_A ** 0.5) * (mianownik_B ** 0.5))
    return corr

###################################################################################################################

def regresja_liniowa(lista_x, lista_y):
    """ Oblicza współczynnik kierunkowy i wyraz wolny dla regresji liniowej dwóch list, zwraca współczynnik kierunkowy i wyraz wolny """
    srednia_listy_x = srednia_listy(lista_x)
    srednia_listy_y = srednia_listy(lista_y)
    licznik = 0
    mianownik = 0
    for item in range(len(lista_x)):
        licznik = licznik + (lista_x[item] - srednia_listy_x) * (lista_y[item] - srednia_listy_y)
        mianownik = mianownik + (lista_x[item] - srednia_listy_x) ** 2
    a = licznik / mianownik
    b = srednia_listy_y - a * srednia_listy_x
    return a, b

