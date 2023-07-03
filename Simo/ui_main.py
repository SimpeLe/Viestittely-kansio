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
# - kopio pyqt\env\scripts\pyuic5.exe työkansioon
# - pyuic5 -x -o ui_login_application.py ui_login_application.ui (kansiossa jossa pyuic5.e3xe on)
# (seuraava käynnistää ohjelman. Katso että komentokehotteen edessä lukee "(env)")
# (jos ei lue "(env)", käynnistä virtuaaliympäristö env\scripts\activate)
# - python ui_login_application.py 

# - tee törkeesti muutoksia main.py fileen Code Studiossa
#     from ui_login_application import Ui_MainWindow

#     from PyQt5 import QtWidgets as qtw
#     from PyQt5 import QtCore as qtc
