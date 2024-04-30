import sys
from PyQt5.QtCore import QFile, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QWidget, QPushButton, QGridLayout, QGraphicsView
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
        
        # Rysowanie sieci sensorycznej
        self.draw_network()

        # Tworzenie obiektu NetworkDisplay i przekazanie QGraphicsView
        self.network_display = NetworkDisplay(self.graphicsView)
        self.resetButton.clicked.connect(self.network_display.fun)

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
        self.appName.setFont(QFont("Arial", 18))
        self.appName.setGeometry(QtCore.QRect(30, 20, 351, 61))
        self.appName.setObjectName("appName")
        self.appName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Reset sensor position
        self.resetButton = QPushButton("Reset", self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(110, 110, 161, 51))
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
        self.numberSlider.setMinimum(1)
        self.numberSlider.setMaximum(30)
        self.numberSlider.setTickInterval(1)
        self.numberSlider.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Number slider name
        self.numberSliderName = QLabel(self.centralwidget)
        self.numberSliderName.setGeometry(QtCore.QRect(20, 220, 351, 61))
        self.numberSliderName.setText("Number of sensors")
        self.numberSliderName.setFont(QFont("Arial", 24))
        self.numberSliderName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Number slider num
        self.numberSliderNum = QLabel(self.centralwidget)
        self.numberSliderNum.setText("0")
        self.numberSliderNum.setFont(QFont("Arial", 32))
        self.numberSliderNum.setGeometry(QtCore.QRect(110, 340, 141, 61))
        self.numberSliderNum.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Range slider
        self.rangeSlider = QSlider(Qt.Horizontal, self.centralwidget)
        self.rangeSlider.setGeometry(QtCore.QRect(30, 520, 331, 51))
        self.rangeSlider.setMinimum(1)
        self.rangeSlider.setMaximum(10)
        self.rangeSlider.setTickInterval(1)
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
        self.rangeSliderNum.setText("0")
        self.rangeSliderNum.setFont(QFont("Arial", 32))
        self.rangeSliderNum.setStyleSheet(str(stylesheet, encoding='utf-8'))

    def draw_network(self):
        pass

    def update_label(self, label_widget, value):
        # Aktualizuj etykietę na podstawie przekazanego widgetu i wartości suwaka
        label_widget.setText(str(value))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
