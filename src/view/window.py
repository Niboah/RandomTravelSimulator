
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, QRectF
from PyQt6.QtWidgets import QMainWindow, QWidget


CELL_SIZE = 20
HALF_CELL_SIZE = 10

class MainWindow(QMainWindow):
    def __init__(self,matrix,colors):
        super().__init__()
        self.setWindowTitle("Random travel simulation")
        self.setGeometry(100, 100, 1000, 850)
        self.label = QtWidgets.QLabel()
        self.setCentralWidget(self.label)
        self.matrix = matrix
        self.colors = colors
        self.ySize = len(matrix) + 1
        self.xSize = len(matrix[0]) + 1
        
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
    
        for y, row in enumerate(self.matrix):
            for x, value in enumerate(row):
                if value > 0. and y < len(self.matrix):                   
                    pen.setWidth(CELL_SIZE)
                    painter.setPen(pen)
                    color = QtGui.QColor.fromHsv(int(self.colors[value]), 105, 255, 255)
                    pen.setColor(color)

                    painter.drawPoint(((x+1)*CELL_SIZE)+HALF_CELL_SIZE, ((y+1)*CELL_SIZE)+HALF_CELL_SIZE)

                elif value < 0:
                    pen.setWidth(HALF_CELL_SIZE)
                    painter.setPen(pen)
                    color = QtGui.QColor.fromHsv(int(self.colors[value]), 255, 255, 255)
                    pen.setColor(color)

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

        

    def animate(self):
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(10, 10)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.anim.setStartValue(QPoint(100,0))
        self.anim.setEndValue(QPoint(400, 400))
        self.anim.setDuration(15000)
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
        