# Form implementation generated from reading ui file 'delete_pop_up.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_pop_up_delete(object):
    def setupUi(self, pop_up_delete):
        pop_up_delete.setObjectName("pop_up_delete")
        pop_up_delete.resize(400, 300)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(pop_up_delete)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblDelete = QtWidgets.QLabel(parent=pop_up_delete)
        self.lblDelete.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblDelete.setObjectName("lblDelete")
        self.verticalLayout.addWidget(self.lblDelete)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnY = QtWidgets.QPushButton(parent=pop_up_delete)
        self.btnY.setObjectName("btnY")
        self.horizontalLayout.addWidget(self.btnY)
        self.btnN = QtWidgets.QPushButton(parent=pop_up_delete)
        self.btnN.setObjectName("btnN")
        self.horizontalLayout.addWidget(self.btnN)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(pop_up_delete)
        QtCore.QMetaObject.connectSlotsByName(pop_up_delete)

    def retranslateUi(self, pop_up_delete):
        _translate = QtCore.QCoreApplication.translate
        pop_up_delete.setWindowTitle(_translate("pop_up_delete", "Form"))
        self.lblDelete.setText(_translate("pop_up_delete", "TextLabel"))
        self.btnY.setText(_translate("pop_up_delete", "Yes"))
        self.btnN.setText(_translate("pop_up_delete", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pop_up_delete = QtWidgets.QWidget()
    ui = Ui_pop_up_delete()
    ui.setupUi(pop_up_delete)
    pop_up_delete.show()
    sys.exit(app.exec())
