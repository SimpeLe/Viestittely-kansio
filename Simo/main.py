# 20230703 9:55
# Simo-hakemistossa
# - python -m venv env
# - env\scripts\activate
# - pip list
# - pip install pyqt5 pyqt5-tools
# - python.exe -m pip install --upgrade pip
#   TAI C:\Users\Simis\AppData\Local\Programs\Python\Python311\python.exe -m pip install --upgrade pip
# (desingner kansio on syvällä kansiorakenteessa, seuraavassa oikotie)
# - qt5-tools designer
# - resurssienhallinnassa kopio pyqt\env\scripts\pyuic5.exe työkansioon
# - pyuic5 -x -o ui_kotisivu.py ui_kotisivu.ui (kansiossa jossa pyuic5.e3xe on)
# - pyuic5 -x -o ui_laheta.py ui_laheta.ui
# - pyuic5 -x -o ui_vastaanota.py ui_vastaanota.ui
# (seuraava käynnistää ohjelman. Katso että komentokehotteen edessä lukee "(env)")
# (jos ei lue "(env)", käynnistä virtuaaliympäristö env\scripts\activate)
# - python ui_kotisivu.py 

# - tee törkeesti muutoksia main.py fileen Code Studiossa
from ui_kotisivu import Ui_MainWindow
from ui_laheta import Ui_Form
# from ui_vastaanota import Ui_MainWindow

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class fkotisivu(qtw.QMainWindow): # pitää matchata  widget-tyyppiin, joka on valittu designerissa
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #napin painalluksen yhdistäminen luokan metodiin
        self.ui.pkirjaudu_pushButton.clicked.connect(self.login_click) 
# #        self.ui.cb_checkbox.setChecked(True)
        self.show()

    def login_click(self):
 #        if users.username == self.ui.txt_username.text() and users.password==self.ui.txt_password.text():
        if self.ui.pkayttaja_lineEdit.text() == "kalle" and self.ui.psalis_lineEdit.text() == "k":
            print("Kalle sisällä")
            qtw.QMessageBox.information(self, 'ONNISTUI', 'Olet kirjautunut Viestittely-ohjelmaan')
            # self.hide()
            # self.ui = flaheta_klikkaus() # tuo suoraan lähetä-ikkunan
            # napin painalluksen yhdistäminen luokan metodiin
            self.ui.plaheta_pushButton.clicked.connect(self.flaheta_klikkaus) 
        else:
            qtw.QMessageBox.critical(self, 'KIRJAUTUMISVIRHE', "Kirjoita oikea käyttäjätunnus ja salasana")
        
        
# class TokaWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#         self.show()
#         self.conn = db.connect('BOOKS')
#         book = db.fetch_latest_book(self.conn)
#         self.ui.btn_push.setText(book)

class flaheta_klikkaus(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()

if __name__=='__main__':
    app = qtw.QApplication([])
    kotisivu = fkotisivu()
    app.exec_()
