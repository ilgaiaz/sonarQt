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

from kalmanpy import KalmanFilter
from forms.main import Ui_MainWindow

def hcsr04Filter():
    sigma_alpha = 0.001
    sigma_omega = 0.002
    x0 = np.array([0]).reshape(1,1)
    F = np.array([1]).reshape(1, 1)
    B = np.array([0]).reshape(1,1)
    H = np.array([1]).reshape(1, 1)
    #System noise covariance matrix
    Q = np.array([sigma_alpha]).reshape(1, 1)
    #Measurement noise covariance matrix
    R = np.array([sigma_omega]).reshape(1, 1)
    kf= KalmanFilter(F=F, H=H, Q=Q, R=R, x0=x0)

    return kf



class Mapping(QtCore.QThread):
    signalMapping = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

    def run( self ):
        self.signalMapping.emit()

class Sonar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ser = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.kalmanFilter = hcsr04Filter()
        self.theta = []
        self.r = []
        self.kf_r = []

        self.map = Mapping()
        self.mapThread = QtCore.QThread()
        self.mapThread.started.connect(self.map.run)
        self.map.signalMapping.connect(self.mapping)
        self.map.moveToThread(self.mapThread)

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
        else:
            self.ui.lbConnectionStatus.setText("Connesione stabilita!")
            self.ui.btnMapping.setEnabled(True)

    def onMappingClicked(self):
        self.ui.btnConnection.setEnabled(False)
        self.ui.btnMapping.setEnabled(False)
        self.mapThread.start()


    def mapping(self):
        fig  = plot.figure()
        fig.add_subplot(111, projection='polar')

        self.ser.write(b'A')
        #read line from serial port
        line = self.ser.readline().strip()
        coordinate = line.decode('ascii')
        #Remove special char
        coordinate = coordinate.replace('\r', '')
        coordinate = coordinate.replace('\n', '')
        while (coordinate != 'E'):
            #Get value from the string
            degree = re.split('[;]', coordinate)[0]
            distance = re.split('[;]', coordinate)[1]
            #Save and convert value on float
            self.theta.append(math.radians(float(degree)))
            self.r.append(float(distance))
            self.kf_r.append(self.kalmanFilter.predicted_state()[0])
            
            #read line from serial port
            line = self.ser.readline().strip()
            coordinate = line.decode('ascii')
            #Remove special char
            coordinate = coordinate.replace('\r', '')
            coordinate = coordinate.replace('\n', '')

            self.kalmanFilter.update(float(distance))
            time.sleep(0.5)

        plot.polar(self.theta, self.kf_r)
        plot.polar(self.theta, self.r, 'bo')
        # Display the mapping
        plot.show()
        self.r.clear()
        self.kf_r.clear()
        self.theta.clear()
        self.ui.btnMapping.setEnabled(True)
        self.ui.btnConnection.setEnabled(True)
        self.mapThread.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Sonar()
    main_window.show()
    app.exec()
