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
		
		self.txt = ['dvoje', 'troje', 'štiri']
		h_boxes = QtWidgets.QHBoxLayout()
		l = QtWidgets.QLabel('       ')

		h_boxes.addWidget(l)

		l_box = QtWidgets.QVBoxLayout()
		r_box = QtWidgets.QVBoxLayout()

		self.PlayButtons = list()
		for i in range(0, 3):
			self.PlayButtons.append(QtWidgets.QPushButton("Igra v %s" % self.txt[i]))
			self.PlayButtons[i].clicked.connect(self.Play_game)
			l_box.addStretch()
			l_box.addWidget(self.PlayButtons[i])

		self.b_restart = QtWidgets.QPushButton('Ponastavi igro')
		self.b_restart.clicked.connect(self.Ponastavi)

		r_box.addStretch()
		r_box.addWidget(self.b_restart)
		
		for i in range(0, 5):
			l_box.addStretch()
		
		h_boxes.addLayout(l_box)
		h_boxes.addStretch()
		h_boxes.addLayout(r_box)

		self.setLayout(h_boxes)

	def Ponastavi(self):
		self.game_started = 0

	def Play_game(self, i):
		if self.game_started == 0:
			sender = self.sender()
			for i in range(0, 3):
				if sender.text().find(self.txt[i]) > 0:
					stigralcev = i+2
					break
			print(stigralcev)
			self.game_started = 1

	def clearLayout(self):
		while self.count():
			child = self.takeAt(0)
			if child.widget():
				child.widget().deleteLater()

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.Start_game()
sys.exit(app.exec_())