from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Graph(FigureCanvas):
    def __init__(self, parent=None, active_sensors=None, monitored_area=None, subset_count=0):
        super().__init__(Figure(figsize=(6, 4), facecolor="#333333"))
        self.setParent(parent)
        self.active_sensors = active_sensors
        self.monitored_area = monitored_area
        self.subset_count = subset_count
        self.plot()

    def plot(self):
        if self.active_sensors is None or self.monitored_area is None:
            return
        
        ax = self.figure.add_subplot(111)
        ax.clear()

        # Plotting the line chart
        x_values = range(1, self.subset_count + 1)  # Tworzenie listy wartości dla osi X
        ax.plot(x_values, self.active_sensors, label='Active sensors', marker='o', color='#017365')
        ax.plot(x_values, self.monitored_area, label='Monitored area (%)', marker='o', color='red')  

        ax.set_xlabel('Subsets', color='white')
        ax.set_ylabel('Values', color='white')
        ax.set_title('Active sensors and Monitored area by Subset', color='white')
        ax.legend(loc='upper right', fontsize='small', facecolor='black', edgecolor='white', labelcolor='white')
        ax.set_xticks(x_values)
        
        # Ustawienie koloru tła obszaru wykresu
        ax.set_facecolor('#333333')

        self.draw()

    def set_subset_count(self, subset_count):
        self.subset_count = subset_count
        self.plot()

class GraphWindow(QMainWindow):
    def __init__(self, active_sensors, monitored_area, subset_count):
        super().__init__()
        self.setWindowTitle('Simulation results')
        self.setGeometry(300, 300, 800, 600)
        self.setStyleSheet("QMainWindow {background-color: black; color: white;}")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.plot_canvas = Graph(self, active_sensors, monitored_area, subset_count)
        layout.addWidget(self.plot_canvas)