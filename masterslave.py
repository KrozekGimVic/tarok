import random
from Player import Player
from Talon import Talon


def doloci_karto(index):                            #   vrne opis karte: (jetarok, katerabarva, index)
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

    karte=random.sample(range(1, 55), 54)
    #karte=range(1, 55)
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
    
def klici(stigralcev, najvisjaigra, igralec):
    if stigralcev==4 and najvisjaigra<4:            #   pri ne-solo-igri v štiri vpraša igralca, ki je šel igrat katerega kralja bo klical 
        kralji = ["karo", "kriz", "pik", "src"]
        print(igralec, "kralj")
        a = input()
        #   print(a)
        for i in range(0, 3):
            if(a.lower()==kralji[i]):
                return (i+1)*8
    else:
        return 0                                    #   vrne 0, če v igri sodelujeta 2 ali 3 igralci ali pa je igra solo

def stih(miza, stigralcev):                         #   dobi karte po vrsti, kot so padale in vrne igralca, ki je pobral štih 
    tarok = list()
    barva = list()
    index = list()
    for miza in miza:
        a, b, c = doloci_karto(miza)
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

def igra(stigralcev, kralj, igralec):               #   "odsimulira" igro za število igralcev (stigralcev):
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
        if stigralcev==4:    
            for j in range(0, 4):
                if miza[j]==kralj:
                    slepar=(j+zacne)%4
                    players[igralec].poberi(players[slepar].dodaj_partnerja(igralec))
                    ubozca = list()
                    for k in range(0, 4):
                        if k!=slepar and k!=igralec:
                            ubozca.append(k)
                    players[ubozca[1]].poberi(players[ubozca[0]].dodaj_partnerja(ubozca[1]))
                    players[ubozca[1]].poberi(talon.daj_ostank())

        zacne += stih(miza, stigralcev)
        zacne = zacne % stigralcev
        par = players[zacne].poberi(miza)
        if par != 0:
            players[par].poberi(miza)
    ubozca.append(igralec)
    ubozca.append(slepar)
    return ubozca

def prin_rezultat(ubozci):
    print("Rezultat je:")
    print("igralec ", ubozci[2], " je z igralcem ", ubozci[3], " dosegel ", players[ubozci[2]].sestevk(), " tock.")
    print("igralec ", ubozci[0], " je z igralcem ", ubozci[1], " dosegel ", players[ubozci[1]].sestevk(), " tock.")
    if players[ubozci[1]].sestevk()>players[ubozci[2]].sestevk():
        print("Zmagala sta ", ubozci[0], " in ", ubozci[1], ".")
    else:
        print("Zmagala sta ", ubozci[2], " in ", ubozci[3], ".")

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
    kupck, stkart = talon.odpri(stkupckov, igralec) #   mu pokaže talon
    for karta in kupck:
        players[igralec].add(karta)
    players[igralec].zalozi(stkart, igralec)

print(najvisjaigra)

ubozci = igra(stigralcev, kralj, igralec)           #   odsimulira igro

#prinall()
prin_rezultat(ubozci)
