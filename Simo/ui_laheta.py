# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_laheta.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("BradPittHat.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.centralwidget.setObjectName("centralwidget")
        self.lylaotsikko_label = QtWidgets.QLabel(self.centralwidget)
        self.lylaotsikko_label.setGeometry(QtCore.QRect(260, 30, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lylaotsikko_label.setFont(font)
        self.lylaotsikko_label.setObjectName("lylaotsikko_label")
        self.lvastaanottaja_label = QtWidgets.QLabel(self.centralwidget)
        self.lvastaanottaja_label.setGeometry(QtCore.QRect(40, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lvastaanottaja_label.setFont(font)
        self.lvastaanottaja_label.setObjectName("lvastaanottaja_label")
        self.lviesti_label = QtWidgets.QLabel(self.centralwidget)
        self.lviesti_label.setGeometry(QtCore.QRect(140, 170, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lviesti_label.setFont(font)
        self.lviesti_label.setObjectName("lviesti_label")
        self.llaheta_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.llaheta_pushButton.setGeometry(QtCore.QRect(100, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.llaheta_pushButton.setFont(font)
        self.llaheta_pushButton.setStatusTip("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("laheta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.llaheta_pushButton.setIcon(icon1)
        self.llaheta_pushButton.setObjectName("llaheta_pushButton")
        self.lperu_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.lperu_pushButton.setGeometry(QtCore.QRect(520, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lperu_pushButton.setFont(font)
        self.lperu_pushButton.setStatusTip("")
        self.lperu_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("peru.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lperu_pushButton.setIcon(icon2)
        self.lperu_pushButton.setCheckable(True)
        self.lperu_pushButton.setObjectName("lperu_pushButton")
        self.lvastaanottaja_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lvastaanottaja_lineEdit.setGeometry(QtCore.QRect(210, 130, 271, 31))
        self.lvastaanottaja_lineEdit.setStatusTip("")
        self.lvastaanottaja_lineEdit.setObjectName("lvastaanottaja_lineEdit")
        self.lsalattu_tdsto_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lsalattu_tdsto_lineEdit.setGeometry(QtCore.QRect(490, 170, 271, 31))
        self.lsalattu_tdsto_lineEdit.setStatusTip("")
        self.lsalattu_tdsto_lineEdit.setObjectName("lsalattu_tdsto_lineEdit")
        self.lveistintalletuspolku_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lveistintalletuspolku_lineEdit.setGeometry(QtCore.QRect(210, 170, 271, 31))
        self.lveistintalletuspolku_lineEdit.setStatusTip("")
        self.lveistintalletuspolku_lineEdit.setObjectName("lveistintalletuspolku_lineEdit")
        self.lsijoitusavainpolku_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lsijoitusavainpolku_lineEdit.setGeometry(QtCore.QRect(210, 400, 271, 31))
        self.lsijoitusavainpolku_lineEdit.setStatusTip("")
        self.lsijoitusavainpolku_lineEdit.setObjectName("lsijoitusavainpolku_lineEdit")
        self.lkirjoitusavainpolku_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lkirjoitusavainpolku_lineEdit.setGeometry(QtCore.QRect(210, 360, 271, 31))
        self.lkirjoitusavainpolku_lineEdit.setStatusTip("")
        self.lkirjoitusavainpolku_lineEdit.setObjectName("lkirjoitusavainpolku_lineEdit")
        self.laloitusnro_label = QtWidgets.QLabel(self.centralwidget)
        self.laloitusnro_label.setGeometry(QtCore.QRect(60, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.laloitusnro_label.setFont(font)
        self.laloitusnro_label.setObjectName("laloitusnro_label")
        self.lvastaanottaja_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.lvastaanottaja_label_3.setGeometry(QtCore.QRect(70, 360, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lvastaanottaja_label_3.setFont(font)
        self.lvastaanottaja_label_3.setObjectName("lvastaanottaja_label_3")
        self.lvastaanottaja_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.lvastaanottaja_label_4.setGeometry(QtCore.QRect(80, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lvastaanottaja_label_4.setFont(font)
        self.lvastaanottaja_label_4.setObjectName("lvastaanottaja_label_4")
        self.laloitusnro_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.laloitusnro_lineEdit.setGeometry(QtCore.QRect(210, 320, 271, 31))
        self.laloitusnro_lineEdit.setStatusTip("")
        self.laloitusnro_lineEdit.setText("")
        self.laloitusnro_lineEdit.setObjectName("laloitusnro_lineEdit")
        self.lkirjoitusavain_tdsto_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lkirjoitusavain_tdsto_lineEdit.setGeometry(QtCore.QRect(490, 360, 271, 31))
        self.lkirjoitusavain_tdsto_lineEdit.setStatusTip("")
        self.lkirjoitusavain_tdsto_lineEdit.setObjectName("lkirjoitusavain_tdsto_lineEdit")
        self.lsalattu_tdsto_lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lsalattu_tdsto_lineEdit_3.setGeometry(QtCore.QRect(490, 400, 271, 31))
        self.lsalattu_tdsto_lineEdit_3.setStatusTip("")
        self.lsalattu_tdsto_lineEdit_3.setObjectName("lsalattu_tdsto_lineEdit_3")
        self.lviesti_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.lviesti_textBrowser.setGeometry(QtCore.QRect(210, 210, 551, 101))
        self.lviesti_textBrowser.setStatusTip("")
        self.lviesti_textBrowser.setObjectName("lviesti_textBrowser")
        self.lvastaanottaja_label.setBuddy(self.lvastaanottaja_lineEdit)
        self.lviesti_label.setBuddy(self.lveistintalletuspolku_lineEdit)
        self.laloitusnro_label.setBuddy(self.laloitusnro_lineEdit)
        self.lvastaanottaja_label_3.setBuddy(self.lkirjoitusavain_tdsto_lineEdit)
        self.lvastaanottaja_label_4.setBuddy(self.lsalattu_tdsto_lineEdit_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lvastaanottaja_lineEdit, self.lveistintalletuspolku_lineEdit)
        Form.setTabOrder(self.lveistintalletuspolku_lineEdit, self.lsalattu_tdsto_lineEdit)
        Form.setTabOrder(self.lsalattu_tdsto_lineEdit, self.lviesti_textBrowser)
        Form.setTabOrder(self.lviesti_textBrowser, self.laloitusnro_lineEdit)
        Form.setTabOrder(self.laloitusnro_lineEdit, self.lkirjoitusavainpolku_lineEdit)
        Form.setTabOrder(self.lkirjoitusavainpolku_lineEdit, self.lkirjoitusavain_tdsto_lineEdit)
        Form.setTabOrder(self.lkirjoitusavain_tdsto_lineEdit, self.lsijoitusavainpolku_lineEdit)
        Form.setTabOrder(self.lsijoitusavainpolku_lineEdit, self.lsalattu_tdsto_lineEdit_3)
        Form.setTabOrder(self.lsalattu_tdsto_lineEdit_3, self.llaheta_pushButton)
        Form.setTabOrder(self.llaheta_pushButton, self.lperu_pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Viestittely-lähetä"))
        self.lylaotsikko_label.setText(_translate("Form", "Viestittely-lähetä"))
        self.lvastaanottaja_label.setText(_translate("Form", "Vastaanottajan IP:"))
        self.lviesti_label.setText(_translate("Form", "Viesti:"))
        self.llaheta_pushButton.setToolTip(_translate("Form", "lähetä viesti, ALT+L"))
        self.llaheta_pushButton.setText(_translate("Form", "Lähetä"))
        self.llaheta_pushButton.setShortcut(_translate("Form", "Alt+L"))
        self.lperu_pushButton.setToolTip(_translate("Form", "peru ja siirry takaisin kotisivulle, ALT+P"))
        self.lperu_pushButton.setText(_translate("Form", "Peru"))
        self.lperu_pushButton.setShortcut(_translate("Form", "Alt+P"))
        self.lvastaanottaja_lineEdit.setToolTip(_translate("Form", "vastaanottajan IP"))
        self.lsalattu_tdsto_lineEdit.setToolTip(_translate("Form", "salattu viesti-tiedosto"))
        self.lsalattu_tdsto_lineEdit.setText(_translate("Form", "lopuksi salattu viesti-tiedosto"))
        self.lveistintalletuspolku_lineEdit.setToolTip(_translate("Form", "viestin talletuspolku"))
        self.lveistintalletuspolku_lineEdit.setText(_translate("Form", "viestin talletuspolku"))
        self.lsijoitusavainpolku_lineEdit.setToolTip(_translate("Form", "sijoitusavaimen talletuspolku"))
        self.lsijoitusavainpolku_lineEdit.setText(_translate("Form", "sijoitusavaimen polku"))
        self.lkirjoitusavainpolku_lineEdit.setToolTip(_translate("Form", "kirjoitusavaimen talletuspolku"))
        self.lkirjoitusavainpolku_lineEdit.setText(_translate("Form", "kirjoitusavaimen polku"))
        self.laloitusnro_label.setText(_translate("Form", "Aloitusnumero:"))
        self.lvastaanottaja_label_3.setText(_translate("Form", "Kirjoitusavain:"))
        self.lvastaanottaja_label_4.setText(_translate("Form", "Sijoitusavain:"))
        self.laloitusnro_lineEdit.setToolTip(_translate("Form", "kirjoita joku luku <5000. Ei saa olla sama kuin viime kerralla."))
        self.lkirjoitusavain_tdsto_lineEdit.setToolTip(_translate("Form", "kirjoitusavain-tiedostonimi"))
        self.lkirjoitusavain_tdsto_lineEdit.setText(_translate("Form", "kirjoitusavain-tiedostonimi"))
        self.lsalattu_tdsto_lineEdit_3.setToolTip(_translate("Form", "sijoitusavain-tiedostonimi"))
        self.lsalattu_tdsto_lineEdit_3.setText(_translate("Form", "sijoitusavain-tiedostonimi"))
        self.lviesti_textBrowser.setToolTip(_translate("Form", "kirjoita viestisi tähän"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
