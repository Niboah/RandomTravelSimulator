import sys
import numpy as np

from PyQt6.QtWidgets import QApplication
from src.model.config import configure
from src.view.window import MainWindow

if __name__ == '__main__':
    unique_cities, matrix, points,points2,EveryDay,allFlyer = configure()
    colors = np.linspace(1, 359, len(unique_cities))

    app = QApplication(sys.argv)
    window = MainWindow(matrix,colors,points,points2,EveryDay,allFlyer)
    window.show()

    sys.exit(app.exec())