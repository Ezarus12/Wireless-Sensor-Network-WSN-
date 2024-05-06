import sys
from PyQt5.QtCore import QFile, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QWidget, QPushButton, QGraphicsView, QToolBar, QAction, QProgressBar, QMessageBox, QCheckBox, QAction
from PyQt5.QtGui import QFont, QIcon
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
        style_file = QFile("Styles/styles.css")
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stylesheet = style_file.readAll()
            style_file.close()
        else:
            print("Failed to open styles file")

        button_style_file = QFile("Styles/offButton.css")
        if button_style_file.open(QFile.ReadOnly | QFile.Text):
            buttonStylesheet = button_style_file.readAll()
            button_style_file.close()
        else:
            print("Failed to open styles file")

        # Creating widgets
        self.create_widgets(stylesheet, buttonStylesheet)
        self.create_toolbar()
        
        # Tworzenie obiektu NetworkDisplay i przekazanie QGraphicsView
        self.network_display = NetworkDisplay(self.graphicsView)
        self.network_display.simulationMode = 'A'

        # Rysowanie sieci sensorycznej
        self.draw_network()
        #self.add_toolbar()
        self.resetButton.clicked.connect(lambda: self.reset())
        self.resetButton.clicked.connect(lambda: self.update_label(self.inactiveSensorsNum, self.network_display.inactive_sensors))
        
        self.startButton.clicked.connect(lambda: self.startBatteryDecrease())

        self.targetButton.clicked.connect(lambda: self.changeSimulationMode("Target", stylesheet, buttonStylesheet))
        self.areaButton.clicked.connect(lambda: self.changeSimulationMode("Area", stylesheet, buttonStylesheet))

        self.numberSlider.valueChanged.connect(lambda value: self.update_label(self.numberSliderNum, value))
        self.rangeSlider.valueChanged.connect(lambda value: self.update_label(self.rangeSliderNum, value))
        
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        Settings = QAction(QIcon("setting.png"), "Settings", self)
        toolbar.setStyleSheet("background-color: gray;")
        Edit = QAction("Edit", self)
        toolbar.addAction(Settings)
        toolbar.addAction(Edit)

    def resizeEvent(self, event):
        width = event.size().width()
        height = event.size().height()
        #Resize terrain represenation
        self.graphicsView.resize(math.floor(width*0.521),math.floor(height*0.926))
        self.graphicsView.move(math.floor(width*0.47),math.floor(height*0.02))

        #Resize title and intials
        self.titleText.resize(math.floor(width*0.2), math.floor(height*0.02))
        self.titleText.setFont(QFont("Rubik.tff", math.floor(width*0.2/21)))
        self.titleText.move(math.floor(width*0.01),math.floor(height*0.02))

        self.initials.resize(math.floor(width*0.2), math.floor(height*0.016))
        self.initials.setFont(QFont("Rubik.tff", math.floor(width*0.2/32)))
        self.initials.move(math.floor(width*0.01),math.floor(height*0.048))

        #Resize sliders

        #Number slider
        self.numberSliderName.resize(math.floor(width*0.2), math.floor(height*0.025))
        self.numberSliderName.setFont(QFont("Rubik.tff", math.floor(width*0.2/16)))
        self.numberSliderName.move(math.floor(width*0.01),math.floor(height*0.1))

        self.numberSliderNum.resize(math.floor(width*0.08), math.floor(height*0.05))
        self.numberSliderNum.setFont(QFont("Rubik.tff", math.floor(width*0.2/16)))
        self.numberSliderNum.move(math.floor(width*0.16),math.floor(height*0.089))

        self.numberSlider.resize(math.floor(width*0.2), math.floor(height*0.04))
        self.numberSlider.move(math.floor(width*0.011),math.floor(height*0.14))

        #Range slider
        self.rangeSliderName.resize(math.floor(width*0.2), math.floor(height*0.04))
        self.rangeSliderName.setFont(QFont("Rubik.tff", math.floor(width*0.2/16)))
        self.rangeSliderName.move(math.floor(width*0.01),math.floor(height*0.23))

        self.rangeSliderNum.resize(math.floor(width*0.05), math.floor(height*0.05))
        self.rangeSliderNum.setFont(QFont("Rubik.tff", math.floor(width*0.2/16)))
        self.rangeSliderNum.move(math.floor(width*0.118),math.floor(height*0.226))

        self.rangeSlider.resize(math.floor(width*0.2), math.floor(height*0.04))
        self.rangeSlider.move(math.floor(width*0.01),math.floor(height*0.28))

        #Target slider
        self.targetSliderName.resize(math.floor(width*0.2), math.floor(height*0.04))
        self.targetSliderName.setFont(QFont("Rubik.tff", math.floor(width*0.2/16)))
        self.targetSliderName.move(math.floor(width*0.01),math.floor(height*0.37))

        self.targetSliderNum.resize(math.floor(width*0.05), math.floor(height*0.05))
        self.targetSliderNum.setFont(QFont("Rubik.tff", math.floor(width*0.2/16)))
        self.targetSliderNum.move(math.floor(width*0.073),math.floor(height*0.365))

        self.targetSlider.resize(math.floor(width*0.2), math.floor(height*0.04))
        self.targetSlider.move(math.floor(width*0.01),math.floor(height*0.42))

        #Reset button
        self.resetButton.resize(math.floor(width*0.15), math.floor(height*0.06))
        self.resetButton.move(math.floor(width*0.035),math.floor(height*0.50))

        #Start button
        self.startButton.resize(math.floor(width*0.17), math.floor(height*0.1))
        self.startButton.move(math.floor(width*0.025),math.floor(height*0.60))

        #Inactive sensors
        self.inactiveSensors.resize(math.floor(width*0.16), math.floor(height*0.1))
        self.inactiveSensors.move(math.floor(width*0.26),math.floor(height*0.06))
        self.inactiveSensors.setFont(QFont("Rubik.tff", math.floor(width*0.2/16)))

        self.inactiveSensorsNum.resize(math.floor(width*0.05), math.floor(height*0.1))
        self.inactiveSensorsNum.move(math.floor(width*0.393), math.floor(height*0.06))
        self.inactiveSensorsNum.setFont(QFont("Rubik.tff", math.floor(width*0.2/16)))

        #Progress Bar
        self.progressBarName.resize(math.floor(width*0.2), math.floor(height*0.1))
        self.progressBarName.move(math.floor(width*0.25),math.floor(height*0.50))
        self.progressBarName.setFont(QFont("Rubik.tff", math.floor(width*0.2/16)))

        self.progressBar.resize(math.floor(width*0.2), math.floor(height*0.1))
        self.progressBar.move(math.floor(width*0.25),math.floor(height*0.60))
        

    def create_widgets(self, stylesheet, buttonStylesheet):
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
        self.titleText.setFont(QFont("Rubik.tff", 20))
        self.titleText.setGeometry(QtCore.QRect(20, 10, 420, 61))
        self.titleText.setStyleSheet(str(stylesheet, encoding='utf-8'))

        self.initials = QLabel(self.centralwidget)
        self.initials.setText("Filip Dabrowski")
        self.initials.setFont(QFont("Rubik.tff", 18))
        self.initials.setGeometry(QtCore.QRect(0, 0, 360, 30))
        self.initials.setStyleSheet(str(stylesheet, encoding='utf-8'))
        self.initials.setStyleSheet("color: white;")

        #Reset sensor position
        self.resetButton = QPushButton("Reset sensors", self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(110, 1000, 340, 51))
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
        self.numberSliderName.setFont(QFont("Rubik.tff", 24))
        self.numberSliderName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Number slider num
        self.numberSliderNum = QLabel(self.centralwidget)
        self.numberSliderNum.setText("30")
        self.numberSliderNum.setFont(QFont("Rubik.tff", 24))
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
        self.rangeSliderName.setFont(QFont("Rubik.tff", 24))
        self.rangeSliderName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Range slider num
        self.rangeSliderNum = QLabel(self.centralwidget)
        self.rangeSliderNum.setGeometry(QtCore.QRect(120, 580, 141, 61))
        self.rangeSliderNum.setText("10")
        self.rangeSliderNum.setFont(QFont("Rubik.tff", 32))
        self.rangeSliderNum.setStyleSheet(str(stylesheet, encoding='utf-8'))
        self.rangeSliderNum.setStyleSheet("color: white;")

        #Target slider
        self.targetSlider = QSlider(Qt.Horizontal, self.centralwidget)
        self.targetSlider.setGeometry(QtCore.QRect(30, 520, 331, 51))
        self.targetSlider.setMinimum(0)
        self.targetSlider.setMaximum(25)
        self.targetSlider.setTickInterval(10)
        self.targetSlider.setValue(10)
        self.targetSlider.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Target slider name
        self.targetSliderName = QLabel(self.centralwidget)
        self.targetSliderName.setGeometry(QtCore.QRect(30, 430, 351, 61))
        self.targetSliderName.setText("Targets:")
        self.targetSliderName.setFont(QFont("Rubik.tff", 24))
        self.targetSliderName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Target slider num
        self.targetSliderNum = QLabel(self.centralwidget)
        self.targetSliderNum.setGeometry(QtCore.QRect(120, 580, 141, 61))
        self.targetSliderNum.setText("0")
        self.targetSliderNum.setFont(QFont("Rubik.tff", 32))
        self.targetSliderNum.setStyleSheet(str(stylesheet, encoding='utf-8'))
        self.targetSliderNum.setStyleSheet("color: white;")

        #Inactive sensors
        self.inactiveSensors = QLabel(self.centralwidget)
        self.inactiveSensors.setGeometry(QtCore.QRect(500, 80, 350, 60))
        self.inactiveSensors.setText("Inactive Sensors:")
        self.inactiveSensors.setFont(QFont("Rubik.tff", 24))
        self.inactiveSensors.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Inactive sensors num
        self.inactiveSensorsNum = QLabel(self.centralwidget)
        self.inactiveSensorsNum.setGeometry(QtCore.QRect(760, 82, 60, 60))
        self.inactiveSensorsNum.setText("0")
        self.inactiveSensorsNum.setFont(QFont("Rubik.tff", 24))
        self.inactiveSensorsNum.setStyleSheet(str(stylesheet, encoding='utf-8'))
        self.inactiveSensorsNum.setStyleSheet("color: white;")

        #Battery life progress bar
        self.progressBarName = QLabel(self.centralwidget)
        self.progressBarName.setGeometry(QtCore.QRect(400, 530, 351, 61))
        self.progressBarName.setText("Sensors battery life")
        self.progressBarName.setFont(QFont("Rubik.tff", 24))
        self.progressBarName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(500, 382, 370, 60))
        self.progressBar.setValue(100)
        self.progressBar.setStyleSheet(str(stylesheet, encoding='utf-8'))

        #Simulation mode buttons

        self.modeName = QLabel(self.centralwidget)
        self.modeName.setGeometry(QtCore.QRect(540, 210, 351, 61))
        self.modeName.setText("Simulation mode")
        self.modeName.setFont(QFont("Rubik.tff", 24))
        self.modeName.setStyleSheet(str(stylesheet, encoding='utf-8'))

        self.targetButton = QPushButton("Target", self.centralwidget)
        self.targetButton.setGeometry(QtCore.QRect(500, 280, 340, 120))
        self.targetButton.setStyleSheet(str(buttonStylesheet, encoding='utf-8')) 

        self.areaButton = QPushButton("Area", self.centralwidget)
        self.areaButton.setGeometry(QtCore.QRect(500, 420, 340, 120))
        self.areaButton.setStyleSheet(str(stylesheet, encoding='utf-8'))     

    def reset(self):
        self.progressBar.setValue(100)
        self.network_display.ResetSensors(self.numberSlider.value(), self.rangeSlider.value())

    def draw_network(self):
        self.update_label(self.inactiveSensorsNum, self.network_display.inactive_sensors)
        pass

    def update_label(self, label_widget, value):
        # Aktualizuj etykietę na podstawie przekazanego widgetu i wartości suwaka
        label_widget.setText(str(value))
    
    def decreaseBatteryLife(self):
        # Decrease battery life by 10% every 200 milliseconds
        if self.progressBar.value() > 0:
            self.progressBar.setValue(self.progressBar.value() - 1)
            for i, sensor in enumerate(self.network_display.sensors):
                if sensor.isActive:
                    sensor.fade_range_area(self.progressBar.value())
                        
        else:
            self.timer.stop()
            self.network_display.simulation()
            self.update_label(self.inactiveSensorsNum, self.network_display.inactive_sensors)
            print(self.network_display.monitoringAnyTarget)
            if self.network_display.sensors and self.network_display.simulationMode == 'A' or self.network_display.monitoringAnyTarget:
                self.progressBar.setValue(100)
                self.startBatteryDecrease()
            else:
                self.progressBar.setValue(0)
                #Enable Ui interactive widgets:
                self.changeUIstate(True)
                
    def changeUIstate(self, state):
        self.numberSlider.setEnabled(state)
        self.rangeSlider.setEnabled(state)
        self.startButton.setEnabled(state)
        self.resetButton.setEnabled(state)
        self.targetSlider.setEnabled(state)

    def startBatteryDecrease(self):
        #disable UI interactive widgets:
        self.changeUIstate(False)
        if not self.network_display.sensors:
            message_box = QMessageBox()
            message_box.setWindowTitle("Cannot start the simulation")
            message_box.setText("All of the sensors ran out of their battery")
            message_box.setStyleSheet("QMessageBox { background-color: #333333; } QMessageBox QLabel { color: white; }")
            message_box.exec_()
            self.changeUIstate(True)
            return
        if not self.network_display.monitoringAnyTarget and self.network_display.simulationMode == 'T':
            message_box = QMessageBox()
            message_box.setWindowTitle("Cannot start the simulation")
            message_box.setText("None of the targets is being monitored")
            message_box.setStyleSheet("QMessageBox { background-color: #333333; } QMessageBox QLabel { color: white; }")
            message_box.exec_()
            self.changeUIstate(True)
            return
        self.progressBar.setValue(100)
        self.timer = QTimer()
        self.timer.timeout.connect(self.decreaseBatteryLife)
        self.timer.start(10)  # Decrease battery every 200 milliseconds

    #Change simulation mode and switch button stylesheets
    def changeSimulationMode(self, mode, stylesheet, buttonStylesheet):
        if mode == "Target":
            self.network_display.simulationMode = 'T'
            self.targetButton.setStyleSheet(str(stylesheet, encoding='utf-8')) 
            self.areaButton.setStyleSheet(str(buttonStylesheet, encoding='utf-8'))
        elif mode == "Area":
            self.network_display.simulationMode = 'A'
            self.targetButton.setStyleSheet(str(buttonStylesheet, encoding='utf-8')) 
            self.areaButton.setStyleSheet(str(stylesheet, encoding='utf-8'))
        else:
            print("Mode must be \"Target\" or \"Area\"")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
