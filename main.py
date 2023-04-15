import sys
import view
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
win = view.view_window()
win.show()
sys.exit(app.exec())
