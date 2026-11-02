# 1 Vad är en zon, och vad är skillnaden mot ett nät?

En zon är en grupp interface med samma säkerhetsnivå medan ett nät är ett adressområde. En zon skyddar inte två nät mot varandra men en zon kan hålla fler nät.

# 2 Vad är en DMZ till för, och varför får den inte nå insidan?

DMZ är till för att tjänster ska nås utifrån. Den får ej nå insidan eftersom en server som är åtkomlig utifrån kommer bli angripen (förr eller senare).Skyddet är att den inte når insidan, vilket gör att om DMZ blir angripen når inte angriparen insidan.  

# 3 I vilken ordning läser routern en ACL, och när slutar den läsa?

Routern läser en ACL uppifrån och ner. Den slutar vid första tillfälle den når en matchning.

# 4 Vad kan en extended ACL som en standard-ACL inte kan?

En extended ACL kan se mottagaradress, protokoll och portnummer medan en standard-ACL bara ser vem som skickar.

# 5 Vad är implict deny, och hur många rader måste en ACL ha för att den ska finnas?

Implicit deny är en onsynlig rad längst ner som nekar allt som ingen rad släppt igenom. Det finns i varje ACL, även en med en enda rad.

# 6 Vad betyder wildcard-masken 0.0.0.63, och vilket prefix motsvarar den?

Wildcard-masken 0.0.0.63 betyder sista talet i adressen  får vara vad som helst mellan 0-63. Alltså alla 64 adresser som ryms inom /26.

# 7 Räknas riktningen in från trafikens eller routerns synvinkel?

In räknas från routerns väg in, inte trafikens.

# 8 Vilket kommando visar om en regel faktiskt träffat något?

Kommandot 'show access-lists' visar om regeln faktistk träffat något. Räknaren efter varje rad säger hur många paket som träffat regeln.

# 9 Vad skyddar port security mot som en ACL inte ser?

Security port skyddar enheter som kopplas in på en switchport. En ACL ser bara trafik som passerar routern, den som kopplar in mot en switch bryter inte mot någon ACL.

# 10 Vad är skillnaden mellan violation restrict och violation shutdown?

Violation restrict blockerar överskjutande trafik och loggar medan violation shutdown stänger porten helt och någon måste slå på den för hand efteråt.

# 11 Skriv den engelska termen för vart och ett av följande: zon, riktning, inplicit deny och port security. Provet frågar efter dem.

zone, direction, implicit deny och port security. 

# 12 Skriv wildcard-masken för vart och ett av följande: 192.168.1.0/26, 192.168.2.0/24, 10.0.0.0/30 och en enda värd. Räkna fram varje mask genom att dra nätmasken från 255, och visa mellanledet.

Wildcard-masken är nätmasken subtraherat från 255.255.255.255, tal för tal.

/26:
Nätmask: 255.255.255.192
Wildcard: 0.0.0.63

/24:
Nätmask: 255.255.255.0
Wildcard: 0.0.0.255

/30:
Nätmask: 255.255.255.252
Wildcard: 0.0.0.3

En enda värd:
Nätmask: 255.255.255.255
Wildcard: 0.0.0.0

# 13 En kollega har skrivit 'deny ip 192.168.1.0 0.0.0.128 any'. Vilka adresser täcker den raden? Vilka två av Nordviks fyra nät hamnar innanför, och vilket blir det oväntade resultatet?

0.0.0.127 motsvarar /25, och raden täcker därför 192.168.1.0 till 1i2.168.1.127. Det gör att VLAN 10 (192.168.1.0/26) och VLAN 20 (192.168.1.64/26) hamnar innanför. Den oväntade delen är att ekonominätet stoppas också, även fast kollegan skrev raden för att stoppa kontoret. Därför raden ser rätt ut vid en snabb blick.

# 14 Här är en ACL. Kontoret når fortfarande ekonomiservern trorts att raden finns. lägg märkte till att den nekande raden saknar räknare helt. Vad är fel?
<img width="519" height="84" alt="Screenshot From 2026-10-26 16-34-17" src="https://github.com/user-attachments/assets/81ccccae-bfa6-4fab-a64b-c1b62a3681ef" />

Ordningen är fel, och det syns på att den nekade raden saknar räknare helt. Raden 'permit ip any any' står först och verkställs först, så den nekade raden blir överskriven.

# 15 Här är ett utdrag från ett interface där en ACL nyss satts. Ingenting fungerar längre. Vad hände?
<img width="519" height="84" alt="Screenshot From 2026-10-26 16-34-24" src="https://github.com/user-attachments/assets/19933126-a1ef-4194-8856-ae5fa261d2ac" />

Listan saknar 'permit ip any any', vilket gör att en nekad rad och den onsyliga sista raden nekar allt.

# 16 Skriv den fullständiga konfigurationen som stoppar gästnätet från allt inne i huset men släpper ut det mot internet: listan, alla rader i rätt ordning, och raden som sätter den på rätt interface i rätt riktning.

ip access-list extended GAST

permit udp 192.168.1.128 0.0.0.63 host 192.168.1.129 eq 67

permit udp 192.168.1.129 0.0.0.63 host 192.168.1.1 eq 53

deny ip 192.168.1.128 0.0.0.63 192.168.1.0 0.0.0.255

permit ip any any

interface GigabitEthernet0/0.30

ip access-group GAST in

# 17 Skriv konfigurationen för port security på Gi0/5 till Gi0/9: högst en adress per port, inlärd och sparad automatiskt, och porten ska stängas av vid överträdelse.

interface range GigabitEthernet0/5-9

switchport mode access

switchport port-security

switchport port-security maximum 1

switchport port-security mac-address sticky

switchport port-security violation shutdown

# 18 Ny beställning, som ersätter den i genomgången: "Ekonomiavdelningen kan inte nå utvecklingsservern (192.168.1.15 i kontorsnätet). Utvecklarna ska däremot kunna nå ekonomisystemet. Skriv listan, säg vilket interface och vilken riktning den ska ha, och beskriv hur du bevisar båda halvorna.

deny ip 192.168.1.64 0.0.0.63 host 192.168.1.15

permit ip any any

Den sätts mot sub-interfacet för VLAN 20 med riktningen in, så nära avsändaren som, möjligt. Utvecklingsservern står i kontorsnätet 192.168.1.15 och ekonomisystemet i ekonominätet på 192.168.1.70. De ligger i olika VLAN, så
all trafik mellan dem passerar routern, annars ser ingen ACL den.

Från ekonominätet ska pingen mot 192.168.1.15 misslyc-
kas, och från kontorsnätet ska pingen mot 192.168

# 19 "Ingen utifrån ska kunna nå något i huset, utom vår webbserver." Nordvikhar ingen webbserver idag men ska köpa en. Beskriv var den ska stå, vilken zon den hör hemma i och vad som händer om du ställer den i kontorsnätet.

Webbservern ska stå i DMZ, en egen zon med eget interface på brandväggen. Sätts den i kontorsnätet istället får den som kontaktar servern direkt tillgång till alla arbetsplatser, filservern och ekonomisystemet. Servern är den enda maskinen utomstående får nå, och därmed mest sannolikt att bli angripen.

# 20 "Konsulten som kommer på tisdag ska bara komma åt sin egen dator och skrivaren, ingenting annat". Beskriv två helt olika sätt att lösa det, och säg vilket du väljer och varför.

Lösning 1: VLAN för konsulter, med en ACL som bara släpper genom trafik till skrivaren. Krävs att konsulten sitter mot den porten men fungerar för framtida besökare.

Lösning 2: Port security på porten konsulten sitter mot, som specifikt låser porten konsulten sitter på. Stoppar någon annan från att koppla in sig där, men stoppar konsulten från att nå resten av nätet.

Bästa alternativet är första, då kravet handlar om att vad konsulten får nå, inte om vem som får sitta på porten. Port security löser problemet men inte exakt så vi vill.

# Skriv fem meningar till en kollega som aldrig hört talas om implicit deny, där du förklarar varför en ACL med en enda nekande rad kan ta ner ett helt nät.

När man konfigurerar nätverk använder man regelistor för att bestämma vilken trafik som släpps fram. Det som är lätt att missa är att varje lista slutar med en osynlig rad som nekar allt. Denna dolda regel är inbyggd från grunden och går inte att ta bort. Om man därför skapar en lista med enbart nekande rader, kommer den att stoppa allting. Det är just därför ett sådant misstag kan kapa all kommunikation och ta ner ett helt nätverk.

# 22 Vad är baseline, och varför måste den mästas innan felet?

En baseline är en dokumenterad mätning av nätverkets eller systemets normala prestanda, trafikmönster och resursanvändning under normala driftförhållanden. För att kunna avgöra om något har gått sönder eller presterar dåligt måste man först veta hur "normalt" ser ut. Utan en baseline har ni ingen referenspunkt att jämföra med när en avvikelse uppstår, vilket gör det mycket svårt att avgöra om ett visst värde är onormalt eller ej.

# 23 Vad gör PAT som statsik NAT inte gör?

PAT (Port Address Translation) gör det möjligt för ett helt privat nätverk att dela på en enda publik IP-adress samtidigt, genom att skilja på anslutningarna med hjälp av unika portnummer. Statisk NAT, å andra sidan, gör en fast 1-till-1-mappning där en specifik lokal IP-adress enbart kan kommunicera ut via en specifik dedikerad publik IP-adress.

# 24 En ping ger inget svar. Vilka två saker kan ha gått fel?

Brandväggen blockerar trafiken: Målenheten eller en brandvägg längs vägen (t.ex. en router eller operativsystemets egna skydd) blockerar ICMP-trafik, vilket gör att enheten ignorerar ping-förfrågan trots att den är igång. Målenheten är offline eller nås inte: Målenheten är avstängd, har en felaktig IP-adress, eller så finns det ett routing-/kabelbrott i nätverket som gör att paketen aldrig når fram.