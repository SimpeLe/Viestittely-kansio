Toteutus:
1. Viestittely-kotisivu
   - käyttäjätunnus ja salasana-koodissa
   - käyttäjä- ja salasanahallinta (esim järjestelmävastaavan työt) eivät sisälly tähän versioon
   - sisäänkirjautumisen tarkastus
     
2. Viestittely-lähetä
   - käyttöliittymän toteutus pyqt:lla
   - odota kunnes käyttäjä kirjoittaa asematunnuksen (ja talletuspolku) viestin talletuspolku-kenttään, ohjelma kopio sen muihin talletuspolku-kenttiin
   - kenttään salattu viesti-tiedosto, ohjelma kirjoittaa oletusnimen "viesti.txt"
   - ALOITUSNUMERO ei saa olla sama kuin viimekerralla. ALOITUSNUMERO talletetaan c:\windows-kansioon tai muualle mihin python pystyy kirjoittamaan piilotettuun txt-tiedostoon
   - luo Kirjoitusavain-tiedosto, 1Mt, yksi merkitsevä merkki 128-merkin joukossa, kun käyttäjä klikkaa lähetä-painiketta
   - luo Sijoitusavain-tiedosto
   - luo aloituskohta Sijoitusavaimeen aloitusnumeron perusteella eli luo merkitsemättömiä merkkejä aloitusnumeroon asti
   - salakirjoita viesti tiedostoon
     
3. Viestittely-vastaanota
3.1. Avaa viesti
   - odota kunnes käyttäjä kirjoittaa asematunnuksen (ja talletuspolku) viestin talletuspolku-kenttään, ohjelma kopio sen muihin talletuspolku-kenttiin
   - kenttään salattu viesti-tiedosto, ohjelma kirjoittaa oletusnimen "viesti.txt"
   - kun käyttäjä on kirjoittanut tarvittavat kentät, ohjelma on valmis jatkamaan
   - purku siirtyy sijoitusavaimen aloitusnumero kohtaan, kun käyttäjä klikkaa vastaanota-painiketta
   - hae viestistä sijoitusavaimen osoittama merkki l. pura sijoitusavain ja talleta tauluun sijoitusavainpurku-taulu
   - sijoitusavainpurku-taulun mukaan voidaan hakea kirjoitusavaimesta oikeat merkit
   - esitä selväkielinen viesti

4. Tiedoston siirto
   - KIRJOITUSAVAIN välitetään tietoturvallisesti tiedostossa esim Signal, Telegram, Wickr
   - SIJOITUSAVAIN välitetään tietoturvallisesti tiedostossa
   - ALOITUSNUMERO välitetään toisella medialla kuin tiedostossa esim suusanallisesti, SMS, puhelu.
   - SALATTU VIESTI välitetään tiedostossa mielellään tietoturvallisesti FTP:llä, jonka on luotu Pythonin UI:lla. Jos aikaa jää, viestin voisi välittää Torpy:llä.

5. Viestittely-kopio (johonkin versioon)
