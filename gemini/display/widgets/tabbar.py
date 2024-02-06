from __future__ import annotations

import PySide6.QtWidgets

import gemini


class TabBar:
    def __init__(self, parent: PySide6.QtWidgets.QWidget):
        self.widget = PySide6.QtWidgets.QFrame(parent)
        self.layout = PySide6.QtWidgets.QHBoxLayout(parent)
        self.widget.setLayout(self.layout)
        self.widget.show()
        self.tabs = []
        self.active = 0

    class _Tab:
        def __init__(self, url: str, tab_bar: gemini.display.widgets.TabBar):
            self.url = url
            self.body = ""
            self.status = 0
            self.tab_bar = tab_bar
            self.widget = PySide6.QtWidgets.QFrame(self.tab_bar.widget)
            self.widget.setFrameStyle(PySide6.QtWidgets.QFrame.Shape.StyledPanel)
            self.tab_bar.layout.addWidget(self.widget)
            self.widget.show()

    def new_tab(self, url: str = "about:none") -> None:
        self.tabs.append(self._Tab(url, self))
