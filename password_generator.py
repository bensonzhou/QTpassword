# Form implementation generated from reading ui file 'password_generator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_passwordgenerator(object):
    def setupUi(self, passwordgenerator):
        passwordgenerator.setObjectName("passwordgenerator")
        passwordgenerator.resize(539, 428)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../ICONS/Magicons-2867-Flat-Icons-2/Magicons - 2867 Flat Icons/Magicons - 2687 icons/PNG/@2x/Technology Devices/bigproc.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        passwordgenerator.setWindowIcon(icon)
        passwordgenerator.setAutoFillBackground(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(passwordgenerator)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=passwordgenerator)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_target = QtWidgets.QLineEdit(parent=passwordgenerator)
        self.lineEdit_target.setObjectName("lineEdit_target")
        self.horizontalLayout.addWidget(self.lineEdit_target)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=passwordgenerator)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinBox_count = QtWidgets.QSpinBox(parent=passwordgenerator)
        self.spinBox_count.setMinimum(8)
        self.spinBox_count.setMaximum(20)
        self.spinBox_count.setObjectName("spinBox_count")
        self.horizontalLayout_2.addWidget(self.spinBox_count)
        self.checkBox_upper = QtWidgets.QCheckBox(parent=passwordgenerator)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_upper.setFont(font)
        self.checkBox_upper.setObjectName("checkBox_upper")
        self.horizontalLayout_2.addWidget(self.checkBox_upper)
        self.checkBox_lower = QtWidgets.QCheckBox(parent=passwordgenerator)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_lower.setFont(font)
        self.checkBox_lower.setObjectName("checkBox_lower")
        self.horizontalLayout_2.addWidget(self.checkBox_lower)
        self.checkBox_num = QtWidgets.QCheckBox(parent=passwordgenerator)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_num.setFont(font)
        self.checkBox_num.setObjectName("checkBox_num")
        self.horizontalLayout_2.addWidget(self.checkBox_num)
        self.checkBox_puc = QtWidgets.QCheckBox(parent=passwordgenerator)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_puc.setFont(font)
        self.checkBox_puc.setObjectName("checkBox_puc")
        self.horizontalLayout_2.addWidget(self.checkBox_puc)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(parent=passwordgenerator)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=passwordgenerator)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_result = QtWidgets.QLineEdit(parent=passwordgenerator)
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.horizontalLayout_3.addWidget(self.lineEdit_result)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(passwordgenerator)
        QtCore.QMetaObject.connectSlotsByName(passwordgenerator)

    def retranslateUi(self, passwordgenerator):
        _translate = QtCore.QCoreApplication.translate
        passwordgenerator.setWindowTitle(_translate("passwordgenerator", "密码生成小工具"))
        passwordgenerator.setToolTip(_translate("passwordgenerator", "<html><head/><body><p><span style=\" font-weight:700;\">用于自动生成密码并保存在本地文本文件内的一个实用小工具。</span></p></body></html>"))
        self.label.setText(_translate("passwordgenerator", "密码归属地："))
        self.label_3.setText(_translate("passwordgenerator", "密码位数："))
        self.checkBox_upper.setText(_translate("passwordgenerator", "大写字母"))
        self.checkBox_lower.setText(_translate("passwordgenerator", "小写字母"))
        self.checkBox_num.setText(_translate("passwordgenerator", "数字"))
        self.checkBox_puc.setText(_translate("passwordgenerator", "标点符号"))
        self.pushButton.setText(_translate("passwordgenerator", "生成密码"))
        self.label_2.setText(_translate("passwordgenerator", "生成的密码："))
