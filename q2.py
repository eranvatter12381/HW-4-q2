import sys
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
        # כאן נכתוב יחד את קריאת הקובץ

    def plot_graph(self):
        """מתודה זמנית לציור גרף - נערוך אותה בשלב הבא"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
        ax.set_title("Temporary Graph")
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = IceCreamWindow()
    window.show()
    sys.exit(app.exec())