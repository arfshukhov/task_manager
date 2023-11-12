# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerYShFii.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QMetaObject, \
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont,QFontDatabase, QIcon,\
    QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
from PySide6.QtWidgets import *


class Ui_TaskManager(QMainWindow):
    def setupUi(self, TaskManager):
        if not TaskManager.objectName():
            TaskManager.setObjectName(u"TaskManager")
        TaskManager.resize(1086, 599)
        self.centralwidget = QWidget(TaskManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 80, 1061, 471))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.monday_list = QListView(self.horizontalLayoutWidget)
        self.monday_list.setObjectName(u"monday_list")

        self.horizontalLayout.addWidget(self.monday_list)

        self.tuesday_list = QListView(self.horizontalLayoutWidget)
        self.tuesday_list.setObjectName(u"tuesday_list")

        self.horizontalLayout.addWidget(self.tuesday_list)

        self.wednesday_list = QListView(self.horizontalLayoutWidget)
        self.wednesday_list.setObjectName(u"wednesday_list")

        self.horizontalLayout.addWidget(self.wednesday_list)

        self.thursday_list = QListView(self.horizontalLayoutWidget)
        self.thursday_list.setObjectName(u"thursday_list")

        self.horizontalLayout.addWidget(self.thursday_list)

        self.friday_list = QListView(self.horizontalLayoutWidget)
        self.friday_list.setObjectName(u"friday_list")
        self.friday_list.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.horizontalLayout.addWidget(self.friday_list)

        self.saturday_list = QListView(self.horizontalLayoutWidget)
        self.saturday_list.setObjectName(u"saturday_list")

        self.horizontalLayout.addWidget(self.saturday_list)

        self.sunday_list = QListView(self.horizontalLayoutWidget)
        self.sunday_list.setObjectName(u"sunday_list")
        self.sunday_list.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.horizontalLayout.addWidget(self.sunday_list)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 49, 1061, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.monday_label = QLabel(self.horizontalLayoutWidget_2)
        self.monday_label.setObjectName(u"monday_label")

        self.horizontalLayout_2.addWidget(self.monday_label)

        self.tuesday_label = QLabel(self.horizontalLayoutWidget_2)
        self.tuesday_label.setObjectName(u"tuesday_label")

        self.horizontalLayout_2.addWidget(self.tuesday_label)

        self.wednesday_label = QLabel(self.horizontalLayoutWidget_2)
        self.wednesday_label.setObjectName(u"wednesday_label")

        self.horizontalLayout_2.addWidget(self.wednesday_label)

        self.thursday_label = QLabel(self.horizontalLayoutWidget_2)
        self.thursday_label.setObjectName(u"thursday_label")

        self.horizontalLayout_2.addWidget(self.thursday_label)

        self.friday_label = QLabel(self.horizontalLayoutWidget_2)
        self.friday_label.setObjectName(u"friday_label")

        self.horizontalLayout_2.addWidget(self.friday_label)

        self.saturday_label = QLabel(self.horizontalLayoutWidget_2)
        self.saturday_label.setObjectName(u"saturday_label")

        self.horizontalLayout_2.addWidget(self.saturday_label)

        self.sunday_label = QLabel(self.horizontalLayoutWidget_2)
        self.sunday_label.setObjectName(u"sunday_label")

        self.horizontalLayout_2.addWidget(self.sunday_label)

        self.add_task_button = QPushButton(self.centralwidget)
        self.add_task_button.setObjectName(u"add_task_button")
        self.add_task_button.setGeometry(QRect(10, 10, 75, 23))
        TaskManager.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TaskManager)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1086, 22))
        TaskManager.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TaskManager)
        self.statusbar.setObjectName(u"statusbar")
        TaskManager.setStatusBar(self.statusbar)

        self.retranslateUi(TaskManager)

        QMetaObject.connectSlotsByName(TaskManager)
    # setupUi

    def retranslateUi(self, TaskManager):
        TaskManager.setWindowTitle(QCoreApplication.translate("TaskManager", u"Task Manager", None))
        self.monday_label.setText(QCoreApplication.translate("TaskManager", u"MONDAY", None))
        self.tuesday_label.setText(QCoreApplication.translate("TaskManager", u"TUESDAY", None))
        self.wednesday_label.setText(QCoreApplication.translate("TaskManager", u"WEDNESDAY", None))
        self.thursday_label.setText(QCoreApplication.translate("TaskManager", u"THURSDAY", None))
        self.friday_label.setText(QCoreApplication.translate("TaskManager", u"FRIDAY", None))
        self.saturday_label.setText(QCoreApplication.translate("TaskManager", u"SATURDAY", None))
        self.sunday_label.setText(QCoreApplication.translate("TaskManager", u"SUNDAY", None))
        self.add_task_button.setText(QCoreApplication.translate("TaskManager", u"ADD TASK", None))
    # retranslateUi



class Ui_AddTaskWidget(QDialog):
    def setupUi(self, AddTaskWidget):
        if not AddTaskWidget.objectName():
            AddTaskWidget.setObjectName(u"AddTaskWidget")
        AddTaskWidget.resize(626, 359)
        self.calendar_widget = QCalendarWidget(AddTaskWidget)
        self.calendar_widget.setObjectName(u"calendar_widget")
        self.calendar_widget.setGeometry(QRect(20, 20, 321, 261))
        self.time_edit = QTimeEdit(AddTaskWidget)
        self.time_edit.setObjectName(u"time_edit")
        self.time_edit.setGeometry(QRect(110, 300, 151, 31))
        self.text_edit = QTextEdit(AddTaskWidget)
        self.text_edit.setObjectName(u"text_edit")
        self.text_edit.setGeometry(QRect(350, 20, 261, 261))
        self.done_button = QPushButton(AddTaskWidget)
        self.done_button.setObjectName(u"done_button")
        self.done_button.setGeometry(QRect(520, 300, 81, 31))
        self.label = QLabel(AddTaskWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 300, 71, 31))

        self.retranslateUi(AddTaskWidget)

        QMetaObject.connectSlotsByName(AddTaskWidget)
    # setupUi

    def retranslateUi(self, AddTaskWidget):
        AddTaskWidget.setWindowTitle(QCoreApplication.translate("AddTaskWidget", u"Form", None))
        self.done_button.setText(QCoreApplication.translate("AddTaskWidget", u"Done", None))
        self.label.setText(QCoreApplication.translate("AddTaskWidget", u"Choice time", None))
    # retranslateUi


class Ui_NotOriginalTaskDialog(QDialog):
    def setupUi(self, NotOriginalTaskDialog):
        if not NotOriginalTaskDialog.objectName():
            NotOriginalTaskDialog.setObjectName(u"NotOriginalTaskDialog")
        NotOriginalTaskDialog.resize(400, 213)
        self.pushButton = QPushButton(NotOriginalTaskDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 170, 101, 31))
        self.label = QLabel(NotOriginalTaskDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 361, 31))
        self.label_2 = QLabel(NotOriginalTaskDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 351, 81))

        self.retranslateUi(NotOriginalTaskDialog)

        QMetaObject.connectSlotsByName(NotOriginalTaskDialog)
    # setupUi

    def retranslateUi(self, NotOriginalTaskDialog):
        NotOriginalTaskDialog.setWindowTitle(QCoreApplication.translate("NotOriginalTaskDialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("NotOriginalTaskDialog", u"OK", None))
        self.label.setText(QCoreApplication.translate("NotOriginalTaskDialog",
                                u"You are failed on creation of task. It seems that task is already exists.", None))
        self.label_2.setText("")
    # retranslateUi


class Ui_CompleteTaskDialog(QDialog):
    def setupUi(self, CompleteTaskDialog):
        if not CompleteTaskDialog.objectName():
            CompleteTaskDialog.setObjectName(u"CompleteTaskDialog")
        CompleteTaskDialog.resize(385, 241)
        self.time_l = QLabel(CompleteTaskDialog)
        self.time_l.setObjectName(u"time_l")
        self.time_l.setGeometry(QRect(20, 10, 341, 31))
        self.label = QLabel(CompleteTaskDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 170, 131, 41))
        self.text_l = QTextEdit(CompleteTaskDialog)
        self.text_l.setObjectName(u"text_l")
        self.text_l.setGeometry(QRect(30, 50, 331, 71))
        self.text_l.setReadOnly(True)
        self.status = QLabel(CompleteTaskDialog)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(40, 140, 49, 16))
        self.complete = QPushButton(CompleteTaskDialog)
        self.complete.setObjectName(u"complete")
        self.complete.setGeometry(QRect(100, 210, 75, 24))
        self.cancel = QPushButton(CompleteTaskDialog)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(180, 210, 75, 24))

        self.retranslateUi(CompleteTaskDialog)

        QMetaObject.connectSlotsByName(CompleteTaskDialog)
    # setupUi

    def retranslateUi(self, CompleteTaskDialog):
        CompleteTaskDialog.setWindowTitle(QCoreApplication.translate("CompleteTaskDialog", u"Complete task", None))
        self.time_l.setText("")
        self.label.setText(QCoreApplication.translate("CompleteTaskDialog", u"\u0421omplete this task?", None))
        self.status.setText("")
        self.complete.setText(QCoreApplication.translate("CompleteTaskDialog", u"Complete", None))
        self.cancel.setText(QCoreApplication.translate("CompleteTaskDialog", u"Cancel", None))
    # retranslateUi
