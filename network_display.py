from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem, QGraphicsPixmapItem, QApplication
from PyQt5.QtGui import QBrush, QColor, QPixmap
import random
import math
import time
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
            
            
 
    def createSubset(self):
        for i, sensor in enumerate(self.sensors):
            for j, other_sensor in enumerate(self.sensors[i+1:], start=i+1):
                distance = math.sqrt(((sensor.xPos - other_sensor.xPos) ** 2) + ((sensor.yPos - other_sensor.yPos) ** 2))
                if distance <= (self.sensorRange / 2) and sensor.isActive and sensor.hasPower:
                    self.inactive_sensors += 1
                    sensor.isActive = False
                    sensor.change_color_inactive()

    #Create next subset of sensors and turn off all the sensors from the previous subset
    def nextSubset(self):
        to_remove = []
        for sensor in self.sensors:
            if sensor.isActive:
                sensor.hasPower = False
                sensor.change_color_off()
            else:
                sensor.isActive = True
                sensor.change_color_active()
            if not sensor.hasPower:
                to_remove.append(sensor)

        #Deleting dead sensors
        for sensor in to_remove:
            self.sensors.remove(sensor)
        self.inactive_sensors = 0
        self.createSubset()
        self.scene.update()
    
    def simulation(self):
        #while self.sensors:
            #time.sleep(2)  # Pause for 2 seconds before the next iteration
            print("odpalone")
            self.nextSubset()
            self.scene.update()  # Manually trigger the scene update
            QApplication.processEvents()  # Process pending GUI events
            
            

    def fun(self, num, range):
        self.scene.clear() #Clearing the scene of all the previous sensor and ranges
        self.sensors.clear()
        self.set_sensorNum(num)
        self.set_sensorRange(range)
        self.draw_network()
    
    def set_sensorNum(self, num):
        self.sensorNum = num
        
    def set_sensorRange(self, num):
        self.sensorRange = num*10

    def load_terrainImage(self, name):
        self.terrain_image = QPixmap(name)
        if self.terrain_image.isNull():
            print("Error: Failed to load terrain image")
            return