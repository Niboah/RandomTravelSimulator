
from ast import main
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, QRectF, QTimer, QRect
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPainter, QPen, QFont
import time

CELL_SIZE = 20
HALF_CELL_SIZE = 10

class MainWindow(QMainWindow):
    def __init__(self,matrix,colors,points,points2,EveryDay,allFlyer):
        super().__init__()
        self.setWindowTitle("Random travel simulation")
        self.setGeometry(100, 100, 1000, 850)        

        self.layout = QHBoxLayout()

        self.label = QtWidgets.QLabel()
        self.layout.addWidget(self.label)
        
        self.rightLayout = QVBoxLayout()
        self.layout.addLayout(self.rightLayout)

        self.genMapBotton =  QPushButton("GenMap")
        self.genMapBotton.clicked.connect(self.genMap)
        self.rightLayout.addWidget(self.genMapBotton)

        self.startBotton =  QPushButton("Start")
        self.startBotton.clicked.connect(self.start)
        self.startBotton.setEnabled(False)
        self.rightLayout.addWidget(self.startBotton)

        self.days = QtWidgets.QLabel()
        self.rightLayout.addWidget(self.days)
        self.days.setFont(QFont('Arial', 20)) 
        self.days.setGeometry(QRect(70, 80, 100, 100))
        self.info = QtWidgets.QLabel()
        self.rightLayout.addWidget(self.info)
        self.space = QtWidgets.QLabel()
        self.rightLayout.addWidget(self.space)

        self.count = 0
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        
        self.matrix = matrix

        self.colors = colors
        self.ySize = len(matrix) + 1
        self.xSize = len(matrix[0]) + 1

        self.points=points
        self.points2=points2
        self.EveryDay = EveryDay
        self.allFlyer = allFlyer

        self.initialize()
        self.drawMatrix()

        self.listChild = []
        self.listAni=[]
        for i in range(20):
            child = QWidget(self)
            child.setStyleSheet("background-color:red;border-radius:15px;")
            child.resize(HALF_CELL_SIZE,HALF_CELL_SIZE )
            child.setVisible(False)
            self.listChild.append(child)

            anim = QPropertyAnimation(child, b"pos")
            self.listAni.append(anim)

        
    def genMap(self):
        self.drawCell()
        self.drawMatrix()
        self.startBotton.setEnabled(True)
        self.genMapBotton.setEnabled(False)

    def start(self):
        self.reflesh()
        f = self.allFlyer[self.count]
        self.count+=1
        if self.count==366:
            self.count=0
        childI=0
        for name,origin,dest in f:
            (x,y)=self.points2[self.points[origin]]
            (a,b)=self.points2[self.points[dest]]
            self.drawLine(x,y,a,b,self.listChild[childI],self.listAni[childI])
            childI+=1
        self.startBotton.setText("Next")
            
            
    def initialize(self):
        canvas = QtGui.QPixmap(850, 850)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)

    def drawMatrix(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        for x in range(CELL_SIZE,(self.xSize*CELL_SIZE)+HALF_CELL_SIZE,CELL_SIZE):
            painter.drawLine(x,CELL_SIZE, x, (self.xSize*CELL_SIZE))

        for y in range(CELL_SIZE,(self.ySize*CELL_SIZE)+HALF_CELL_SIZE,CELL_SIZE):
            painter.drawLine(CELL_SIZE,y, (self.ySize*CELL_SIZE), y)

        painter.end()
        self.label.setPixmap(canvas)
    
    def drawCell(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        

        for y in range(0,len(self.matrix)):
            for x in range(0,len(self.matrix)):
                value = self.matrix[y][x]
                if value > 0 :
                    pen.setWidth(CELL_SIZE)

                    ciudades = list(self.points.keys())

                    intensidad = self.EveryDay[self.count][ciudades[value-1]] / 300
                    
                    color = QtGui.QColor.fromHsv(int(self.colors[value-1]), int(200*intensidad) + 55 , 255, 255)

                    pen.setColor(color)
                    painter.setPen(pen)
                    

                    painter.drawPoint(((x+1)*CELL_SIZE)+HALF_CELL_SIZE, ((y+1)*CELL_SIZE)+HALF_CELL_SIZE)

                elif value < 0:
                    pen.setWidth(HALF_CELL_SIZE)
                    color = QtGui.QColor.fromHsv(int(self.colors[(value*-1)-1]), 255, 255, 255)
                    pen.setColor(color)
                    painter.setPen(pen)
                    rectangle = QRectF(((x+1)*CELL_SIZE)+HALF_CELL_SIZE, ((y+1)*CELL_SIZE)+HALF_CELL_SIZE, int(HALF_CELL_SIZE/10), int(HALF_CELL_SIZE/10))
                    painter.drawEllipse(rectangle)

        painter.end()
        self.label.setPixmap(canvas)

    def drawLine(self,iX,iY,dX,dY,c,anim):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(((iX+1)*CELL_SIZE)+HALF_CELL_SIZE, ((iY+1)*CELL_SIZE)+HALF_CELL_SIZE, ((dX+1)*CELL_SIZE)+HALF_CELL_SIZE, ((dY+1)*CELL_SIZE)+HALF_CELL_SIZE)
        painter.end()
        self.label.setPixmap(canvas)

        
        c.setVisible(True)
        
        anim.setStartValue(QPoint(((iX+1)*CELL_SIZE)+HALF_CELL_SIZE,((iY+1)*CELL_SIZE)+HALF_CELL_SIZE))
        anim.setEndValue(QPoint(((dX+1)*CELL_SIZE)+HALF_CELL_SIZE, ((dY+1)*CELL_SIZE)+HALF_CELL_SIZE))
        anim.setDuration(1500)
        
        anim.start()

    def drawText(self,text,x,y):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(20)
        painter.setFont(font)

        painter.drawText(x*CELL_SIZE, y*CELL_SIZE, text)
        painter.end()
        self.label.setPixmap(canvas)

    def reflesh(self):
        self.label.clear()
        self.initialize()
        self.drawCell()
        self.drawMatrix()
        self.writeInfo()

    def writeInfo(self):
        d = self.EveryDay[self.count]
        self.days.setText("Day "+str(self.count))
        self.info.setText("Number of people in the city:\n")
        for p,n in d.items():
            (x,y)=self.points2[self.points[p]]
            self.drawText(p,x,y+1)
            self.info.setText(self.info.text()+" \n"+p+" "+str(n))
        