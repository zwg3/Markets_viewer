# Form implementation generated from reading ui file 'markets_pages_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_M_Pages(object):
    def setupUi(self, M_Pages):
        M_Pages.setObjectName("M_Pages")
        M_Pages.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=M_Pages)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cbMPages = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbMPages.setObjectName("cbMPages")
        self.gridLayout.addWidget(self.cbMPages, 3, 0, 1, 1)
        self.lblMpages = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblMpages.setObjectName("lblMpages")
        self.gridLayout.addWidget(self.lblMpages, 2, 0, 1, 1)
        self.lMPages = QtWidgets.QListWidget(parent=self.centralwidget)
        self.lMPages.setObjectName("lMPages")
        self.gridLayout.addWidget(self.lMPages, 5, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 1, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout.addWidget(self.btnDelete, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        M_Pages.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=M_Pages)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        M_Pages.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=M_Pages)
        self.statusbar.setObjectName("statusbar")
        M_Pages.setStatusBar(self.statusbar)

        self.retranslateUi(M_Pages)
        QtCore.QMetaObject.connectSlotsByName(M_Pages)

    def retranslateUi(self, M_Pages):
        _translate = QtCore.QCoreApplication.translate
        M_Pages.setWindowTitle(_translate("M_Pages", "MainWindow"))
        self.lblMpages.setText(_translate("M_Pages", "Select a page"))
        self.btnDelete.setText(_translate("M_Pages", "Delete selected item"))
        self.label.setText(_translate("M_Pages", "Double-click the listed items for a more detailed view"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    M_Pages = QtWidgets.QMainWindow()
    ui = Ui_M_Pages()
    ui.setupUi(M_Pages)
    M_Pages.show()
    sys.exit(app.exec())
