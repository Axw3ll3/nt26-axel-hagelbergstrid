# 1 Vad gör en router som en switch inte gör?

En router flyttar trafik mellan olika nät. En switch flyttar trafik inom ett nät. Routern jobbar med IP-adresser medan switchen på MAC-adresser.

# 2 Vad betyder bosktaven C respektive S i routingtabellen?

C betyder ansluten rutt (connected), routern sitter själv i nätet. S betyder statisk rutt (static), någon skrev den för hand.

# 3 Varför får du två rader när du sätter en adress på interface?

Du får 2 rader för att visa information kring nätet (C-raden) ooch en för routerns egna adress i nätet (L-raden). L-raden har alltid /32 och finns för att routern ska veta vad som är till för den själv.

# 4 Vad betyder longest prefix match, och vilken rad vinner om två passar?

Longest prefix match betyder att den mest exakta raden vinner, den med störst siffra i mängd korrekt efter snedstreck. Passar 2 rader väljer routern den med längst prefix.

# 5 Varför är 0.0.0.0/0 alltid den sista utvägen?

0.0.0.0/0 är sista utvägen då prefixet 0 betyder ingen del av adressen behöver stämma. Den passar alla adresser och är därför alltid den sämsta träffen.

# 6 Vad är ett sub-interface, och varför behövs det på en router med få portar?

Sub-interface är en del av ett fysiskt interface. Det behövs på en router med få portar med få portar för att kunna vara en gateway att köra flera VLAN över en enda kabel.

# 7 Vilken rad måste komma före adressen på ett sub-interface och varför?

Raden som måste komma före adressen på ett sub-interface är 'encapsulation dot1Q <vlan>' eftersom annars vet inte roturern vilken VLAN interfacet tillhör, vilket i sig gör att den vägrar ta emot adressen.

# 8 En ping ger inget svar. Vilka två saker kan ha gått fel?

De två saker som kan gått fel är att paketet aldrig kom fram, eller svaret aldrig kom tillbaka. Ping är 2 resor, du vet bara att en misslyckades.

# 9 Vad är en blackhole-rutt, och varför är den svår att hitta?

En blackhole-rutt är ett hopp som inte finns eller inte vet vägen vidare. Den är svår att hitta då raden ser helt korrekta ut i tabellen, då routern kontrollerar aldrig att nästa hopp svarar.

# 10 Vad visar traceroute som ping inte visar?

Traceroute visar var paketet tog slut, Ping säger inget om det kom fram eller inte. Traceroute säger alltså hur långt den kom och vilken router som var den sista som svarade.

# 11 Skriv den engelska termen för vart och ett av följande: routing-tabell, ansluten rutt, statisk rutt, nästa hopp och sub-interface. Provet frågar efter dem.

routing-table, connected route, static route, next hop and sub-interface.

# 12 Länken mellan Göteborg och Borås är 10.0.0.0/30. Hur många adresser innehåller nätet, hur många av dem går att sätta på ett interface, vilka är de? Räkna, skriv inte av.

10.0.0.0/30 innehåller 4 adresser. .0, .1, .2 och .3.
.0 är nätadressen och .3 är broadcastadressen. .1 och .2 går att sätta på ett interface.

# 13 En kollega föreslår 10.0.0.0/24 till länken istället. Räkna ut hur många adresser som då står oanvända, och skriv en mening om varför det ändå kan vara ett rimligt val i ett stort nät.

/24 ger 256 adresser, 254 användbara. Två av dessa används i detta scenario så 252 oanvända. Rimligt val eftersom en organisation som ger varje länk en hel /24 slipper räkna, slipper misstag och kan läsa av vilken länk direkt på adressen. Priset betalas i adresser, i ett internt 10.-nät finns det gott om dem.

# 14 Här är en routingtabell. Ett paket ska till 192.168.2.50. Vilken rad används, och vad händer med paketet?

Raden S 192.168.2.0/24 via 10.0.0.2 används. Paketet skickas till 10.0.0.2 som är routern till andra änden av länken.

# 15 Här är ett utdrag från Nordviks router. Datorer i VLAN 20 når varandra men inte sin gateway. Vad är fel?

Raden 'encapsulation dot 1Q 21' är fel. Sub-interfacet heter .20, har ekonominätets adress, men lyssnar på VLAN 21, som inte finns på switchen.

# 16 Skriv den fullständiga konfigurationen för sub-interfacet mot VLAN 30 på R-Nordvik-1: rätt namn, rätt VLAN, rätt adress, rätt mask enligt bilaga G. Skriv raderna i den ordning routern kräver.

interface GigabitEthernet0/0.30
encapsulation dot1Q 30
ip address 192.168.1.129 255.255.255.192

# 17 Skriv de två rutter som behövs för att Göteborg och Borås ska nå varandra - en på varje router. Ange på vilken router varje rad ska skrivas.

På R-Nordvik-1 behöver vi skriva:
ip route 192.168.2.0 255.255.255.0 10.0.0.2

På R-Boras-1 behöver vi skriva:
ip route 192.168.1.0 255.255.255.0 10.0.0.1

# 18 Nordviks ekonomiavdelning ska kunna nå filserver i kontorsnätet. Kontorspersonalen ska inte kunna nå ekonominätet. Driftpersonalen ska nå bägge. Beskriv vad du kan lösa med routing den här veckan, och vad som måste vänta till kapitel 9. Skriv den konfiguration du faktiskt kan göra nu.

Det jag kan lösa nu är så att ekonomi kan nå filservern, genom att sub-interfacen finns och routern därmed routar mellan alla fyra näten automatiskt.

Det jag inte kan lösa är att kontoret inte ska kunna nå ekonominätet. Routing kopplar ihop saker, inte separerar. Att stoppa trafik kräver ACL, vilket kommer i kap. 9.

# 19 Skriv fem meningar till en kollega som aldrig hört talas om routing, där du förklarar varför en ping kan gå fram utan att komma tillbaka.

En ping består av två separata resor: en förfrågan som skickas iväg och ett svar som ska ta sig tillbaka. När nätverksutrustningen dirigerar datatrafik görs beslut om vilken väg paketet ska ta helt oberoende för varje enskild resa. Det innebär att routern på avsändarsidan kan veta exakt hur den ska skicka iväg paketet till mottagaren, medan mottagarens sida saknar information om hur svaret ska ta sig tillbaka. Eftersom vägen framåt och vägen tillbaka är två helt skilda beslut kan den första sträckan fungera perfekt samtidigt som returvögen misslyckas, eller tvärtom. Det är därför din ping kan nå ända fram till destinationen utan att du någonsin får svar tillbaka.