# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\ws\flow_classifier\ui_qt\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 100, 631, 461))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(530, 270, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 71, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setGeometry(QtCore.QRect(10, 120, 611, 71))
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 133, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(149, 20, 133, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(288, 20, 41, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_pitch = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_pitch.setGeometry(QtCore.QRect(149, 40, 133, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_pitch.sizePolicy().hasHeightForWidth())
        self.lineEdit_pitch.setSizePolicy(sizePolicy)
        self.lineEdit_pitch.setObjectName("lineEdit_pitch")
        self.comboBox_L = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_L.setGeometry(QtCore.QRect(288, 40, 41, 20))
        self.comboBox_L.setEditable(True)
        self.comboBox_L.setObjectName("comboBox_L")
        self.lineEdit_flowrate = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_flowrate.setGeometry(QtCore.QRect(10, 40, 133, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_flowrate.sizePolicy().hasHeightForWidth())
        self.lineEdit_flowrate.setSizePolicy(sizePolicy)
        self.lineEdit_flowrate.setObjectName("lineEdit_flowrate")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(410, 20, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(341, 20, 133, 15))
        self.label_9.setObjectName("label_9")
        self.comboBox_ratio = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ratio.setGeometry(QtCore.QRect(341, 40, 61, 20))
        self.comboBox_ratio.setEditable(True)
        self.comboBox_ratio.setObjectName("comboBox_ratio")
        self.lineEdit_total_flow_rate = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_total_flow_rate.setGeometry(QtCore.QRect(410, 40, 121, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_total_flow_rate.sizePolicy().hasHeightForWidth())
        self.lineEdit_total_flow_rate.setSizePolicy(sizePolicy)
        self.lineEdit_total_flow_rate.setObjectName("lineEdit_total_flow_rate")
        self.comboBox_experiment = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_experiment.setGeometry(QtCore.QRect(280, 20, 151, 20))
        self.comboBox_experiment.setObjectName("comboBox_experiment")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(210, 20, 81, 16))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 611, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 591, 39))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_method = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_method.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_method.setHorizontalSpacing(6)
        self.gridLayout_method.setVerticalSpacing(1)
        self.gridLayout_method.setObjectName("gridLayout_method")
        self.comboBox_type_liquid = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_type_liquid.setGeometry(QtCore.QRect(90, 20, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_type_liquid.sizePolicy().hasHeightForWidth())
        self.comboBox_type_liquid.setSizePolicy(sizePolicy)
        self.comboBox_type_liquid.setObjectName("comboBox_type_liquid")
        self.textEdit_res = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_res.setGeometry(QtCore.QRect(10, 300, 611, 151))
        self.textEdit_res.setObjectName("textEdit_res")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 50, 611, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setGeometry(QtCore.QRect(10, 20, 591, 47))
        self.widget.setObjectName("widget")
        self.gridLayout_liquid_vals = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_liquid_vals.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_liquid_vals.setObjectName("gridLayout_liquid_vals")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 0, 631, 101))
        self.groupBox_5.setObjectName("groupBox_5")
        self.widget1 = QtWidgets.QWidget(self.groupBox_5)
        self.widget1.setGeometry(QtCore.QRect(10, 40, 511, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.lineEdit_trainPath = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_trainPath.sizePolicy().hasHeightForWidth())
        self.lineEdit_trainPath.setSizePolicy(sizePolicy)
        self.lineEdit_trainPath.setObjectName("lineEdit_trainPath")
        self.horizontalLayout_3.addWidget(self.lineEdit_trainPath)
        self.pushButton_setTrainPath = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_setTrainPath.sizePolicy().hasHeightForWidth())
        self.pushButton_setTrainPath.setSizePolicy(sizePolicy)
        self.pushButton_setTrainPath.setObjectName("pushButton_setTrainPath")
        self.horizontalLayout_3.addWidget(self.pushButton_setTrainPath)
        self.widget2 = QtWidgets.QWidget(self.groupBox_5)
        self.widget2.setGeometry(QtCore.QRect(10, 70, 511, 31))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.widget2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.lineEdit_testPath = QtWidgets.QLineEdit(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_testPath.sizePolicy().hasHeightForWidth())
        self.lineEdit_testPath.setSizePolicy(sizePolicy)
        self.lineEdit_testPath.setObjectName("lineEdit_testPath")
        self.horizontalLayout_5.addWidget(self.lineEdit_testPath)
        self.pushButton_setTestPath = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_setTestPath.sizePolicy().hasHeightForWidth())
        self.pushButton_setTestPath.setSizePolicy(sizePolicy)
        self.pushButton_setTestPath.setObjectName("pushButton_setTestPath")
        self.horizontalLayout_5.addWidget(self.pushButton_setTestPath)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.label_5.setObjectName("label_5")
        self.comboBox_experiment_2 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_experiment_2.setGeometry(QtCore.QRect(130, 20, 211, 20))
        self.comboBox_experiment_2.setObjectName("comboBox_experiment_2")
        self.pushButton_training = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_training.setGeometry(QtCore.QRect(530, 70, 91, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_training.sizePolicy().hasHeightForWidth())
        self.pushButton_training.setSizePolicy(sizePolicy)
        self.pushButton_training.setObjectName("pushButton_training")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        self.menuCommand = QtWidgets.QMenu(self.menubar)
        self.menuCommand.setObjectName("menuCommand")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionTrain = QtWidgets.QAction(MainWindow)
        self.actionTrain.setObjectName("actionTrain")
        self.menuCommand.addAction(self.actionRun)
        self.menuCommand.addAction(self.actionTrain)
        self.menuCommand.addAction(self.actionQuit)
        self.menubar.addAction(self.menuCommand.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flow Classifier"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Testing"))
        self.pushButton.setText(_translate("MainWindow", "Run Simulation"))
        self.label_4.setText(_translate("MainWindow", "Type of Liquid?"))
        self.groupBox.setTitle(_translate("MainWindow", "Custom"))
        self.label_6.setText(_translate("MainWindow", "org.flowrate"))
        self.label_7.setText(_translate("MainWindow", "pitch"))
        self.label_8.setText(_translate("MainWindow", "L"))
        self.label_10.setText(_translate("MainWindow", "total_flow_rate"))
        self.label_9.setText(_translate("MainWindow", "ratio"))
        self.label.setText(_translate("MainWindow", "Experiments"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Method"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Liquid Values"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Training"))
        self.label_11.setText(_translate("MainWindow", "Train data"))
        self.pushButton_setTrainPath.setText(_translate("MainWindow", "set"))
        self.label_12.setText(_translate("MainWindow", " Test data"))
        self.pushButton_setTestPath.setText(_translate("MainWindow", "set"))
        self.label_5.setText(_translate("MainWindow", "Experiments for Training"))
        self.pushButton_training.setText(_translate("MainWindow", "Training"))
        self.menuCommand.setTitle(_translate("MainWindow", "Command"))
        self.actionRun.setText(_translate("MainWindow", "Run!"))
        self.actionRun.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionTrain.setText(_translate("MainWindow", "Train"))
        self.actionTrain.setShortcut(_translate("MainWindow", "Ctrl+T"))
