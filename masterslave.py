import random
from Player import Player
from Talon import Talon
from Miza import Miza

def prinall():									  #   izpiše stanje vseh igralcev in talona
	'''for i in range(0, 12):
		for j in range(0, 4):
			players[j].prin(i)'''
	for i in range(0, 4):
		players[i].prink()
	print()
	talon.prin()

def razdeli(stigralcev):							#   razdeli karte med igralce in talon

	#karte=random.sample(range(1, 55), 54)
	karte=range(1, 55)
	for i in range (0, 6):
		talon.dodaj(karte[i])

	for i in range (0, 2):
		for j in range(0, stigralcev):
			for k in range(int(6+i*24+j*24/stigralcev), int(6+i*24+(j+1)*24/stigralcev)):
				players[j].add(karte[k])

def vrstaigre(stigralcev):						  #   vrne tip igre, ki se ga bo igralo in igralca, ki je šel igrat v obliki (igralec, igra)
	igre=[0, 0, 0, 0]							   #   če nihče ne gre igrat nič vrne (0, 0)
	runde=0
	vote=1
	najvisjaigra=0
	igralec=-1
	while 1:										#   dokler ni jasno kdo bo šel igrat (vsi ali en igralec manj imajo tip igre enak 0)
		for i in range (0, stigralcev):
			if igre[i]!=0 or runde==0:
				if i!=igralec:
					print(i+1)
					igre[i]=int(input())			#   igralec gre lahko igrati, če viša igro ali je na vrsti pred tistim, ki ima trenutno najvišjo igro in mu jo izenači
					if najvisjaigra<igre[i] or (najvisjaigra==igre[i] and i<igralec):
						najvisjaigra=igre[i]
						igralec=i
					else:
						igre[i]=0
		if igre.count(0)==3:						#   1 igralec ima veljavno igro in gre igrat
			print(igralec)
			k=int(input())
			if k>najvisjaigra:					  #   svojo igro lahko še viša
				najvisjaigra=k
			return igralec+1, najvisjaigra
		if igre.count(0)==4:						#   nihče ni šel igrat, igralo se bo klopa
			return 0, 0
		print(igre)
		runde+=1
	
def klici(stigralcev, najvisjaigra, igralec):
	if stigralcev==4 and najvisjaigra<4:			#   pri ne-solo-igri v štiri vpraša igralca, ki je šel igrat katerega kralja bo klical 
		kralji = ["karo", "kriz", "pik", "src"]
		print(igralec, "kralj")
		a = input()
		#   print(a)
		for i in range(0, 3):
			if(a.lower()==kralji[i]):
				return (i+1)*8
	else:
		return 0									#   vrne 0, če v igri sodelujeta 2 ali 3 igralci ali pa je igra solo

def igra(stigralcev, kralj, igralec):			   #   "odsimulira" igro za število igralcev (stigralcev):
	miza = Miza()
	miza.klici(kralj)
	zacne = 0
	ubozca = list()
	for i in range(0, int(48/stigralcev)):			 #   48/stigralcev je število rund
		for j in range(0, stigralcev):
			print((zacne+j)%stigralcev)
			st=int(input())
			while players[(zacne+j)%stigralcev].vrzi(st)==0:
				#print((zacne+j)%stigralcev, players[(zacne+j)%stigralcev].prink())
				st=int(input())
			print("add", st)
			miza.add(st)

		slepar = miza.razjasnitev(igralec)
		if slepar > -1 and slepar < 4:
			prinall()
			print(slepar, igralec)
			a = players[slepar].dodaj_partnerja(igralec)
			players[igralec].poberi(a)
			for k in range(0, 4):
				if k!=slepar and k!=igralec:
					ubozca.append(k)
			players[ubozca[1]].poberi(players[ubozca[0]].dodaj_partnerja(ubozca[1]))
			players[ubozca[1]].poberi(talon.daj_ostank())
			ubozca.append(igralec)
			ubozca.append(slepar)

		zacne += miza.stih()						#   dobi karte po vrsti, kot so padale in vrne igralca, ki je pobral štih
		zacne = zacne % stigralcev
		print("zacne", zacne)
		par = players[zacne].poberi(miza.daj())
		if par != 0:
			players[par].poberi(miza.daj())
	return ubozca

def prin_rezultat(ubozci):
	print("Rezultat je:")
	print("igralec ", ubozci[2], " je z igralcem ", ubozci[3], " dosegel ", players[ubozci[2]].sestevk(), " tock.")
	print("igralec ", ubozci[0], " je z igralcem ", ubozci[1], " dosegel ", players[ubozci[1]].sestevk(), " tock.")
	if players[ubozci[1]].sestevk()>players[ubozci[2]].sestevk():
		print("Zmagala sta ", ubozci[0], " in ", ubozci[1], ".")
	else:
		print("Zmagala sta ", ubozci[2], " in ", ubozci[3], ".")

stigralcev = int(input())						   #   dobi število igralcev, ki bodo igrali

players = [Player()]								#   ustvari toliko objektov Player()

for i in range(1, stigralcev):
	players.append(Player())

talon = Talon()									 #   ustvari talon

razdeli(stigralcev)								 #   razdeli karte
prinall()
igralec, najvisjaigra = vrstaigre(stigralcev)	   #   ugotovi tip igre
print(igralec)

kralj = klici(stigralcev, najvisjaigra, igralec)	#   vpraša tistega igralca, ki gre igrat v katerem kralju gre igrat 

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

ubozci = igra(stigralcev, kralj, igralec)		   #   odsimulira igro

#prinall()
prin_rezultat(ubozci)
