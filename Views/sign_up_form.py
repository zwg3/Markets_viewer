# Form implementation generated from reading ui file 'sign_up_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Sign_up_form(object):
    def setupUi(self, Sign_up_form):
        Sign_up_form.setObjectName("Sign_up_form")
        Sign_up_form.resize(400, 300)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Sign_up_form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblFname = QtWidgets.QLabel(parent=Sign_up_form)
        self.lblFname.setObjectName("lblFname")
        self.verticalLayout_2.addWidget(self.lblFname)
        self.lnFname = QtWidgets.QLineEdit(parent=Sign_up_form)
        self.lnFname.setObjectName("lnFname")
        self.verticalLayout_2.addWidget(self.lnFname)
        self.lblLname = QtWidgets.QLabel(parent=Sign_up_form)
        self.lblLname.setObjectName("lblLname")
        self.verticalLayout_2.addWidget(self.lblLname)
        self.lnLname = QtWidgets.QLineEdit(parent=Sign_up_form)
        self.lnLname.setObjectName("lnLname")
        self.verticalLayout_2.addWidget(self.lnLname)
        self.lblUsername = QtWidgets.QLabel(parent=Sign_up_form)
        self.lblUsername.setObjectName("lblUsername")
        self.verticalLayout_2.addWidget(self.lblUsername)
        self.lnUsername = QtWidgets.QLineEdit(parent=Sign_up_form)
        self.lnUsername.setObjectName("lnUsername")
        self.verticalLayout_2.addWidget(self.lnUsername)
        self.lblPassword = QtWidgets.QLabel(parent=Sign_up_form)
        self.lblPassword.setObjectName("lblPassword")
        self.verticalLayout_2.addWidget(self.lblPassword)
        self.lnPassword = QtWidgets.QLineEdit(parent=Sign_up_form)
        self.lnPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lnPassword.setObjectName("lnPassword")
        self.verticalLayout_2.addWidget(self.lnPassword)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnSignUp = QtWidgets.QPushButton(parent=Sign_up_form)
        self.btnSignUp.setObjectName("btnSignUp")
        self.horizontalLayout_3.addWidget(self.btnSignUp)
        self.btnCancel = QtWidgets.QPushButton(parent=Sign_up_form)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_3.addWidget(self.btnCancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Sign_up_form)
        QtCore.QMetaObject.connectSlotsByName(Sign_up_form)

    def retranslateUi(self, Sign_up_form):
        _translate = QtCore.QCoreApplication.translate
        Sign_up_form.setWindowTitle(_translate("Sign_up_form", "Form"))
        self.lblFname.setText(_translate("Sign_up_form", "First name"))
        self.lblLname.setText(_translate("Sign_up_form", "Last name"))
        self.lblUsername.setText(_translate("Sign_up_form", "User name"))
        self.lblPassword.setText(_translate("Sign_up_form", "Password"))
        self.btnSignUp.setText(_translate("Sign_up_form", "Sign up"))
        self.btnCancel.setText(_translate("Sign_up_form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sign_up_form = QtWidgets.QWidget()
    ui = Ui_Sign_up_form()
    ui.setupUi(Sign_up_form)
    Sign_up_form.show()
    sys.exit(app.exec())
