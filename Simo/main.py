# 20230801 14:59
# Simo-hakemistossa
# - python -m venv env
# seuraava käynnistää ohjelman env
# - env\scripts\activate
# - pip list
# - pip install pyqt5 pyqt5-tools
# - python.exe -m pip install --upgrade pip
#   TAI C:\Users\Simis\AppData\Local\Programs\Python\Python311\python.exe -m pip install --upgrade pip
#
# (desingner kansio on syvällä kansiorakenteessa, seuraavassa oikotie)
# - qt5-tools designer
# - resurssienhallinnassa kopio pyqt\env\scripts\pyuic5.exe työkansioon
# (kansiossa jossa pyuic5.e3xe on)
# - pyuic5 -x -o ui_kotisivu.py ui_kotisivu.ui 
# - pyuic5 -x -o ui_laheta.py ui_laheta.ui
# - pyuic5 -x -o ui_vastaanota.py ui_vastaanota.ui
#
# gitbashissä isähakemistossa githubin kloonaus: 
# git clone https://SimpeLe@github.com/SimpeLe/Viestittely-kansio
#
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

# from PyQt5 import QtQuick 2.2
# from PyQt5 import QtQuick 1.0

#import test_file_dialog as kans_hall
import fileMessageHandler as send
import fileReceiverHandler as pickup


class Claheta_klikkaus(qtw.QWidget): #tiedostoselaimet
    def __init__(self):
        super().__init__()
        self.title = 'Viestittely-lähetä - kansioselaus'
        self.ui = laheta()
        self.ui.setupUi(self)
        self.show()
        self.ui.lvastaanottaja_lineEdit.setFocus()
        self.ui.lviestiselaa_pushButton.clicked.connect(self.kansio_selaus_klikkaus)
        self.ui.llaheta_pushButton.clicked.connect(self.laheta_klik)
    
    def laheta_klik(self):
        print("tässä kutsu laheta-metodia")
#????????? jos keretään, voit tarkastaa onko muoto oikein

#????????? jos keretään, voit tarkastaa onko hakemisto olemassa
#????????? jos keretään, voit tarkastaa onko alotusnumero numero ja <5000

#????????? luo uusi kirjoitusavain vain kerran esim kerran kuussa tms
        send.createSourceCharacterFile(1) 
        send.testsearchPositionFromCharFile()
# käyttäjän kirjoittama viesti on kentässä: lviesti_plainTextEdit        
#????????? luo uusi salattu viesti-tiedosto (nyt testMessage.txt)

# kutsu file socketia

    def kansio_selaus_klikkaus(self):
        print("tässä avaa kansio-keskustelu ikkuna")
        hakemistoPolku = self.openSaveDirectoryNameDialog()
        print("def kansio_selaus_klikkaus hakemistoPolku: ", hakemistoPolku)
        # self.openFileNamesDialog()
        # self.saveFileDialog()
        # self.saveDirectoryDialog
        self.show()
        # kirjoittaa kenttään harmaan tekstin, joka häviää, kun fokus siirtyy kenttään
        # self.ui.lveistintalletuspolku_lineEdit.setPlaceholderText(qtc.QCoreApplication.translate("Form", "Nikke Nakkerton1"))
        self.ui.lveistintalletuspolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", hakemistoPolku))
        self.ui.lkirjoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", hakemistoPolku))
        self.ui.lsijoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", hakemistoPolku))
                

    def openSaveDirectoryNameDialog(self):
        # options = qtw.QFileDialog.Options()
        # options |= qtw.QFileDialog.DontUseNativeDialog
        # dialog = qtw.QFileDialog(self)
        # dialog.setFileMode(qtw.QFileDialog.DirectoryOnly)
        # #qtw.QFileDialog.setFileMode(qtw.QFileDialog.DirectoryOnly)
        dirName = qtw.QFileDialog.getExistingDirectory(self,"Viestittely-lähetä kansio-selaus")
        # dirName = qtw.QFileDialog.getExistingDirectory(self,"Viestittely-lähetä kansio-selaus", "", options=options)
        # dirName, _ = qtw.QFileDialog.getOpenFileName(self,"Viestittely-lähetä kansio-selaus", "","Text files (*.txt)", options=options)
        if dirName:
            print(dirName)
            return dirName


    def openFileNamesDialog(self):
        options = qtw.QFileDialog.Options()
        options |= qtw.QFileDialog.DontUseNativeDialog
        files, _ = qtw.QFileDialog.getOpenFileNames(self,"qtw.QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
    
    def saveFileDialog(self):
        options = qtw.QFileDialog.Options()
        options |= qtw.QFileDialog.DontUseNativeDialog
        fileName, _ = qtw.QFileDialog.getSaveFileName(self,"qtw.QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        self.setWindowTitle(self.title)
        if fileName:
            print(fileName)

    def saveDirectoryDialog(self):
        print ('saveDirectoryDialogin sisällä')
        options = qtw.QFileDialog.Options()
        options |= qtw.QFileDialog.DontUseNativeDialog
        sDirectory, _ = qtw.QFileDialog.getExistingDirectory(self,"qtw.QFileDialog.getExistingDirectory()","","All Files (*);;Text Files (*.txt)", options=options)
        if sDirectory:
            print(sDirectory)
            return sDirectory



class Cvastaanota_klikkaus(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = vastota()
        self.ui.setupUi(self)
        self.show()
        self.ui.vveistintalletuspolku_lineEdit.setFocus()
        self.ui.vviestiselaa_pushButton.clicked.connect(self.vastota_kansio_selaus_klikkaus)        
        self.ui.vvastaanota_pushButton.clicked.connect(self.vastaanota_klik) 

    def vastota_kansio_selaus_klikkaus(self):
        print("tässä avaa vastota (pickup) kansio-keskustelu ikkuna")
        vastOtaHakemistoPolku = self.openPickupDirectoryNameDialog()
        print("def vastota_kansio_selaus_klikkaus vastOtaHakemistoPolku: ", vastOtaHakemistoPolku)
        self.show()
        # kirjoittaa kenttään harmaan tekstin, joka häviää, kun fokus siirtyy kenttään
        # self.ui.lveistintalletuspolku_lineEdit.setPlaceholderText(qtc.QCoreApplication.translate("Form", "Nikke Nakkerton1"))
        self.ui.vveistintalletuspolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", vastOtaHakemistoPolku))
        self.ui.vkirjoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", vastOtaHakemistoPolku))
        self.ui.vsijoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", vastOtaHakemistoPolku))
    
    def openPickupDirectoryNameDialog(self):
        pickupDirName = qtw.QFileDialog.getExistingDirectory(self,"Viestittely-vastaanota kansio-selaus")
        if pickupDirName:
            print(pickupDirName)
            return pickupDirName

    def vastaanota_klik(self):
        print("tässä kutsu vastaanota-metodia")
# purettu viesti on kentässä: vviesti_plainTextEdit
        pickup.testfindIndexFromSourceCharFile()


# pitää matchata  widget-tyyppiin, joka on valittu designerissa
class Ckotisivu(qtw.QMainWindow): 
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lahetasivu = None
        self.vastotasivu = None
        self.show()
        self.ui.pkayttaja_lineEdit.setFocus()

        self.login_click()
#??????????        # napin painalluksen yhdistäminen luokan metodiin
#??????????        self.ui.pkirjaudu_pushButton.clicked.connect(self.login_click) 
# #        self.ui.cb_checkbox.setChecked(True)


    def login_click(self):
#   #        if users.username == self.ui.txt_username.text() and users.password==self.ui.txt_password.text():
#??????????         if self.ui.pkayttaja_lineEdit.text() == "k" and self.ui.psalis_lineEdit.text() == "k":
            print("Käyttäjä",self.ui.pkayttaja_lineEdit.text(),"sisällä")
            self.ui.plaheta_pushButton.setEnabled(True)
            self.ui.pvastaanota_pushButton.setEnabled(True)
            self.ui.pkopio_pushButton.setEnabled(True)
            self.ui.pkayttaja_lineEdit.setEnabled(False)
            self.ui.psalis_lineEdit.setEnabled(False)
            self.ui.pkirjaudu_pushButton.setEnabled(False)
            # self.hide()
            ## napin painalluksen yhdistäminen luokan metodiin ##
            self.ui.plaheta_pushButton.clicked.connect(self.show_claheta_klikkaus) 
            self.ui.pvastaanota_pushButton.clicked.connect(self.show_cvastaanota_klikkaus) 
#??????????        else:
#??????????            qtw.QMessageBox.critical(self, 'KIRJAUTUMISVIRHE', "Kirjoita oikea käyttäjätunnus ja salasana")
        
    def show_claheta_klikkaus(self, checked):
#        self.hide()
        self.lahetasivu = Claheta_klikkaus()

    def show_cvastaanota_klikkaus(self, checked):
#        self.hide()
        self.vastotasivu = Cvastaanota_klikkaus()

if __name__=='__main__':
    print("main alkaa")
    app = qtw.QApplication([])
    kotisivu = Ckotisivu()
    app.exec_()

  
