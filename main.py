"""
    Shortest Path Finding Visualization
"""
from src.config import *
from src.mainwindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("fusion"))  # windows / macos / fusion
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
