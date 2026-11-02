# 1 Vad är skillnaden på ett VLAN och IP-nät?

VLAN är på lager 2 och handlar om vilka portar som hör ihop. IP-nät är lager 3 och handlar om adresserna.

# 2 Vad skiljer en access-port från en trunk?

En access-port tillghör ett enda VLAN, där sitter datorn. En trunk bär flera VLAN samtidigt, där sitter andra switchar eller en router.

# 3 Vilka två rader behövs för att lägga en port i ett VLAN, och varför räcker inte den ena?

Switchport mode access och switchport access vlan <nummer>. Utan den första står porten fortfarande kvar i automatiskt läge och kan välja något annat än vad man tänkt.

# 4 Vad gör taggningen, och var i nätet finns taggen?

Taggningen skriver VLAN-nummer i ramen. Taggen lever endast på trunkar, mellan switchar och till enj router.Den sätts på när ramen går in i en trunk och tas av innan den går ut på en access-port.

# 5 Varför ska en trunk aldrig kopplas till en dator?

En trunk ska aldrig kopplas till en dator då en dator inte förstår sig på taggade ramar. Dem kastar dem alternativt behandlar dem fel.

# 6 Vad är native VLAN, och vad är standardvärdet?

Native VLAN är VLAN som går otaggat över till trunken. Standardvärdet är VLAN 1 på alla Cisco-switchar.

# 7 Vad går fel om två switchar har olika native VLAN?

Om två switchar har olika native VLAN skapas otaggad trafik från det ena nätet som ska hamna i det andra. Cisco switchar stänger Ciscos spanning tree av de två inblandade VLAN:en på porten, och loggen fylls med raden omRECVV_PVID_ERR. Mot en annan switch från en annan tilverkare finns inga sådanna spärrar, och då hoppar trafiken mellan näten tyst.

# 8 Vad förhindrar STP, och hur gör den det?

Det STP förhindrar är att ramar går runt i en cirkel för evigt. Den gör det genom att stänga av de portar som skulle skapa cirkelnm, och öpppnar dem igen om den öppna vägen går sönder.

# 9 Vad betyder BLK i show spanning-tree, och vad ska du göra åt det?

BLK betydfer att STP stängt av porten avsiktligt. Du ska inte göra något åt det, då porten är en reserv, och att dra ur kabeln är ett säkert sätt att ta ner nätet.

# 10 Vad händer om du kör switchport trunk allowed vlan två gånger med olika nummer?

Den andra listan skriver över den första. Du har då bara de VLAN du skrev
sist. Vill du lägga till använder du add.

# 11 Skriv den engelska termen för vart och ett av följande: access-port, trunk, taggning, native VLAN och root bridge. Provet frågar efter dem.

Access port, native VLAN, Tagging och root bridge.

# 12 Nordviks fyra VLAN delar 192.168.1.0/24 i fyra lika stora delar. Räkna ut nätadrress, gatewayadress, första och sista användbara adress samt broadcastadress för alla fyra. Använda schemat i bilaga C och skriv svaret som en tabell.

VLAN
10
Nät
192.168.1.0/26
Gateway
192.168.1.1
Användbara
.1–.62
Broadcast
192.168.1.63

VLAN 
20
Nät
192.168.1.64/26
Gateway
192.168.1.65
Användbara
.65–.126
Broadcast
192.168.1.127

VLAN
30
Nät
192.168.1.128/26
Gateway
192.168.1.129
Användbara
.129–.190
Broadcast
192.168.1.191

VLAN
99
Nät
192.168.1.192/26
Anvädnbara
.193–.254
Gateway
192.168.1.193
Broadcast
192.168.1.255

# 13 Ekonomiavdelningen växer till 70 datorer. Räcker /26? Räknaut hur många adresser en /26 ger, hur många av dem som går att använda, och vilken mask som skulle behövas i stället.

Nej, en /26 räcker inte. Den ger 64 adresser, varav 62 går att använda: nätadressen och broadcastadressen är upptagna. 70 datorer kräver minst
70 användbara adresser, alltså en /25 med 128 adresser och 126 användbara.

# 14 Här är ett utdrag från två switchar som är hopkopplade.Datorer i VLAN 20 når inte varandra över trunken, men VLAN 10 fungerar. Vad är fel?
<img width="559" height="174" alt="Screenshot 2026-09-08 135327" src="https://github.com/user-attachments/assets/1725d44a-d3ea-41db-8404-708dd9031210" />

VLAN 20 saknas i allowed-listan på SW-Nordvik-1.
Trunken bär bara 10, 30 och 99 från den sidan.

# 15 Här är ett utdrag från en switch. En dator i port Gi0/5 får ingen adress från DHCP-servern, som sitter i VLAN 10. Vad frågar du efter härnäst?
<img width="563" height="209" alt="Screenshot 2026-09-08 135344" src="https://github.com/user-attachments/assets/907fbd39-768f-4452-9110-8d687c42deea" />

Fråga vilket VLAN porten ligger i. Gi0/5 står under
VLAN1,inte under VLAN10där DHCP-servern finns.

# 16 Skriv den fullständiga konfigurationen för trunken mellan SW-Nordvik-1 och SW-Nordvik-2. Den ska bära VLAN 10, 20, 30 och 99, ha native VLAN 999 och inte förhandla om läget. Skriv varje rad, i rätt ordning, från configure terminal till end.

configure terminal
interface GigabitEthernet0/24
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk native vlan 999
switchport trunk allowed vlan 10,20,30,99
switchport nonegotiate
end

# 17 Port Gi0/11 till Gi0/14 på SW-Nordvik-1 ska läggas i VLAN 20 och slippa vänta på STP när en dator kopplas in. Skriv konfigurationen med så få rader som möjligt.

interface range GigabitEthernet0/11- 14
switchport mode access
switchport access vlan 20
spanning-tree portfast

# 18 Nordviks gäster ska kunna nå internet men ingenting annat i huset. Ekonomiavdelningen ska ha ett eget nät som varken kontoret eller gästerna når. Driftpersonalen ska kunna nå switcharna från sitt eget nät. Skriv den VLAN konfiguration switchen behöver, och säg vilken del av kravet du inte kan lösa med VLANensamt.

Tre VLAN behövs: gäst, ekonomi och drift. Konfigurationen skapar dem, sätter access-portarna och lägger alla på trunken. Det du inte kan lösa med VLAN ensamt är kravet att gästerna ska nå internet. VLAN
skiljer nät åt — det kopplar inte ihop dem. Att gästerna ska ut kräver routing i
kapitel 5, och att de inte ska nå något annat kräver en ACL i kapitel 9.

# 19 Skriv fem meningar till en kollega som aldrig hört talas om VLAN, där du förklarar varför två datorer i samma switch ändå inte kan nå varandra.

Ett VLAN är en inställning i switchen som uppdelar portarna i olika virtuella grupper. Switchen är konfigurerad att bara släppa igenom datatrafik mellan portar som tillhör exakt samma grupp. Om två datorer är kopplade till portar i två olika grupper, spärras kommunikationen helt mellan dem. Detta sker rent mjukvarumässigt i switchens internminne, vilket innebär att det inte syns på utsidan vilka portar som hör ihop. Därför kan två datorer sitta i samma fysiska enhet bredvid varandra utan att nå varandra förrän en router kopplar ihop deras grupper.
