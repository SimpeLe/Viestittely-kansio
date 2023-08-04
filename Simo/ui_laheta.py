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
        icon.addPixmap(QtGui.QPixmap("cards.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.centralwidget.setToolTipDuration(2)
        self.centralwidget.setObjectName("centralwidget")
        self.lylaotsikko_label = QtWidgets.QLabel(self.centralwidget)
        self.lylaotsikko_label.setGeometry(QtCore.QRect(260, 20, 251, 61))
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
        self.llaheta_pushButton.setIconSize(QtCore.QSize(32, 32))
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
        self.lvastaanottaja_lineEdit.setGeometry(QtCore.QRect(210, 130, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lvastaanottaja_lineEdit.setFont(font)
        self.lvastaanottaja_lineEdit.setStatusTip("")
        self.lvastaanottaja_lineEdit.setMaxLength(12)
        self.lvastaanottaja_lineEdit.setObjectName("lvastaanottaja_lineEdit")
        self.lsalattu_tdsto_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lsalattu_tdsto_lineEdit.setEnabled(False)
        self.lsalattu_tdsto_lineEdit.setGeometry(QtCore.QRect(590, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lsalattu_tdsto_lineEdit.setFont(font)
        self.lsalattu_tdsto_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lsalattu_tdsto_lineEdit.setStatusTip("")
        self.lsalattu_tdsto_lineEdit.setText("")
        self.lsalattu_tdsto_lineEdit.setReadOnly(True)
        self.lsalattu_tdsto_lineEdit.setClearButtonEnabled(False)
        self.lsalattu_tdsto_lineEdit.setObjectName("lsalattu_tdsto_lineEdit")
        self.lveistintalletuspolku_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lveistintalletuspolku_lineEdit.setGeometry(QtCore.QRect(210, 170, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lveistintalletuspolku_lineEdit.setFont(font)
        self.lveistintalletuspolku_lineEdit.setToolTipDuration(-1)
        self.lveistintalletuspolku_lineEdit.setText("")
        self.lveistintalletuspolku_lineEdit.setObjectName("lveistintalletuspolku_lineEdit")
        self.lsijoitusavainpolku_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lsijoitusavainpolku_lineEdit.setEnabled(False)
        self.lsijoitusavainpolku_lineEdit.setGeometry(QtCore.QRect(210, 400, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lsijoitusavainpolku_lineEdit.setFont(font)
        self.lsijoitusavainpolku_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lsijoitusavainpolku_lineEdit.setStatusTip("")
        self.lsijoitusavainpolku_lineEdit.setText("")
        self.lsijoitusavainpolku_lineEdit.setReadOnly(True)
        self.lsijoitusavainpolku_lineEdit.setObjectName("lsijoitusavainpolku_lineEdit")
        self.lkirjoitusavainpolku_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lkirjoitusavainpolku_lineEdit.setEnabled(False)
        self.lkirjoitusavainpolku_lineEdit.setGeometry(QtCore.QRect(210, 360, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lkirjoitusavainpolku_lineEdit.setFont(font)
        self.lkirjoitusavainpolku_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lkirjoitusavainpolku_lineEdit.setStatusTip("")
        self.lkirjoitusavainpolku_lineEdit.setText("")
        self.lkirjoitusavainpolku_lineEdit.setReadOnly(True)
        self.lkirjoitusavainpolku_lineEdit.setObjectName("lkirjoitusavainpolku_lineEdit")
        self.lkirjoitusavain_label = QtWidgets.QLabel(self.centralwidget)
        self.lkirjoitusavain_label.setGeometry(QtCore.QRect(70, 360, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lkirjoitusavain_label.setFont(font)
        self.lkirjoitusavain_label.setObjectName("lkirjoitusavain_label")
        self.lsijoitusavain_label = QtWidgets.QLabel(self.centralwidget)
        self.lsijoitusavain_label.setGeometry(QtCore.QRect(80, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lsijoitusavain_label.setFont(font)
        self.lsijoitusavain_label.setObjectName("lsijoitusavain_label")
        self.lkirjoitusavain_tdsto_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lkirjoitusavain_tdsto_lineEdit.setEnabled(False)
        self.lkirjoitusavain_tdsto_lineEdit.setGeometry(QtCore.QRect(580, 360, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lkirjoitusavain_tdsto_lineEdit.setFont(font)
        self.lkirjoitusavain_tdsto_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lkirjoitusavain_tdsto_lineEdit.setStatusTip("")
        self.lkirjoitusavain_tdsto_lineEdit.setText("")
        self.lkirjoitusavain_tdsto_lineEdit.setReadOnly(True)
        self.lkirjoitusavain_tdsto_lineEdit.setObjectName("lkirjoitusavain_tdsto_lineEdit")
        self.lsijoitusavain_tdsto_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lsijoitusavain_tdsto_lineEdit.setEnabled(False)
        self.lsijoitusavain_tdsto_lineEdit.setGeometry(QtCore.QRect(580, 400, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lsijoitusavain_tdsto_lineEdit.setFont(font)
        self.lsijoitusavain_tdsto_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lsijoitusavain_tdsto_lineEdit.setStatusTip("")
        self.lsijoitusavain_tdsto_lineEdit.setText("")
        self.lsijoitusavain_tdsto_lineEdit.setReadOnly(True)
        self.lsijoitusavain_tdsto_lineEdit.setObjectName("lsijoitusavain_tdsto_lineEdit")
        self.lviesti_plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.lviesti_plainTextEdit.setGeometry(QtCore.QRect(210, 210, 551, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lviesti_plainTextEdit.setFont(font)
        self.lviesti_plainTextEdit.setPlainText("")
        self.lviesti_plainTextEdit.setObjectName("lviesti_plainTextEdit")
        self.lviestiselaa_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.lviestiselaa_pushButton.setGeometry(QtCore.QRect(510, 170, 51, 31))
        self.lviestiselaa_pushButton.setObjectName("lviestiselaa_pushButton")
        self.lvastaanottaja_label.setBuddy(self.lvastaanottaja_lineEdit)
        self.lviesti_label.setBuddy(self.lveistintalletuspolku_lineEdit)
        self.lkirjoitusavain_label.setBuddy(self.lkirjoitusavain_tdsto_lineEdit)
        self.lsijoitusavain_label.setBuddy(self.lsijoitusavain_tdsto_lineEdit)

        self.retranslateUi(Form)
        self.lperu_pushButton.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lvastaanottaja_lineEdit, self.lveistintalletuspolku_lineEdit)
        Form.setTabOrder(self.lveistintalletuspolku_lineEdit, self.lviestiselaa_pushButton)
        Form.setTabOrder(self.lviestiselaa_pushButton, self.lviesti_plainTextEdit)
        Form.setTabOrder(self.lviesti_plainTextEdit, self.llaheta_pushButton)
        Form.setTabOrder(self.llaheta_pushButton, self.lperu_pushButton)
        Form.setTabOrder(self.lperu_pushButton, self.lsalattu_tdsto_lineEdit)
        Form.setTabOrder(self.lsalattu_tdsto_lineEdit, self.lkirjoitusavainpolku_lineEdit)
        Form.setTabOrder(self.lkirjoitusavainpolku_lineEdit, self.lkirjoitusavain_tdsto_lineEdit)
        Form.setTabOrder(self.lkirjoitusavain_tdsto_lineEdit, self.lsijoitusavainpolku_lineEdit)
        Form.setTabOrder(self.lsijoitusavainpolku_lineEdit, self.lsijoitusavain_tdsto_lineEdit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Viestittely-lähetä"))
        Form.setToolTip(_translate("Form", "Vie kursori haluamaasi kenttään tai painikkeelle, niin näet vihjeen."))
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
        self.lvastaanottaja_lineEdit.setPlaceholderText(_translate("Form", "vastaanottajan ip esim 127.0.0.25"))
        self.lsalattu_tdsto_lineEdit.setToolTip(_translate("Form", "salatun viesti-tiedoston nimi"))
        self.lsalattu_tdsto_lineEdit.setPlaceholderText(_translate("Form", "Message.txt"))
        self.lveistintalletuspolku_lineEdit.setToolTip(_translate("Form", "salatun viestin talletuspolku"))
        self.lveistintalletuspolku_lineEdit.setStatusTip(_translate("Form", "StatusTip viestin talletuspolku", "StatusTip-disambiquation viestin talletuspolku "))
        self.lveistintalletuspolku_lineEdit.setWhatsThis(_translate("Form", "whatsThis viestin talletuspolku", "whatsThis-disambiquation viestin talletuspolku "))
        self.lveistintalletuspolku_lineEdit.setPlaceholderText(_translate("Form", "viestin talletuspolku"))
        self.lsijoitusavainpolku_lineEdit.setToolTip(_translate("Form", "sijoitusavaimen talletuspolku"))
        self.lsijoitusavainpolku_lineEdit.setPlaceholderText(_translate("Form", "sijoitusavaimen tallennuspolku"))
        self.lkirjoitusavainpolku_lineEdit.setToolTip(_translate("Form", "kirjoitusavaimen talletuspolku"))
        self.lkirjoitusavainpolku_lineEdit.setPlaceholderText(_translate("Form", "kirjoitusavaimen tallennuspolku"))
        self.lkirjoitusavain_label.setText(_translate("Form", "Kirjoitusavain:"))
        self.lsijoitusavain_label.setText(_translate("Form", "Sijoitusavain:"))
        self.lkirjoitusavain_tdsto_lineEdit.setToolTip(_translate("Form", "kirjoitusavain-tiedostonimi"))
        self.lkirjoitusavain_tdsto_lineEdit.setPlaceholderText(_translate("Form", "sourceCharacterFile.txt"))
        self.lsijoitusavain_tdsto_lineEdit.setToolTip(_translate("Form", "sijoitusavain-tiedostonimi"))
        self.lsijoitusavain_tdsto_lineEdit.setPlaceholderText(_translate("Form", "locationKeyFile.txt"))
        self.lviesti_plainTextEdit.setToolTip(_translate("Form", "kirjoita viestisi tähän"))
        self.lviesti_plainTextEdit.setStatusTip(_translate("Form", "kirjoita viestisi tähänkirjoita"))
        self.lviesti_plainTextEdit.setWhatsThis(_translate("Form", "kirjoita viestisi tähänkirjoita"))
        self.lviesti_plainTextEdit.setPlaceholderText(_translate("Form", "kirjoita viestisi tähän"))
        self.lviestiselaa_pushButton.setToolTip(_translate("Form", "selaa välitettävien tiedostojen talletuspolkua"))
        self.lviestiselaa_pushButton.setText(_translate("Form", "Selaa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
