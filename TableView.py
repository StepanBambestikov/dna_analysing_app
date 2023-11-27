from PyQt5.QtCore import Qt
from PyQt5.QtGui import QClipboard, QGuiApplication, QKeySequence
from PyQt5.QtWidgets import QTableView, QMenu, QAction


class TableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, pos):
        menu = QMenu()
        copyAction = QAction("Copy", self)
        copyAction.triggered.connect(self.copySelection)
        menu.addAction(copyAction)
        menu.exec_(self.viewport().mapToGlobal(pos))

    def copySelection(self):
        selection = self.selectionModel().selectedIndexes()
        if selection:
            rows = sorted(index.row() for index in selection)
            columns = sorted(index.column() for index in selection)
            csv = ""
            for row in range(rows[0], rows[-1] + 1):
                row_data = []
                for column in range(columns[0], columns[-1] + 1):
                    index = self.model().index(row, column)
                    row_data.append(str(self.model().data(index)))
                csv += ",".join(row_data) + "\n"
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(csv)

    def keyPressEvent(self, event):
        if event.matches(QKeySequence.Copy):
            self.copySelection()
        else:
            super().keyPressEvent(event)