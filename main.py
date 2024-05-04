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




def main():

    num_rows = 40
    num_cols = 40
    unique_cities = getCities()

    matrix = np.zeros((num_rows, num_cols), dtype=object)
    
    negative_numbers = [-i for i in range(1, len(unique_cities) + 1)]
    matrix = np.random.randint(0, len(unique_cities), size=(num_rows, num_cols))
    # Colocar números únicos en posiciones aleatorias en la matriz
    np.random.seed(42)  # Para reproducibilidad
    city_indices = np.random.choice(num_rows * num_cols, size=len(unique_cities), replace=False)
    for idx, num in zip(city_indices, negative_numbers):
        row = idx // num_cols  # Calcular la fila
        col = idx % num_cols   # Calcular la columna
        matrix[row, col] = num
    
    ################################################################################

    colors = np.linspace(1, 359, len(unique_cities))

    app = QApplication(sys.argv)
    window = MainWindow(matrix,colors)
    window.initialize()
    window.show()

    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()