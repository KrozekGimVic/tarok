import random

def vrednost(index):                                #   returns the number of points of the card with the index "index", counted at the end of the game
                                                    #   vrne vrednost karte z indeksom "index", kot je računan na koncu igre
    if index==33 or index==54 or index==53:         #   pagat, škis in mond, ki so vredni 5 točk
        return 5
    if index>32:                                    #   vsi ostali taroki
        return 1
    index%=8                                        #   index postane index barvne karte
    if index==0:
        index+=8
    if index>4:                                     #   8 je kralj, 7 dama, 6 kaval, 5 pob -> če odštejemo 3 dobimo njihovo vrednost
        return index-3
    return 1                                        #   platelci vredni 1 točko



class Player():                                     #   objekt za igralce
    
    def __init__(self):
        self.karte = list()                         #   karte na roki igralca
        self.kup = list()                           #   kup pobranih kart
    
    def add(self, karta):
        self.karte.append(karta)                    #   dobivanje kart pri razdeljevanju 

    def vrzi(self, karta):                          #   odmetavanje kart med igro
        if(self.karte.count(karta)>0):              #   vrne 1, če igralec to karto ima in 0, če je nima
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

    def poberi(self, mizo):                         #   na svoj kup doda vse karte, ki so bile na mizi
        for i in range(0, len(mizo)):
            self.kup.append(vrednost(mizo[i]))

    def sestevk(self):                              #   sešteje vrednost svojih kart
        if len(self.kup)%3==0:
            return sum([i for i in self.kup]) - int(len(self.kup)/3)*2
        return sum([i for i in self.kup]) - int(len(self.kup)/3)*2 -1

    def zalozi(self, stkart, igralec):              #   založi podane karte in vrne tiste, ki jih igralec ni imel
        i=0
        while i<stkart:
            print(igralec)
            karta = int(input())
            if self.vrzi(karta)==1:
                self.kup.append(karta)
            i+=1



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
        print(kupcki)
        kupck = int(input())                        #   igralcu da kupček, ki si ga izbere in da ostanek v "ostank"
        for karta in kupcki[kupck]:
            players[igralec].add(karta)
        kupcki.pop(kupck)
        for kupcki in kupcki:
            self.ostank.extend(kupcki)
        players[igralec].zalozi(6-len(self.ostank), igralec)

    def prin(self):
        print(self.karte)
        print(self.ostank)

def karta(index):                                   #   vrne opis karte: (jetarok, katerabarva, index)
    if(index>32):                                   #   jetarok je 1 če je karta tarok, drugače pa 0
        return 1, 0, index-32                       #   katerabarva določi barvo s števili od 1 do 4
    barva=int(index/8)+1                            #   "index" ti pove številko taroka (škis je 22) ali pa moč barve (1 je najmanjši platelc, 8 pa kralj)
    index=index%8
    if(index==0):
        index+=8
    return 0, barva, index

def prinall():                                      #   izpiše stanje vseh igralcev in talona
    i=0
    for Player in players:
        players[i].prin()
        i+=1
    print()
    talon.prin()

def razdeli(stigralcev):                            #   razdeli karte med igralce in talonu

    #karte=random.sample(range(1, 55), 54)
    karte=range(1, 55)
    for i in range (0, 6):
        talon.dodaj(karte[i])

    for i in range (0, 2):
        for j in range(0, stigralcev):
            for k in range(int(6+i*24+j*24/stigralcev), int(6+i*24+(j+1)*24/stigralcev)):
                players[j].add(karte[k])

def vrstaigre(stigralcev):                          #   vrne tip igre, ki se ga bo igralo in igralca, ki je šel igrat v obliki (igralec, igra)
    igre=[0, 0, 0, 0]                               #   če nihče ne gre igrat nič vrne (0, 0)
    runde=0
    vote=1
    najvisjaigra=0
    igralec=-1
    while 1:                                        #   dokler ni jasno kdo bo šel igrat (vsi ali en igralec manj imajo tip igre enak 0)
        for i in range (0, stigralcev):
            if igre[i]!=0 or runde==0:
                if i!=igralec:
                    print(i+1)
                    igre[i]=int(input())            #   igralec gre lahko igrati, če viša igro ali je na vrsti pred tistim, ki ima trenutno najvišjo igro in mu jo izenači
                    if najvisjaigra<igre[i] or (najvisjaigra==igre[i] and i<igralec):
                        najvisjaigra=igre[i]
                        igralec=i
                    else:
                        igre[i]=0
        if igre.count(0)==3:                        #   1 igralec ima veljavno igro in gre igrat
            print(igralec)
            k=int(input())
            if k>najvisjaigra:                      #   svojo igro lahko še viša
                najvisjaigra=k
            return igralec+1, najvisjaigra
        if igre.count(0)==4:                        #   nihče ni šel igrat, igralo se bo klopa
            return 0, 0
        print(igre)
        runde+=1
        #print(stigralcev)
        #print(igre.count(0))
    
def klici(stigralcev, najvisjaigra, igralec):
    if stigralcev==4 and najvisjaigra<4:            #   pri ne-solo-igri v štiri vpraša igralca, ki je šel igrat katerega kralja bo klical 
        kralji = ["kriz", "pik", "src", "karo"]
        print(igralec, "kralj")
        a = input()
        #   print(a)
        for i in range(0, 3):
            if(a.lower()==kralji[i]):
                return i+1
    else:
        return 0                                    #   vrne 0, če v igri sodelujeta 2 ali 3 igralci ali pa je igra solo

def stih(miza, stigralcev):                         #   dobi karte po vrsti, kot so padale in vrne igralca, ki je pobral štih 
    tarok = list()
    barva = list()
    index = list()
    for miza in miza:
        a, b, c = karta(miza)
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

def igra(stigralcev):                               #   "odsimulira" igro za število igralcev (stigralcev):
    for i in range(0, int(48/stigralcev)):          #   48/stigralcev je število rund
        miza = list()
        zacne = 0
        for j in range(zacne, zacne+stigralcev):
            print((zacne+j)%stigralcev+1)
            st=int(input())
            while players[(zacne+j)%stigralcev].vrzi(st)==0:
                print(j+1)
                st=int(input())
            print(st)
            miza.append(st)
        zacne += stih(miza, stigralcev)
        zacne = zacne % stigralcev
        players[zacne].poberi(miza)

stigralcev = int(input())                           #   dobi število igralcev, ki bodo igrali

players = [Player()]                                #   ustvari toliko objektov Player()

for i in range(1, stigralcev):
    players.append(Player())

talon = Talon()                                     #   ustvari talon

razdeli(stigralcev)                                 #   razdeli karte
#prinall()
igralec, najvisjaigra = vrstaigre(stigralcev)       #   ugotovi tip igre
print(igralec)

kralj = klici(stigralcev, najvisjaigra, igralec)    #   vpraša tistega igralca, ki gre igrat v katerem kralju gre igrat 

if najvisjaigra<7:
    stkupckov = najvisjaigra%3
    if stkupckov==0:
        stkupckov=3
    stkupckov = 4 - stkupckov
    stkupckov = int(6/stkupckov)
    talon.odpri(stkupckov, igralec)                 #   mu pokaže talon

print(najvisjaigra)

igra(stigralcev)                                    #   odsimulira igro

prinall()
