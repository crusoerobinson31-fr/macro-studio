from PySide6.QtWidgets import (
    QMainWindow, QPushButton, QTextEdit, QWidget, QVBoxLayout
)

from .player import MacroPlayer
from .macro_engine import Macro

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MacroStudio")
        self.setMinimumSize(500, 350)

        self.macro = Macro()
        self.player = MacroPlayer(self.log)

        # Macro de démonstration
        self.macro.add_step("Click", "Gauche", 0.5)
        self.macro.add_step("Key", "CTRL+C", 0.5)
        self.macro.add_step("Key", "CTRL+V", 0.5)

        self.logbox = QTextEdit()
        self.logbox.setReadOnly(True)

        btn_play = QPushButton("▶ Lancer la macro")
        btn_play.clicked.connect(self.run_macro)

        btn_stop = QPushButton("⏹ Stop")
        btn_stop.clicked.connect(self.player.stop)

        layout = QVBoxLayout()
        layout.addWidget(btn_play)
        layout.addWidget(btn_stop)
        layout.addWidget(self.logbox)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def log(self, message: str):
        self.logbox.append(message)

    def run_macro(self):
        self.player.play(self.macro)
