202308015
py:stä exe:een

asenna virtuaali ympäristö toimimaan (env)
pip install pyinstaller
pyinstaller --onefile 7.py
(luo dist-kansion, jossa yksi exe-tdsto)
(tarvittava-kansio, pitää kopioda dist-kansioon)

(luodaan myös 7.spec-file, jota voi muuttaa, esim hidden import-kohtaan voi lisätä kirjastoja)


