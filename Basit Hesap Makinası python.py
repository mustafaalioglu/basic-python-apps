import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Hesap Makinasi")
        self.setGeometry(200,200,600,600)
        self.initUI()
        
    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText("Sayi 1: ")
        self.lbl_num1.move(50,30)
        
        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText("Sayi 2: ")
        self.lbl_num2.move(50,70)
        
        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(150,30)
        self.txt_num1.resize(200,32)
        
        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(150,70)
        self.txt_num2.resize(200,32)
        
        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150,110)
        self.btn_topla.clicked.connect(self.hesapla)
        
        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çikar")
        self.btn_cikar.move(150,140)
        self.btn_cikar.clicked.connect(self.hesapla)
        
        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText("Çarp")
        self.btn_carp.move(150,170)
        self.btn_carp.clicked.connect(self.hesapla)
        
        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText("Böl")
        self.btn_bol.move(150,200)
        self.btn_bol.clicked.connect(self.hesapla)
        
        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("Sonuç: ")
        self.lbl_sonuc.move(150,230)
        
    def hesapla(self):
        sender = self.sender().text()
        if sender == "Topla":
            result = int(self.txt_num1.text()) + int(self.txt_num2.text())
        elif sender == "Çikar":
            result = int(self.txt_num1.text()) - int(self.txt_num2.text())
        elif sender == "Çarp":
            result = int(self.txt_num1.text()) * int(self.txt_num2.text())
        elif sender == "Böl":
            result = int(self.txt_num1.text()) / int(self.txt_num2.text())
                
        self.lbl_sonuc.setText("Sonuç: "+str(int(result)))
        
def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    
app()