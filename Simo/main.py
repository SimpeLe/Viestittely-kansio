# 20230817 14:03
# Simo-hakemistossa
# - python -m venv env
# seuraava käynnistää ohjelman env
# - env\scripts\activate
# - pip list
# - pip freeze > requirements.txt  # pip list eli kirjastot versioineen tiedostoon
# - pip install pyqt5 pyqt5-tools
# - pip3 install tqdm
# - pip install numpy
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
# - pyuic5 -x -o ui_kopioi.py ui_kopioi.ui
#
# gitbashissä isähakemistossa githubin kloonaus: 
# git clone https://SimpeLe@github.com/SimpeLe/Viestittely-kansio
#
# (seuraava käynnistää ohjelman. Katso että komentokehotteen edessä lukee "(env)")
# (jos ei lue "(env)", käynnistä virtuaaliympäristö env\scripts\activate)
# - python ui_kotisivu.py 
# - python main.py
 
# - tee törkeesti muutoksia main.py fileen Code Studiossa
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import os
import re
import string
import socket

# from PyQt5 import QtQuick 2.2
# from PyQt5 import QtQuick 1.0

from ui_kotisivu import Ui_MainWindow
from ui_laheta import Ui_Form as laheta
from ui_vastaanota import Ui_Form as vastota
from ui_kopioi import Ui_Form as kopio

import fileMessageHandler as send
import fileReceiverHandler as pickup
import socketSendFile as socSend
import socketReceiveFile as socRecv


#########################################################################################################################
# käyttöliittymän(UI) laheta-sivu. Käyttäjä kirjoittaa viestin ja luodaan salattu viesti
class Claheta_klikkaus(qtw.QWidget): #
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
        # print("tässä kutsu laheta-metodia")        
        hakemistopolku = self.ui.lveistintalletuspolku_lineEdit.text()
        # print ("def lahet_klik(self):ssä hakemistopolku: ", hakemistopolku)
        # käyttäjän kirjoittama viesti on kentässä: lviesti_plainTextEdit  
        lahetettavaViesti = self.ui.lviesti_plainTextEdit.toPlainText()
        # print ("lahetettavaViesti toPlainText():n jälkeen: ",lahetettavaViesti)

        # sisältääkö viesti vain ASCII- ja scandi-merkkejä? Jos ei sisällä, korvaa sallimaton merkki alaviivalla "_"
        sallitutMerkit = string.ascii_letters + string.digits + string.punctuation +"äöåÄÖÅ" +'.' + "\n" + " " + "\t" + "\v" + "\r" 
        for kirjain in lahetettavaViesti:
            if kirjain not in sallitutMerkit:
                # print("kirjain: ", kirjain)
                lahetettavaViesti = lahetettavaViesti.replace(kirjain, '_')
                # print("lahetettavaViesti (if not sallitutMerkit:ssa):", lahetettavaViesti)
        # print ("laheta_klik(self):ssa lahetettavaViesti:", lahetettavaViesti)

        # Viestin maksimi pituus ja kirjoitetun viestin pituus
        # print("lahetettavaViesti:ssä on merkkejä:", len(lahetettavaViesti))
        ViestinMaxPituus = 12 
        viestinPituus = len(lahetettavaViesti)
        if viestinPituus <= ViestinMaxPituus:
            viestiPituusOK = True
        else:
            viestiPituusOK = False

        # Onko tallennuspolku olemassa? Onko viesti riittävän lyhyt? 
        if hakemistopolku != "" and os.path.isdir(hakemistopolku) \
            and lahetettavaViesti != "" and viestiPituusOK:  
            send.setLogger()
            send.getPathFromUI(hakemistopolku)
            send.getMessageFromUI(lahetettavaViesti)
            send.createMessage()
            IP_LahetysValinta = qtw.QMessageBox.question(self, 'Tiedostojen kirjoitus', \
                "Viestin ja avaimien tallennus päättyi. Haluatko lähettää viestin IP-osoitteeseen? Jos kyllä, vastaanottajan IP-serveri pitää olla päällä ", \
                qtw.QMessageBox.Yes | qtw.QMessageBox.No, qtw.QMessageBox.No)
            jataLahetysIkkunaAuki = True
            if IP_LahetysValinta == qtw.QMessageBox.Yes:
                # print("* Lähetä viesti IP:hen")
                vastOttIP = self.ui.lvastaanottaja_lineEdit.text()
                vastOttPortti = self.ui.lvastaanottajanportti_lineEdit.text()
                try:
                    # print("vastOttIP 2. IP muoto oikein:", vastOttIP)
                    socket.inet_aton(vastOttIP)
                    IPmuotoinen = True
                except socket.error:
                    # print("vastOttIP 3. IP muotovirhe:", vastOttIP)
                    IPmuotoinen = False
                # print ("vastOttPortti 1.: ", vastOttPortti)
                if IPmuotoinen and vastOttPortti != "" and vastOttPortti.isnumeric():
                    vastOttPortti = int(vastOttPortti)
                    if vastOttPortti > 0 and vastOttPortti < 65535:
                        IPeiVastaa = socSend.sendFileViaIP(vastOttIP, vastOttPortti, "messageFile.txt")
                        if IPeiVastaa:
                            jataLahetysIkkunaAuki = False
                            qtw.QMessageBox.critical(self, 'IP-osoite ei vastaa', "Pyydä vastaanottajaa avaamaan IP-vastaanotto")        
                    elif vastOttPortti < 0 or vastOttPortti > 65535:
                        jataLahetysIkkunaAuki = False
                        qtw.QMessageBox.critical(self, 'Portti on mahdoton', "Kirjoita mahdollinen porttinumero 1-65535")        
                elif not(IPmuotoinen):
                        jataLahetysIkkunaAuki = False
                        qtw.QMessageBox.critical(self, 'IP-osoite on mahdoton', "Kirjoita mahdollinen osoite")        
                elif vastOttPortti == "" or not(vastOttPortti.isnumeric()):
                    jataLahetysIkkunaAuki = False
                    qtw.QMessageBox.critical(self, 'Portti on mahdoton', "Kirjoita mahdollinen porttinumero 1-65535")        
            if jataLahetysIkkunaAuki:
                self.close()
        elif hakemistopolku == "" or os.path.isdir(hakemistopolku) == False: 
            qtw.QMessageBox.critical(self, 'Kansio puuttuu', "Valitse olemassa oleva tallennuspolku")
        elif lahetettavaViesti == "" or viestiPituusOK == False:
            qtw.QMessageBox.critical(self, 'Viesti puuttuu', f"Kirjoita viesti, jossa on enintään {ViestinMaxPituus} merkkiä")
        
    # kutsu kansio-keskustelu ikkunaa ja täytä UI:n kansio kentät
    def kansio_selaus_klikkaus(self):
        # print("tässä avaa kansio-keskustelu ikkuna")
        hakemistoPolku = self.openSaveDirectoryNameDialog()
        # print("def kansio_selaus_klikkaus(self) hakemistoPolku: ", hakemistoPolku)
        # self.openFileNamesDialog()
        # self.saveFileDialog()
        # self.saveDirectoryDialog
        self.show()
        # kirjoittaa kenttään harmaan tekstin, joka häviää, kun fokus siirtyy kenttään
        # self.ui.lveistintalletuspolku_lineEdit.setPlaceholderText(qtc.QCoreApplication.translate("Form", "Nikke Nakkerton1"))
        self.ui.lveistintalletuspolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", hakemistoPolku))
        self.ui.lkirjoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", hakemistoPolku))
        self.ui.lsijoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", hakemistoPolku))
        return hakemistoPolku
                
    # avaa resurssienhallinnan tyyppinen kansio-valinta-ikkuna
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
            # print(dirName)
            return dirName


    # def openFileNamesDialog(self):
    #     options = qtw.QFileDialog.Options()
    #     options |= qtw.QFileDialog.DontUseNativeDialog
    #     files, _ = qtw.QFileDialog.getOpenFileNames(self,"qtw.QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
    #     if files:
    #         print(files)
    
    # def saveFileDialog(self):
    #     options = qtw.QFileDialog.Options()
    #     options |= qtw.QFileDialog.DontUseNativeDialog
    #     fileName, _ = qtw.QFileDialog.getSaveFileName(self,"qtw.QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    #     self.setWindowTitle(self.title)
    #     if fileName:
    #         print(fileName)

    # def saveDirectoryDialog(self):
    #     print ('saveDirectoryDialogin sisällä')
    #     options = qtw.QFileDialog.Options()
    #     options |= qtw.QFileDialog.DontUseNativeDialog
    #     sDirectory, _ = qtw.QFileDialog.getExistingDirectory(self,"qtw.QFileDialog.getExistingDirectory()","","All Files (*);;Text Files (*.txt)", options=options)
    #     if sDirectory:
    #         print(sDirectory)
    #         return sDirectory



#########################################################################################################################
# kun käyttäjä klikkaa "vastaanota"-painiketta kotisivu-näytössä, haluaa purkaa salatun viestin
class Cvastaanota_klikkaus(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = vastota()
        self.ui.setupUi(self)
        self.show()
        self.ui.vveistintalletuspolku_lineEdit.setFocus()
        self.ui.vviestiselaa_pushButton.clicked.connect(self.vastota_kansio_selaus_klikkaus)        
        self.ui.vvastaanota_pushButton.clicked.connect(self.vastaanota_klik) 
        self.ui.vIP_vastaanotto_pushButton.clicked.connect(self.VastOtaViestiIP_lla) 


    # kun käyttäjä klikkaa "Selaus"-painiketta, hän pääsee selaamaan kansioita
    def vastota_kansio_selaus_klikkaus(self):
        # print("tässä avaa vastota (pickup) kansio-keskustelu ikkuna")
        vastOtaHakemistoPolku = self.openPickupDirectoryNameDialog()
        # print("def vastota_kansio_selaus_klikkaus(self):ssä vastOtaHakemistoPolku: ", vastOtaHakemistoPolku)
        self.show()
        self.ui.vveistintalletuspolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", vastOtaHakemistoPolku))
        self.ui.vkirjoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", vastOtaHakemistoPolku))
        self.ui.vsijoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", vastOtaHakemistoPolku))
    
    # selaa kansioita vastaanotto-sivulla
    def openPickupDirectoryNameDialog(self):
        pickupDirName = qtw.QFileDialog.getExistingDirectory(self,"Viestittely-vastaanota kansio-selaus")
        if pickupDirName:
            # print(pickupDirName)
            return pickupDirName

    # kun käyttäjä klikkaa "Vastaanota"-painiketta, pura salattu viesti
    def vastaanota_klik(self):
        # print("tässä kutsu vastaanota-metodia")
        vastOtaPolku = self.ui.vveistintalletuspolku_lineEdit.text()
        # print ("vastaanota_klik(self):ssä vastOtaPolku: ", vastOtaPolku)
        if vastOtaPolku != "" and os.path.isdir(vastOtaPolku):
            pickup.setLogger()
            pickup.getPathFromUI(vastOtaPolku)
            pickup.findCharByIndexFromSourceCharFile() 
            # purettu viesti on kentässä: vviesti_plainTextEdit
            purettuviesti = pickup.offerMessageToUI()
            self.ui.vviesti_plainTextEdit.setPlainText(purettuviesti) 
        elif vastOtaPolku == "" or os.path.isdir(vastOtaPolku) == False: 
            qtw.QMessageBox.critical(self, 'Kansio puuttuu', "Valitse olemassa oleva tallennuspolku")

    # käynnistä socket serveri viestin vastaanottamiseksi IP-osoitteella
    def VastOtaViestiIP_lla(self):
        qtw.QMessageBox.information(self, 'IP-osoitteesi odottaa viestiä', \
            "Odota, kunnes viesti saapuu tai odota hetki, kunnes vastaanotto päättyy. Paina OK, niin vastaanotto alkaa")
        IPvastaOtaPolku = self.ui.vveistintalletuspolku_lineEdit.text()
        # print ("VastOtaViestiIP_lla(self):ssä IPvastaOtaPolku: ", IPvastaOtaPolku)
        if IPvastaOtaPolku != "" and os.path.isdir(IPvastaOtaPolku):
## ????????????? vaihda työkansio käyttäjän valitsemaksi        
            # parametrit: socket-portti, sekunnit (jotka serveri odottaa viestiä)...
            # ja polku, johon IP-viesti luetaa
            socRecv.RecvFileViaIP(5001, 7, IPvastaOtaPolku) 
        elif IPvastaOtaPolku == "" or os.path.isdir(IPvastaOtaPolku) == False: 
            qtw.QMessageBox.critical(self, 'Kansio puuttuu', "Valitse olemassa oleva tallennuspolku")



#########################################################################################################################
# käyttöliittymän(UI) kopioi-sivu. Käyttäjä kopio tai noutaa viestejä
class Ckopio_Klikkaus(qtw.QWidget): 
    def __init__(self):
        super().__init__()
        self.title = 'Viestittely-kopio'
        self.ui = kopio()
        self.ui.setupUi(self)
        self.show()
        self.valitse_kopio_nouda()
        self.ui.kselaalahdekansio_pushButton.setFocus()
        self.ui.kselaalahdekansio_pushButton.clicked.connect(self.klahdekansio_selaus_klikkaus)
        self.ui.kselaakohdekansio_pushButton.clicked.connect(self.kkohdekansio_selaus_klikkaus)
        self.ui.kkopio_pushButton.clicked.connect(self.kopio_klik)
        self.ui.knouda_pushButton.clicked.connect(self.nouda_klik)


    def valitse_kopio_nouda(self):
        box = qtw.QMessageBox()
        box.setIcon(qtw.QMessageBox.Question)
        box.setWindowTitle('Kopioi tai nouda')
        box.setText('Haluatko kopioida viestin monien joukkoon vai noutaa viestin useiden joukosta?')
        box.setStandardButtons(qtw.QMessageBox.Yes|qtw.QMessageBox.No)
        buttonY = box.button(qtw.QMessageBox.Yes)
        buttonY.setText('Kopioi')
        buttonN = box.button(qtw.QMessageBox.No)
        buttonN.setText('Nouda')
        box.exec_()
        if box.clickedButton() == buttonN:
            self.ui.knouda_pushButton.setEnabled(True)
            self.ui.kkopio_pushButton.setEnabled(False)
            # kirjoittaa kenttään harmaan tekstin, joka häviää, kun fokus siirtyy kenttään
            self.ui.klahde_tdsto_lineEdit.setPlaceholderText(qtc.QCoreApplication.translate("Form", "Messages.txt"))
            self.ui.kkohde_tdsto_lineEdit.setPlaceholderText(qtc.QCoreApplication.translate("Form", "MessageFile.txt"))

    # kutsu lahde kansio-keskustelu ikkunaa
    def klahdekansio_selaus_klikkaus(self):
        lahdehakemistoPolku = qtw.QFileDialog.getExistingDirectory(self,"Viestittely-kopio kansio-selaus")
        self.show()
        self.ui.klahdepolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", lahdehakemistoPolku))
        self.ui.kkohdepolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", lahdehakemistoPolku))
        return lahdehakemistoPolku

    # kutsu kohde kansio-keskustelu ikkunaa
    def kkohdekansio_selaus_klikkaus(self):
        kohdehakemistoPolku = qtw.QFileDialog.getExistingDirectory(self,"Viestittely-nouda kansio-selaus")
        self.show()
        self.ui.kkohdepolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", kohdehakemistoPolku))
        return kohdehakemistoPolku
 
    # kutsu tiedostojen kopiointi metodeja
    def kopio_klik(self):
        lahdepolku = self.ui.klahdepolku_lineEdit.text()
        kohdepolku = self.ui.kkohdepolku_lineEdit.text()
        # Ovatko kansiot olemassa? 
        if os.path.isdir(lahdepolku) and os.path.isdir(kohdepolku):
            print("tässä kutsu tiedoston kopiointia")  
        elif os.path.isdir(lahdepolku) == False: 
            qtw.QMessageBox.critical(self, 'Lähdetiedoston kansio puuttuu', "Valitse olemassa oleva kansiopolku")
        elif os.path.isdir(kohdepolku) == False: 
            qtw.QMessageBox.critical(self, 'Kohdetiedoston kansio puuttuu', "Valitse olemassa oleva kansiopolku")

    # kutsu tiedostojen nouda metodeja
    def nouda_klik(self):
        lahdePolku = self.ui.klahdepolku_lineEdit.text()
        kohdePolku = self.ui.kkohdepolku_lineEdit.text()
        # Ovatko kansiot olemassa? 
        if os.path.isdir(lahdePolku) and os.path.isdir(kohdePolku):
            print("tässä kutsu tiedoston noutoa")  
        elif os.path.isdir(lahdePolku) == False: 
            qtw.QMessageBox.critical(self, 'Lähdetiedoston kansio puuttuu', "Valitse olemassa oleva kansiopolku")
        elif os.path.isdir(kohdePolku) == False: 
            qtw.QMessageBox.critical(self, 'Kohdetiedoston kansio puuttuu', "Valitse olemassa oleva kansiopolku")


        
#########################################################################################################################
# pääsivu - kotisivu
class Ckotisivu(qtw.QMainWindow): 
    # pitää matchata  widget-tyyppiin, joka on valittu designerissa
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lahetasivu = None
        self.vastotasivu = None
        self.show()
        self.ui.pkayttaja_lineEdit.setFocus()
        # napin painalluksen yhdistäminen luokan metodiin
        self.ui.pkirjaudu_pushButton.clicked.connect(self.login_click) 
        # self.ui.cb_checkbox.setChecked(True)

    # tarkastetaan käyttäjätunnus ja salasana
    def login_click(self):
        # if users.username == self.ui.txt_username.text() and users.password==self.ui.txt_password.text():
        if self.ui.pkayttaja_lineEdit.text() == "k" and self.ui.psalis_lineEdit.text() == "k":
            # print("Käyttäjä",self.ui.pkayttaja_lineEdit.text(),"sisällä")
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
            self.ui.pkopio_pushButton.clicked.connect(self.show_ckopio_klikkaus) 
        else:
            qtw.QMessageBox.critical(self, 'KIRJAUTUMISVIRHE', "Kirjoita oikea käyttäjätunnus ja salasana")
        
    def show_claheta_klikkaus(self, checked):
#        self.hide()
        self.lahetasivu = Claheta_klikkaus()

    def show_cvastaanota_klikkaus(self, checked):
#        self.hide()
        self.vastotasivu = Cvastaanota_klikkaus()
    
    def show_ckopio_klikkaus(self, checked):
#        self.hide()
        self.kopioSivu = Ckopio_Klikkaus()

if __name__=='__main__':
    print("main alkaa")
    app = qtw.QApplication([])
    kotisivu = Ckotisivu()
    app.exec_()

    

  
