from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QColor
import random
import math

class NetworkDisplay:
    def __init__(self, graphics_view):
        self.scene = QGraphicsScene()
        self.sensorNum = 40
        self.sensorRange = 100
        graphics_view.setScene(self.scene)
        self.draw_network()
        

    def draw_network(self):
        # Reprezentacja terenu
        terrain_rect = self.scene.addRect(0, 0, 990, 990)  #Terain size fitted to the widget size
        terrain_rect.setBrush(QBrush(QColor(105, 105, 105)))  #Terrain color

        # Reprezentacja sensora
        for i in range(self.sensorNum):
            sensorSize = 10
            sensorX = random.randint(math.floor(self.sensorRange*0.5),math.floor(990-self.sensorRange*0.5))
            sensorY = random.randint(math.floor(self.sensorRange*0.5),math.floor(990-self.sensorRange*0.5))
            sensor = QGraphicsEllipseItem(sensorX, sensorY, sensorSize, sensorSize)  #Sensor position and size
            sensor.setBrush(QBrush(QColor(20, 20, 20)))  #Sensor color

            # Reprezentacja zasięgu sensora
            range_circle = QGraphicsEllipseItem(sensorX + (0.5*sensorSize) - (0.5*self.sensorRange), sensorY + (0.5*sensorSize) - (0.5*self.sensorRange), self.sensorRange, self.sensorRange)  # Przykładowa pozycja i rozmiar zasięgu sensora
            range_circle.setBrush(QBrush(QColor(30, 119, 109, 50)))
            
            self.scene.addItem(range_circle)
            self.scene.addItem(sensor)

    def fun(self, num, range):
        self.scene.clear() #Clearing the scene of all the previous sensor and ranges
        self.set_sensorNum(num)
        self.set_sensorRange(range)
        self.draw_network()
    
    def set_sensorNum(self, num):
        self.sensorNum = num
        
    def set_sensorRange(self, num):
        self.sensorRange = num*10
