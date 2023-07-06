# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_kotisivu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("BradPittHat.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pylaotsikko_label = QtWidgets.QLabel(self.centralwidget)
        self.pylaotsikko_label.setGeometry(QtCore.QRect(260, 30, 190, 29))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pylaotsikko_label.setFont(font)
        self.pylaotsikko_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pylaotsikko_label.setObjectName("pylaotsikko_label")
        self.pkayttaja_label = QtWidgets.QLabel(self.centralwidget)
        self.pkayttaja_label.setGeometry(QtCore.QRect(110, 130, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pkayttaja_label.setFont(font)
        self.pkayttaja_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pkayttaja_label.setObjectName("pkayttaja_label")
        self.psalis_label = QtWidgets.QLabel(self.centralwidget)
        self.psalis_label.setGeometry(QtCore.QRect(160, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.psalis_label.setFont(font)
        self.psalis_label.setObjectName("psalis_label")
        self.pkirjaudu_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pkirjaudu_pushButton.setGeometry(QtCore.QRect(250, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pkirjaudu_pushButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("kirjaudu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pkirjaudu_pushButton.setIcon(icon1)
        self.pkirjaudu_pushButton.setObjectName("pkirjaudu_pushButton")
        self.plaheta_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.plaheta_pushButton.setEnabled(False)
        self.plaheta_pushButton.setGeometry(QtCore.QRect(110, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plaheta_pushButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("laheta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plaheta_pushButton.setIcon(icon2)
        self.plaheta_pushButton.setIconSize(QtCore.QSize(32, 32))
        self.plaheta_pushButton.setObjectName("plaheta_pushButton")
        self.pvastaanota_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pvastaanota_pushButton.setEnabled(False)
        self.pvastaanota_pushButton.setGeometry(QtCore.QRect(250, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pvastaanota_pushButton.setFont(font)
        self.pvastaanota_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("vastaanota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pvastaanota_pushButton.setIcon(icon3)
        self.pvastaanota_pushButton.setObjectName("pvastaanota_pushButton")
        self.pkopio_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pkopio_pushButton.setEnabled(False)
        self.pkopio_pushButton.setGeometry(QtCore.QRect(390, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pkopio_pushButton.setFont(font)
        self.pkopio_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pkopio_pushButton.setAutoFillBackground(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("kopio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pkopio_pushButton.setIcon(icon4)
        self.pkopio_pushButton.setObjectName("pkopio_pushButton")
        self.pkayttaja_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pkayttaja_lineEdit.setGeometry(QtCore.QRect(250, 130, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pkayttaja_lineEdit.setFont(font)
        self.pkayttaja_lineEdit.setPlaceholderText("")
        self.pkayttaja_lineEdit.setObjectName("pkayttaja_lineEdit")
        self.psalis_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.psalis_lineEdit.setGeometry(QtCore.QRect(250, 170, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.psalis_lineEdit.setFont(font)
        self.psalis_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.psalis_lineEdit.setObjectName("psalis_lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pkayttaja_label.setBuddy(self.pkayttaja_lineEdit)
        self.psalis_label.setBuddy(self.psalis_lineEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pkayttaja_lineEdit, self.psalis_lineEdit)
        MainWindow.setTabOrder(self.psalis_lineEdit, self.pkirjaudu_pushButton)
        MainWindow.setTabOrder(self.pkirjaudu_pushButton, self.plaheta_pushButton)
        MainWindow.setTabOrder(self.plaheta_pushButton, self.pvastaanota_pushButton)
        MainWindow.setTabOrder(self.pvastaanota_pushButton, self.pkopio_pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Viestittely-kotisivu"))
        MainWindow.setToolTip(_translate("MainWindow", "Vie kursori haluamaasi kenttään tai painikkeelle, niin näet vihjeen."))
        self.pylaotsikko_label.setText(_translate("MainWindow", "Viestittely-kotisivu"))
        self.pkayttaja_label.setText(_translate("MainWindow", "Käyttäjä&tunnus:"))
        self.psalis_label.setText(_translate("MainWindow", "&Salasana:"))
        self.pkirjaudu_pushButton.setToolTip(_translate("MainWindow", "Kirjaudu Viestittely-ohjelmaan"))
        self.pkirjaudu_pushButton.setText(_translate("MainWindow", "Kirjaud&u"))
        self.plaheta_pushButton.setToolTip(_translate("MainWindow", "Siirry lähetä-sivulle"))
        self.plaheta_pushButton.setText(_translate("MainWindow", "&Lähetä"))
        self.pvastaanota_pushButton.setToolTip(_translate("MainWindow", "Siirry vastaanota-sivulle"))
        self.pvastaanota_pushButton.setText(_translate("MainWindow", "&Vastaanota"))
        self.pvastaanota_pushButton.setShortcut(_translate("MainWindow", "Alt+V"))
        self.pkopio_pushButton.setToolTip(_translate("MainWindow", "Siirry kopio-sivulle"))
        self.pkopio_pushButton.setText(_translate("MainWindow", "&Kopio"))
        self.pkopio_pushButton.setShortcut(_translate("MainWindow", "Alt+K"))
        self.pkayttaja_lineEdit.setToolTip(_translate("MainWindow", "käyttäjätunnus"))
        self.psalis_lineEdit.setToolTip(_translate("MainWindow", "Käyttäjätunnuksen salasana"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
