import heapq
import math

# Marcin Puwalski ISINS 4 rok 7 semrestr

class Punkt:
    def __init__(self, wspolrzedne, wartosc):
        self.wspolrzedne = wspolrzedne
        self.wartosc = wartosc
        self.heurystyka = 0.0
        self.wynik = 9999
        self.skad = None

def Mahnattan(punkt1, punkt2):
    x1, y1 = punkt1
    x2, y2 = punkt2
    return abs(x2 - x1) + abs(y2 - y1)

def Euklides(punkt1, punkt2):
    x1, y1 = punkt1
    x2, y2 = punkt2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def Zaladuj(Mapa):
    zPliku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
        [5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 5, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    zPliku = zPliku[::-1]
    for y in range(0, 20):
        wiersz = []
        for x in range(0, 20):
            biezacyPunkt = Punkt((x, y), zPliku[y][x])
            wiersz.append(biezacyPunkt)
        Mapa.append(wiersz)


def OdbudujSciezke(Mapa, poczatek, koniec):
    wynik = []
    while not (koniec[0] == poczatek[0] and koniec[1] == poczatek[1]):
        wynik.append(koniec)
        koniec = Mapa[koniec[1]][koniec[0]].skad
    wynik.append(poczatek)
    while len(wynik) > 0:
        biezacy = wynik.pop()
        Mapa[biezacy[1]][biezacy[0]].wartosc = 3


def AGwiazdka(Mapa, poczatek, koniec):
    kolejka = []
    Mapa[poczatek[1]][poczatek[0]].biezacyWynik = 0
    Mapa[poczatek[1]][poczatek[0]].wartosc = 1
    heapq.heappush(kolejka, (99999, poczatek))

    while len(kolejka) > 0:
        elementZKolejki = heapq.heappop(kolejka)
        biezacyX, biezacyY = elementZKolejki[1]
        Mapa[biezacyY][biezacyX].wartosc = 2
        if biezacyY == koniec[1] and biezacyX == koniec[0]:
            OdbudujSciezke(Mapa, poczatek, koniec)
            return

        dozwoloneRuchy = []
        if biezacyY > 0 and Mapa[biezacyY - 1][biezacyX].wartosc != 5:
            dozwoloneRuchy.append((biezacyX, biezacyY - 1))
        if biezacyY < 19 and Mapa[biezacyY + 1][biezacyX].wartosc != 5:
            dozwoloneRuchy.append((biezacyX, biezacyY + 1))
        if biezacyX > 0 and Mapa[biezacyY][biezacyX - 1].wartosc != 5:
            dozwoloneRuchy.append((biezacyX - 1, biezacyY))
        if biezacyX < 19 and Mapa[biezacyY][biezacyX + 1].wartosc != 5:
            dozwoloneRuchy.append((biezacyX + 1, biezacyY))

        for (ruchX, ruchY) in dozwoloneRuchy:
            biezacyPunkt = Mapa[biezacyY][biezacyX]
            docelowyPunkt = Mapa[ruchY][ruchX]
            if docelowyPunkt.wartosc == 2:
                continue

            spodziewanyWynik = biezacyPunkt.biezacyWynik + 1.0
            if docelowyPunkt.wartosc == 0 or (docelowyPunkt.wartosc == 1 and spodziewanyWynik < docelowyPunkt.biezacyWynik):
                docelowyPunkt.wartosc = 1
                docelowyPunkt.heurystyka = Euklides(
                    docelowyPunkt.wspolrzedne, koniec)
                docelowyPunkt.skad = (biezacyX, biezacyY)
                docelowyPunkt.biezacyWynik = spodziewanyWynik
                heapq.heappush(kolejka, (docelowyPunkt.biezacyWynik +
                                         docelowyPunkt.heurystyka, docelowyPunkt.wspolrzedne))

    print("Nie ma ścieżki z początku do końca na tej planszy\n")


def Wypisz(Mapa):
    for y in range(0, 20):
        for x in range(0, 20):
            if Mapa[19-y][x].wartosc == 5:
                print("#", end=" ")
            elif Mapa[19-y][x].wartosc == 3:
                print("o", end=" ")
            else:
                print(".", end=" ")
        print("\n", end="")
    print("\n", end="")


if __name__ == "__main__":
    Mapa = []
    Zaladuj(Mapa)
    print("Przed działaniem algorytmu")
    Wypisz(Mapa)
    print("Algorytm")
    AGwiazdka(Mapa, poczatek=(0, 0), koniec=(19, 19))
    print("Po wykonaniu algorytmu")
    Wypisz(Mapa)
