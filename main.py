
# 20230823 13:10
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
# git clone --branch main https://SimpeLe@github.com/SimpeLe/Viestittely-kansio
# 
# (seuraava käynnistää ohjelman. Katso että komentokehotteen edessä lukee "(env)")
# (jos ei lue "(env)", käynnistä virtuaaliympäristö env\scripts\activate)
# - python ui_kotisivu.py 
# - python main.py
 
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import os
import re
import string
import socket

from ui_kotisivu import Ui_MainWindow
from ui_laheta import Ui_Form as laheta
from ui_vastaanota import Ui_Form as vastota
from ui_kopioi import Ui_Form as kopio

import fileMessageHandler as send
import fileReceiverHandler as pickup
import fileMessageCopier as copy
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

    # käyttäjän lähetä-painikkeen klikkaus kutsuu laheta-metodia. Viestin salaus, avain-tiedostojen luonti, lähetys ehkä IP:llä
    def laheta_klik(self):
        lahHakPolku = self.ui.lveistintalletuspolku_lineEdit.text()
        lahetettavaViesti = self.ui.lviesti_plainTextEdit.toPlainText()

        # sisältääkö viesti vain ASCII- ja scandi-merkkejä? Jos ei sisällä, korvaa sallimaton merkki alaviivalla "_"
        sallitutMerkit = string.ascii_letters + string.digits + string.punctuation +"äöåÄÖÅ" +'.' + "\n" + " " + "\t" + "\v" + "\r" 
        for kirjain in lahetettavaViesti:
            if kirjain not in sallitutMerkit:
                lahetettavaViesti = lahetettavaViesti.replace(kirjain, '_')

        # Viestin maksimi pituus ja kirjoitetun viestin pituus
        ViestinMaxPituus = 10000 
        if lahetettavaViesti != "" and len(lahetettavaViesti) <= ViestinMaxPituus:
            viestiPituusOK = True
        else:
            viestiPituusOK = False
        # Onko tallennuspolku olemassa? Onko viesti riittävän lyhyt? 
        if os.path.isdir(lahHakPolku) and lahHakPolku != "C:/" \
            and viestiPituusOK:  
            # send.setLogger()
            send.getPathFromUI(lahHakPolku)
            send.getMessageFromUI(lahetettavaViesti)
            send.createMessage()
            IP_LahetysValinta = qtw.QMessageBox.question(self, 'Tiedostojen kirjoitus', \
                "Viestin ja avaimien tallennus päättyi. Haluatko lähettää viestin IP-osoitteeseen? Jos kyllä, vastaanottajan IP-serveri pitää olla päällä ", \
                qtw.QMessageBox.Yes | qtw.QMessageBox.No, qtw.QMessageBox.No)
            jataLahetysIkkunaAuki = True
            # käyttäjä haluaa lähettää viestin IP-osoitteeseen ja porttii
            if IP_LahetysValinta == qtw.QMessageBox.Yes:
                vastOttIP = self.ui.lvastaanottaja_lineEdit.text()
                vastOttPortti = self.ui.lvastaanottajanportti_lineEdit.text()
                # onko IP-osoite osoitteen muotoinen ja portti mahdollinen, jos ei virhe-ilmoituksia
                try:
                    socket.inet_aton(vastOttIP)
                    IPmuotoinen = True
                except socket.error:
                    IPmuotoinen = False
                if IPmuotoinen and vastOttPortti != "" and vastOttPortti.isnumeric():
                    vastOttPortti = int(vastOttPortti)
                    if vastOttPortti > 0 and vastOttPortti < 65535:
                        IPeiVastaa = socSend.sendFileViaIP(vastOttIP, vastOttPortti, lahHakPolku, "messageFile.txt")
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
        elif os.path.isdir(lahHakPolku) == False: 
            qtw.QMessageBox.critical(self, 'Epäkelpo kansio', "Valitse olemassa oleva kansiopolku")
        elif lahHakPolku == "C:/":
            qtw.QMessageBox.critical(self, 'Epäkelpo kansio', "Kansioon ole ei kirjoitusoikeutta. Valitse toinen kansiopolku")
        elif viestiPituusOK == False:
            qtw.QMessageBox.critical(self, 'Epäkelpo viesti', f"Kirjoita viesti, jossa on enintään {ViestinMaxPituus} merkkiä")
        
    # kutsu kansio-keskustelu ikkunaa ja täytä UI:n kansio kentät
    def kansio_selaus_klikkaus(self):
        selausPolku = self.openSaveDirectoryNameDialog()
        self.show()
        self.ui.lveistintalletuspolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", selausPolku))
        self.ui.lkirjoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", selausPolku))
        self.ui.lsijoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", selausPolku))
        return selausPolku
                
    # avaa resurssienhallinnan tyyppinen kansio-valinta-ikkuna
    def openSaveDirectoryNameDialog(self):
        dirName = qtw.QFileDialog.getExistingDirectory(self,"Viestittely-lähetä kansio-selaus")
        if dirName:
            # print(dirName)
            return dirName



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
        vastOtaHakemistoPolku = self.openPickupDirectoryNameDialog()
        self.show()
        self.ui.vveistintalletuspolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", vastOtaHakemistoPolku))
        self.ui.vkirjoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", vastOtaHakemistoPolku))
        self.ui.vsijoitusavainpolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", vastOtaHakemistoPolku))
    
    # selaa kansioita vastaanotto-sivulla
    def openPickupDirectoryNameDialog(self):
        pickupDirName = qtw.QFileDialog.getExistingDirectory(self,"Viestittely-vastaanota kansio-selaus")
        if pickupDirName:
            return pickupDirName

    # kun käyttäjä klikkaa "Vastaanota"-painiketta, pura salattu viesti
    def vastaanota_klik(self):
        vastOtaPolku = self.ui.vveistintalletuspolku_lineEdit.text()
        if os.path.isdir(vastOtaPolku) and vastOtaPolku != "C:/" :
            pickup.getPathFromUI(vastOtaPolku)
            pickup.findCharByIndexFromSourceCharFile()
            purettuviesti = pickup.offerMessageToUI()
            self.ui.vviesti_plainTextEdit.setPlainText(purettuviesti) 
            if purettuviesti == "" or purettuviesti == None:
                    qtw.QMessageBox.critical(self, 'Epäkelpo kansio tai tiedostoja puuttuu', \
                        "Kansiossa ei ole viestiä tai avain tiedostoja tai viesti on tuhottu, kun se on jo luettu")
        elif os.path.isdir(vastOtaPolku) == False: 
            qtw.QMessageBox.critical(self, 'Epäkelpo kansio', "Valitse olemassa oleva kansiopolku")
        elif vastOtaPolku == "C:/" :
            qtw.QMessageBox.critical(self, 'Epäkelpo kansio', "Kansioon ole ei kirjoitusoikeutta. Valitse toinen kansiopolku")

    # käynnistä socket serveri viestin vastaanottamiseksi IP-osoitteella
    def VastOtaViestiIP_lla(self):
        vastOtaPortti = self.ui.vvastaanottajanportti_lineEdit.text()
        IPvastaOtaPolku = self.ui.vveistintalletuspolku_lineEdit.text()
        # print ("VastOtaViestiIP_lla(self):ssä IPvastaOtaPolku: ", IPvastaOtaPolku)
        vkotiKansio = os.getcwd()
        # print ("main vkotiKansio:", vkotiKansio)
        # vkotiKansio = vkotiKansio.replace("\\","/")
        # print ("main vkotiKansio:", vkotiKansio)
        # print ("main kohdeKansio:", IPvastaOtaPolku)
        # os.chdir(IPvastaOtaPolku)
        # vtyoKansio = os.getcwd()
        # print ("main tyoKansio:", tyoKansio)
        # print ("main tyoKansio:", tyoKansio)
        # jos UI:ssä kansiopolku on epäkelpo käytä ohjelman vkotikansiota
        if os.path.isdir(IPvastaOtaPolku) == False:
            IPvastaOtaPolku = vkotiKansio
        if vastOtaPortti.isnumeric():
            vastOtaPortti = int(vastOtaPortti)
            if vastOtaPortti > 0 and vastOtaPortti < 65535:
                IPvastOttoOdotusAika = 20 #sekuntia
                qtw.QMessageBox.information(self, 'IP-osoitteesi ja porttisi dottaa viestiä', \
                    f"Odota, kunnes viesti saapuu tai odota {IPvastOttoOdotusAika} sekuntia. Paina OK, niin vastaanotto alkaa")
                # parametrit: socket-portti, sekunnit (jotka serveri odottaa viestiä)...
                # ja polku, johon IP-viesti luetaa
                socRecv.RecvFileViaIP(vastOtaPortti, IPvastOttoOdotusAika, IPvastaOtaPolku) 
            elif vastOtaPortti < 0 or vastOtaPortti > 65535:
                qtw.QMessageBox.critical(self, 'Portti on mahdoton', "Kirjoita mahdollinen porttinumero 1-65535")
        elif not (vastOtaPortti.isnumeric()):
            qtw.QMessageBox.critical(self, 'Portti on mahdoton', "Kirjoita mahdollinen porttinumero 1-65535")
        # tyoKansio = os.getcwd()
        # print ("main tyokansio2:", tyoKansio)



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

    # valinta-ikkuna haluaako käyttäjä kopoida vai noutaa
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

    # kutsu lahde-tiedoston kansio-keskustelu ikkunaa
    def klahdekansio_selaus_klikkaus(self):
        lahdehakemistoPolku = qtw.QFileDialog.getExistingDirectory(self,"Viestittely-kopio kansio-selaus")
        self.show()
        self.ui.klahdepolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", lahdehakemistoPolku))
        self.ui.kkohdepolku_lineEdit.setText(qtc.QCoreApplication.translate("MainWindow", lahdehakemistoPolku))
        return lahdehakemistoPolku

    # kutsu kohde-tiedoston kansio-keskustelu ikkunaa
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
            copy.copyOneMessageToList(kohdepolku, lahdepolku) # new 27.8
        elif os.path.isdir(lahdepolku) == False: 
            qtw.QMessageBox.critical(self, 'Lähdetiedoston epäkelpo kansio', "Valitse olemassa oleva kansiopolku")
        elif os.path.isdir(kohdepolku) == False: 
            qtw.QMessageBox.critical(self, 'Kohdetiedoston epäkelpo kansio', "Valitse olemassa oleva kansiopolku")

    # kutsu tiedostojen nouda metodeja
    def nouda_klik(self):
        lahdePolku = self.ui.klahdepolku_lineEdit.text()
        kohdePolku = self.ui.kkohdepolku_lineEdit.text()
        # Ovatko kansiot olemassa? 
        if os.path.isdir(lahdePolku) and os.path.isdir(kohdePolku):
            copy.retrieveCopy(kohdePolku, lahdePolku)  # new 27.8
        elif os.path.isdir(lahdePolku) == False: 
            qtw.QMessageBox.critical(self, 'Lähdetiedoston epäkelpo kansio', "Valitse olemassa oleva kansiopolku")
        elif os.path.isdir(kohdePolku) == False: 
            qtw.QMessageBox.critical(self, 'Kohdetiedoston epäkelpo kansio', "Valitse olemassa oleva kansiopolku")


        
#########################################################################################################################
# pääsivu - kotisivu
class Ckotisivu(qtw.QMainWindow): 
    # 
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
    # print("main alkaa")
    app = qtw.QApplication([])
    kotisivu = Ckotisivu()
    app.exec_()

