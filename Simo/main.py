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
# - python main.py 

# - tee törkeesti muutoksia main.py fileen Code Studiossa
from ui_kotisivu import Ui_MainWindow
from ui_laheta import Ui_Form as laheta
from ui_vastaanota import Ui_Form as vastota

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class Claheta_klikkaus(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = laheta()
        self.ui.setupUi(self)
        self.show()


class Cvastaanota_klikkaus(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = vastota()
        self.ui.setupUi(self)
        self.show()


class Ckotisivu(qtw.QMainWindow): # pitää matchata  widget-tyyppiin, joka on valittu designerissa
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lahetasivu = None
        self.vastotasivu = None
        #napin painalluksen yhdistäminen luokan metodiin
        self.ui.pkirjaudu_pushButton.clicked.connect(self.login_click) 
# #        self.ui.cb_checkbox.setChecked(True)
        self.show()

    def login_click(self):
 #        if users.username == self.ui.txt_username.text() and users.password==self.ui.txt_password.text():
        if self.ui.pkayttaja_lineEdit.text() == "k" and self.ui.psalis_lineEdit.text() == "k":
            print(self.ui.pkayttaja_lineEdit.text()," sisällä")
            # qtw.QMessageBox.information(self, 'ONNISTUI', 'Olet kirjautunut Viestittely-ohjelmaan')
            self.ui.plaheta_pushButton.setEnabled(True)
            self.ui.pvastaanota_pushButton.setEnabled(True)
            self.ui.pkopio_pushButton.setEnabled(True)
            self.ui.pkayttaja_lineEdit.setEnabled(False)
            self.ui.psalis_lineEdit.setEnabled(False)
            self.ui.pkirjaudu_pushButton.setEnabled(False)
            # self.hide()
            ## napin painalluksen yhdistäminen luokan metodiin ##
            # self.ui = flaheta_klikkaus() # tuo suoraan lähetä-ikkunan
            # self.ui.plaheta_pushButton.clicked.connect(self.Claheta_klikkaus) #'Ckotisivu' object has no attribute 'claheta_klikkaus'
            # self.ui.plaheta_pushButton.clicked.connect(Claheta_klikkaus) #tuo koti-ikkunan uudelleen näkyville

            # self.laheta_form = claheta_klikkaus() # tuo suoraan läheteä-ikkunan
            # self.laheta_form.show() # tuo suoraan läheteä-ikkunan

            self.ui.plaheta_pushButton.clicked.connect(self.show_claheta_klikkaus) 
            self.ui.pvastaanota_pushButton.clicked.connect(self.show_cvastaanota_klikkaus) 
        else:
            qtw.QMessageBox.critical(self, 'KIRJAUTUMISVIRHE', "Kirjoita oikea käyttäjätunnus ja salasana")
        
    def show_claheta_klikkaus(self, checked):
        if self.lahetasivu is None:
            self.lahetasivu = Claheta_klikkaus()
            self.lahetasivu.show()
        else:
            self.lahetasivu.close()
            self.lahetasivu = None

    def show_cvastaanota_klikkaus(self, checked):
        if self.vastotasivu is None:
            self.vastotasivu = Cvastaanota_klikkaus()
            self.vastotasivu.show()
        else:
            self.vastota.close()
            self.vastotasivu = None

if __name__=='__main__':
    app = qtw.QApplication([])
    kotisivu = Ckotisivu()
    app.exec_()
