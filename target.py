from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QColor

class Target(QGraphicsEllipseItem):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        self.xPos = x
        self.yPos = y        
        self.setBrush(QBrush(QColor(255, 0, 0)))  # Sensor color

        #Flags
        self.monitored = False #Is target being monitored by any sensor

    def getX(self):
        return self.xPos
    
    def getY(self):
        return self.yPos