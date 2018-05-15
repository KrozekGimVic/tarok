import random

def vrednost(index):
    if index==33 or index==54 or index==53:
        return 5
    if index>32:
        return 1
    index%=8
    if index==0:
        index+=8
    if index>4:
        return index-3
    return 1

class Talon():

    def __init__(self):
        self.karte = list()

    def dodaj(self, karta):
        self.karte.append(karta)

    def razdeli(self, stkupckov):
        for i in range (0, int(stkupckov)):
            for j in range(0, int(6/stkupckov)):
                print(self.karte[0])
                self.karte.pop(0)
            print()

    def prin(self):
        print(self.karte)


class Player():    
    
    def __init__(self):
        self.karte = list()
        self.kup = list()
    
    def add(self, karta):
        self.karte.append(karta)

    def vrzi(self, karta):
        if(self.karte.count(karta)>0):
            self.karte.remove(karta)
            return 1
        else:
            return 0

    def prin(self):
        print(self.karte)
        print(self.kup)
        print("1.", self.kup.count(1))
        print("2.", self.kup.count(2))
        print("3.", self.kup.count(3))
        print("4.", self.kup.count(4))
        print("5.", self.kup.count(5))
        print("stkart", len(self.kup))
        print("vsota", self.sestevk())

    def poberi(self, mizo):
        for i in range(0, len(mizo)):
            self.kup.append(vrednost(mizo[i]))

    def sestevk(self):
        if len(self.kup)%3==0:
            return sum([i for i in self.kup]) - int(len(self.kup)/3)*2
        return sum([i for i in self.kup]) - int(len(self.kup)/3)*2 -1


def karta(index):
    if(index>32):
        return 1, 0, index-32
    barva=int(index/8)+1
    index=index%8
    if(index==0):
        index+=8
    return 0, barva, index

def prinall():
    '''for i in range(0, 12):
        player1.prin(i)
        player2.prin(i)
        player3.prin(i)
        player4.prin(i)'''
    player1.prin()
    player2.prin()
    player3.prin()
    player4.prin()
    talon.prin()

def razdeli(stigralcev):

    #karte=random.sample(range(1, 55), 54)
    karte=range(1, 55)
    for i in range (0, 6):
        talon.dodaj(karte[i])

    for i in range (0, 2):
        for j in range(0, stigralcev):
            for k in range(int(6+i*24+j*24/stigralcev), int(6+i*24+(j+1)*24/stigralcev)):
                if(j==0):
                   player1.add(karte[k])
                elif(j==1):
                    player2.add(karte[k])
                elif(j==2):
                    player3.add(karte[k])
                else:
                    player4.add(karte[k])

def vrstaigre(stigralcev):
    igre=[0, 0, 0, 0]
    runde=0
    vote=1
    najvecjaigra=0
    while vote:
        for i in range (0, stigralcev):
            if any([igre[i]!=0, runde==0]):
                print(i)
                igre[i]=int(input())
                if najvecjaigra<=igre[i]:
                    najvecjaigra=igre[i]
                    igralec=i
                else:
                    igre[i]=0
            if igre.count(0)==3 and runde>0:
                return igralec+1, najvecjaigra
            print(igre)
        runde+=1
        #print(stigralcev)
        #print(igre.count(0))
    
def klici(stigralcev):
    if(stigralcev==4):
        kralji = ["kriz", "pik", "src", "karo"]
        print(igralec, "kralj")
        a = input()
        #   print(a)
        for i in range(0, 3):
            if(a.lower()==kralji[i]):
                return i+1
    else:
        return 0

def stih(miza, stigralcev):
    tarok = list()
    barva = list()
    index = list()
    for i in range(0, stigralcev):
        a, b, c = karta(miza[i])
        tarok.append(a)
        barva.append(b)
        index.append(c)
    zmaga = -1
    maks = 0
    if tarok.count(1)>0:
        for i in range(0, stigralcev):
            if tarok[i]==1 and index[i]>maks:
                maks=index[i]
                zmaga=i
        return zmaga
    topbarva=barva[0]
    maks=index[0]
    zmaga=0
    for i in range(1, stigralcev):
        if barva[i]==topbarva and index[i]>maks:
            maks=index[i]
            zmaga=i
    return zmaga

def igra(stigralcev):
    for i in range(0, int(48/stigralcev)):
        miza = list()
        zacne = 0
        for j in range(zacne, zacne+stigralcev):
            if((j+zacne)%4==0):
                print(j+1)
                st=int(input())
                while player1.vrzi(st)==0:
                    print(j+1)
                    st=int(input())
                print(st)
                miza.append(st)
            elif((j+zacne)%4==1):
                print(j+1)
                st=int(input())
                while player2.vrzi(st)==0:
                    print(j+1)
                    st=int(input())
                print(st)
                miza.append(st)
            elif((j+zacne)%4==2):
                print(j+1)
                st=int(input())
                while player3.vrzi(st)==0:
                    print(j+1)
                    st=int(input())
                print(st)
                miza.append(st)
            else:
                print(j+1)
                st=int(input())
                while player4.vrzi(st)==0:
                    print(j+1)
                    st=int(input())
                print(st)
                miza.append(st)
        zacne = stih(miza, stigralcev)
        if zacne==0:
            player1.poberi(miza)
        elif zacne==1:
            player2.poberi(miza)
        elif zacne==2:
            player3.poberi(miza)
        elif zacne==3:
            player4.poberi(miza)


player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()
talon = Talon()

stigralcev = int(input())

razdeli(stigralcev)
#prinall()
igralec, najvecjaigra = vrstaigre(stigralcev)
print(igralec)

kralj = klici(stigralcev)

talon.razdeli(int(6/(4-najvecjaigra)))

print(najvecjaigra)

igra(stigralcev)

print(player1.sestevk())
print(player2.sestevk())
print(player3.sestevk())
print(player4.sestevk())
prinall()
