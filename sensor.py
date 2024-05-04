from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QColor
import math 

class Sensor(QGraphicsEllipseItem):
    def __init__(self, x, y, size, range):
        super().__init__(x, y, size, size)
        self.xPos = x
        self.yPos = y        
        self.range = range
        self.setBrush(QBrush(QColor(14, 236, 210)))  # Sensor color

        #Flags
        self.isActive = True
        self.hasPower = True
        
    def draw_range(self):
        self.range_area = QGraphicsEllipseItem(self.xPos + (0.5*self.rect().width()) - (0.5*self.range), self.yPos + (0.5*self.rect().height()) - (0.5*self.range), self.range, self.range)
        self.range_area.setBrush(QBrush(QColor(32, 179, 162, 50)))
        return 

    def change_color_inactive(self):
        self.setBrush(QBrush(QColor(105, 105, 105)))  # Sensor color
        self.range_area.setBrush(QBrush(QColor(3, 57, 51, 50)))

    def change_color_active(self):
        self.setBrush(QBrush(QColor(14, 236, 210)))  # Sensor color
        self.range_area.setBrush(QBrush(QColor(32, 179, 162, 50)))

    def change_color_off(self):
        self.setBrush(QBrush(QColor(85, 85, 85)))  # Sensor color
        self.range_area.setBrush(QBrush(QColor(3, 57, 51, 0)))