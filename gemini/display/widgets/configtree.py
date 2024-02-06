from __future__ import annotations

import copy

import PySide6.QtWidgets

import gemini


class ConfigTree(PySide6.QtWidgets.QFrame):
    def __init__(self, storage: gemini.Storage):
        super().__init__()

        self.storage = copy.deepcopy(storage.data)
        self.widget = PySide6.QtWidgets.QTreeWidget()
        self.widget.setColumnCount(2)
        self.widget.setHeaderLabels(["Name", "Type"])

        items = []
        for key, values in self.storage.items():
            item = PySide6.QtWidgets.QTreeWidgetItem([key])
            for value in values:
                child = PySide6.QtWidgets.QTreeWidgetItem([key, str(values)])
                item.addChild(child)
            items.append(item)

        self.widget.insertTopLevelItems(0, items)
