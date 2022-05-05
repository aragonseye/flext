#!/usr/bin/env python3


from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget,  QMenuBar, QMainWindow, QTextEdit
import sys


class mainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Pee Editor")
		self.resize(500,500)

		# menubar 

		#New file action
		newAction = QAction(QIcon('new.png'), '&New', self)
		newAction.setShortcut('Ctrl+N')
		newAction.setStatusTip('New Document')
		newAction.triggered.connect(self.newCall)

		# Open file action
		openAction = QAction(QIcon('open.png'), '&Open', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open File')
		openAction.triggered.connect(self.openCall)

		# exit application
		exitAction = QAction(QIcon('open.png'), '&Close', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit')
		exitAction.triggered.connect(self.exitCall)

		# File Menu
		mbar = self.menuBar()
		file = mbar.addMenu('&File')
		file.addAction(newAction)
		file.addAction(openAction)
		file.addAction(exitAction)


	def newCall(self):
		print('New')

	def openCall(self):
		print('Open')

	def exitCall(self):
		self.close()

class textBox():
	def __init__(self,target):

		t = QTextEdit(target)
		t.setFixedSize(500,500) 
		t.setTabStopDistance(8)
		t.setFont(QFont("Courier New", 18))
		t.setAcceptRichText(False)
		t.toPlainText()

app = QApplication(sys.argv)
w = mainWindow()
text = textBox(w)
w.show()
app.exec()
