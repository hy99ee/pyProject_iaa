# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hy99ee/Dev/projects/pyProject_2.1_iaa/MainWindow/forms_ui/mainWindowForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(987, 820)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem, 2, 0, 1, 1)
        self.pbClose = QtWidgets.QPushButton(self.centralwidget)
        self.pbClose.setMinimumSize(QtCore.QSize(84, 34))
        self.pbClose.setMaximumSize(QtCore.QSize(84, 34))
        self.pbClose.setObjectName("pbClose")
        self.gridLayout_10.addWidget(self.pbClose, 2, 2, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.printStage = QtWidgets.QStackedWidget(self.centralwidget)
        self.printStage.setObjectName("printStage")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.decision1 = QtWidgets.QFrame(self.page)
        self.decision1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision1.setObjectName("decision1")
        self.gridLayout = QtWidgets.QGridLayout(self.decision1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.decision1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.linePrint = QtWidgets.QLineEdit(self.decision1)
        self.linePrint.setMinimumSize(QtCore.QSize(0, 34))
        self.linePrint.setMaximumSize(QtCore.QSize(16777215, 34))
        self.linePrint.setObjectName("linePrint")
        self.gridLayout.addWidget(self.linePrint, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.gridLayout_5.addWidget(self.decision1, 0, 0, 1, 1)
        self.printStage.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.decision2 = QtWidgets.QFrame(self.page_2)
        self.decision2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.decision2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decision2.setObjectName("decision2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.decision2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.viewLayout = QtWidgets.QGridLayout()
        self.viewLayout.setObjectName("viewLayout")
        self.gridLayout_8.addLayout(self.viewLayout, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.decision2, 0, 0, 1, 1)
        self.printStage.addWidget(self.page_2)
        self.gridLayout_9.addWidget(self.printStage, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbClosePirint = QtWidgets.QPushButton(self.centralwidget)
        self.pbClosePirint.setMinimumSize(QtCore.QSize(84, 34))
        self.pbClosePirint.setMaximumSize(QtCore.QSize(84, 34))
        self.pbClosePirint.setObjectName("pbClosePirint")
        self.horizontalLayout_3.addWidget(self.pbClosePirint)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout_9.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 1, 0, 1, 3)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setContentsMargins(6, -1, 6, -1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.chooseStage = QtWidgets.QFrame(self.centralwidget)
        self.chooseStage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chooseStage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chooseStage.setObjectName("chooseStage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.chooseStage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.chooseStage)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 0, 1, 1)
        self.pbStart3 = QtWidgets.QPushButton(self.chooseStage)
        self.pbStart3.setMinimumSize(QtCore.QSize(0, 50))
        self.pbStart3.setObjectName("pbStart3")
        self.gridLayout_2.addWidget(self.pbStart3, 0, 2, 1, 1)
        self.pbStart2 = QtWidgets.QPushButton(self.chooseStage)
        self.pbStart2.setMinimumSize(QtCore.QSize(0, 50))
        self.pbStart2.setObjectName("pbStart2")
        self.gridLayout_2.addWidget(self.pbStart2, 0, 1, 1, 1)
        self.pbStart1 = QtWidgets.QPushButton(self.chooseStage)
        self.pbStart1.setMinimumSize(QtCore.QSize(0, 50))
        self.pbStart1.setObjectName("pbStart1")
        self.gridLayout_2.addWidget(self.pbStart1, 0, 0, 1, 1)
        self.l1 = QtWidgets.QLabel(self.chooseStage)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.gridLayout_2.addWidget(self.l1, 1, 0, 1, 1)
        self.l2 = QtWidgets.QLabel(self.chooseStage)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")
        self.gridLayout_2.addWidget(self.l2, 1, 1, 1, 1)
        self.l3 = QtWidgets.QLabel(self.chooseStage)
        self.l3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3.setObjectName("l3")
        self.gridLayout_2.addWidget(self.l3, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 3, 0, 1, 1)
        self.gridLayout_11.addWidget(self.chooseStage, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_11, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 987, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")

        self.retranslateUi(MainWindow)
        self.printStage.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbClose.setText(_translate("MainWindow", "Выход"))
        self.label_2.setText(_translate("MainWindow", "Что получаем:"))
        self.pbClosePirint.setToolTip(_translate("MainWindow", "Закрыть решение и вернуться в главное меню"))
        self.pbClosePirint.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "Выберете номер задания:"))
        self.pbStart3.setStatusTip(_translate("MainWindow", "Внимание, это не так быстро"))
        self.pbStart3.setText(_translate("MainWindow", "Задание №3"))
        self.pbStart2.setText(_translate("MainWindow", "Задание №2"))
        self.pbStart1.setText(_translate("MainWindow", "Задание №1"))
        self.l1.setText(_translate("MainWindow", "Энтропия"))
        self.l2.setText(_translate("MainWindow", "Скользящие средние"))
        self.l3.setText(_translate("MainWindow", "Монте-карло - это не город"))
        self.action.setText(_translate("MainWindow", "О программе"))