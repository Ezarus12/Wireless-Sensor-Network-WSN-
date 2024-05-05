import sys
from PyQt5.QtCore import QFile, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QWidget, QPushButton, QGraphicsView, QToolBar, QAction, QProgressBar, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from network_display import NetworkDisplay
import math

#Variables
windowHeight = 1080
windowWidth = 1920
aspectRatio = 16/9

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
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stylesheet = style_file.readAll()
            style_file.close()
        else:
            print("Failed to open styles file")
        
        # Creating widgets
        self.create_widgets(stylesheet)
        
        # Tworzenie obiektu NetworkDisplay i przekazanie QGraphicsView
        self.network_display = NetworkDisplay(self.graphicsView)

        # Rysowanie sieci sensorycznej
        self.draw_network()
        #self.add_toolbar()

        self.resetButton.clicked.connect(lambda: self.network_display.fun(self.numberSlider.value(), self.rangeSlider.value()))
        self.resetButton.clicked.connect(lambda: self.update_label(self.inactiveSensorsNum, self.network_display.inactive_sensors))
        
        self.startButton.clicked.connect(lambda: self.startBatteryDecrease())
        #self.startButton.clicked.connect(lambda: self.network_display.simulation())

        self.numberSlider.valueChanged.connect(lambda value: self.update_label(self.numberSliderNum, value))
        self.rangeSlider.valueChanged.connect(lambda value: self.update_label(self.rangeSliderNum, value))
        
    def add_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        Options = QAction("Options", self)
        Edit = QAction("Edit", self)
        toolbar.addAction(Options)
        toolbar.addAction(Edit)

    def resizeEvent(self, event):
        width = event.size().width()
        height = event.size().height()
        #Resize terrain represenation
        self.graphicsView.resize(math.floor(width*0.521),math.floor(height*0.926))
        self.graphicsView.move(math.floor(width*0.47),math.floor(height*0.04))

        #Resize title and intials
        self.titleText.resize(math.floor(width*0.2), math.floor(height*0.02))
        self.titleText.setFont(QFont("Arial", math.floor(width*0.2/21)))
        self.titleText.move(math.floor(width*0.01),math.floor(height*0.02))

        self.initials.resize(math.floor(width*0.2), math.floor(height*0.016))
        self.initials.setFont(QFont("Arial", math.floor(width*0.2/32)))
        self.initials.move(math.floor(width*0.01),math.floor(height*0.045))

        #Resize sliders
        self.numberSliderName.resize(math.floor(width*0.2), math.floor(height*0.023))
        self.numberSliderName.setFont(QFont("Arial", math.floor(width*0.2/16)))
        self.numberSliderName.move(math.floor(width*0.01),math.floor(height*0.1))

        self.numberSliderNum.resize(math.floor(width*0.08), math.floor(height*0.05))
        self.numberSliderNum.setFont(QFont("Arial", math.floor(width*0.2/16)))
        self.numberSliderNum.move(math.floor(width*0.16),math.floor(height*0.087))

        self.numberSlider.resize(math.floor(width*0.2), math.floor(height*0.04))
        self.numberSlider.move(math.floor(width*0.01),math.floor(height*0.14))

        self.rangeSliderName.resize(math.floor(width*0.2), math.floor(height*0.04))
        self.rangeSliderName.setFont(QFont("Arial", math.floor(width*0.2/16)))
        self.rangeSliderName.move(math.floor(width*0.01),math.floor(height*0.23))

        self.rangeSliderNum.resize(math.floor(width*0.05), math.floor(height*0.05))
        self.rangeSliderNum.setFont(QFont("Arial", math.floor(width*0.2/16)))
        self.rangeSliderNum.move(math.floor(width*0.118),math.floor(height*0.226))

        self.rangeSlider.resize(math.floor(width*0.2), math.floor(height*0.04))
        self.rangeSlider.move(math.floor(width*0.01),math.floor(height*0.30))

        print("XD")

    def create_widgets(self, stylesheet):
        #Creating app name widget
        self.appName = QLabel(self.central_widget)
        self.appName.setText("Wireless Sensor Network (WSN)")
        self.appName.setFont(QFont("Roboto", 32))
        self.appName.setMaximumHeight(300) # Ustawienie maksymalnej wysokości na 100 pikseli
        

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        #App name
        self.titleText = QLabel(self.centralwidget)
        self.titleText.setText("Wireless Sensor Network (WSN)")
        self.titleText.setFont(QFont("Arial", 20))
        self.titleText.setGeometry(QtCore.QRect(20, 10, 420, 61))
        self.titleText.setStyleSheet(str(stylesheet, encoding='utf-8'))

        self.initials = QLabel(self.centralwidget)
        self.initials.setText("Filip Dabrowski")
        self.initials.setFont(QFont("Arial", 18))
        self.initials.setGeometry(QtCore.QRect(0, 0, 360, 30))
        self.initials.setStyleSheet(str(stylesheet, encoding='utf-8'))
        self.initials.setStyleSheet("color: white;")

        #Reset sensor position
        self.resetButton = QPushButton("Reset", self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(110, 1000, 161, 51))
        self.resetButton.setObjectName("pushButton_2")
        self.resetButton.setStyleSheet(str(stylesheet, encoding='utf-8'))
        self.setCentralWidget(self.centralwidget)
       
        #Creating graphic view representing terrain and the sensors
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
        self.numberSlider.setMaximum(150)
        self.numberSlider.setTickInterval(1)
        self.numberSlider.setValue(30)
        self.numberSlider.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Number slider name
        self.numberSliderName = QLabel(self.centralwidget)
        self.numberSliderName.setGeometry(QtCore.QRect(20, 220, 351, 61))
        self.numberSliderName.setText("Number of sensors:")
        self.numberSliderName.setFont(QFont("Arial", 24))
        self.numberSliderName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Number slider num
        self.numberSliderNum = QLabel(self.centralwidget)
        self.numberSliderNum.setText("30")
        self.numberSliderNum.setFont(QFont("Arial", 24))
        self.numberSliderNum.setGeometry(QtCore.QRect(110, 340, 141, 61))
        self.numberSliderNum.setStyleSheet(str(stylesheet, encoding='utf-8'))
        self.numberSliderNum.setStyleSheet("color: white;")

        #Range slider
        self.rangeSlider = QSlider(Qt.Horizontal, self.centralwidget)
        self.rangeSlider.setGeometry(QtCore.QRect(30, 520, 331, 51))
        self.rangeSlider.setMinimum(0)
        self.rangeSlider.setMaximum(25)
        self.rangeSlider.setTickInterval(10)
        self.rangeSlider.setValue(10)
        self.rangeSlider.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Range slider name
        self.rangeSliderName = QLabel(self.centralwidget)
        self.rangeSliderName.setGeometry(QtCore.QRect(30, 430, 351, 61))
        self.rangeSliderName.setText("Sensor range:")
        self.rangeSliderName.setFont(QFont("Arial", 24))
        self.rangeSliderName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Range slider num
        self.rangeSliderNum = QLabel(self.centralwidget)
        self.rangeSliderNum.setGeometry(QtCore.QRect(120, 580, 141, 61))
        self.rangeSliderNum.setText("10")
        self.rangeSliderNum.setFont(QFont("Arial", 32))
        self.rangeSliderNum.setStyleSheet(str(stylesheet, encoding='utf-8'))
        self.rangeSliderNum.setStyleSheet("color: white;")

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

        #Battery life progress bar
        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(500, 382, 370, 60))
        self.progress_bar.setValue(100)
        self.progress_bar.setStyleSheet(str(stylesheet, encoding='utf-8'))

    def draw_network(self):
        self.update_label(self.inactiveSensorsNum, self.network_display.inactive_sensors)
        pass

    def update_label(self, label_widget, value):
        # Aktualizuj etykietę na podstawie przekazanego widgetu i wartości suwaka
        self.progress_bar.setValue(100)
        label_widget.setText(str(value))
    
    def decreaseBatteryLife(self):
        # Decrease battery life by 10% every 200 milliseconds
        if self.progress_bar.value() > 0:
            self.progress_bar.setValue(self.progress_bar.value() - 1)
            if self.progress_bar.value() <= 80:
                for i, sensor in enumerate(self.network_display.sensors):
                    if sensor.isActive:
                        print(self.progress_bar.value())
                        sensor.fade_range_area(self.progress_bar.value())
                        
        else:
            self.timer.stop()
            self.network_display.simulation()
            self.update_label(self.inactiveSensorsNum, self.network_display.inactive_sensors)
            if self.network_display.sensors:
                self.progress_bar.setValue(100)
                self.startBatteryDecrease()
            else:
                self.progress_bar.setValue(0)

    def startBatteryDecrease(self):
        if not self.network_display.sensors:
            message_box = QMessageBox()
            message_box.setWindowTitle("Cannot start the simulation")
            message_box.setText("All of the sensors ran out of their battery")
            message_box.setStyleSheet("QMessageBox { background-color: #333333; } QMessageBox QLabel { color: white; }")
            message_box.exec_()
            return
        self.progress_bar.setValue(100)
        self.timer = QTimer()
        self.timer.timeout.connect(self.decreaseBatteryLife)
        self.timer.start(10)  # Decrease battery every 200 milliseconds


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
