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

              ![kuva](https://github.com/SimpeLe/Viestittely-kansio/assets/135036998/2ef167f2-e9bd-475a-ba64-6d1c4f086b7c)




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

                ![kuva](https://github.com/SimpeLe/Viestittely-kansio/assets/135036998/7255f525-b24e-4185-b303-13f7fe5f9cbf)



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




