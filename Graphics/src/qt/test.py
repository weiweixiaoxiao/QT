#-*- coding:utf8 -*-  
  
from PyQt4.QtCore import *  
from PyQt4.QtGui import *   
from PyQt4 import QtGui  
from PyQt4.phonon import Phonon
import math 
import cv2 
  
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf-8"))  
  
class PixItem(QGraphicsItem):  
    def __init__(self,QPixmap):  
        super(PixItem,self).__init__()  
        self.pix = QPixmap  
      
    def boundingRect(self):  
        return QRectF(-2 - self.pix.width()/2,-2 - self.pix.height()/2,self.pix.width() + 4,self.pix.height() + 4)  
      
    def paint(self,painter,option,widget):  
        painter.drawPixmap(-self.pix.width()/2,-self.pix.height()/2,self.pix)  
  
class MainWidget(QWidget):  
    def __init__(self):  
        super(MainWidget,self).__init__()  
  
        self.angle = 0  
        self.scale = 5  
        self.shear = 5  
        self.translate =50  
        self.name = 'file/backgroud.jpg'  
        
        self.scene = QGraphicsScene()  
        self.scene.setSceneRect(-200,-200,400,400)  
        self.pixmap = QPixmap(self.name)  
        self.item = PixItem(self.pixmap)  
          
        self.scene.addItem(self.item)  
        self.item.setPos(0,0)  
          
        self.view = QGraphicsView()  
        self.view.setScene(self.scene)  
        self.view.setMinimumSize(200,200)  
          
        self.ctrlFrame = QFrame()  
        self.createControllFrame()  
          
        self.rightlayout = QVBoxLayout()  
        self.rightlayout.addWidget(self.openImage)  
        self.rightlayout.addWidget(self.rotateGroup)  
        self.rightlayout.addWidget(self.scaleGroup)  
        self.rightlayout.addWidget(self.shearGroup)  
        self.rightlayout.addWidget(self.translateGroup) 
        self.rightlayout.addWidget(self.outlineGroup)
        self.rightlayout.addWidget(self.openVideo)  
        
        # videolayout
        self.video = Phonon.VideoWidget(self)
        self.video.setMinimumSize(200, 200)
        
          
        self.leftlayout = QHBoxLayout()  
        self.leftlayout.addWidget(self.view)  
#         self.leftlayout.addWidget(self.ctrlFrame)
#         self.leftlayout.addWidget(self.video)  
        self.leftlayout.addWidget(self.ctrlFrame)        
          
        self.mainlayout = QHBoxLayout()  
        self.mainlayout.addLayout(self.leftlayout)  
        self.mainlayout.addLayout(self.rightlayout)  
        self.setLayout(self.mainlayout)  
          
        self.setWindowTitle(self.tr("Graphics Item 的各种变形"))   

    def createControllFrame(self):  
        self.openImage = QtGui.QPushButton('图像导入', self)
        self.connect(self.openImage, SIGNAL("clicked()"), self.openImgAction)  
        
        self.rotateGroup = QGroupBox(self.tr("旋转"))  
        rotateSlider = QSlider()  
        rotateSlider.setOrientation(Qt.Horizontal)  
        rotateSlider.setRange(0,360)  
        self.connect(rotateSlider,SIGNAL("valueChanged(int)"),self.slotRotate)  
        rotateLayout = QHBoxLayout()  
        rotateLayout.addWidget(rotateSlider)  
        self.rotateGroup.setLayout(rotateLayout)  
          
        self.scaleGroup = QGroupBox(self.tr("缩放"))  
        scaleSlider = QSlider()  
        scaleSlider.setOrientation(Qt.Horizontal)  
        self.connect(scaleSlider,SIGNAL("valueChanged(int)"),self.slotScale)  
        scaleLayout = QHBoxLayout()  
        scaleLayout.addWidget(scaleSlider)  
        self.scaleGroup.setLayout(scaleLayout)  
          
        self.shearGroup = QGroupBox(self.tr("切变"))  
        shearSlider = QSlider()  
        shearSlider.setOrientation(Qt.Horizontal)  
        self.connect(shearSlider,SIGNAL("valueChanged(int)"),self.slotShear)  
        shearLayout = QHBoxLayout()  
        shearLayout.addWidget(shearSlider)  
        self.shearGroup.setLayout(shearLayout)  
          
          
        self.translateGroup = QGroupBox(self.tr("位移"))  
        translateSlider = QSlider()  
        translateSlider.setOrientation(Qt.Horizontal)  
        self.connect(translateSlider,SIGNAL("valueChanged(int)"),self.slotTranslate)  
        translateLayout = QHBoxLayout()  
        translateLayout.addWidget(translateSlider)  
        self.translateGroup.setLayout(translateLayout)  
        
        self.outlineGroup = QtGui.QPushButton('图像轮廓检测', self)
        self.connect(self.outlineGroup, SIGNAL("clicked()"), self.outlineAction) 
        
        self.openVideo = QtGui.QPushButton('运动物体检测', self)
        self.connect(self.openVideo, SIGNAL("clicked()"), self.openVideoAction)
        
    @pyqtSlot()   
    def openImgAction(self):
        imgName = QtGui.QFileDialog.getOpenFileName(self,'打开图片',options = QFileDialog.DontUseNativeDialog)
        print(imgName) 
        self.name = imgName
        self.pixmap = QPixmap(self.name)  
        self.item = PixItem(self.pixmap)  
        self.scene.addItem(self.item) 
    
                        
    def outlineAction(self):    
        img = cv2.imread(self.name)  
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
        ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)      
        _,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
        cv2.drawContours(img,contours,-1,(0,0,255),3)
        cv2.imshow("img outline", img)  
        cv2.waitKey(0)        
  
    def openVideoAction(self):
        imgName = QtGui.QFileDialog.getOpenFileName(self,'打开图片',options = QFileDialog.DontUseNativeDialog)
        print(imgName) 
        self.name = imgName
        self.pixmap = QPixmap(self.name)  
        self.item = PixItem(self.pixmap)  
        self.scene.addItem(self.item) 
          
    def slotRotate(self,value):  
        self.item.rotate(value - self.angle)  
        self.angle = value  
      
    def slotScale(self,value):  
        if value  > self.scale:  
            s = math.pow(1.1,(value - self.scale))  
        else:  
            s = math.pow(1/1.1,(self.scale - value))  
        self.item.scale(s,s)  
        self.scale = value  
      
    def slotShear(self,value):  
        self.item.shear((value - self.shear)/10.0,0)  
        self.shear = value  
      
    def slotTranslate(self,value):  
        self.item.translate(value - self.translate,value - self.translate)  
        self.translate = value  
    
    def slotOutline(self,value):
        self.item.shape()
        
      
if __name__ == '__main__':  
    import sys  
    app = QApplication(sys.argv)  
    mainwindow = MainWidget()  
    mainwindow.show()  
    sys.exit(app.exec_())  