from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem, QGraphicsPixmapItem, QApplication, QGraphicsLineItem, QMessageBox
from PyQt5.QtGui import QBrush, QColor, QPixmap, QPen
from PyQt5.QtCore import Qt, QTimer
import random
import math
import time
from sensor import Sensor
from target import Target

class NetworkDisplay:
    def __init__(self, graphics_view):
        self.scene = QGraphicsScene()
        self.sensorNum = 40
        self.sensorRange = 100
        self.sensorSize = 10
        self.detectionRange = 1000
        self.inactive_sensors = 0
        self.simulationMode = '' # [A] - For area coverage and [T] - For target coverage
        self.targetNum = 10
        self.monitoringAnyTarget = False
        self.visualizeSensorsComunnication = False
        self.delayVSN = False
        # Representation of sensors
        self.sensors = []
        self.targets = []
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

        if self.simulationMode == 'T':
            self.generateTargets(self.targetNum)



        for i in range(self.sensorNum):
            sensorX = random.randint(math.floor(self.sensorRange*0.5), math.floor(990-self.sensorRange*0.5))
            sensorY = random.randint(math.floor(self.sensorRange*0.5), math.floor(990-self.sensorRange*0.5))
            sensor = Sensor(sensorX, sensorY, self.sensorSize, self.sensorRange)  # Sensor position, size, and range
            sensor.draw_range()  # Draw the sensor range
            self.scene.addItem(sensor)
            self.scene.addItem(sensor.range_area)
            self.sensors.append(sensor)

        if self.simulationMode == 'T':
            self.createSubsetTarget()
        else:
            self.createSubset()
            
    def generateTargets(self, num):
        for i in range(num):
            targetX = random.randint(math.floor(self.sensorRange*0.5), math.floor(990-self.sensorRange*0.5))
            targetY = random.randint(math.floor(self.sensorRange*0.5), math.floor(990-self.sensorRange*0.5))
            target = Target(targetX, targetY, 15)
            self.targets.append(target)
            self.scene.addItem(target)

    def visualizeNetwork(self, sensor, other_sensor):
        #Draw a line between two sensors
        line = QGraphicsLineItem(sensor.xPos + self.sensorSize/2, sensor.yPos + self.sensorSize/2 , other_sensor.xPos + self.sensorSize/2, other_sensor.yPos + self.sensorSize/2)
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(Qt.red)
        line.setPen(pen)
        line.setOpacity(0.1)
        self.scene.addItem(line)
        QApplication.processEvents()
        if self.delayVSN:
            time.sleep(0.01)  

    def createSubset(self):
        for i, sensor in enumerate(self.sensors):
            for j, other_sensor in enumerate(self.sensors[i+1:], start=i+1):
                distance = math.sqrt(((sensor.xPos - other_sensor.xPos) ** 2) + ((sensor.yPos - other_sensor.yPos) ** 2))
                if distance <= self.detectionRange: #change to neightbaurs range
                    if distance <= (self.sensorRange / 2) and sensor.isActive and sensor.hasPower:
                        self.inactive_sensors += 1
                        sensor.isActive = False
                        sensor.change_color_inactive()
                    if self.visualizeSensorsComunnication:
                        self.visualizeNetwork(sensor, other_sensor)


    def createSubsetTarget(self):
        for sensor in self.sensors:
            for target in self.targets:
                distance = math.sqrt(((sensor.xPos - target.xPos) ** 2) + ((sensor.yPos - target.yPos) ** 2))
                if distance <= (self.sensorRange / 2) and not target.monitored:
                    target.monitored = True
                    sensor.monitoring = True
                    self.monitoringAnyTarget = True
            if not sensor.monitoring:
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
        if self.simulationMode == 'T':
            for i, target in enumerate(self.targets):
                target.monitored = False
                if i + 1 == self.targetNum:
                    self.monitoringAnyTarget = False
            self.createSubsetTarget()
        else:
            self.createSubset()
        self.scene.update()
    
    def simulation(self):
        self.nextSubset()
        QApplication.processEvents()  # Process pending GUI events
            
            

    def ResetSensors(self, sensorNum, range, targetNum):
        self.scene.clear() #Clearing the scene of all the previous sensor and ranges
        self.sensors.clear()
        self.targets.clear()
        self.set_sensorNum(sensorNum)
        self.set_sensorRange(range)
        self.set_targetNum(targetNum)
        self.draw_network()
    
    def set_sensorNum(self, num):
        self.sensorNum = num
        
    def set_sensorRange(self, num):
        self.sensorRange = num*10

    def set_targetNum(self, num):
        self.targetNum = num

    def set_detectionRange(self, num):
        self.detectionRange = num

    def load_terrainImage(self, name):
        self.terrain_image = QPixmap(name)
        if self.terrain_image.isNull():
            print("Error: Failed to load terrain image")
            return