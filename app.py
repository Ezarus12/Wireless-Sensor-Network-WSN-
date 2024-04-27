import sys
import numpy
import math
import matplotlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#Variables
windowHeight = 1080
windowWidth = 1920

class Window(QMainWindow):
    def __init__(self):
        super().__init__() #initializing parent object
    
        self.setWindowTitle("Wireless Sensor Network") # Setting window title

        self.setGeometry(0,0,windowWidth,windowHeight) # Defining window position and resolution

        self.central_widget = QWidget() # Creating central widget
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        #Creating slider for the sensor number
        self.sensor_slider = QSlider(Qt.Horizontal)
        self.sensor_slider.setMinimum(1)
        self.sensor_slider.setMaximum(20)
        self.sensor_slider.setValue(10)
        self.sensor_slider.setTickInterval(1)
        self.sensor_slider.setTickPosition(QSlider.TicksBelow)
        
        self.sensor_slider.setFixedWidth(math.floor(0.2*windowWidth))
        self.sensor_slider.setFixedHeight(math.floor(0.2*windowHeight))

        self.sensor_slider.move(0, 0)
        
        layout.addWidget(self.sensor_slider)
        self.central_widget.setLayout(layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())