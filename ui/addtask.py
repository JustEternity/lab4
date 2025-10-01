from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TaskWin(object):
    def setupUi(self, TaskWin):
        TaskWin.setObjectName("TaskWin")
        TaskWin.resize(405, 395)
        TaskWin.setMinimumSize(QtCore.QSize(405, 395))
        TaskWin.setMaximumSize(QtCore.QSize(405, 395))
        TaskWin.setStyleSheet("#TaskWin {\n"
"    background-color: #ccffff;\n"
"    border: 1px solid #dee2e6;\n"
"}")
        self.nametask = QtWidgets.QLineEdit(parent=TaskWin)
        self.nametask.setGeometry(QtCore.QRect(30, 50, 331, 21))
        self.nametask.setObjectName("nametask")
        self.nametask.setStyleSheet("#nametask {\n"
"    background-color: #FFFCE9;\n"
"}")
        self.label = QtWidgets.QLabel(parent=TaskWin)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.abouttask = QtWidgets.QTextEdit(parent=TaskWin)
        self.abouttask.setGeometry(QtCore.QRect(30, 110, 331, 191))
        self.abouttask.setAccessibleName("")
        self.abouttask.setAccessibleDescription("")
        self.abouttask.setAutoFillBackground(False)
        self.abouttask.setObjectName("abouttask")
        self.abouttask.setStyleSheet("#abouttask {\n"
"    background-color: #FFFCE9;\n"
"}")
        self.savetask = QtWidgets.QPushButton(parent=TaskWin)
        self.savetask.setGeometry(QtCore.QRect(260, 330, 101, 31))
        self.savetask.setObjectName("savetask")
        self.savetask.setStyleSheet("#savetask {\n"
"    background-color: #FFCC99;\n"
"    border: 1px solid #dee2e6;\n"
"    border-radius: 10%;\n"
"}")
        self.deletetask = QtWidgets.QPushButton(parent=TaskWin)
        self.deletetask.setGeometry(QtCore.QRect(150, 330, 101, 31))
        self.deletetask.setObjectName("deletetask")
        self.deletetask.setStyleSheet("#deletetask {\n"
"    background-color: #FFCC99;\n"
"    border: 1px solid #dee2e6;\n"
"    border-radius: 10%;\n"
"}")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=TaskWin)
        self.dateTimeEdit.setGeometry(QtCore.QRect(30, 80, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setStyleSheet("#dateTimeEdit {\n"
"    background-color: #FFFCE9;\n"
"}")

        self.retranslateUi(TaskWin)
        QtCore.QMetaObject.connectSlotsByName(TaskWin)

    def retranslateUi(self, TaskWin):
        _translate = QtCore.QCoreApplication.translate
        TaskWin.setWindowTitle(_translate("TaskWin", "Task"))
        self.nametask.setPlaceholderText(_translate("TaskWin", "Название задачи"))
        self.label.setText(_translate("TaskWin", "Задача"))
        self.abouttask.setPlaceholderText(_translate("TaskWin", "Описание задачи"))
        self.savetask.setText(_translate("TaskWin", "Сохранить"))
        self.deletetask.setText(_translate("TaskWin", "Удалить"))
