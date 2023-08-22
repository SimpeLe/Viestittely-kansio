Käyttötapaus 				Kirjautuminen sovellukseen

Tavoite					Käyttäjä kirjautuu onnistuneesti sovellukseen
Käyttäjä				Salatun viestin lähettäjä/vastaanottaja
Esiehto					Käyttäjällä on oikeat kirjautumistunnukset 		
Jälkiehto				Käyttäjä on kirjautunut sisään sovellukseen	
Käyttötapauksen kulku			Käyttäjä avaa sovelluksen
Sovelluksen kirjautumissivu aukeaa
Käyttäjä syöttää käyttäjätunnuksen ja salasanan
Sovellus tarkastaa ovatko tunnus ja salasana oikeat
Käyttäjä kirjataan sisään sovellukseen ja pääsivu aukeaa

Poikkeuksellinen toiminta		Käyttäjä antaa väärät kirjautumistiedot ja ei pääse sisään 						sovellukseen 	

![kuva](https://github.com/SimpeLe/Viestittely-kansio/assets/135036998/13a832c7-b98e-4301-896b-151e0b1f2085)



Käyttötapaus 				Viestin lähettäminen ensimmäisellä kerralla
Tavoite					Käyttäjä lähettää salatun viestin
Käyttäjä				Salatun viestin lähettäjä
Esiehto					Käyttäjä osaa kansiorakenteen tietokoneessa		
Jälkiehto				Käyttäjä on lähettänyt viestin onnistuneesti	
Käyttötapauksen kulku			Käyttäjä syöttää vastaanottajan IP-osoitteen “lähetä” sivulla
Käyttäjä valitsee kansion mihin salausavaimet kirjoitetaan
Käyttäjä kirjoittaa viestin ja valitsee “lähetä”
Sovellus luo salausavaimet ja salatun viestin
Sovellus lähettää salatun viestin 
Poikkeuksellinen toiminta		Käyttäjä valitsee kansioksi muistitikun mutta poistaa sen 						tietokoneesta, tiedostot eivät tallennu kansioon

![kuva](https://github.com/SimpeLe/Viestittely-kansio/assets/135036998/f4c31971-26cc-40da-8a46-4c39663d65d5)



Käyttötapaus 				Viestin vastaanottaminen
Tavoite					Käyttäjä vastaanottaa salatun viestin
Käyttäjä				Salatun viestin vastaanottaja
Esiehto					Käyttäjä osaa kansiorakenteen tietokoneessa		
Jälkiehto				Käyttäjä on vastaanottanut viestin onnistuneesti	
Käyttötapauksen kulku			Käyttäjä käynnistää sovelluksen internet yhteyden
Sovellus vastaanottaa viestin
Käyttäjä valitsee kansion missä salausavaimet sijaitsevat
Käyttäjä valitsee “vastaanota”
Sovellus avaa viestin luettavaksi viestikenttään					
Poikkeuksellinen toiminta		Käyttäjä valitsee kansioksi väärän kansion missä ei ole 							salausavaimia, viestin avaaminen ei onnistu

![kuva](https://github.com/SimpeLe/Viestittely-kansio/assets/135036998/8d0d2980-94da-43dd-8666-4e946b8b1152)




