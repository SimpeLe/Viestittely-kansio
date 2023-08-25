**Python TYPO4 kevät 2023 Viestittely-ohjelman kuvaus**

Viestittely-ohjelmaa käytetään viestien salaamiseen. Lähettäjä ja vastaanottaja käyttävät saman ohjelman eri sivuja. Lähettäjä voi lähettää viestin vastaanottajan IP-osoitteseen ja porttiin, jos vastaanottajan reitittimessä on portti avattu. Viestissä voi käyttää amerikkalaista (ASCII) tai suomalaista (åäö) merkistöä. 

Viestittely-ohjelma luo lähetyksessä salatun viesti-tiedoston ja kaksi avain-tiedostoa. Avaimet annetaan vastaanottajalle esim tikulla tai postitse. Itse salatun viestin voi lähettää esim ohjelmilla Signal, Telegram, Wickr, Outlookilla.

Ohjelma tiedostoja ovat: fileMessageHandler.py, fileReceiverHandler.py, main.py, socketReceiveFile.py, socketSendFile.py. 23.8.2023 Python versio on 3.11.4.
- main.py, käynnistä Viestittely-ohjelma tästä tiedostosta. Ohjelman käyttäjä tunnus on 'k' ja salasana 'k'. 

Jos ajat ohjelmaa Pythonilla, pitää asentaa seuraavat kirjastot.
- pip install pyqt5 pyqt5-tools
- pip3 install tqdm
- pip install numpy

requirements.txt:n mukaan kirjastoversiot ovat:
async-generator==1.10
attrs==23.1.0
beautifulsoup4==4.12.2
certifi==2023.5.7
cffi==1.15.1
charset-normalizer==3.1.0
click==8.1.3
colorama==0.4.6
exceptiongroup==1.1.1
h11==0.14.0
idna==3.4
mysql-connector-python==8.0.32
numpy==1.25.2
outcome==1.2.0
pycparser==2.21
PyQt5==5.15.9
pyqt5-plugins==5.15.9.2.3
PyQt5-Qt5==5.15.2
PyQt5-sip==12.12.1
pyqt5-tools==5.15.9.3.3
PySocks==1.7.1
python-dotenv==1.0.0
qt5-applications==5.15.2.2.3
qt5-tools==5.15.2.1.3
requests==2.31.0
selenium==4.9.1
sniffio==1.3.0
sortedcontainers==2.4.0
soupsieve==2.4.1
tqdm==4.65.0
trio==0.22.0
trio-websocket==0.10.2
urllib3==2.0.2
wsproto==1.2.0
