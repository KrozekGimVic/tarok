import random

class Game():    
    
    def razdelikarte(stigralcev):
        karte=random.sample(range(1, 55), 54)
        player = [list(), list(), list(), list()]
        #for i in range (0, 54):
         #   print(i, karte[i])
        talon = list()
        for i in range (0, 6):
            talon.append(karte[i])
            #for i in range(0, stigralcev) :
                #player[i].notify()
        for i in range (0, 2):
            for j in range(0, stigralcev):
                for k in range(int(6+i*24+j*24/stigralcev), int(6+i*24+(j+1)*24/stigralcev)):
                    player[j].append(karte[k])
                    #for n in range(0, stigralcev):
                        #if n!=j:
                            #player[n].notify(j)
        for i in range (0, stigralcev):
            print(player[i])
        print(talon)
    
    stigralcev=4
    
    def uprasajigralce(stigralcev):
        igre=[0, 0, 0, 0]
        runde=0
        vote=1
        while vote:
            for i in range (0, stigralcev):
                if any([igre[i]!=0, runde==0]):
                    print("a")
                    #giveallplayers(najvisjaigra)
                    #igre[i]=getanswer(player[i])
                    #if najvecjaigra<igre[i]:
                        #najvecjaigra=igre[i]
                        #igralec=i
                    #else:
                        #igre[i]=0
                    #if igre[i]==0:
                        #playerigra[i]=false
            runde+=1
            if(igre.count(0)==stigralcev-1):
                vote=0
        #if stigralcev==4:
            #askplayer[igralec] za kralja
    
    razdelikarte(stigralcev)
    
    uprasajigralce(stigralcev)
    
    '''najvisjaigra = 0
    igre=[0, 0, 0, 0]
    igreprej=igre
    igralec
    playerigra=[true, true, true, true]
    print(player1, player2, player3, player4, talon)
    
    if'''


#stigralcev=input()

Game()
