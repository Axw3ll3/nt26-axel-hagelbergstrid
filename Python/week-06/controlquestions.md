# 1 Ge två olika skäl till att NAT behövs.

NAT behöver för adresserna inte räcker till, många enheter ska dela på offentliga adresser. 

# 2 Vad betyder inside respektive outside, och sitter märkningen på nätet eller på interfacet?

Inside är sidan ens egna nät ligger, outside är omvärlden. Märkningen sitter på interface, inte nätet.

# 3 Vad skiljer Inside local från Inside global?

Inside local är den faktiska adressen enheten har, inside global är adressen omvärlden ser att den har.

# 4 Vad gör PAT som statisk NAT inte gör?

PAT byter portnummer vilket låter många enheter dela på en enda adress. Statisk NAT kräver en offentlig adress per enhet.

# 5 Varför fungerar inte en förbindelse som börjar utifrån, utan särskild konfiguration?

Förbindelsen som börjar utifrån fungerar inte utan särskilt konfiguration eftersom översättningen skapas när någon på insidan skickar ut något. Kommer förbindelsen utifrån finns ingen anteckning och routern vet inte vem paketet ska till.

# 6 Vilket ord i NAT-kommandot gör det till PAT?

overload är ordet som gör NAT till PAT.

# 7 Varför är NAT ingen säkerhetsfunktion?

NAT är ingen säkerhetsfunktion då att utifrån inte når in är en bieffekt av funktionen, inte skydd. Skyddet kommer från brandväggen.

# 8 Vilka två saker måste finnas på enheten innan crypto key generate rsa fungerar?

De som behövs är ett domännamn och ett hostname. Nyckeln får sitt namn utifrån dessa 2, utan dessa 2 funkar inte kommandot.

# 9 Vilken rad stänger dörren för telnet?

transport input ssh, annars står telnet fortfarande öppet.

# 10 Nämn tre saker som ska bort ur en konfigurationsfil innan du committar den.

enable secret, username ... secret och SNMP community strings. Privata nycklar om de följt med i en säkerhetskopia ska även bort.

# 11 Skriv den engelska termen för vart och ett av följande: översättning, insida, utsida och sanering. Provet frågar efter dem.

translation, inside, outside, sanitization.

# 12 Listan access-list 1 permit 192.168.1.0 0.0.0.255 släpper ut alla fyra VLAN på en gång. Skriv i stället fyra rader, en per VLAN, med rätt wildcard-mask för en /26. Räkna fram masken, skriv inte av.

access-list 1 permit 192.168.1.0 0.0.0.63

access-list 1 permit 192.168.1.64 0.0.0.63

access-list 1 permit 192.168.1.128 0.0.0.63

access-list 1 permit 192.168.1.192 0.0.0.63


# 13 Nordvik har 70 datorer på insidan och en offentlig adress. Varje dator har i snitt tolv samtidiga förbindelser. Hur många rader står det då i show ip nat translations? Räcker portnumren?

70 datorer med 12 förbindelser blir alltså 70x12 vilket blir 840 rader i tabellen. Portnumrena räcker med goda marginal då PAT använder portnummer från 1024 o framåt. Alltså drygt 64 000 per offentlig adress. 840 av 64 000 är drygt en procent

# 14 Här är en NAT-tabell. Hur många enheter på insidan syns i utdatan, och hur många offentliga adresser använder de?
<img width="533" height="166" alt="Screenshot 2026-09-21 174132" src="https://github.com/user-attachments/assets/47970e8f-c444-4bc8-9f56-6a5ad961a704" />

Två enheter, 192.168.1.42 och 192.168.1.52, den använder en enda offentlig adress, 203.0.113.10.

# 15 Här är ett utdrag från en router där ingenting kommer ut på internet. Vad är fel?
<img width="544" height="189" alt="Screenshot 2026-09-21 174354" src="https://github.com/user-attachments/assets/1a5de9fa-9a6e-4319-bfa1-23ecb18078fb" />

Interfacen är pekade åt fel håll. Gi0/0.10 står som outside interfaces när det i själva verket är det interna sub-interfacet medan Gi0/1 står som inside interface vilket är fel.

# 16 Skriv den fullständiga konfigurationen som ger gästnätet, och bara gästnätet, en väg ut via PAT. Alla andra nät ska lämnas orörda.

access-list 2 permit 192.168.1.128 0.0.0.63
ip nat inside source list 2 interface GigabitEthernet0/1

interface GigabitEthernet0/0.30
ip nat inside

# 17 Skriv de rader som krävs för att slå på SSH på en router som just startats med tom konfiguration. Ta med allt som behövs, i rätt ordning. Skriv <losenord> där ett lösenord ska stå — aldrig ett riktigt.

hostname R-Nordvik-1
ip domain-name nordvik-example
crypto key generate rsa
username drift privilege 15 secret <losenord>
ip ssh version 2
line vty 0 4
transport input ssh
login local
line vty 5 15
transport input ssh
login local

# 18 Nordvik har köpt upp ett företag som använder samma adressrymd som Nordvik själva. Ledningen vill att ekonomiavdelningarna på de två kontoren ska kunna nå varandras filservrar, men inget annat ska kopplas ihop. Beskriv vad du gör, i vilken ordning, och vad du behöver komma överens om med den andra sidans tekniker innan du rör något.

Först: Kom överens om vilka påhittade adressrymder som ska användas åt vardera håll med andra sidans tekniker.
Sedan: Bygg översättning från båda ändar, så varje sida ser den adnra under en adress som inte krockar.
Sist: Begränsa ekonomiservrar, det görs med en ACL som pekar ut just de två adresserna, inte hela näten.

# 19 Skriv fem meningar till en kollega som aldrig hört talas om NAT, där du förklarar hur sjuttio datorer kan dela på en enda adress.

Tänk dig att alla sjuttiotalet datorer på kontoret bor i samma lägenhetshus och vill skicka brev utomlands.

När en dator skickar en förfrågan tar routern brevet och ersätter datorns lokala adress med företagets enda gemensamma, utåtriktade adress. För att veta vem som ska ha svaret tilldelar routern varje förfrågan ett unikt portnummer, lite som att sätta ett specifikt lägenhetsnummer på avsändaren. Routern antecknar sedan noggrant detta byte och portnummer i en egen intern tabell innan den skickar iväg data paketet. När svaret kommer tillbaka från internet tittar routern i sin tabell, ser vilket portnummer det kom till, och hittar rätt dator så att paketet skickas vidare till den ursprungliga avsändaren.