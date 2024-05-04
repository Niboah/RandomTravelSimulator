import random
import sys
import sys
import time
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, QRectF
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import numpy as np
import pandas as pd


from src.utils.read_file import getCities
from src.view.window import MainWindow


def find_adjacent_position_with_zero(matrix, x, y):
    for i in range(max(0, x - 1), min(x + 2, len(matrix))):
        for j in range(max(0, y - 1), min(y + 2, len(matrix[0]))):
            if (i, j) != (x, y) and matrix[i][j] == 0:
                return (i, j)
    return None

def main():

    num_rows = 40
    num_cols = 40
    unique_cities = getCities()

    matrix = np.zeros((num_rows, num_cols), dtype=object)
    
    negative_numbers = [-i for i in range(1, len(unique_cities) + 1)]
    #matrix = np.random.randint(0, len(unique_cities), size=(num_rows, num_cols))
    # Colocar números únicos en posiciones aleatorias en la matriz
    np.random.seed(42)  # Para reproducibilidad

    points = []

    city_indices = np.random.choice(num_rows * num_cols, size=len(unique_cities), replace=False)
    for idx, num in zip(city_indices, negative_numbers):
        row = idx // num_cols  # Calcular la fila
        col = idx % num_cols   # Calcular la columna
        matrix[row, col] = num
        points.append((row,col))

    vector=[(0,1),(1,0),(0,-1),(-1,0)]
    zeros=num_rows*num_cols-17

    while zeros>0:
        for i in range (1,18):
            coordenadas = np.argwhere(matrix==-i)
            coordenadas2 = np.argwhere(matrix==i)
            coordenadas=np.concatenate((coordenadas,coordenadas2))
            for x,y in coordenadas:
                for xdir,ydir in vector:
                    nx=x+xdir
                    ny=y+ydir
                    if(nx>=0 and nx <num_rows and ny>=0 and ny <num_cols and matrix[nx,ny]==0):
                        matrix[nx,ny]=i
                        zeros-=1
    
    
    ################################################################################

    colors = np.linspace(1, 359, len(unique_cities))

    app = QApplication(sys.argv)
    window = MainWindow(matrix,colors)
    window.show()

    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()