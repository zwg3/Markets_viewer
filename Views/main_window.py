# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnMarketsPage = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnMarketsPage.setObjectName("btnMarketsPage")
        self.gridLayout.addWidget(self.btnMarketsPage, 0, 0, 1, 1)
        self.btnLeaveReview = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLeaveReview.setObjectName("btnLeaveReview")
        self.gridLayout.addWidget(self.btnLeaveReview, 2, 0, 1, 1)
        self.btnUsrReviews = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnUsrReviews.setObjectName("btnUsrReviews")
        self.gridLayout.addWidget(self.btnUsrReviews, 3, 0, 1, 1)
        self.btnSearch = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSearch.setObjectName("btnSearch")
        self.gridLayout.addWidget(self.btnSearch, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnMarketsPage.setText(_translate("MainWindow", "Display markets data"))
        self.btnLeaveReview.setText(_translate("MainWindow", "Review market"))
        self.btnUsrReviews.setText(_translate("MainWindow", "Check out user reviews"))
        self.btnSearch.setText(_translate("MainWindow", "Search markets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
