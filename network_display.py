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

        # Representation of sensors
        sensors = []
        for i in range(self.sensorNum):
            sensorSize = 10
            sensorX = random.randint(math.floor(self.sensorRange*0.5), math.floor(990-self.sensorRange*0.5))
            sensorY = random.randint(math.floor(self.sensorRange*0.5), math.floor(990-self.sensorRange*0.5))
            sensor = Sensor(sensorX, sensorY, sensorSize, self.sensorRange)  # Sensor position, size, and range
            
            range_circle = sensor.draw_range()  # Draw the sensor range

            self.scene.addItem(sensor)
            self.scene.addItem(range_circle)
            sensors.append(sensor)

        print("Bliskosb:")
        for i, sensor in enumerate(sensors):
            for j, other_sensor in enumerate(sensors):
                if i != j:  # Avoid comparing a sensor with itself
                    distance = math.sqrt(((sensor.xPos - other_sensor.xPos) ** 2) + ((sensor.yPos - other_sensor.yPos) ** 2)) #Caluclating the distance from pythagorean theorem
                    if distance <= (self.sensorRange / 2): #Distance is smaller than the radius
                        print("Sensor", i, "and Sensor", sensors.index(other_sensor), "are within range") 
                        print("Distance: ", distance)     

    def fun(self, num, range):
        self.scene.clear() #Clearing the scene of all the previous sensor and ranges
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