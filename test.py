import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure(figsize=(6, 4))
        self.ax = self.fig.add_subplot(111)
        super(PlotCanvas, self).__init__(self.fig)
        self.setParent(parent)
        self.plot()

    def plot(self):
        subsets = ['Subset:1', 'Subset:2', 'Subset:3', 'Subset:4', 'Subset:5']
        active_sensors = [65, 23, 4, 1, 0]
        monitored_area = [51.025, 18.055, 3.14, 0.785, 0]

        self.ax.clear()

        # Plotting the line chart
        self.ax.plot(subsets, active_sensors, label='Active sensors', marker='o')
        self.ax.plot(subsets, monitored_area, label='Monitored area (%)', marker='o')

        self.ax.set_xlabel('Subsets')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Active sensors and Monitored area by Subset')
        self.ax.legend()

        self.draw()

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Second Window')
        self.setGeometry(300, 300, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.plot_canvas = PlotCanvas(self)
        layout.addWidget(self.plot_canvas)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Button to open the second window
        self.open_second_window_button = QPushButton('Open Second Window')
        self.open_second_window_button.clicked.connect(self.openSecondWindow)
        layout.addWidget(self.open_second_window_button)

        self.show()

    def openSecondWindow(self):
        self.second_window = SecondWindow()
        self.second_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
