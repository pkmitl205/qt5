import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class main(QDialog):
    def __init__(self):
        super(main, self).__init__()
        loadUi('main.ui', self)
        self.setWindowTitle('pyQt5 GUI')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label_2.setText('Welcome : '+self.lineEdit.text()+' '+self.lineEdit_2.text())

app=QApplication(sys.argv)
widget=main()
widget.show()
sys.exit(app.exec_())