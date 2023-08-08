**1 Tavoite** 
Luoda ohjelma, jolla voidaan lähettää viestejä salatusti. Ohjelman pitää olla kohtuullisen helppo käyttää, pieni ja nopea. Ohjelma ei saisi luoda logitiedostoja ja viestit pitäisi olla liki mahdoton purkaa. Toivottavaa on projektin jäsenet selviävät projektista suht ehyinä ja järjissään. Projekti toteuttaa laajasti opetushallituksen määrittelemän tietotekniikan perustutkinnon osantutkinnon tavoitteet.



**2 Asiakas**
Huumekauppiaat, terrosisti-sissit (ryssän kiusaajat) ja koirien ystävät, jotka haluavat käyttää salattua viestintää. Asiakas käyttää amerikkalaista (ASCII) tai suomalaista (åäö) merkistöä. Asiakas ymmärtää kansio/hakemisto-rakenteesta. Asiakas osaa tai oppii tiedonvälitysohjelman käytön esim. Signal, Telegram, Wickr.



**3 Käyttötapaukset**
Salatun viestin lähettäminen ja vastaanotto



**4 Vaatimusmäärittely**
Ohjelma pitää olla suht helppo ja miellyttävä käyttää, selkeä, pieni, nopea ja kaunis. Käyttöliittymä pitää toimi Windowsissa ja ohjataan hiirellä. Ohjelma välittää teksti-tiedostoja, ei kuvaa. Ohjelma salaa maksimissaan 10 000 merkkiä pitkän viestin. Salausavaimien luonti pitää onnistua milloin vain. Vaikka projektin asenne on letkeä, tavoitteet ovat korkealla.


 
**5 Tekninen toteutus ja testaus**
Projekti toteutetaan Windows 10 ja 11:lla. Versiohallinta ja projekti-aikataulutus tapahtuu GitHubissa. Projektikokoukset järjestetään MS Meetissä ja ne aikataulutetaan MS Outlookissa. Ohjelman käyttöliittymän suunnitelma luodaan sivustolla marvelapp.com. Käyttöliittymä luodaan PyQt5:llä. Ohjelma koodataan Python 3.11.4:lla. Testaukseen käytetään Unit Test-ympäristöä. Toteutukseen tukena käytetään tiimikaveria, opettajia, luokkakavereita, opintomateriaalia ja DuckDuckGo:ta.



**6. Projektivaiheet**

6.1. Yleistä
   - Projektisuunnitelma alustavaa suunnitelmaa. Aluksi kevyesti toimiva perussovellus jota voidaan laajentaa, ei liian isoa targettia kerralla

6.2. Määrittely
   - 6.2.1. Määritä oikeat termit yksiseliiteisesti niin että kummatkin osapuolet tietävät
   mistä asiasta puhutaan, näin koomunikointi pysyy selvänä.
   - 6.2.2. Kerää käyttäjä- ja järjestelmä vaatimukset
   - 6.2.3. Kerää ohjelmisto vaatimukset
   - 6.2.4. Tee käyttäjätapauksia
   - 6.2.5. Suunnittele UI kevytversio, esim. vertaa Kallen chat-sovellukseen, aluksi vähän protoillaan ei tarkkaa UI leiskaa heti
   UI:ssa pitää vaikka aluksi olla painonappi jolla avaa tiedoston mistä viesti voidaan lukea tiedostosta (myöhemmin viestin 
   lähetys), viesti luetaan ja näytetään viestikentässä
   - 6.2.6. Mieti rajapintoja eri ohjelmiston osien välillä esim. UI -tiedostun luku
   - 6.2.7. Määrittele salaukseen liittyvät termit vrt. kohta 1

6.3. Suunnittelu
   - 6.3.1. Toteutusmäärittely
   - 6.3.2. Vuokaavio/toimintalogiikka
   - 6.3.3. Teksti-tiedostojen suhteet https://github.com/SimpeLe/Viestittely-kansio/blob/Maarittely/Teksti_tiedostojen_suhteet.jpg
   - 6.3.4. Testaussuunnitelma
   
6.4. Toteutus - käyttöliittymä https://marvelapp.com/prototype/6c705j0/screen/92062571
   - 6.4.1. Viestittely-kotisivu (PyQt Simis) https://github.com/SimpeLe/Viestittely-kansio/blob/Maarittely/Kotisivu%2020230626.jpg
   - 6.4.2. Viestittely-lähetä (Simis) https://github.com/SimpeLe/Viestittely-kansio/blob/Maarittely/Laheta-sivu%2020230626.jpg
   - 6.4.3. Viestittely-vastaanota (Simis) https://github.com/SimpeLe/Viestittely-kansio/blob/Maarittely/Vastaanota-sivu%2020230626.jpg
   - 6.4.5. ehkä Viestittely-kopio (Simis) https://github.com/SimpeLe/Viestittely-kansio/blob/Maarittely/Kopio-sivu%2020230626.jpg
  
6.5. Toteutus - ohjelmointi
?? näytä koodia tai print screen  
   - 6.5.1. Viestittely-kotisivu (Simis)
   - 6.5.2. Viestittely-lähetä (Ville)
   - 6.5.3. Viestittely-vastaanota (Ville)
   - 6.5.4. Tiedoston siirto (Ville, Simis)
   - 6.5.5. ehkä Viestittely-kopio (Ville)
   
-- 6.6. Testaus
  
-- 6.7. Käyttöönotto
   6.7.1. Käyttöohje


