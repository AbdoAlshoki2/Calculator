import ctypes
from email.charset import QP
from sys                  import(argv, exit)
from PyQt5.QtWidgets      import(QGridLayout, QFrame, QLabel, QPushButton, QLineEdit)
from PyQt5.Qt             import(QApplication, QMainWindow)
from PyQt5.QtGui          import(QFont)


class CALCULATOR(QMainWindow):

	def __init__(self, Developer):
		QMainWindow.__init__(self)

		self.Developer = Developer

		self.screen_width  = ctypes.windll.user32.GetSystemMetrics(0)
		self.screen_height = ctypes.windll.user32.GetSystemMetrics(1)
		self.width  = 500
		self.height = 600

		self.setWindowTitle('Calculator')
		self.setGeometry(int((self.screen_width-self.width)/2),
                         int((self.screen_height-self.height)/2),
                         self.width,
                         self.height)
		self.setFixedSize(self.width, self.height)


		self.GUI()
		self.Connect()


	def GUI(self):
		self.frame = QFrame(self)
		self.frame.setFixedSize(self.width, self.height)
		self.grid = QGridLayout(self.frame)

		self.Box = QLineEdit(self)
		self.Box.setFixedSize(self.width-20,30)
		self.Box.setReadOnly(True)
		self.Box.setFont(QFont('Arial',16))
		self.grid.addWidget(self.Box,0,0,1,4)

		self.Result = QLabel(self)
		self.Result.setText('Result here!')
		self.Result.setFixedSize(self.width-20,30)
		self.Result.setFont(QFont('Arial',18))
		self.grid.addWidget(self.Result,1,0,1,3)

		self.B0 = QPushButton('0')
		self.B1 = QPushButton('1')
		self.B2 = QPushButton('2')
		self.B3 = QPushButton('3')
		self.B4 = QPushButton('4')
		self.B5 = QPushButton('5')
		self.B6 = QPushButton('6')
		self.B7 = QPushButton('7')
		self.B8 = QPushButton('8')
		self.B9 = QPushButton('9')

		self.Badd = QPushButton('+')
		self.Bsub = QPushButton('-')
		self.Bmul = QPushButton('×')
		self.Bdiv = QPushButton('÷')

		self.Beq  = QPushButton('=')

		self.Bdel = QPushButton('Delete')

		self.grid.addWidget(self.B0,5,0)
		self.grid.addWidget(self.B1,4,0)
		self.grid.addWidget(self.B2,4,1)
		self.grid.addWidget(self.B3,4,2)
		self.grid.addWidget(self.B4,3,0)
		self.grid.addWidget(self.B5,3,1)
		self.grid.addWidget(self.B6,3,2)
		self.grid.addWidget(self.B7,2,0)
		self.grid.addWidget(self.B8,2,1)
		self.grid.addWidget(self.B9,2,2)

		self.grid.addWidget(self.Badd,5,3)
		self.grid.addWidget(self.Bsub,4,3)
		self.grid.addWidget(self.Bmul,3,3)
		self.grid.addWidget(self.Bdiv,2,3)

		self.grid.addWidget(self.Beq ,5,1,1,2)

		self.grid.addWidget(self.Bdel,1,3)


		for i in self.frame.children():
			if type(i) != QPushButton: continue
			i.setFixedSize(int((self.width-60)/4),int((self.height-160)/4))
			i.setFont(QFont('Arial',20))
		
		self.Beq .setFixedSize(int((self.width-60)/2+10),int((self.height-160)/4))
		self.Bdel.setFixedSize(int((self.width-60)/4),30)
		self.Bdel.setFont(QFont('Arial',16))


	def Connect(self):
		self.B0.clicked.connect(lambda: self.Write('0'))
		self.B1.clicked.connect(lambda: self.Write('1'))
		self.B2.clicked.connect(lambda: self.Write('2'))
		self.B3.clicked.connect(lambda: self.Write('3'))
		self.B4.clicked.connect(lambda: self.Write('4'))
		self.B5.clicked.connect(lambda: self.Write('5'))
		self.B6.clicked.connect(lambda: self.Write('6'))
		self.B7.clicked.connect(lambda: self.Write('7'))
		self.B8.clicked.connect(lambda: self.Write('8'))
		self.B9.clicked.connect(lambda: self.Write('9'))

		self.Badd.clicked.connect(lambda: self.Write_Symbol('+'))
		self.Bsub.clicked.connect(lambda: self.Write_Symbol('-'))
		self.Bmul.clicked.connect(lambda: self.Write_Symbol('×'))
		self.Bdiv.clicked.connect(lambda: self.Write_Symbol('÷'))
		
		self.Beq .clicked.connect(lambda: self.Equal ())
		self.Bdel.clicked.connect(lambda: self.Delete())



	def Write(self, num):
		self.Box.setText(self.Box.text()+num)
	

	def Write_Symbol(self , symbol):
		if self.Box.text()[-1].isdigit():
			self.Box.setText(self.Box.text()+symbol)
	

	def Equal(self):
		txt = self.Box.text()
		
		if txt == '':return
		if not txt[-1].isdigit(): return
		
		txt = txt.replace('×','*')
		txt = txt.replace('÷','/')
		
		result = eval(str(txt))
		self.Result.setText(str(result))
	

	def Delete(self):
		txt = self.Box.text()
		txt = txt[0:-1]
		self.Box.setText(txt)





root = QApplication(argv)
root.setStyle('Fusion')

MyCalculator = CALCULATOR("Abdo Alshoki")
MyCalculator.show()

exit(root.exec_())









#	Alshoki - Omar 19