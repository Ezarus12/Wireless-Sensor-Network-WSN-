from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QColor
import math 

sensor_color_active = QColor(14, 236, 210)
sensor_color_inActive = QColor(105, 105, 105)
sensor_color_off = QColor(85, 85, 85)

#Sensor class containg postition, range, and states for the sensor, representing it by the dot and semi-translucent range area
class Sensor(QGraphicsEllipseItem):
    def __init__(self, x: int, y: int, size: int, range: int):
        super().__init__(x, y, size, size) #initiaite parent object
        self.xPos = x
        self.yPos = y        
        self.range = range
        self.rangeAreaOpacity = 50 # Percentage value of the range area opacity
        self.setBrush(QBrush(sensor_color_active))  # Sensor color

        #Flags
        self.isActive = True
        self.hasPower = True
        self.monitoring = False #Is sensor monitoring any target

    def draw_range(self):
        #Allign the range area to the sensor's position
        self.range_area = QGraphicsEllipseItem(self.xPos + (0.5*self.rect().width()) - (0.5*self.range), self.yPos + (0.5*self.rect().height()) - (0.5*self.range), self.range, self.range)
        self.range_area.setBrush(QBrush(QColor(32, 179, 162, self.rangeAreaOpacity))) #Range color at 50% opacity
        return 

    def change_color_inactive(self):
        self.setBrush(QBrush(sensor_color_inActive))  # Sensor color
        self.range_area.setBrush(QBrush(QColor(3, 57, 51, self.rangeAreaOpacity))) # Range area color

    def change_color_active(self):
        self.setBrush(QBrush(sensor_color_active))  # Sensor color
        self.range_area.setBrush(QBrush(QColor(32, 179, 162, self.rangeAreaOpacity))) # Range area color

    def change_color_off(self):
        self.setBrush(QBrush(sensor_color_off))  # Sensor color
        self.range_area.setBrush(QBrush(QColor(3, 57, 51, 0))) # Range area color

    #Fade the sensor's area by the given percentage (Lower the opacity)
    # value (int): percentage value to fade the area
    def fade_range_area(self, value):
        opacity = math.floor(self.rangeAreaOpacity*((value/100)))
        self.range_area.setBrush(QBrush(QColor(255, 0, 0, opacity)))

