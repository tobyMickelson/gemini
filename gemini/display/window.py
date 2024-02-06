from __future__ import annotations

import PySide6.QtWidgets


class Window:
    def __init__(self):
        self.layout = PySide6.QtWidgets.QVBoxLayout()
        self.window = PySide6.QtWidgets.QWidget()
        self.window.setLayout(self.layout)
        self.window.setWindowTitle("QHBoxLayout")

    def start(self):
        self.window.show()
