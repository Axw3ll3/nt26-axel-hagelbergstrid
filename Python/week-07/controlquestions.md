# 1 Vad är en baseline, och varför måste den mätas innan felet?

Baseline är hur nätet ser ut när allt fungerar. Det måste mätas innan felet för annars har man inget värde att jämföra med.

# 2 Varför räcker det inte att veta att det går 40 megabit just nu?

Siffran 40 megabit i sig betyder inget. Man behöver ha kapacitet och mönster över dygnet för att det ska betyda något.

# 3 Vilka fyra delar består en loggrad av?

En loggrad innehåller tidsstämpel, facility, nivå och mnemonic. Nivå och mnemonic är 2 ord från Cisco och är inte standardens.

# 4 Vilken loggnivå är allvarligast, 0 eller 7?

0 är värst. Skalan går från 7 som minst allvarlig och 0 som allvarligast.

# 5 Vad händer med enhetens logg vid en omstart, och vad gör du åt det?

Vid omstart töms loggen, därför det är viktigt att skicka loggen till en loggserver. Detta för att säkra att historiken finns kvar även vid omstart.

# 6 Vad frågar SNMP efter som syslog inte svarar på?

SNMP frågar om siffror i form av hur mycket trafik, hur många fel, hur varm enheten är. Sysloggen berättar vad som hänt, SNMP hur mycket.

# 7 Vilka tre frågor ställer du till en graf, i vilken ordning?

Till en graf frågar man om den normala nivån, när den ändrades och vad hände just då. I den ordningen. 

# 8 Nämn två visningsfilter i Wireshark och vad visar det?

Några visningsfilter i Wireshark är: 
'ip.addr' vilket visar all trafik till eller från en adress. 
tcp.port som visar all trafik på en port.
'arp' som visar ARP-trafik
'stp' som visar spanning-tree

# 9 Vad är skillnaden mellan ett visningsfilet och ett capture-filter?

Visningsfiltret döljer i efterhand, efter allt fångats. Capture-filter betämmer vad som fångas från början, samt har ett helt annat syntax.

# 10 Varför står lösernordet inte i Python-skriptet?

Lösenordet står inte i Python-skriptet eftersom det commitas. Ett lösen i en fil som ligger i ett repo är samma fel som en osanerad konfiguration, och det frågas därför efter när skriptet körs.

# 11 Skriv den engelska termen för vart och ett följande av följande: avvikelse, loggnivå och visningsfilter. Provet frågar efter dem.

anomaly, severity level, display filter

# 12 Loggen visar tre portflappar: 02:14:03.112–02:14:09.887, 02:31:44.201–02:31:51.664 och 03:02:18.339–03:02:25.005. Räkna ut hur länge varje avbrott varade, hur lång tid som gick mellan det första och det sista, och hur stor andel av porten var nere.

Avbrott 1: 6.775 sekudner

Avbrott 2: 7.463 sekunder

Avbrott 3: 6.666 sekunder

Sammanlagt: 20.9 sekunder

Från första raden till sista gick det 48 min och 22 sek, alltså 2902 sek. Porten var nere 20,9 sekunder av det, vilket blir 0.72 procent.

# 13 Nordviks förbindelse ut är 100 Mbit/s. Grafen visar i snitt 38 Mbit/s under ett femminutersintervall. Räkna ut hur många gigabyte som passerade under de fem minuterna, och förklara varför siffran inte säger något huruvida någon fick vänta.

38 megabit/s i 300 sekunder ger 11400 megabit. Dividerar vi detta med 8 blir det 1425, drygt 1.4 gigabyte. 

Det sägs inget om väntetid, eftersom vi pratar om ett medelvärde över 5 min. Trettio sek av totalstopp och fyra och en halv minut av tomgång ger samma medelvärde som en jämn ström.

# 14 Här är ett utdrag ur en logg. Vad hände, hur länge varade det, och varöfr skulle du inte hitta det med show interfaces status?
<img width="762" height="328" alt="image" src="https://github.com/user-attachments/assets/bbb5e7ad-c550-4b81-b049-d48535c59fd9" />

Porten gick ner och upp 3 gånger på dryga 48 min. Avbrotten varade 6.8, 7.5 respektive 6.7 sekunder.

# 15 Här är ett utdrag från en enhet där loggen verkar tom. Vad är förklaringen, och vilken rad avslöjar den?
<img width="753" height="127" alt="image" src="https://github.com/user-attachments/assets/4dda27c0-36a5-4237-9c6e-317e91558894" />

Raden uptime is 11 minutes. Enheten har startat om vilket leder till att loggminnet töms.

# 16 Skriv de rader som krävs för att en router ska tidsstämpla loggen med milisekunder, spara 16 kB logg i minnet, hämta tid från 192.168.1.16 och skicka nivå 0 till 5 till loggservern 192.168.1.17.

service timestamps log datetime msec
loggin buffered 16384
ntp server 192.168.1.16
logging trap 5
logging host 192.168.1.17

# 17 En kollega har satt logging trap 7 i drift och loggsekvensen fylls. Skriv den enda rad som rättar det, och skriv i en mening vad som slutar synas.

logging trap 5
Det som slutas skickas till loggservern är informational (nivå 6) och debugging (nivå 7).

# 18 Nordviks ledning vill få ett meddalnde när förbindelsen mot internet är onormalt belastad, men inte varje gång någon laddar ner en stor fil. Beskriv vad du behöver mäta, under hur lång tid, och vilken gräns du skulle sätta. Motivera varför just den gränsen, och vad du gör om larmen ändå kommer för ofta.

Det som behövs mätas är trafikvolym, i minst två veckor innan gränsen sätts. Viktigt att använda percentil istället för medelvärde så enstaka nedladdningar inte triggar larmet.

En rimlig gräns att larma är när den 95 percentilen över en timme överstiger baseline tydligt, inte när en enstaka mätpunkt gör det.

Kommer larmen ändå för ofta får man höja tidsfönstret innan gränsen. Ett larm som ignoreras är värre än inget larm.

# 19 Skriv fem meningar till en kollega som aldrig hört talas om baseline, där du förklarar varöfr ett mätvärde utan historik är värdelöst.

Ett enskilt mätvärde i nätverket säger ingenting i sig självt om du inte har något referensvärde att jämföra det mot. Utan en historisk baseline vet du helt enkelt inte om 80 % processorbelastning eller en viss svarstid är ett normalt tillstånd eller ett akut problem. För att jämförelsen ska vara relevant måste baslinjedatan dessutom komma från exakt samma nätverk, eftersom alla miljöer har sina egna unika trafikmönster. Det är också avgörande att denna historik samlas in i förväg under normal drift, eftersom det är för sent att skapa en baslinje när ett avbrott väl inträffat. Kort sagt gör en baseline att du kan skilja på normal aktivitet och faktiska avvikelser i systemet.