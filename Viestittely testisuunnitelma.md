1. TESTAUKSET TAVOITTEET		
	ohjelma toimii suomeksi	
	ohjelma toimii toivotulla tavalla ja tavoitteiden mukaan, kts kohta 9	
	vain oikeat syötteet kelpaavat ohjelmalle (moduli-testaus)	
	salattu- ja avain-tiedostojen luonti ja purku (moduli-testaus)	
	käyttöliittymä ja tiedostojen luonti toimivat yhdessä (yhdistämis-testi)	
	testejä tehdessä arvioidaan suorituskyvyä, periaatteessa ohjelma on niin pieni että vasteajat ovat siedettävät	
	käytettävyystestaus: ohjelma toimii hiirellä ja pitkälti pelkällä näppäimistöllä	
		
		
2. TESTIKATTAVUUS		
	ei testata muita laiteympäristöjä 	
	ei testata kuin windows 10 tai uudempi	
	ei testata onko IP-osoite olemassa	
	ei testata viestissä kuin ASCII merkit ja skandinaaviset aakkoset (åäö)	
		
		
3. TESTI MENETELMÄT		
	Pythonissa ajaminen: funktio, py-tiedosto (yksikkötestau) ja py-tiedostojen yhteistoiminta (integraatio- ja järjestelmätestaus)	
	Oikean ja virheellisen data syöttäminen	
	Print komennot ja logi-tiedosto	
	Regressiotestaus yksikkö- ja integraatio testien ohessa	
	Testejä ei automatisoida	
	Suoritykykytestaus yksikkö- ja integraatio testien ohessa 	
	- ei kuormitus, skaalautuvuus, kuormanjako- ja tasapaino ongelmia, koska pieni yhden käyttäjän sovellus yhdellä koneella	
		
		
4. TESTI RESURSSIT		
	Ville ja Simopekka	
	PC ja Windows 10 tai uudempi	
	Visual Studio Code, Python ja sen kirjastot	
	maksimissaan kaksi viikkoa	
	testaajilla ei lisäkoulutuksen tarvetta, poislukien opiskeltujen asioiden kertaaminen	
		
		
5. TESTIN VASTUUT JA ROOLIT		
	Ville tiedostojen muodostamisen ja vastaanoton testauksen suunnittelu ja testi	
	Simopekka käyttöliittymän ja socket IP-viestin välityksen testauksen suunnittelu ja testi	
	Ville ja Simopekka käyttöliittymän ja tiedostojen käytön yhteistoiminta	
		
		
5. TESTIAIKATAULU		
	Viikko 33 aikaa testaukselle, kehittämiselle ja korjaamiselle, tarvittaessa toinen viikko 34	
		
		
6. POISTUMISSUUNNITELMA		
	testaus päättyy riittävän onnistuneesti, esim toteutuu kohta 9.2. Melko tärkeitä testejä	
	viimeistään 23.8.2023	
		
		
7. RISKIT		
	käyttäjä lopettaa monimutkaisen ohjelman käytön	
	saadaanko python koodista yhden tiedoston exe-tiedosto	
	ei tietoturvariskejä datassa	
	salasana vain python koodissa, joten toimialueen salasanat eivät ole vaarassa	
	eri syistä johtuvat viiveet	
		
		
8. SEURANTA JA RAPORTOINTI		
	Aamu- ja iltapäiväpalavereissä seurataan testien etenemistä	
	Viikko palaverissä seurataan ja raportoidaan testien etenemistä	
		
		
9. PRIORITEETIT		
	9.1. Oleellisimpia testejä	
		ohjelma käynnistyy
		"kotisivulla" ohjelma päästää sisälle, ohjelma siirtyy "lähetä-sivulle", ohjelma siirtyy "vastaanota-sivulle"
		"lähetä-sivulla" käyttäjä voi kirjoittaa tallennuspolun, käyttäjä voi kirjoittaa viestin, salausavain-tiedostot luodaan, viesti salataan
		"vastaanota-sivulla" käyttäjä voi kirjoittaa hakemistopolun, viesti puretaan salausavaimia käyttäen
		käyttäjä voi sulke ohjelman
		viestin ja avaimien välitys toimii myös USP-tikulla
	9.2. Melko tärkeitä testejä	
		"lähetä-sivulla" valittu kansio on olemassa, viesti-kentässä lukee viesti, viesti sisältää vain sallittuja merkkejä (nyt ASCII ja åäö)
		"vastaanota-sivulla" valittu kansio on olemassa
	9.3. Hyvä olisi toimia testejä	
		"lähetä-sivulla" IP-numeroon lähetys toimii
		"vastaanota-sivulla" IP-numeron kuuntelu ja vastaanotto toimii
	9.4. Jatkokehitys testejä	
		IP-viestin lähettäminen toiselle toimialueelle
		"kopio viesti" toiminto kaikkineen
		IP-viestien vastaanoton (socket server) pyöriminen taustalla
		monen IP-viestin vastaanotto (socket server), todella hakala, koska nyt Viestittely-ohjelma purkaa viimeisimmän saapuneen viestin
		UTF-8 -merkistön salliminen viestissä
		message-tiedostossa olevien indeksien arvoja muutetaan satunnaisesti. Locationkeyfilessa on jokaiselle kirjaimelle oma satunnainen luku.
		
