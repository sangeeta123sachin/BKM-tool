import sys
#from bkmMain import *
from bkmCheckInformation import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class bkmCheckInformation( Ui_mainWindow):
    def __init__(self):

        self.ChildWindow = QtGui.QMainWindow()
        super().setupUi(self.ChildWindow)

        self.QuitButton.clicked.connect(self.ButtonClicked)
        self.ChildWindow.show()


    def ButtonClicked(self):
        self.emit(SIGNAL("closed()"))






if __name__ == '__main__':
    app = QtGui.QApplication([])
    bkmCheckInformation()
    app.exec_()




