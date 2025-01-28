import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QWidget,
    QGridLayout,
    QHBoxLayout,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class SilverCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Silver Calculator")
        self.setGeometry(100, 100, 400, 500)
        self.setWindowIcon(QIcon("icon.png"))
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        main_layout = QVBoxLayout()
        self.central_widget.setLayout(main_layout)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet(
            """
            font-size: 32px;
            padding: 10px;
            background: #ffffff;
            border: 2px solid #cccccc;
            border-radius: 10px;
            color: #333333;
            """
        )
        main_layout.addWidget(self.display)

        self.button_grid = QGridLayout()
        main_layout.addLayout(self.button_grid)

        buttons = [
            "C", "←", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "=", ""
        ]

        for i, button in enumerate(buttons):
            if button:
                row = i // 4
                col = i % 4
                btn = QPushButton(button)
                btn.setStyleSheet(
                    """
                    QPushButton {
                        font-size: 18px;
                        padding: 15px;
                        background: #f9f9f9;
                        border: 2px solid #dddddd;
                        border-radius: 8px;
                        color: #333333;
                    }
                    QPushButton:hover {
                        background: #e6f7ff;
                        border: 2px solid #66b3ff;
                    }
                    QPushButton:pressed {
                        background: #cceeff;
                    }
                    """
                )
                btn.clicked.connect(self.on_button_click)
                self.button_grid.addWidget(btn, row, col)

        footer_layout = QHBoxLayout()
        footer_label = QPushButton("Silver Calculator", self)
        footer_label.setStyleSheet(
            "font-size: 12px; color: #888; background: none; border: none; padding: 5px;"
        )
        footer_layout.addStretch()
        footer_layout.addWidget(footer_label)
        footer_layout.addStretch()
        main_layout.addLayout(footer_layout)

        self.central_widget.setStyleSheet("background-color: #f4f4f4;")

    def on_button_click(self):
        sender = self.sender().text()

        if sender == "C":
            self.display.clear()
        elif sender == "←":
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        elif sender == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        elif sender == "%":
            try:
                result = float(self.display.text()) / 100
                self.display.setText(str(result))
            except ValueError:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + sender)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SilverCalculator()
    window.show()
    sys.exit(app.exec_())
