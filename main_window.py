from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwags) -> None:
        super().__init__(parent, *args, **kwags)

        self.setWindowTitle("Calculadora")
        self.setFixedSize(421, 455)

        self.central_widget = QWidget()

        self.v_layout = QVBoxLayout()
        self.central_widget.setLayout(self.v_layout)

        self.setCentralWidget(self.central_widget)
