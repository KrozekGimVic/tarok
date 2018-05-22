def doloci_karto(index):							#   vrne opis karte: (jetarok, katerabarva, index)
	if(index>32):								   #   jetarok je 1 če je karta tarok, drugače pa 0
		return 1, 0, index-32					   #   katerabarva določi barvo s števili od 1 do 4
	barva=int(index/8)+1							#   "index" ti pove številko taroka (škis je 22) ali pa moč barve (1 je najmanjši platelc, 8 pa kralj)
	index=index%8
	if(index==0):
		index+=8
	return 0, barva, index

class Miza():

	def __init__(self):
		self.tarok = list()
		self.barva = list()
		self.index = list()
		self.karte = list()
		self.klican = 0
		self.stkart = 0

	def add(self, karta):
		if self.stkart == 0:
			self.karte.clear()
		self.karte.append(karta)
		self.tarok.append(0)
		self.barva.append(0)
		self.index.append(0)
		self.tarok[self.stkart], self.barva[self.stkart], self.index[self.stkart] = doloci_karto(karta)
		self.stkart += 1

	def klici(self, kralj):
		self.klican = kralj

	def stih(self):
		if self.tarok.count(1)>0:
			zmaga = -1
			maks = 0
			for i in range(0, self.stkart):
				if self.tarok[i]==1 and self.index[i]>maks:
					maks=self.index[i]
					zmaga=i
			self.rm()
			return zmaga
		topbarva=self.barva[0]
		maks=self.index[0]
		zmaga=0
		for i in range(1, self.stkart):
			if self.barva[i]==topbarva and self.index[i]>maks:
				maks=self.index[i]
				zmaga=i
		self.rm()
		return zmaga

	def rm(self):
		self.stkart = 0
		self.tarok.clear()
		self.barva.clear()
		self.index.clear()

	def daj(self):
		return self.karte

	def razjasnitev(self, igralec):
		if self.klican!=0:
			for i in range(0, 4):
				if self.karte[i] == self.klican:
					slepar=i%4
					self.klican = 0
					return slepar
			return -1
		else:
			return -1