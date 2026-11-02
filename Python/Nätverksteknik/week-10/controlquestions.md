# 1 Vad gör en VPN-tunnel med paket, i fem steg?

En VPN-tunnel krypterar paketet och processen ser ut såhär:
Först skapas paketet med interna dresser.
Routern krypterar paketet.
Routern packar in det i ett nytt paket med offentliga adresser.
Packetet skickas över internet.
Routern i andra änden packar upp, dekrypterar och skickar in det i sitt nät.

# 2 Vad skyddar ett VPN, och vad skyddar det inte?

VPN skyddar innehållet. Att två adresser pratar med varandra, när och hur mycket de pratar med varandra skyddas inte.

# 3 Vad är skillnaden mellan site-to-site och remote access?

Skillnaden på site-to-site och remote access är att site-to-site går mellan två routrar och gäller alla på kontoret medan remote access går mellan en dator och router samt gäller en person.

# 4 Varför krockar NAT och kryptering, och vad heter lösningen.

NAT och kryptering krockar för NAT körs i routern innan den krypterar. Trafiken får den offentliga adressen och matchar inte lsitan vad som ska in i tunneln. Lösningen är en deny-rad först i NAT-listan, som undantar trafik. Sitter NAT-enheten istället på vägen mellan de två routrarna heter lösningen NAT traversal — ESP saknar portnummer, och NAT traversal lägger till ett UDP-lager som ger den några.

# 5 Varför går små paket fram men inte stora, genom en tunnel?

Små (yttre) paket är inte stora nog för att få plats i tunnelns lager. Är det märkt att det inte får delas skickar routern tillbaka ett ICMP-meddelande med rätt storlek. Filtreras det meddelandet bort försvinner paketet i tystnad.

# 6 Nämn två skillnader mellan traditionell VPN och SD-WAN.

Skillnaden på VPN och SD-WAN är att SD-WAN konfigureras centralt istället för per enhet, använder flera förbindelser samtidigt och väljer väg efter mätvärden istället för statiska rutter, kopplar om automatiskt vid avbrott

# 7 Vad är den största vinsten med en lastbalanserare, och varför är det inte kapacietet?

Största vinsten med lastbalanserare är tillgänglighet. Med två servrar bakom en lastbalanserare kan uppdatera den ena under dagen utan att det märks av.

# 8 Vad kan en lastbalanserare på lager 7 som en på lager 4 inte kan?

En lastbalanserare på lager 7 kan läsa innehållet i förfrågan. Den kan därmed skicka olika delar av samma tjänst till olika servrar medan en lager 4 lastbalanserare bara ser adress och portnummer.

# 9 Vilka två kommandon visar att en tunnel är uppe respektive att trafik går igenom?

'show crypto isakmp s'a visar statusen/om tunneln är uppe. 'show crypto ipsec sa' visar hur många paket som passerat.

# 10 Vilken fråga ställer du först när något inte fungerar, oavsett vecka?

Frågan du alltid ställer först är: vilket lager är jag på?

# 11 Skriv den engelska termen för vart och ett av följande: tunnel, kryptering, lastbalanserare och plats-till-plats. Provet frågar efter dem.

tunnel, encryption, load balancer, site-to-site.

# 12 Ett IP-paket får som mest vara 1500 byte på en vanlig Ethernetlänk. IPsec i tunnelläge lägger på ett nyt IP-huvud på 20 byte och ett ESP-huvud och en snans på tillsammans omkring 38 byte. Hur stort får det inre paketet vara? Räkna, och skriv en mening om vad som händer med ett paket som är större.

1500 - 20 - 38 blir mattematiken, vilket blir 1442 byte. Inre paket som är större än så får inte plats. Antingen delas dem upp i 2 vilket kostar tid, eller så kastas det  längst vägen då det inte får delas upp, och då försvinner det tyst.

# 13 Nordviks tunnel-ACL täcker 192.168.1.0/26 mot 192.168.2.0/26. Skriv de två raderna - en per route - med rätt wildcardmasker och näten omvända. Räkna fram maskerna.

Wildcard för /26 är 0.0.0.63. 

För Nordviks router blir det:
permit ip 192.168.1.0 0.0.0.63 192.168.2.0 0.0.0.63

För Borås router blir det:
permit ip 192.168.2.0 0.0.0.63 192.168.1.0 0.0.0.63

# 14 Här är ett utdrag från en router. Tunneln sägs vara uppe, men användarna når ingenting på andra sidan. Vad är fel?
<img width="527" height="108" alt="image" src="https://github.com/user-attachments/assets/2884e49b-77ce-43c6-96db-fd05922609c5" />

Trafik går ut men ingen kommer tillbaka. encaps står på rad 382, decaps på 0. Då decaps står så högst kommer den inte skicka något tillbaka eller det som skickas kommer inte fram. 

# 15 Här är två ACL:er, en från varje sida av en tunnel. Varför kommer ingen trafik igenom.
<img width="527" height="108" alt="image" src="https://github.com/user-attachments/assets/732fe2c4-9812-4817-b4a1-1689488360b3" />

ACL-listorna speglar inte varandra. Göteborg pekar mot 192.168.2.0/26 medan Borås pekar på 192.168.1.0/24 istället för /26.

# 16 Skriv den ACL som pekar ut vilken trafik som ska in i tunneln mellan Göteborg och Mölndal, i båda ändarna. Ange på vilken router varje rad ska skrivas, och varför de två listorna msåte vara varandras spegelbild.

På R-Nordvik-1:
ip access-list extended VPN-MOLNDAL

permit ip 192.168.1.0 0.0.0.63 192.168.3.0 0.0.0.63

På R-Molndal-1:
ip access-list extended VPN-GOTEBORG

permit ip 192.168.3.0 0.0.0.63 192.168.1.0 0.0.0.63

# 17 Skriv de rader som undantar trafiken mellan Göteborg och Borås från NAT, givet att NAT-listan i dag är acces-list 1 permit 192.168.1.0 0.0.0.255.

De rader som undantar trafiken mellan Göteborg och Borås från NAT är:

no access-list 1

access-list 101 deny ip 192.168.1.0 0.0.0.255 192.168.2.0 0.0.0.255

access-list 101 permit ip 192.168.1.0 0.0.0.255 any

ip nat inside source list 101 interface GigabitEthernet0/1 overload

# 18 Nordvik ska koppla ihop Mölndalskontoret med Göteborg. Ledningen vill inte hyra en förbindelse, och ekonomifiler ska inte kunna läsas av utomstående. Säljarna ska dessutom kunna nå ekonomisystemet från hotell. Beskriv vilka två lösningar du föreslår, vad som skiljer dem, och vilken du bygger dem i.

Två lösningar krävs och löser varsin grej.

Site-to-site mellan Mölndal och Göteborg, för att koppla ihop kontoren. Den är alltid uppe och märks inte av användarna.

Remote access för säljarna som ansluter från hotell med egen dator. 

Först bygger man site-to-site, då den är färre rörliga delar. Den berör fler personer och ger dig en fungerande tunnel att felsöka mot innan du lägger till klientdelen.

# 19 Skriv fem meningar till en kollega som aldrig hört talas om VPN, där du förklarar varför en tunnel över internet kan vara säkert.

Ett VPN (Virtual Private Network) fungerar som en privat och krypterad förbindelse mellan din enhet och företagets nätverk när du surfar över internet. Innan dina filer eller meddelanden skickas iväg görs innehållet helt oläsbart med hjälp av stark kryptering. För att informationen ska kunna färdas obemärkt genom det publika internet, packas detta oläsbara innehåll sedan in i ett vanligt internetpaket – ungefär som ett brev som läggs i ett tilläggskuvert. Väl framme är det enbart de två godkända ändarna, alltså din dator och företagets server, som har nyckeln för att packa upp och läsa informationen. Det är dock viktigt att komma ihåg att ett VPN inte gör dig anonym på nätet, utan det skyddar bara själva transporten av din data mot snokande ögon.

# Återblick

# 20 Vad är implicit deny, och varför kan en ACL med en enda rad ta ner ett helt nät?

Implicit deny: Är den inbyggda, osynliga standardregeln som automatiskt placeras längst ner i alla Access Control Lists (ACL:er). Den innebär att all trafik som inte uttryckligen har tillåtits av tidigare rader nekas. Om du applicerar en ny eller ofullständig ACL på ett kritiskt gränssnitt (t.ex. en routerport) och bara skriver en enda regel – eller om regeln är felformulerad – kommer all annan trafik som passerar gränssnittet att träffas av implicit deny. Detta klipper omedelbart av viktig nätverkstrafik, inklusive administrationstrafik (som SSH), vilket gör att administratören blir utelåst och inte kan backa ändringen.

# 21 Vad händer med en accesspunkt som får för lite ström, och varför ser felet ut som ett nätverksfel?

När en accesspunkt (AP) får för lite ström (t.ex. på grund av felaktig PoE-förhandling eller en överbelastad switch) räcker effekten till för att starta enhetens processor, men inte för att driva radiomodulerna på full effekt. Enheten drabbas av spänningsfall, stänger av radion eller kraschar och startar om i en ond cirkel. Switchens portlänk lyser ofta grönt (eftersom nätverkskabeln har kontakt och processorn är vaken), vilket lurar en att tro att enheten fungerar. Men eftersom Wi-Fi-radion är avstängd eller loopar i omstarter kan klienter varken hitta nätverket eller ansluta, vilket felaktigt upplevs som ett rent trådlöst nätverksbortfall.

# 22 Räkna ut nätadress, broadcast och adressintervall för 192.168.1.192/26, utan att slå upp något.

Adressintervallet för 192.168.1.192/26 är:
Nätadress: 192.168.1.192
Broadcastadress: 192.168.1.255
Adressintervall: 192.168.1.193 - 192.168.1.254 