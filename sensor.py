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

    def draw_range(self):
        range_circle = QGraphicsEllipseItem(self.xPos + (0.5*self.rect().width()) - (0.5*self.range), self.yPos + (0.5*self.rect().height()) - (0.5*self.range), self.range, self.range)
        range_circle.setBrush(QBrush(QColor(30, 119, 109, 50)))
        return range_circle