class Talon():                                      #   objekt za držanje talona

    def __init__(self):
        self.karte = list()
        self.ostank = list()

    def dodaj(self, karta):                         #   pri razdeljevanju prejme karte in jih shrani v karte
        self.karte.append(karta)

    def odpri(self, stkupckov, igralec):            #   razdeli karte na kupčke in jih poda igralcem
        kupcki = [list()]
        for i in range (0, int(stkupckov)):
            for j in range(0, int(6/stkupckov)):
                print(self.karte[0])
                kupcki[i].append(self.karte.pop(0))
            kupcki.append(list())
            print()
        kupcki.pop(6)
        kupck = int(input())                        #   igralcu da kupček, ki si ga izbere in da ostanek v "ostank"
        for i in range(0, len(kupcki)):
            if i!=kupck:
                self.ostank.extend(kupcki[i])
        return kupcki[kupck], 6-len(self.ostank)

    def daj_ostank(self):
        ostanek = self.ostank.copy()
        self.ostank.clear()
        return ostanek

    def prin(self):
        print(self.karte)
        print(self.ostank)