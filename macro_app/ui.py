from PySide6.QtWidgets import QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MacroStudio")
        self.setMinimumSize(400, 200)

        label = QLabel("MacroStudio démarre ✅", self)
        label.move(100, 80)
