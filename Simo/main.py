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
from ui_laheta import Ui_MainWindow
from ui_vastaanota import Ui_MainWindow


from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
#
