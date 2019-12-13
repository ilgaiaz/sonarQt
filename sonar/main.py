import numpy as np
import matplotlib.pyplot as plot
import math
import time
#import serial
import time
import re
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from sonar.forms.main import Ui_MainWindow


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
            time.sleep(10)
            self.ser = serial.Serial('/dev/ttyUSB0')
        except:
            self.ui.lbConnectionStatus.setText("Connection error!!\nUnable to connect with ATMEGA328P")
            print("Connection error. Unable to connect with ATMEGA328P")
            self.ui.btnConnection.setEnabled(True)
        else:
            self.ui.lbConnectionStatus.setText("Connesione stabilita!")
            self.ui.btnConnection.setEnabled(True)

    def onMappingClicked(self):
        self.ui.btnConnection.setEnabled(False)
        mapping()

    def mapping(self):
        fig  = plot.figure()
        fig.add_subplot(111, projection='polar')

        r = [100, 100, 300, 300, 300, 300, 40, 40, 20, 20, 20, 300, 57, 60, 55, 49, 100, 55, 55, 300, 300, 200, 10, 11, 13, 10, 10, 300, 300, 88, 88, 90, 10, 10, 12, 300]
        theta = []
        for i in range(0, len(r)):
            theta.append(math.radians(5.625 * i))

        while i < 10000000000:
            i = i + 1
        plot.polar(theta, r)
        # Display the cardioids -

        plot.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Sonar()
    main_window.show()
    app.exec()
