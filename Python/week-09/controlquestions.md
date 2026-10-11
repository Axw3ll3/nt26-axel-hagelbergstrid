# 1 Vad gör en VPN-tunnel med paket, i fem steg?

# 2 Vad skyddar ett VPN, och vad skyddar det inte?

# 3 Vad är skillnaden mellan site-to-site och remote access?

# 4 Varför krockar NAT och kryptering, och vad heter lösningenP

# 5 Varför går små paket fram men inte stora, genom en tunnel?

# 6 Nämn två skillnader mellan traditionell VPN och SD-WAN.

# 7 Vad är den största vinsten med en lastbalanserare, och barför är det inte kapacietet?

# 8 Vad kan en lastbalanserare på lager 7 som en på lager 4 inte kan?

# 9 Vilka två kommandon visar att en tunnel är uppe respektive att trafik går igenom?

# 10 Vilken fråga ställer du först när något inte fungerar, oavsett vecka?

# 11 Skriv den engelska termen för vart och ett av följande: tunnel, kryptering, lastbalanserare och plats-till-plats. Provet frågar efter dem.

# 12 Ett IP-paket får som mest vara 1500 byte på en vanlig Ethernetlänk. IPsec i tunnelläge lägger på ett nyt IP-huvud på 20 byte och ett ESP-huvud och en snans på tillsammans omkring 38 byte. Hur stort får det inre paketet vara? Räkna, och skriv en mening om vad som händer med ett paket som är större.

# 13 Nordviks tunnel-ACL täcker 192.168.1.0/26 mot 192.168.2.0/26. Skriv de två raderna - en per route - med rätt wildcardmasker och näten omvända. Räkna fram maskerna.

# 14 Här är ett utdrag från en router. Tunneln sägs vara uppe, men användarna når ingenting på andra sidan. Vad är fel?

# 15 Här är två ACL:er, en från varje sida av en tunnel. Varför kommer ingen trafik igenom.

# 16 Skriv den ACL som pekar ut vilken trafik som ska in i tunneln mellan Göteborg och Mölndal, i båda ändarna. Ange på vilken router varje rad ska skrivas, och varför de två listorna msåte vara varandras spegelbild.

# 17 Skriv de rader som undantar trafiken mellan Göteborg och Borås från NAT, givet att NAT-listan i dag är acces-list 1 permit 192.168.1.0 0.0.0.255.

# 18 Nordvik ska koppla ihop Mölndalskontoret med Göteborg. Ledningen vill inte hyra en förbindelse, och ekonomifiler ska inte kunna läsas av utomstående. Säljarna ska dessutom kunna nå ekonomisystemet från hotell. Beskriv vilka två lösningar du föreslår, vad som skiljer dem, och vilken du bygger dem i.

# 19 Skriv fem meningar till en kollega som aldrig hört talas om VPN, där du förklarar varför en tunnel över internet kan vara säkert.

# Återblick

# 20 Vad är implicit deny, och varför kan en ACL med en enda rad ta ner ett helt nät?

# 21 Vad händer med en accesspunkt som får för lite ström, och varför ser felet ut som ett nätverksfel?

# 22 Räkna ut nätadress, broadcast och adressintervall för 192.168.1.192/26, utan att slå upp något.