# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creat_task.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_task_creat(object):
    def setupUi(self, form_task_creat):
        form_task_creat.setObjectName("form_task_creat")
        form_task_creat.resize(276, 229)
        form_task_creat.setMinimumSize(QtCore.QSize(276, 229))
        form_task_creat.setMaximumSize(QtCore.QSize(276, 229))
        self.groupBox = QtWidgets.QGroupBox(form_task_creat)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 261, 201))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_2.setObjectName("label_2")
        self.task = QtWidgets.QLineEdit(self.groupBox)
        self.task.setGeometry(QtCore.QRect(10, 40, 241, 21))
        self.task.setObjectName("task")
        self.time = QtWidgets.QLineEdit(self.groupBox)
        self.time.setGeometry(QtCore.QRect(10, 90, 241, 21))
        self.time.setObjectName("time")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 261, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_6.setObjectName("label_6")
        self.task_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.task_2.setGeometry(QtCore.QRect(10, 40, 241, 21))
        self.task_2.setObjectName("task_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 160, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 130, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 90, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.retranslateUi(form_task_creat)
        QtCore.QMetaObject.connectSlotsByName(form_task_creat)

    def retranslateUi(self, form_task_creat):
        _translate = QtCore.QCoreApplication.translate
        form_task_creat.setWindowTitle(_translate("form_task_creat", "Form"))
        self.groupBox.setTitle(_translate("form_task_creat", "Создать задачу"))
        self.label.setText(_translate("form_task_creat", "Введите описание задачи"))
        self.label_2.setText(_translate("form_task_creat", "Выберете время"))
        self.pushButton.setText(_translate("form_task_creat", "Создать"))
        self.pushButton_2.setText(_translate("form_task_creat", "Отмена"))
        self.groupBox_2.setTitle(_translate("form_task_creat", "Создать задачу"))
        self.label_5.setText(_translate("form_task_creat", "Введите описание задачи"))
        self.label_6.setText(_translate("form_task_creat", "Выберете время"))
        self.pushButton_3.setText(_translate("form_task_creat", "Создать"))
        self.pushButton_4.setText(_translate("form_task_creat", "Отмена"))
