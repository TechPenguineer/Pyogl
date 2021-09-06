from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class Frame(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Frame, self).__init__(*args, **kwargs)
            
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        
    def Create():
        app = QtWidgets.QApplication(sys.argv)
        main = Frame()
        main.show()
        sys.exit(app.exec_())
        
    def CreateFrame(x_pos, y_pos, x_size, y_size):
        if __name__ == "__main__":
            Frame.Create()
