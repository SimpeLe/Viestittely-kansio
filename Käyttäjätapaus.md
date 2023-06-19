1. Kehittynyt käyttäjä lähetettää viestin
Kuka?
	Kehittynyt käyttäjä lähetettää viestin
Mitä?
	Käyttäjä haluaa lähettää PC:llä viestejä salatusti ja helposti.
Miksi?
	Haluaa turvallista viestittelyä.
Esiehto:
	Tiedonvälitysohjelma esim Signal, Telegram, Wickr asennettu
	Vastaanottajan IP
	Tyhjä tikku tai muistikortti USP-portissa
Käyttötapauksen kulku:
	1. Käyttäjä kirjoittaa nastaanottajan IP:n
	2. Käyttäjä kirjoittaa viestin
	3. Käyttäjä kirjoittaa numeron kenttään "satunnainen numero" <5001, jota käytetään avaimen luontiin
	4. Käyttäjä painaa Lähetä-painiketta
	5. Ohjelma salaa viestin ja luo avaimen
	6. Ohjelma kirjoittaa salausavaimen tiedostoon tikulle
 	7. Ohjelma ilmoittaa, kun salausavain kirjoitettu ja viesti lähetetty 
 	8. Käyttäjä välittää avaimen ja satunnainen numero sovitulla tavalla vastaanottajalle esim tikulla
	

3.  Kehittynyt käyttäjä vastaanottaa viestin
Kuka?
	Kehittynyt käyttäjä vastaanottaa viestin
Mitä?
	Käyttäjä haluaa vastaanottaa PC:llä viestejä salatusti ja helposti.
Miksi?
	Haluaa turvallista viestittelyä.
Esiehto:
	Tiedonvälitysohjelma esim Signal, Telegram, Wickr asennettu
   	Lähettäjän IP
Käyttötapauksen kulku:
	1. Käyttäjä vastaanottaa avaimen sovitulla tavalla esim tikulta
 	2. Käyttäjä kirjoittaa Lähettäjän IP:n
 	3. Käyttäjä kirjoittaa avain-tiedoston ja sen polun avain-kenttään
  	4. Käyttäjä kirjoittaa lähettäjän kertoman numeron satunnainen numero-kenttään
  	5. Käyttäjä painaa Vastaanota-painike
   	6. Ohjelma vastaanottaa viestin python ui:lla
	7. Ohjelma ilmoittaa, kun viesti vastaanotettu
 	8. Ohjelma näyttää viestin

 
  	   
