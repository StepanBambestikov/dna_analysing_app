# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1381, 901)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = TableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(520, 30, 751, 731))
        self.tableView.setObjectName("tableView")
        self.processingTypeFrame = QtWidgets.QFrame(self.centralwidget)
        self.processingTypeFrame.setGeometry(QtCore.QRect(10, 30, 477, 71))
        self.processingTypeFrame.setObjectName("processingTypeFrame")
        self.processingTypeLayout = QtWidgets.QHBoxLayout(self.processingTypeFrame)
        self.processingTypeLayout.setObjectName("processingTypeLayout")
        self.processingTypeLabel = QtWidgets.QLabel(self.processingTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.processingTypeLabel.setFont(font)
        self.processingTypeLabel.setObjectName("processingTypeLabel")
        self.processingTypeLayout.addWidget(self.processingTypeLabel)
        self.processingTypeComboBox = QtWidgets.QComboBox(self.processingTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.processingTypeComboBox.setFont(font)
        self.processingTypeComboBox.setObjectName("processingTypeComboBox")
        self.processingTypeComboBox.addItem("")
        self.processingTypeComboBox.addItem("")
        self.processingTypeComboBox.addItem("")
        self.processingTypeLayout.addWidget(self.processingTypeComboBox)
        self.inputFileFrame = QtWidgets.QFrame(self.centralwidget)
        self.inputFileFrame.setGeometry(QtCore.QRect(10, 400, 486, 161))
        self.inputFileFrame.setObjectName("inputFileFrame")
        self.inputFileInnerFrame = QtWidgets.QFrame(self.inputFileFrame)
        self.inputFileInnerFrame.setGeometry(QtCore.QRect(0, 70, 484, 113))
        self.inputFileInnerFrame.setMinimumSize(QtCore.QSize(484, 113))
        self.inputFileInnerFrame.setObjectName("inputFileInnerFrame")
        self.inputFileInnerLayout = QtWidgets.QFormLayout(self.inputFileInnerFrame)
        self.inputFileInnerLayout.setObjectName("inputFileInnerLayout")
        self.inputFileNameLabel = QtWidgets.QLabel(self.inputFileInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.inputFileNameLabel.setFont(font)
        self.inputFileNameLabel.setObjectName("inputFileNameLabel")
        self.inputFileInnerLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.inputFileNameLabel)
        self.inputFileNameLineEdit = QtWidgets.QLineEdit(self.inputFileInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.inputFileNameLineEdit.setFont(font)
        self.inputFileNameLineEdit.setObjectName("inputFileNameLineEdit")
        self.inputFileInnerLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputFileNameLineEdit)
        self.fileSaltConditionLabel = QtWidgets.QLabel(self.inputFileInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.fileSaltConditionLabel.setFont(font)
        self.fileSaltConditionLabel.setObjectName("fileSaltConditionLabel")
        self.inputFileInnerLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.fileSaltConditionLabel)
        self.browseButton = QtWidgets.QPushButton(self.inputFileFrame)
        self.browseButton.setGeometry(QtCore.QRect(300, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.getDataFromInputLabel = QtWidgets.QLabel(self.inputFileFrame)
        self.getDataFromInputLabel.setGeometry(QtCore.QRect(10, 10, 281, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.getDataFromInputLabel.setFont(font)
        self.getDataFromInputLabel.setObjectName("getDataFromInputLabel")
        self.saveFileFrame = QtWidgets.QFrame(self.centralwidget)
        self.saveFileFrame.setGeometry(QtCore.QRect(20, 680, 486, 181))
        self.saveFileFrame.setObjectName("saveFileFrame")
        self.saveFileInnerFrame = QtWidgets.QFrame(self.saveFileFrame)
        self.saveFileInnerFrame.setGeometry(QtCore.QRect(11, 66, 484, 113))
        self.saveFileInnerFrame.setMinimumSize(QtCore.QSize(484, 113))
        self.saveFileInnerFrame.setObjectName("saveFileInnerFrame")
        self.saveFileInnerLayout = QtWidgets.QFormLayout(self.saveFileInnerFrame)
        self.saveFileInnerLayout.setObjectName("saveFileInnerLayout")
        self.saveFileNameLabel = QtWidgets.QLabel(self.saveFileInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.saveFileNameLabel.setFont(font)
        self.saveFileNameLabel.setObjectName("saveFileNameLabel")
        self.saveFileInnerLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.saveFileNameLabel)
        self.saveFileNameLineEdit = QtWidgets.QLineEdit(self.saveFileInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.saveFileNameLineEdit.setFont(font)
        self.saveFileNameLineEdit.setObjectName("saveFileNameLineEdit")
        self.saveFileInnerLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.saveFileNameLineEdit)
        self.saveDirectoryLabel = QtWidgets.QLabel(self.saveFileInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.saveDirectoryLabel.setFont(font)
        self.saveDirectoryLabel.setObjectName("saveDirectoryLabel")
        self.saveFileInnerLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.saveDirectoryLabel)
        self.saveDirectoryLineEdit = QtWidgets.QLineEdit(self.saveFileInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.saveDirectoryLineEdit.setFont(font)
        self.saveDirectoryLineEdit.setObjectName("saveDirectoryLineEdit")
        self.saveFileInnerLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.saveDirectoryLineEdit)
        self.browesSaveButton = QtWidgets.QPushButton(self.saveFileFrame)
        self.browesSaveButton.setGeometry(QtCore.QRect(290, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.browesSaveButton.setFont(font)
        self.browesSaveButton.setObjectName("browesSaveButton")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(10, 570, 481, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.calculateButton.setFont(font)
        self.calculateButton.setObjectName("calculateButton")
        self.writeDataFrame = QtWidgets.QFrame(self.centralwidget)
        self.writeDataFrame.setGeometry(QtCore.QRect(10, 99, 506, 301))
        self.writeDataFrame.setObjectName("writeDataFrame")
        self.writeDataInnerFrame = QtWidgets.QFrame(self.writeDataFrame)
        self.writeDataInnerFrame.setGeometry(QtCore.QRect(11, 98, 484, 151))
        self.writeDataInnerFrame.setMinimumSize(QtCore.QSize(484, 0))
        self.writeDataInnerFrame.setObjectName("writeDataInnerFrame")
        self.writeDataInnerLayout = QtWidgets.QFormLayout(self.writeDataInnerFrame)
        self.writeDataInnerLayout.setObjectName("writeDataInnerLayout")
        self.dnaSequenceLabel = QtWidgets.QLabel(self.writeDataInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dnaSequenceLabel.setFont(font)
        self.dnaSequenceLabel.setObjectName("dnaSequenceLabel")
        self.writeDataInnerLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dnaSequenceLabel)
        self.dnaSequenceLineEdit = QtWidgets.QLineEdit(self.writeDataInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dnaSequenceLineEdit.setFont(font)
        self.dnaSequenceLineEdit.setObjectName("dnaSequenceLineEdit")
        self.writeDataInnerLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dnaSequenceLineEdit)
        self.NaLabel = QtWidgets.QLabel(self.writeDataInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.NaLabel.setFont(font)
        self.NaLabel.setObjectName("NaLabel")
        self.writeDataInnerLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.NaLabel)
        self.NaLineEdit = QtWidgets.QLineEdit(self.writeDataInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.NaLineEdit.setFont(font)
        self.NaLineEdit.setObjectName("NaLineEdit")
        self.writeDataInnerLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NaLineEdit)
        self.CtLabel = QtWidgets.QLabel(self.writeDataInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CtLabel.setFont(font)
        self.CtLabel.setObjectName("CtLabel")
        self.writeDataInnerLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.CtLabel)
        self.CtLineEdit = QtWidgets.QLineEdit(self.writeDataInnerFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CtLineEdit.setFont(font)
        self.CtLineEdit.setObjectName("CtLineEdit")
        self.writeDataInnerLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.CtLineEdit)
        self.writeDataLabel = QtWidgets.QLabel(self.writeDataFrame)
        self.writeDataLabel.setGeometry(QtCore.QRect(10, 40, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.writeDataLabel.setFont(font)
        self.writeDataLabel.setObjectName("writeDataLabel")
        self.appendDataButton = QtWidgets.QPushButton(self.writeDataFrame)
        self.appendDataButton.setGeometry(QtCore.QRect(300, 40, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.appendDataButton.setFont(font)
        self.appendDataButton.setObjectName("appendDataButton")
        self.cleanButton = QtWidgets.QPushButton(self.centralwidget)
        self.cleanButton.setGeometry(QtCore.QRect(1080, 770, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cleanButton.setFont(font)
        self.cleanButton.setObjectName("cleanButton")
        self.saveToFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveToFileButton.setGeometry(QtCore.QRect(520, 770, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.saveToFileButton.setFont(font)
        self.saveToFileButton.setObjectName("saveToFileButton")
        self.fileSavedText = QtWidgets.QLabel(self.centralwidget)
        self.fileSavedText.setGeometry(QtCore.QRect(732, 780, 91, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fileSavedText.setFont(font)
        self.fileSavedText.setObjectName("fileSavedText")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1381, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.processingTypeLabel.setText(_translate("MainWindow", "Model"))
        self.processingTypeComboBox.setItemText(0, _translate("MainWindow", "linear_rel_processing"))
        self.processingTypeComboBox.setItemText(1, _translate("MainWindow", "conv_abs_processing"))
        self.processingTypeComboBox.setItemText(2, _translate("MainWindow", "conv_rel_processing"))
        self.inputFileNameLabel.setText(_translate("MainWindow", "File name"))
        self.fileSaltConditionLabel.setText(_translate("MainWindow", "Condition type: Activity"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.getDataFromInputLabel.setText(_translate("MainWindow", "Get data from input file"))
        self.saveFileNameLabel.setText(_translate("MainWindow", "File name"))
        self.saveDirectoryLabel.setText(_translate("MainWindow", "Save directory"))
        self.browesSaveButton.setText(_translate("MainWindow", "Browse"))
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
        self.dnaSequenceLabel.setText(_translate("MainWindow", "DNA sequence"))
        self.NaLabel.setText(_translate("MainWindow", "[Na+], M"))
        self.NaLineEdit.setText(_translate("MainWindow", "1"))
        self.CtLabel.setText(_translate("MainWindow", "Ct, M"))
        self.CtLineEdit.setText(_translate("MainWindow", "1e-5"))
        self.writeDataLabel.setText(_translate("MainWindow", "Input sequence"))
        self.appendDataButton.setText(_translate("MainWindow", "Append data"))
        self.cleanButton.setText(_translate("MainWindow", "Clean"))
        self.saveToFileButton.setText(_translate("MainWindow", "Save to file"))
        self.fileSavedText.setText(_translate("MainWindow", "Saved!"))
from TableView import TableView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
