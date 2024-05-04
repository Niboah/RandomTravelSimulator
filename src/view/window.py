
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, QRectF, QTimer
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPainter, QPen


CELL_SIZE = 20
HALF_CELL_SIZE = 10

class MainWindow(QMainWindow):
    def __init__(self,matrix,colors):
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

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        
        self.matrix = matrix
        self.colors = colors
        self.ySize = len(matrix) + 1
        self.xSize = len(matrix[0]) + 1

        self.initialize()
        self.drawMatrix()

        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(HALF_CELL_SIZE,HALF_CELL_SIZE )
        self.child.setVisible(False)

        
    def genMap(self):
        self.drawCell()
        self.drawMatrix()
        self.startBotton.setEnabled(True)

    def start(self):
        self.drawLine(10,10,22,23)
 
    def initialize(self):
        canvas = QtGui.QPixmap(1000, 850)
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
                    print(value,y,x,end=" ---")   
                    pen.setWidth(CELL_SIZE)
                    
                    color = QtGui.QColor.fromHsv(int(self.colors[value-1]), 105, 255, 255)
                    pen.setColor(color)
                    painter.setPen(pen)
                    

                    painter.drawPoint(((x+1)*CELL_SIZE)+HALF_CELL_SIZE, ((y+1)*CELL_SIZE)+HALF_CELL_SIZE)

                elif value < 0:
                    pen.setWidth(HALF_CELL_SIZE)
                    color = QtGui.QColor.fromHsv(int(self.colors[(value*-1)-1]), 255, 255, 255)
                    pen.setColor(color)
                    painter.setPen(pen)
                    
                    font = QtGui.QFont()
                    font.setFamily('Times')
                    font.setBold(True)
                    font.setPointSize(10)
                    painter.setFont(font)

                    painter.drawText(((x+1)*CELL_SIZE)+HALF_CELL_SIZE, ((y+1)*CELL_SIZE)+HALF_CELL_SIZE, 'aAA')

                    rectangle = QRectF(((x+1)*CELL_SIZE)+HALF_CELL_SIZE, ((y+1)*CELL_SIZE)+HALF_CELL_SIZE, int(HALF_CELL_SIZE/10), int(HALF_CELL_SIZE/10))
                    painter.drawEllipse(rectangle)

        painter.end()
        self.label.setPixmap(canvas)

    def drawLine(self,iX,iY,dX,dY):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(((iX+1)*CELL_SIZE)+HALF_CELL_SIZE, ((iY+1)*CELL_SIZE)+HALF_CELL_SIZE, ((dX+1)*CELL_SIZE)+HALF_CELL_SIZE, ((dY+1)*CELL_SIZE)+HALF_CELL_SIZE)
        painter.end()
        self.label.setPixmap(canvas)

        self.child.setVisible(True)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setStartValue(QPoint(((iX+1)*CELL_SIZE)+HALF_CELL_SIZE,((iY+1)*CELL_SIZE)+HALF_CELL_SIZE))
        self.anim.setEndValue(QPoint(((dX+1)*CELL_SIZE)+HALF_CELL_SIZE, ((dY+1)*CELL_SIZE)+HALF_CELL_SIZE))
        self.anim.setDuration(1500)
        self.anim.start()

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
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(x, y, text)
        painter.end()
        self.label.setPixmap(canvas)

    def reflesh(self):
        self.label.clear()
        self.initialize()
        self.drawCell()
        self.drawMatrix()