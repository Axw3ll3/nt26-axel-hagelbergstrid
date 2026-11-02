# 1 Varför går det att komma in på en switch över konsolen även när nätverket är nere?

Konsolen går inte via nätverket utan är en direktkoppling mellan din enhet och enheten i fråga, och fungerar därför även när nätverkskonfiguration är trasig eller IP-adress saknas på enheten.

# 2 Vilka tre lägen finns, och hur ser du i prompten vilket du är i?

De tre lägena som finns är: Användarläge som visas via en ">", Privilegierat läge som visas via en "#"  och Konfigurationsläge som visas via "(config)#".

# 3 Vilket kommando tar dig från användarläge till privilegierat läge?

enable

# 4 Vad är skillnaden mellan running-config och startup-config?

Running-config är nuvarande inställningar. Startup-config är inställningarna som laddas in nästa gång enheten startas. De räknas som 2 olika versioner och blir detsamma när man sparar.

# 5 Vad händer med en osparad ändring vid strömavbrott?

De försvinner, enheten startar på startup-config och ändringarna fanns bara i running-config.

# 6 Räkna upp de sju OSI-lagren i ordning.

Fysisk, Data länk, Nätverk, Transport, Session, Presentation, Applikation

# 7 Vilket lager arbetar switchen på? Vilken arbetar en router på?

Switchen jobbar på lager 2 och router på lagerf 3.

# 8 Vad gör en brandvägg som en router inte gör?

Brandväggen filtrerar trafiken som får pasera, inte bara vart den ska. Den håller även reda på pågående anslutningar. Moderna brandväggar kollar även ända upp i lager 7.

# 9 Nämn två saker 'show version' berättar om en okänd enhet.

'Show version' berättar om exempelvis: Modell, IOS-version,, uptime, serienummer

# 10 Vilken hastoghet ska den seriella porten ha, och vad ser du om den är fel?

Seriella porten ska ha 9600 i hastighet. Är det inte denna hastighet visas obegripliga tecken eller ingenting alls på skärmen.

# 11 Här är ett utdrag ur 'show interfaces status'. En av portarna har en kabel i men kommer inte upp, och orsaken är inte kabeln. Vilken port, och vilket kommand skulle du köra härnäst?
<img width="532" height="159" alt="Screenshot 2026-09-01 152306" src="https://github.com/user-attachments/assets/8bd9f7d1-46c7-4c21-840a-ac5ab3a0e9bc" />

Port GI0/3. Den står som disabled, inte att den inte har någon anslutning. Leta efter raden shutdown efter du kört "show running-config interface GigabitEthernet0/3". Det som sägs är att porten är avstängd, inte att kabeln inte är ansluten. Felet ligger på lager 1. Då porten är 'disabled' försöker den inte ens kolla om kabeln är ansluten.

# 12 En kurskamrat visar dig det här och säger switchen "inte tar emot kommandon". Vad har hänt, och vad säger du åt till hen att göra?
<img width="560" height="84" alt="Screenshot 2026-09-01 152309" src="https://github.com/user-attachments/assets/59abf743-d31a-48b7-8396-2b890190026e" />

Hen är i användarläget då prompten slutar på ">". Hostname kommandot finns endast i konfigurationsläget. Hen måste först köra enable och sedan configure terminal för att kunna konfigurera hostname.

# 13 Skriv fem meningar till en kollega som aldrig sett en switch, där du förklarar skillnaden mellan running-config och starting-config. Använd inga engelska termer utan de två namnen.

Running-config är konfigurationen du sitter på just nu, medan startup-config är konfigurationen som startas vid omstarter/uppstarter, lite som en standard version. Vid exempelvis strömavbrott kommer din running-config försvinna och vid nästa uppstart kommer du hamna på din startup-config (standardversion) istället. För att göra din running-config permanent använder man ett kommando som lyder "write memory" för att skriva över det till din startup-config.
