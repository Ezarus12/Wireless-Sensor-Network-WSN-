from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraphArea(FigureCanvas):
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

        # Creating graph
        x_values = range(1, self.subset_count + 1)  # Tworzenie listy wartości dla osi X
        ax.plot(x_values, self.active_sensors, label='Active sensors', marker='o', color='#017365')
        ax.plot(x_values, self.monitored_area, label='Monitored area (%)', marker='o', color='red')  

        ax.set_xlabel('Subsets', color='white')
        ax.set_ylabel('Values', color='white')
        ax.set_title('Active sensors and monitored area', color='white')
        ax.legend(loc='upper right', fontsize='small', facecolor='black', edgecolor='white', labelcolor='white')
        ax.set_xticks(x_values)
        
        # Background color
        ax.set_facecolor('#252525')

        # Ticks and spines colors
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('#017365')
        ax.spines['left'].set_color('#017365')
        ax.spines['top'].set_color('#017365')
        ax.spines['right'].set_color('#017365')

        self.draw()

    def set_subset_count(self, subset_count):
        self.subset_count = subset_count
        self.plot()

class GraphTarget(FigureCanvas):
    def __init__(self, parent=None, active_sensors=None, monitored_targets=None, subset_count=0):
        super().__init__(Figure(figsize=(6, 4), facecolor="#333333"))
        self.setParent(parent)
        self.active_sensors = active_sensors
        self.monitored_area = monitored_targets
        self.subset_count = subset_count
        self.plot()

    def plot(self):
        if self.active_sensors is None or self.monitored_area is None:
            return
        
        ax = self.figure.add_subplot(111)
        ax.clear()

        # Creating graph
        x_values = range(1, self.subset_count + 1)  # Tworzenie listy wartości dla osi X
        ax.plot(x_values, self.active_sensors, label='Active sensors', marker='o', color='#017365')
        ax.plot(x_values, self.monitored_area, label='Monitored Targets', marker='o', color='red')  

        ax.set_xlabel('Subsets', color='white')
        ax.set_ylabel('Values', color='white')
        ax.set_title('Active sensors and monitored targets', color='white')
        ax.legend(loc='upper right', fontsize='small', facecolor='black', edgecolor='white', labelcolor='white')
        ax.set_xticks(x_values)
        
        # Background color
        ax.set_facecolor('#252525')

        # Ticks and spines colors
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('#017365')
        ax.spines['left'].set_color('#017365')
        ax.spines['top'].set_color('#017365')
        ax.spines['right'].set_color('#017365')

        self.draw()
        
    def set_subset_count(self, subset_count):
        self.subset_count = subset_count
        self.plot()

class GraphWindow(QMainWindow):
    def __init__(self, active_sensors, monitored, subset_count, simulation_mode):
        super().__init__()
        self.setWindowTitle('Simulation results')
        self.setWindowIcon(QIcon("Images/logo.png"))
        self.setGeometry(810, 390, 800, 600)
        self.setStyleSheet("QMainWindow {background-color: #252525; color: white;}")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        if simulation_mode == 'A':
            self.plot_canvas = GraphArea(self, active_sensors, monitored, subset_count)
            layout.addWidget(self.plot_canvas)
        elif simulation_mode == 'T':
            self.plot_canvas = GraphTarget(self, active_sensors, monitored, subset_count)
            layout.addWidget(self.plot_canvas)