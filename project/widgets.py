# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1662, 943)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setMinimumSize(QtCore.QSize(506, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.calculateButton.setFont(font)
        self.calculateButton.setObjectName("calculateButton")
        self.gridLayout_2.addWidget(self.calculateButton, 3, 0, 1, 1)
        self.processingTypeFrame = QtWidgets.QFrame(self.centralwidget)
        self.processingTypeFrame.setMinimumSize(QtCore.QSize(506, 71))
        self.processingTypeFrame.setObjectName("processingTypeFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.processingTypeFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.processingTypeLabel = QtWidgets.QLabel(self.processingTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.processingTypeLabel.setFont(font)
        self.processingTypeLabel.setObjectName("processingTypeLabel")
        self.gridLayout.addWidget(self.processingTypeLabel, 0, 0, 1, 1)
        self.processingTypeComboBox = QtWidgets.QComboBox(self.processingTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.processingTypeComboBox.setFont(font)
        self.processingTypeComboBox.setObjectName("processingTypeComboBox")
        self.processingTypeComboBox.addItem("")
        self.gridLayout.addWidget(self.processingTypeComboBox, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.processingTypeFrame, 0, 0, 1, 1)
        self.saveToFileButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.saveToFileButton.setFont(font)
        self.saveToFileButton.setObjectName("saveToFileButton")
        self.gridLayout_2.addWidget(self.saveToFileButton, 5, 1, 1, 1)
        self.tableView = TableView(self.centralwidget)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 0, 1, 5, 3)
        self.fileSavedText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fileSavedText.setFont(font)
        self.fileSavedText.setObjectName("fileSavedText")
        self.gridLayout_2.addWidget(self.fileSavedText, 5, 2, 1, 1)
        self.cleanButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cleanButton.setFont(font)
        self.cleanButton.setObjectName("cleanButton")
        self.gridLayout_2.addWidget(self.cleanButton, 5, 3, 1, 1)
        self.inputFileFrame = QtWidgets.QFrame(self.centralwidget)
        self.inputFileFrame.setMinimumSize(QtCore.QSize(506, 161))
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
        self.browseButton = QtWidgets.QPushButton(self.inputFileFrame)
        self.browseButton.setGeometry(QtCore.QRect(300, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.getDataFromInputLabel = QtWidgets.QLabel(self.inputFileFrame)
        self.getDataFromInputLabel.setGeometry(QtCore.QRect(10, 10, 281, 35))
        self.getDataFromInputLabel.setMinimumSize(QtCore.QSize(281, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.getDataFromInputLabel.setFont(font)
        self.getDataFromInputLabel.setObjectName("getDataFromInputLabel")
        self.gridLayout_2.addWidget(self.inputFileFrame, 2, 0, 1, 1)
        self.writeDataFrame = QtWidgets.QFrame(self.centralwidget)
        self.writeDataFrame.setMinimumSize(QtCore.QSize(506, 301))
        self.writeDataFrame.setObjectName("writeDataFrame")
        self.writeDataInnerFrame = QtWidgets.QFrame(self.writeDataFrame)
        self.writeDataInnerFrame.setGeometry(QtCore.QRect(11, 98, 484, 201))
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
        self.writeDataLabel.setGeometry(QtCore.QRect(10, 40, 271, 35))
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
        self.gridLayout_2.addWidget(self.writeDataFrame, 1, 0, 1, 1)
        self.saveFileFrame = QtWidgets.QFrame(self.centralwidget)
        self.saveFileFrame.setMinimumSize(QtCore.QSize(506, 181))
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
        self.gridLayout_2.addWidget(self.saveFileFrame, 4, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1662, 26))
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
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
        self.processingTypeLabel.setText(_translate("MainWindow", "Model"))
        self.processingTypeComboBox.setItemText(0, _translate("MainWindow", "conv_abs_processing"))
        self.saveToFileButton.setText(_translate("MainWindow", "Save to file"))
        self.fileSavedText.setText(_translate("MainWindow", "Saved!"))
        self.cleanButton.setText(_translate("MainWindow", "Clean"))
        self.inputFileNameLabel.setText(_translate("MainWindow", "File name"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.getDataFromInputLabel.setText(_translate("MainWindow", "Get data from file"))
        self.dnaSequenceLabel.setText(_translate("MainWindow", "DNA sequence"))
        self.NaLabel.setText(_translate("MainWindow", "[Na+], M"))
        self.NaLineEdit.setText(_translate("MainWindow", "1"))
        self.CtLabel.setText(_translate("MainWindow", "Ct, M"))
        self.CtLineEdit.setText(_translate("MainWindow", "1e-5"))
        self.writeDataLabel.setText(_translate("MainWindow", "Input sequence"))
        self.appendDataButton.setText(_translate("MainWindow", "Append data"))
        self.saveFileNameLabel.setText(_translate("MainWindow", "File name"))
        self.saveDirectoryLabel.setText(_translate("MainWindow", "Save directory"))
        self.browesSaveButton.setText(_translate("MainWindow", "Browse"))
from project.table_service.TableView import TableView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())