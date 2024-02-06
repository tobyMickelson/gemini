import sys

import PySide6.QtWidgets

import gemini


app = PySide6.QtWidgets.QApplication([])
window = gemini.display.Window()
storage = gemini.Storage("conf.json")
tree = gemini.display.widgets.ConfigTree(storage)
tab_bar = gemini.display.widgets.TabBar(window.window)
tab_bar.new_tab("a")
tab_bar.new_tab("a")
tab_bar.new_tab("a")

window.start()
sys.exit(app.exec())
