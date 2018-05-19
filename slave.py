import sys
import subprocess
from PyQt5 import QtWidgets, QtGui
from Player import Player
from Talon import Talon

class Window(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()

		self.game_started = 0

		self.Gui_startup()

	def Velikost(self):
		cmd = ['xrandr']
		cmd2 = ['grep', '*']
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
		p.stdout.close()
		 
		resolution_string, junk = p2.communicate()
		resolution = resolution_string.split()[0]
		resolution = str(resolution)
		width, height = resolution.split("x")
		width = width[2:]
		width = int(width)
		height, a = height.split("'")
		height = int(height)

		self.setGeometry(0, 0, width, height)
		
	def Gui_startup(self):
		self.Velikost()
		self.show()


	def Start_game(self):
		self.b_v_dvoje = QtWidgets.QPushButton('Igra v dvoje')
		self.b_v_troje = QtWidgets.QPushButton('Igra v troje')
		self.b_v_stiri = QtWidgets.QPushButton('Igra v štiri')
		self.b_restart = QtWidgets.QPushButton('Ponastavi igro')

		self.b_v_dvoje.clicked.connect(self.V_dvoje)
		self.b_v_troje.clicked.connect(self.V_troje)
		self.b_v_stiri.clicked.connect(self.V_stiri)
		self.b_restart.clicked.connect(self.Ponastavi)

		h_boxes = QtWidgets.QHBoxLayout()
		l = QtWidgets.QLabel('       ')

		h_boxes.addWidget(l)

		l_box = QtWidgets.QVBoxLayout()
		r_box = QtWidgets.QVBoxLayout()

		r_box.addStretch()
		r_box.addWidget(self.b_restart)

		l_box.addStretch()
		l_box.addWidget(self.b_v_dvoje)
		l_box.addStretch()
		l_box.addWidget(self.b_v_troje)
		l_box.addStretch()
		l_box.addWidget(self.b_v_stiri)
		l_box.addStretch()
		l_box.addStretch()
		l_box.addStretch()
		l_box.addStretch()
		l_box.addStretch()
		l_box.addStretch()
		
		h_boxes.addLayout(l_box)
		h_boxes.addStretch()
		h_boxes.addLayout(r_box)

		self.setLayout(h_boxes)

	def Ponastavi(self):
		self.game_started = 0

	def V_dvoje(self):
		if self.game_started == 0:
			self.game_started = 1
			self.Play_game(2)

	def V_troje(self):
		if self.game_started == 0:
			self.game_started = 1
			self.Play_game(3)

	def V_stiri(self):
		if self.game_started == 0:
			self.game_started = 1
			self.Play_game(4)

	def Play_game(self, stigralcev):
		print(stigralcev)

	def clearLayout(self):
		while self.count():
			child = self.takeAt(0)
			if child.widget():
				child.widget().deleteLater()

	'''def changelayout(self):
		self.clearLayout()
		neki = QtWidgets.QLabel('neki')
		nek = QtWidgets.QHBoxLayout()
		nek.addStretch()
		nek.addWidget(neki)
		nek.addStretch()
		self.setLayout(nek)'''

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.Start_game()
a = input()
#window.changelayout()
sys.exit(app.exec_())