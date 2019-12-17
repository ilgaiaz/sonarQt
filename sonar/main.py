import numpy as np
import matplotlib.pyplot as plot
import math
import time
#import serial
import time
import re
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import sys
import serial

from forms.main import Ui_MainWindow

class Mapping(QtCore.QThread):
    signalMapping = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.runs = True

    def run( self ):
        self.signalMapping.emit()
    

class Sonar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ser = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        # Signal/Slot connections
        self.ui.btnConnection.clicked.connect(self.onConnectionClicked)
        self.ui.btnMapping.clicked.connect(self.onMappingClicked)

    def onConnectionClicked(self, ser):
        try:
            #Open port at 9600,8,N,1 no timeout
            #time.sleep(1)
            self.ser = serial.Serial('/dev/ttyUSB0')
        except:
            self.ui.lbConnectionStatus.setText("Connection error!!\nUnable to connect with ATMEGA328P")
            print("Connection error. Unable to connect with ATMEGA328P")
            self.ui.btnMapping.setEnabled(True)
        else:
            self.ui.lbConnectionStatus.setText("Connesione stabilita!")
            self.ui.btnMapping.setEnabled(True)

    def onMappingClicked(self):
        self.ui.btnMapping.setEnabled(False)

        self.map = Mapping()
        self.mapThread = QtCore.QThread()
        self.mapThread.started.connect(self.map.run)
        self.map.signalMapping.connect(self.mapping)
        self.map.moveToThread(self.mapThread)

        self.mapThread.start()


    def mapping(self):
        fig  = plot.figure()
        fig.add_subplot(111, projection='polar')

        r = [100, 100, 300, 300, 300, 300, 40, 40, 20, 20, 20, 300, 57, 60, 55, 49, 100, 55, 55, 300, 300, 200, 10, 11, 13, 10, 10, 300, 300, 88, 88, 90, 10, 10, 12, 300]
        theta = []
        for i in range(0, len(r)):
            theta.append(math.radians(5.625 * i))

        time.sleep(2)
        plot.polar(theta, r)
        # Display the cardioids -
        plot.show()
        self.mapThread.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Sonar()
    main_window.show()
    app.exec()
