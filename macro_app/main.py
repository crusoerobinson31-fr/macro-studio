from macro_app.ui import MainWindow
from PySide6.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
