from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraphBase(FigureCanvas):
    def __init__(self, parent=None, activeSensors=None, monitoredData=None, subsetCount=0, title='', xlabel='', ylabel=''):
        super().__init__(Figure(figsize=(6, 4), facecolor="#333333"))
        self.setParent(parent)
        self.activeSensors = activeSensors
        self.monitoredData = monitoredData
        self.subsetCount = subsetCount
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.plot()

    def plot(self):
        #Return if the data does not exist
        if not self.activeSensors or  not self.monitoredData:
            print("Data necessary for the graph does not exist")
            return
        
        ax = self.figure.add_subplot(111)
        ax.clear()

        x_values = range(1, self.subsetCount + 1)
        ax.plot(x_values, self.activeSensors, label='Active', marker='o', color='#017365')
        ax.plot(x_values, self.monitoredData, label='Monitored', marker='o', color='red')

        ax.set_xlabel(self.xlabel, color='white')
        ax.set_ylabel(self.ylabel, color='white')
        ax.set_title(self.title, color='white')
        ax.legend(loc='upper right', fontsize='small', facecolor='black', edgecolor='white', labelcolor='white')
        ax.set_xticks(x_values)
        
        ax.set_facecolor('#252525')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('#017365')
        ax.spines['left'].set_color('#017365')
        ax.spines['top'].set_color('#017365')
        ax.spines['right'].set_color('#017365')

        self.draw()

class GraphArea(GraphBase):
    def __init__(self, parent=None, activeSensors=None, monitoredData=None, subsetCount=0):
        super().__init__(parent, activeSensors, monitoredData, subsetCount, 'Active sensors and monitored area', 'Subsets', 'Values')

class GraphTarget(GraphBase):
    def __init__(self, parent=None, activeSensors=None, monitoredData=None, subsetCount=0):
        super().__init__(parent, activeSensors, monitoredData, subsetCount, 'Active sensors and monitored targets', 'Subsets', 'Values')

class GraphWindow(QMainWindow):
    def __init__(self, activeSensors, monitored, subsetCount, simulation_mode):
        super().__init__()
        self.setWindowTitle('Simulation results')
        self.setWindowIcon(QIcon("Images/logo.png"))
        self.setGeometry(810, 390, 800, 600)
        self.setStyleSheet("QMainWindow {background-color: #252525; color: white;}")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        if simulation_mode == 'A':
            self.plot_canvas = GraphArea(self, activeSensors, monitored, subsetCount)
            layout.addWidget(self.plot_canvas)
        elif simulation_mode == 'T':
            self.plot_canvas = GraphTarget(self, activeSensors, monitored, subsetCount)
            layout.addWidget(self.plot_canvas)