# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_task.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_chande_task(object):
    def setupUi(self, form_chande_task):
        form_chande_task.setObjectName("form_chande_task")
        form_chande_task.resize(286, 222)
        self.groupBox_2 = QtWidgets.QGroupBox(form_chande_task)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 266, 201))
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

        self.retranslateUi(form_chande_task)
        QtCore.QMetaObject.connectSlotsByName(form_chande_task)

    def retranslateUi(self, form_chande_task):
        _translate = QtCore.QCoreApplication.translate
        form_chande_task.setWindowTitle(_translate("form_chande_task", "Form"))
        self.groupBox_2.setTitle(_translate("form_chande_task", "Изменит задачу"))
        self.label_5.setText(_translate("form_chande_task", "Описание задачи"))
        self.label_6.setText(_translate("form_chande_task", "Время"))
        self.pushButton_3.setText(_translate("form_chande_task", "Изменить"))
        self.pushButton_4.setText(_translate("form_chande_task", "Отмена"))
