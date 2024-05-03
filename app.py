import sys
from PyQt5.QtCore import QFile, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QWidget, QPushButton, QGraphicsView
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from network_display import NetworkDisplay
import math

#Variables
windowHeight = 1080
windowWidth = 1920

class Window(QMainWindow):
    def __init__(self):
        super().__init__() #initializing parent object
    
        self.setWindowTitle("Wireless Sensor Network") # Setting window title
        self.setStyleSheet("background:#252525") # Changing the background color
        self.setGeometry(320, 180, windowWidth, windowHeight) # Defining window position and resolution

        self.central_widget = QWidget() # Creating central widget
        self.setCentralWidget(self.central_widget) # Setting central widget

        #Loading the styles file
        style_file = QFile("styles.css")
        style_file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = style_file.readAll()
        style_file.close()
        
        # Creating widgets
        self.create_widgets(stylesheet)
        
        # Tworzenie obiektu NetworkDisplay i przekazanie QGraphicsView
        self.network_display = NetworkDisplay(self.graphicsView)

        # Rysowanie sieci sensorycznej
        self.draw_network()
        
        self.resetButton.clicked.connect(lambda: self.network_display.fun(self.numberSlider.value(), self.rangeSlider.value()))
        self.resetButton.clicked.connect(lambda: self.update_label(self.inactiveSensorsNum, self.network_display.inactive_sensors))

        self.numberSlider.valueChanged.connect(lambda value: self.update_label(self.numberSliderNum, value))
        self.rangeSlider.valueChanged.connect(lambda value: self.update_label(self.rangeSliderNum, value))
        
    def create_widgets(self, stylesheet):
        #Creating app name widget
        self.app_name = QLabel(self.central_widget)
        self.app_name.setText("Wireless Sensor Network (WSN)")
        self.app_name.setFont(QFont("Roboto", 32))
        self.app_name.setMaximumHeight(100) # Ustawienie maksymalnej wysokości na 100 pikseli

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        #App name
        self.appName = QLabel(self.centralwidget)
        self.appName.setText("Wireless Sensor Network (WSN)")
        self.appName.setFont(QFont("Arial", 20))
        self.appName.setGeometry(QtCore.QRect(30, 10, 410, 61))
        self.appName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        self.initals = QLabel(self.centralwidget)
        self.initals.setText("Filip Dabrowski")
        self.initals.setFont(QFont("Arial", 18))
        self.initals.setGeometry(QtCore.QRect(30, 66, 351, 30))
        self.initals.setStyleSheet(str(stylesheet, encoding='utf-8'))
        self.initals.setStyleSheet("color: white;")


        #Reset sensor position
        self.resetButton = QPushButton("Reset", self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(110, 120, 161, 51))
        self.resetButton.setObjectName("pushButton_2")
        self.resetButton.setStyleSheet(str(stylesheet, encoding='utf-8'))
        self.setCentralWidget(self.centralwidget)
       

        # Tworzenie widoku graficznego i sceny
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(900, 40, 1000, 1000))

        #Star button
        self.startButton = QPushButton("Start Simulation", self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(40, 680, 321, 141))
        self.startButton.setStyleSheet(str(stylesheet, encoding='utf-8'))
        
        #Number slider
        self.numberSlider = QSlider(Qt.Horizontal, self.centralwidget)
        self.numberSlider.setGeometry(QtCore.QRect(20, 290, 311, 51))
        self.numberSlider.setMinimum(0)
        self.numberSlider.setMaximum(60)
        self.numberSlider.setTickInterval(1)
        self.numberSlider.setValue(30)
        self.numberSlider.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Number slider name
        self.numberSliderName = QLabel(self.centralwidget)
        self.numberSliderName.setGeometry(QtCore.QRect(20, 220, 351, 61))
        self.numberSliderName.setText("Number of sensors")
        self.numberSliderName.setFont(QFont("Arial", 24))
        self.numberSliderName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Number slider num
        self.numberSliderNum = QLabel(self.centralwidget)
        self.numberSliderNum.setText("30")
        self.numberSliderNum.setFont(QFont("Arial", 32))
        self.numberSliderNum.setGeometry(QtCore.QRect(110, 340, 141, 61))
        self.numberSliderNum.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Range slider
        self.rangeSlider = QSlider(Qt.Horizontal, self.centralwidget)
        self.rangeSlider.setGeometry(QtCore.QRect(30, 520, 331, 51))
        self.rangeSlider.setMinimum(1)
        self.rangeSlider.setMaximum(25)
        self.rangeSlider.setTickInterval(1)
        self.rangeSlider.setValue(10)
        self.rangeSlider.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Range slider name
        self.rangeSliderName = QLabel(self.centralwidget)
        self.rangeSliderName.setGeometry(QtCore.QRect(30, 430, 351, 61))
        self.rangeSliderName.setText("Sensor range")
        self.rangeSliderName.setFont(QFont("Arial", 24))
        self.rangeSliderName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Range slider num
        self.rangeSliderNum = QLabel(self.centralwidget)
        self.rangeSliderNum.setGeometry(QtCore.QRect(120, 580, 141, 61))
        self.rangeSliderNum.setText("10")
        self.rangeSliderNum.setFont(QFont("Arial", 32))
        self.rangeSliderNum.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Inactive sensors
        self.inactiveSensors = QLabel(self.centralwidget)
        self.inactiveSensors.setGeometry(QtCore.QRect(500, 80, 350, 60))
        self.inactiveSensors.setText("Inactive Sensors:")
        self.inactiveSensors.setFont(QFont("Arial", 24))
        self.inactiveSensors.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Inactive sensors num
        self.inactiveSensorsNum = QLabel(self.centralwidget)
        self.inactiveSensorsNum.setGeometry(QtCore.QRect(760, 82, 60, 60))
        self.inactiveSensorsNum.setText("0")
        self.inactiveSensorsNum.setFont(QFont("Arial", 24))
        self.inactiveSensorsNum.setStyleSheet(str(stylesheet, encoding='utf-8'))

    def draw_network(self):
        self.update_label(self.inactiveSensorsNum, self.network_display.inactive_sensors)
        pass

    def update_label(self, label_widget, value):
        # Aktualizuj etykietę na podstawie przekazanego widgetu i wartości suwaka
        label_widget.setText(str(value))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
