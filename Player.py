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
        self.partner = -1
    
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
        '''print("1.", self.kup.count(1))
        print("2.", self.kup.count(2))
        print("3.", self.kup.count(3))
        print("4.", self.kup.count(4))
        print("5.", self.kup.count(5))'''
        print("stkart", len(self.kup))
        print("vsota", self.sestevk())

    def poberi(self, mizo):                         #   na svoj kup doda vse karte, ki so bile na mizi
        if self.partner==-1:
            self.kup.extend(mizo)
            return 0
        else:
            return self.partner

    def dodaj(self, karte):
        self.kup.extend(karte)

    def sestevk(self):                              #   sešteje vrednost svojih kart
        if len(self.kup)%3==0:
            return sum([vrednost(i) for i in self.kup]) - int(len(self.kup)/3)*2
        return sum([vrednost(i) for i in self.kup]) - int(len(self.kup)/3)*2 -1

    def zalozi(self, stkart, igralec):              #   založi podane karte in vrne tiste, ki jih igralec ni imel
        i=0
        while i<stkart:
            print(igralec)
            karta = int(input())
            if self.vrzi(karta)==1:
                self.kup.append(karta)
            i+=1

    def dodaj_partnerja(self, partnr):
        bivsi_kup = self.kup.copy()
        self.kup.clear()
        self.partner = partnr
        return bivsi_kup