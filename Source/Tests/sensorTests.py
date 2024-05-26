import unittest
import sys
import os
from PyQt5.QtGui import QColor


# Add the /src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sensor import Sensor

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = Sensor(100, 100, 20, 50)
        self.sensor.draw_range()

    def test_initialization(self):
        self.assertEqual(self.sensor.xPos, 100)
        self.assertEqual(self.sensor.yPos, 100)
        self.assertEqual(self.sensor.range, 50)
        self.assertEqual(self.sensor.isActive, True)
        self.assertEqual(self.sensor.hasPower, True)
        self.assertEqual(self.sensor.monitoring, False)
        self.assertEqual(self.sensor.brush().color(), QColor(14, 236, 210))

    def test_draw_range(self):
        self.sensor.draw_range()
        self.assertEqual(self.sensor.range_area.rect().width(), 50)
        self.assertEqual(self.sensor.range_area.rect().height(), 50)
        self.assertEqual(self.sensor.range_area.brush().color(), QColor(32, 179, 162, 50))

    def test_fade_range_area(self):
        self.sensor.fade_range_area(20) # 20% of the 50 expected: 10
        self.assertEqual(self.sensor.range_area.brush().color().alpha(), 10)

if __name__ == '__main__':
    unittest.main()
