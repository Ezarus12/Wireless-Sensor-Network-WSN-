import unittest
import sys
import os
from PyQt5.QtGui import QColor

# Add the /src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from target import Target

class TestTarget(unittest.TestCase):
    def setUp(self):
        self.target = Target(100, 100, 10)

    def test_initialization(self):
        self.assertEqual(self.target.xPos, 100)
        self.assertEqual(self.target.yPos, 100)
        self.assertFalse(self.target.monitored)
        self.assertEqual(self.target.brush().color(), QColor(255, 0, 0))

    def test_getX(self):
        self.assertEqual(self.target.getX(), 100)

    def test_getY(self):
        self.assertEqual(self.target.getY(), 100)

if __name__ == '__main__':
    unittest.main()
