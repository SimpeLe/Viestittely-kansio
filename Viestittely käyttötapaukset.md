**- 1.1. Käyttötapaus	Kirjautuminen sovellukseen**
- **1.2. Tavoite**		Käyttäjä kirjautuu onnistuneesti sovellukseen
- **1.3. Käyttäjä**		Salatun viestin lähettäjä/vastaanottaja
- **1.4. Esiehto**		Käyttäjällä on oikeat kirjautumistunnukset
- **1.5. Jälkiehto**		Käyttäjä on kirjautunut sisään sovellukseen
- **1.6. Käyttötapauksen kulku**		- Käyttäjä avaa sovelluksen
                                - Sovelluksen kirjautumissivu aukeaa
                                - Käyttäjä syöttää käyttäjätunnuksen ja salasanan
                                - Sovellus tarkastaa ovatko tunnus ja salasana oikeat
                                - Käyttäjä kirjataan sisään sovellukseen ja pääsivu aukeaa

- **1.7. Poikkeuksellinen toiminta**		Käyttäjä antaa väärät kirjautumistiedot ja ei pääse sisään
sovellukseen 	

![kuva](https://github.com/SimpeLe/Viestittely-kansio/assets/135036998/13a832c7-b98e-4301-896b-151e0b1f2085)



**- 2.1. Käyttötapaus	Viestin lähettäminen ensimmäisellä kerralla**
- **2.2. Tavoite**		Käyttäjä lähettää salatun viestin
**- 2.3. Käyttäjä**		Salatun viestin lähettäjä
- 2.4. Esiehto		Käyttäjä osaa kansiorakenteen tietokoneessa		
- 2.5. Jälkiehto		Käyttäjä on lähettänyt viestin onnistuneesti	
- 2.6. Käyttötapauksen kulku - Käyttäjä syöttää vastaanottajan IP-osoitteen “lähetä” sivulla
- Käyttäjä valitsee kansion mihin salausavaimet kirjoitetaan
- Käyttäjä kirjoittaa viestin ja valitsee “lähetä”
- Sovellus luo salausavaimet ja salatun viestin
- Sovellus lähettää salatun viestin
  
- 2.7. Poikkeuksellinen toiminta		Käyttäjä valitsee kansioksi muistitikun mutta poistaa sen
tietokoneesta, tiedostot eivät tallennu kansioon

![kuva](https://github.com/SimpeLe/Viestittely-kansio/assets/135036998/f4c31971-26cc-40da-8a46-4c39663d65d5)



**- 3.1. Käyttötapaus 				Viestin vastaanottaminen**
- 3.2. Tavoite					Käyttäjä vastaanottaa salatun viestin
- 3.3. Käyttäjä				Salatun viestin vastaanottaja
- 3.4. Esiehto					Käyttäjä osaa kansiorakenteen tietokoneessa		
- 3.5. Jälkiehto				Käyttäjä on vastaanottanut viestin onnistuneesti	
- 3.6. Käyttötapauksen kulku			Käyttäjä käynnistää sovelluksen internet yhteyden
- Sovellus vastaanottaa viestin
- Käyttäjä valitsee kansion missä salausavaimet sijaitsevat
- Käyttäjä valitsee “vastaanota”
- Sovellus avaa viestin luettavaksi viestikenttään

- 3.7. Poikkeuksellinen toiminta		Käyttäjä valitsee kansioksi väärän kansion missä ei ole
salausavaimia, viestin avaaminen ei onnistu

![kuva](https://github.com/SimpeLe/Viestittely-kansio/assets/135036998/8d0d2980-94da-43dd-8666-4e946b8b1152)




