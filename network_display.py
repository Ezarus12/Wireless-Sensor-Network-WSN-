from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem, QGraphicsPixmapItem
from PyQt5.QtGui import QBrush, QColor, QPixmap
import random
import math
from sensor import Sensor

class NetworkDisplay:
    def __init__(self, graphics_view):
        self.scene = QGraphicsScene()
        self.sensorNum = 40
        self.sensorRange = 100
        self.inactive_sensors = 0
        # Representation of sensors
        self.sensors = []
        graphics_view.setScene(self.scene)
        # Load terrain image
        self.terrain_image = QPixmap("terrain_image.jpg")
        if self.terrain_image.isNull():
            print("Error: Failed to load terrain image")
            return
        self.draw_network()

    def draw_network(self):
        # Create a QGraphicsPixmapItem from the QPixmap
        terrain_pixmap_item = QGraphicsPixmapItem(self.terrain_image)
        self.scene.addItem(terrain_pixmap_item)
        self.inactive_sensors = 0

        for i in range(self.sensorNum):
            sensorSize = 10
            sensorX = random.randint(math.floor(self.sensorRange*0.5), math.floor(990-self.sensorRange*0.5))
            sensorY = random.randint(math.floor(self.sensorRange*0.5), math.floor(990-self.sensorRange*0.5))
            sensor = Sensor(sensorX, sensorY, sensorSize, self.sensorRange)  # Sensor position, size, and range
            
            sensor.draw_range()  # Draw the sensor range
            self.scene.addItem(sensor)
            self.scene.addItem(sensor.range_area)
            self.sensors.append(sensor)

            self.createSubset()
            
        print("Inactive sensors: ", self.inactive_sensors)    
 
    def createSubset(self):
        for i, sensor in enumerate(self.sensors):
            for j, other_sensor in enumerate(self.sensors[i+1:], start=i+1):
                distance = math.sqrt(((sensor.xPos - other_sensor.xPos) ** 2) + ((sensor.yPos - other_sensor.yPos) ** 2))
                if distance <= (self.sensorRange / 2) and sensor.isActive and sensor.hasPower:
                    self.inactive_sensors += 1
                    sensor.isActive = False
                    sensor.change_color_inactive()


    def nextSubset(self):
        for sensor in self.sensors:
            if sensor.isActive:
                sensor.hasPower = False
                sensor.change_color_off()
            else:
                sensor.isActive = True
                sensor.change_color_active()
        for sensor in self.sensors:
                if not sensor.hasPower:
                    self.sensors.remove(sensor)
        self.createSubset()
        self.scene.update()

    def fun(self, num, range):
        self.scene.clear() #Clearing the scene of all the previous sensor and ranges
        self.sensors.clear()
        self.set_sensorNum(num)
        self.set_sensorRange(range)
        self.draw_network()
    
    def set_sensorNum(self, num):
        self.sensorNum = num
        
    def set_sensorRange(self, num):
        self.sensorRange = num

    def load_terrainImage(self, name):
        self.terrain_image = QPixmap(name)
        if self.terrain_image.isNull():
            print("Error: Failed to load terrain image")
            return