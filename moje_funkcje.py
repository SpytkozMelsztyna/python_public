import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from scipy import linalg as la
from scipy import optimize
import math
import copy
import time
import more_itertools
import itertools
from pytube import YouTube
import itertools
import datetime

def CZAS_START():
    czas_start = datetime.datetime.now()
    print('początek obliczeń =',czas_start)
    return czas_start

def CZAS_META(czas_start):
    x = czas_start
    moment = datetime.datetime.now()
    print('koniec obliczeń =',moment, 'czas obliczeń =', moment - x)

def Zegar(czas_komputera):
    # czas_komputera - łapać funkcją time.time() z modułu time
    # Zegar przelicza czas komputera na godziny i minuty
    godziny = int((czas_komputera%86400)//3600)
    minuty = int((((czas_komputera%86400)%3600)/3600)*60)
    print('Czas: ',godziny+2,'h',minuty,'min')

def analiza(alfa):
    #rozklada liczbe alfa na czynniki pierwsze wraz z potegami
    #przykladowo: analiza(72)==[(2,3),(3,2)]

    liczba, czynniki = prime_factors_of(alfa)

    czynniki_pojedyncze = []
    for x in czynniki:
        if x not in czynniki_pojedyncze:
            czynniki_pojedyncze.append(x)

    reprezentacja_liczby = []
    for x in czynniki_pojedyncze:
        reprezentacja_liczby.append((x,czynniki.count(x)))
        # print(x,czynniki.count(x))

    # print(liczba, czynniki)
    # print(liczba, czynniki_pojedyncze)
    # print(liczba, reprezentacja_liczby)
    print(liczba)
    return reprezentacja_liczby

def prime_factors_of(liczba):
    # znajduje rozkład liczby na czynniki
    # jak znajdzie dzielnik to dzieli liczbe
    liczba_kopia = liczba
    dzielniki = []
    while liczba_kopia > 1:
        liczymy = True
        dzielnik = 1
        while liczymy:
            dzielnik+=1
            if liczba_kopia%dzielnik==0:
                dzielniki.append(dzielnik)
                liczba_kopia=liczba_kopia/dzielnik
                liczymy=False
    # return 'liczba',liczba,'ma takie dzielniki',dzielniki
    return liczba, dzielniki

def Prime_Numbers(n):
    # w tablicy P zwracane są wszystkie liczby pierwsze < n
    P = [2]
    for i in range(3,n):
        i_jest_pierwsza = True
        for pom in P:
            if i % pom == 0:
                i_jest_pierwsza = False
                break
        if i_jest_pierwsza:
            P.append(i)
    return(P)

def Composite_Numbers(n):
    # w tablicy CN zwracane są wszystkie liczby złożone < n
    CN = [4]
    LP = Prime_Numbers(n)
    for i in range(5, n):
        if i not in LP:
            CN.append(i)
    return CN

def Semi_Prime_Numbers(n):
    # w tablicy S_P_N zwracane są wszystkie liczby półpierwsze < n
    # liczba półpierwsza jest iloczynem 2 liczb pierwszych
    S_P_N = [4]
    liczby_zlozone = Composite_Numbers(n)
    for liczba in liczby_zlozone:
        liczba_jest_spn = True
        for pom in S_P_N:
            if liczba % pom == 0:
                liczba_jest_spn = False
                break
        if liczba_jest_spn:
            S_P_N.append(liczba)
    return S_P_N

def cyfry_liczby(n):
    # cyfry liczby n zwracane są w tablicy cyfry
    # w tej samej kolejności w jakiej występują w liczbie
    # cyfry_liczby(437) zwraca [4, 3, 7]
    cyfry = []
    while n>0:
        ostatnia_cyfra = n % 10
        cyfry.append(int(ostatnia_cyfra))
        n = (n-ostatnia_cyfra) / 10
    cyfry.reverse()
    return cyfry

def liczba_na_cyfry(n):
    # to jest dokładnie funkcja cyfry_liczby()
    # bo chodziło żeby nazwa korespondowała do nazwy funkcji cyfry_na_liczbe()
    # cyfry liczby n zwracane są w tablicy cyfry
    # w tej samej kolejności w jakiej występują w liczbie
    # cyfry_liczby(437) zwraca [4, 3, 7]
    cyfry = []
    while n>0:
        ostatnia_cyfra = n % 10
        cyfry.append(int(ostatnia_cyfra))
        n = (n-ostatnia_cyfra) / 10
    cyfry.reverse()
    return cyfry

def cyfry_na_liczbe(T):
    # T jest listą cyfr, funkcja zamienia ją na liczbę
    # [3,2,7] -> 3*100+2*10+7 = 327
    podstawa = 10
    wykladnik = -1
    liczba = 0
    while len(T) > 0:
        wykladnik += 1
        ostatnia_cyfra = T.pop()
        liczba += ostatnia_cyfra * podstawa**wykladnik
    return liczba

def czy_lista_od_a_do_b(lista,a,b):
    # sprawdza czy lista zawiera wszystkie liczby od a do b włącznie
    # (dokładnie po jednej sztuce)
    # i żadnych innych ani powtórzeń
    # [3,4,5,6] [5,4,6,3] zwracają True - może być nieposortowana
    # [3,4,5,6,5] [3,4,6,7] zwracają False - nie może być dziur ani/i powtórzeń
    to_jest_lista_od_a_do_b = True
    for pom in range(a,b+1):
        if pom not in lista:
            to_jest_lista_od_a_do_b = False
            break
    return to_jest_lista_od_a_do_b and b - a + 1 == len(lista)

def suma_liczb_listy(lista):
    suma = 0
    for x in lista:
        suma = suma + x
    return suma

def iloczyn_liczb_listy(lista):
    iloczyn = 1
    for x in lista:
        iloczyn = iloczyn * x
    return iloczyn

def czy_lista_ma_rozne_cyfry(lista):
    # działa też dla liczb
    lista_ma_rozne_cyfry = True
    a = []
    for x in lista:
        if x not in a:
            a.append(x)
    #print(a)
    #print(lista)
    return len(a) == len(lista)

x=[1,2,4,5,3,1,9]
print(czy_lista_ma_rozne_cyfry(x))


# print(czy_lista_od_a_do_b(x,1,5))
# print(suma_liczb_listy(x))

#print(Composite_Numbers(40))
#print(Semi_Prime_Numbers(68))

def produkujemy_przekatne_w_gore(zakres1, N1):
    przekatne = []
    for pom in range(0, 2 * N1 - 1):
        przekatne.append([])
    for i in zakres1:
        for j in zakres1:
            przekatne[i + j].append([i, j])
    return przekatne


def produkujemy_przekatne_w_dol(zakres1, N1):
    przekatne = []
    for pom in range(0, 2 * N1 - 1):
        przekatne.append([])
    for i in zakres1:
        for j in zakres1:
            przekatne[i - j].append([i, j])
    return przekatne


def produkujemy_wiersze(zakres1):
    wiersze = []
    for pom in zakres1:
        wiersze.append([])
    for i in zakres1:
        for j in zakres1:
            wiersze[i].append([i, j])
    return wiersze


def produkujemy_kolumny(zakres1):
    kolumny = []
    for pom in zakres1:
        kolumny.append([])
    for j in zakres1:
        for i in zakres1:
            kolumny[j].append([i, j])
    return kolumny

def iloczyn_zbiorow(zbior_1,zbior_2):
    il_zb = []
    for x in zbior_1:
        if x in zbior_2:
            il_zb.append(x)
    return il_zb

def wykres_par(pary):
    # pary to lista list, np. pary = [[1,2],[2,-7],...]

    import matplotlib.pyplot as plt
    # def KOLOR(pom):
    #     if pom % 2 == 0:
    #         return 'r'
    #     else:
    #         return '#4CAF50'

    iksy = []
    igreki = []

    for pom in pary:
        iksy.append(pom[0])
        igreki.append(pom[1])

    plt.plot(iksy,igreki,marker = 'o',ms = 3,mec = '#4CAF50',mfc = 'r')   #linia
#    plt.scatter(iksy,igreki)#,marker = 'o',ms = 3)  #punkty

    plt.grid()
    plt.show()

def otoczenie(x,y):
    return [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]

def otoczenie_pelne(x,y):
    return [[x-1,y],[x+1,y],[x,y-1],[x,y+1],[x-1,y-1],[x+1,y-1],[x-1,y+1],[x+1,y+1]]

# def odleglosc_2_punktow():
