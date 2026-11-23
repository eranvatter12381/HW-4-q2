import sys
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog
)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from About import AboutWindow


class IceCreamWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("רווחים ממכירת גלידה")
        self.resize(750, 600)
        self.temperatures = []
        self.revenues = []
        self.about_window = AboutWindow()
        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        self.load_btn = QPushButton("בחר קובץ נתונים")
        self.load_btn.clicked.connect(self.load_file)
        self.about_btn = QPushButton("About")
        self.about_btn.clicked.connect(self.about_window.show)
        top_layout.addWidget(self.load_btn)
        top_layout.addWidget(self.about_btn)
        main_layout.addLayout(top_layout)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)
        self.setLayout(main_layout)
        self.plot_graph()

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "בחר קובץ גלידה", "", "CSV Files (*.csv)")
        if not file_path:
            return
        self.temperatures = []
        self.revenues = []
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            self.temperatures.append(float(parts[0]))
            self.revenues.append(float(parts[1]))
        self.plot_graph()

    def plot_graph(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        if not self.temperatures:
            ax.set_title("Load Ice Cream.csv to view data")
            self.canvas.draw()
            return
        ax.scatter(self.temperatures, self.revenues, s=1)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_title("Ice Cream Revenue vs. Temperature")
        ax.set_xlabel("Temperature (°C)")
        ax.set_ylabel("Revenue ($)")
        x = np.array(self.temperatures)
        y = np.array(self.revenues)
        m, b = np.polyfit(x, y, 1)
        trendline = m * x + b
        ax.plot(x, trendline, color="red", linewidth=2)
        equation = f"y = {m:.2f}x + {b:.2f}"
        ax.text(0.05, 0.90, equation, transform=ax.transAxes, fontsize=12, color="red", fontweight="bold")
                self.canvas.draw()
if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = IceCreamWindow()
    window.show()
    sys.exit(app.exec())