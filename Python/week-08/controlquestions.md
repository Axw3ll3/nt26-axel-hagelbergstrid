# 1 Varför är luften ett delat medium, och vad betyder det för hastigheten?

Luften är ett delat medium eftersom alla i närheten sänder på samma yta, och bara en i taget kan sända. Hastigheten delas alltså på alla anslutna, och den med sämst signal drar ner takten för dem andra.

# 2 Vilka tre kanaler i 2,4-bandet stör inte varandra?

De 3 kanaler i 2,4-bandet som inte stör varandra är 1, 6 och 11 eftersom det är den planen som gäller i USA. Men i Sverige fungerar även 1, 5, 9 och 13.

# 3 Nämn en fördel och en nackdel med 5-bandet jämfört med 2,4.

5-bandet har fler kanaler som inte överlappar med varandra och färre störningar, men samtidigt har den kortare räckvidd och går sämre genom väggar.

# 4 Var är skillnaden mellan ett SSID, ett VLAN och ett IP-nät?

Skillnaden på SSID, VLAN och IP-nät är att SSID ser man i en telefon, VLAN är esegmentet i Switchen och IP-nätet är adresserna. Samma tanke men på olika sätllen.

# 5 Vad är en beacon, och hur oftast skickas den?

En beacon är ramen accesspunkten skickar för att tala om att den finns. Skickas ungefär tio gånger i sekunden.

# 6 Vad är association, och vem fattar beslutet att byta accesspunkt?

Association är att klienten ansluter sig mot accesspunkten, beslutet att byta accesspunkt görs av klienten, inte nätet.

# 7 Vad gör PoE, och vilken kolumn i 'show power inline' säger hur mycket som är kvar?

PoE ger ström genom nätverkskabel, i kolumnen 'Remaining' får man reda på hur mycket som är kvar av switchens budget.

# 8 Vad händer med en accessopunkt som får för lite ström?

En accesspunkt som får för lite ström startar, men sen kommer den starta om och forsätta i detta mönster. Felet ser ut som ett nätverksfel men är ett strömfel.

# 9 Vad är skillnaden mellan autonomt läge och controllerläger?

Autonomt läge betyder att varje accesspunkt ställs in för hand medan controller hämtar sina inställningar centralt, och du ställer in dessa en gång.

# 10 Blir täckningen bättre av fler accesspunkter? Motivera.

Täckningen blir inte bättre av fler accesspunkter i sig. Fler accesspunkter på sama kanal gör det sämre, men det hjälper bra om kanalplaneringen är gjord.

# 11 Skriv den engelska termen föär vart och ett av följande: delat mediuum, kanal, accesspunkt och strömförsörjning via nätverkskabeln. Provet frågar om dem.

shared medium, channel, accesspoint, Power over Ethernet (PoE)

# 12 Borås har 192.168.2.0/24 att dela på. VLAN 40 och 50 tar en /26 var och VLAN 99 en tredje. Räkna ut alla nätadresserna, gatewayadresserna och broadcastadresserna, och skriv vilken fjärdedel som blir kvar.

VLAN 40
Nät: 192.168.2.0/26
Gateway: 192.168.2.1
Användbara .1-.62
Broadcast: 192.168.2.63

VLAN 50
Nät: 192.168.2.64/26
Gateway: 192.168.2.65
Användbara: .65-.126
Broadcast: 192.168.2.127

VLAN 99
Nät: 192.168.2.192/26
Gateway: 192.168.2.193
Användbara: .193-.254
Broadcast: 192.168.2.255

# 13 En switch har 370 watts PoE-budget och ger 802.3af, alltså högst 15,4 watt per port. Hur många accesspunkter räcker budgeten till, och hur många portar har switchen då kvar utan ström?

370 delat med 15,4 är 24,02. Budgeten har alltså 24 accesspunkter och 0,4 watt blir över. En switch med 24 portar räcker budgeten till precis alla portar. På en med 48 portar står hälften (24) utan ström och den som kopplar en accessport till port 25 kommer aldrig få ström samt starta.

# 14 Här är ett udrag från en switch. En accesspunkt ska sitta i Gi0/3 men kommer aldrig igång. Vad är fel, och vad kontrollerar du härnäst?

Switchens PoE-budget är slut. Remaining står på 0,4 watt, och accessporten kräver 15,4.


# 15 Här är vad en gäst ser efter att ha anslutit till Norvik-Gast i Borås. Vad är fel?

Gästen hamnade i fel nät, i lagernätet. Adressen 192.168.2.34 ligger i 192.168.2.0/26, med andra ord VLAN 40 och gatewayen 192.168.2.1 bekräftar detta. Gästnätet är 192.168.2.64/26 med gateway på 192.168.2.65.

# 16 Skriv konfigurationen för switchporten till en accesspunkt som ska hämta sin adress i VLAN 99 och drivas med PoE. Skriv sedan samma port konfigurerad för autonomt läge istället, med VLAN 40, 50 och 99.

Från controller:
interface GigabitEthernet0/1
switchport mode access
switchport access vlan 99
power inline auto

Från autonomt:
interface GigabitEthernet0/1
switchport trunk encapsulation dot1q
switchportmode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 40,50,99
power inline auto

# 17 Skriv de rader som stänger av PoE på Gi0/10 till Gi0/24 för att spara budget, med så få rader som möjligt.

Kortaste möjliga väg att stänga portarna:
interface range GigabitEthernet0/10 - 24
power inline never

# 18 Nordviks lager i Borås ska ha trådlöst för handdatorer i hela lokalen, och ett gästnät i entrén som bara når internet. Handdatorerna ska nå lagersystemet men aldrig gästnätet. Lokalen är sextio meter lång med betongpelare. Beskrivt vad du behöver besluta om innan du köper något, och skriv den switchkonfiguration accesspunkterna kräver.

De saker man behöver veta innan man köper in saker: hur många accessporter lokalen kräver, vilka kanaler de ska använda och om switchen har PoE-budget för dem alla.
60m med betongpelare betyder fler accesspunkter, och det betyder kanalplanering. I 2,4-bandet har man bara 1,6 och 11 att välja mellan.

# 19 Skriv fem meningar till en kollega som tycker att lösningen på täckning är att köpa fler accesspunkter, där du kort förklarar när det stämmer och nät det gör saken värre.

Att svara enkelt på om vi behöver fler accesspunkter går inte, utan det beror helt på er kanalplanering. Fler enheter hjälper till när täckningen är för liten och signalen helt enkelt inte når fram till en viss yta. Om de placeras för tätt på samma kanal börjar de dock störa varandra och kan göra nätverket ännu sämre. Problemet förvärras av att det bara finns tre kanaler i 2,4 GHz-bandet som är helt fria från överlapp. Innan vi köper mer utrustning måste vi därför kontrollera att vi kan placera dem utan att frekvenserna krockar.