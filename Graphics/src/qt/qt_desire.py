import sys
from PyQt4 import QtGui, QtCore
import cv2
import numpy as np



class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.color = QtGui.QColor(0, 0, 0)

        self.pictureInput = QtGui.QPushButton('图像导入', self)
        self.pictureInput.setCheckable(True)
        self.pictureInput.move(10, 10)

        self.connect(self.pictureInput, QtCore.SIGNAL('clicked()'), self.setAction)

        self.green = QtGui.QPushButton('Green', self)
        self.green.setCheckable(True)
        self.green.move(10, 60)

        self.connect(self.green, QtCore.SIGNAL('clicked()'), self.setAction)

        self.blue = QtGui.QPushButton('Blue', self)
        self.blue.setCheckable(True)
        self.blue.move(10, 110)

        self.connect(self.blue, QtCore.SIGNAL('clicked()'), self.setAction)


        self.statusBar().showMessage('Ready')
        self.square = QtGui.QWidget(self)
        self.square.setGeometry(150, 20, 400, 300)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.color.name())

        self.setWindowTitle('ToggleButton')
        self.setGeometry(300, 300, 560, 340)


    def setAction(self):

        source = self.sender()

        if source.text() == "图像导入":
            if self.pictureInput.isChecked():
                hbox = QtGui.QHBoxLayout(self)
                pixmap = QtGui.QPixmap('file/lotus.jpg')
                label = QtGui.QLabel(self)
                label.setPixmap(pixmap)
                self.img = label
#                 hbox.addWidget(label)
#                 self.setLayout(hbox)



        elif source.text() == "Green":
            if self.green.isChecked():
                self.color.setGreen(255)
            else: self.color.setGreen(0)

        else:
            if self.blue.isChecked():
                self.color.setBlue(255)
            else: self.color.setBlue(0)

        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.color.name())



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()