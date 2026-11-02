# 1 Vad står först i en ram: avsändarens eller mottagarens adress?

Mottagarens adress står först då switchen behöver veta vart ramen ska innan vart den kommer ifrån.

# 2 Hur många tecken har en MAC-adress, och vad betyder den första halvan?

En MAC-adress har 12 tecken, skrivna som 6 par. Första halvan är tillverkaren medan andra halvan är löpnummer. I skriptet räknar du åtta tecken, då två kolon ligger emellan.

# 3 Var får switchen sina anteckningar ifrån? Vem fyller tabellen?

Switchen får sina anteckningar från sig själv med avsändaradressen i varje ram som passerar.

# 4 Vad gör switchen med en ram vars mottagare den inte känner igen?

Skickar ut ramen genom alla portar exkluderat den porten ramen kom ifrån. Genom var svaret återkommer från lär sig switchen var mottagaren sitter.

# 5 Hur länge sitter en anteckning kvar i MAC-tabellen, och varför försvinner den?

En anteckning sitter kvar i MAC-tabellen i 5 min som standard. Detta då folk flyttar datorer och switchen skulle annars skicka trafik till en port där ingen sitter.

# 6 Vilken adress används vid broadcast, och vad betyder den?

FF:FF:FF:FF:FF:FF. Detta betyder "till alla på det här nätet" och slås aldrig upp i tabellen.

# 7 Varför går en ARP-fråga till alla, medan svaret går till en?

Frågan går till alla då avsändaren inte vet vem som ska svara. Svaret kan gå till en, eftersom den som svarar redan sett frågeställarens MAC-adress i ramen som kom in.

# 8 Din dator vill nå en server i ett annat land. Vilken MAC-adress frågar den efter?

Datorn frågar efter MAC-adressen till sin Default Gateway då den aldrig slår upp MAC-adresser utanför sitt eget nät.

# 9 Vad betyder 'Dynamic' respektive 'Static' i kolumnen 'Type'?

Dynamic innebär att switchen lärt sig adressen själv. Static betyder att någon skrivit in den själv eller att adressen tillhör switchen.

# 10 Nämn två saker som gör att en prot visar 'not connected'.

Exempel är trasig kabel, kabel sitter i fel port, enheten i andra änden är avstängd eller porten är avstängd.

# 11 Några veckor senare ringer Anna igen. Här är ett utdrag ur MAC-tabellen. Hon har adressen a4c3.f011.3ab7 och når ingen alls, trots att hennes port är uppe. Vad är fel, och vilken port avslöjar det?
<img width="537" height="110" alt="Screenshot 2026-09-01 154147" src="https://github.com/user-attachments/assets/4c767ca3-33af-4138-829c-a8b5024f2798" />

Annas port ligger på VLAN 99 medan resterande ligger i VLAN 1. Kolumnen VLAN avslöjar detta. Detta då switchen lärt sig adressen, ramen kom fram till porten vilket betyder lager 1 funkar. Kabeln o porten är med detta uteslutna. Addressen finns men trafiken går inte fram vilket betyder ramen stoppas efter switchen tagit emot den, och VLAN är det som gör just det. 

# 12 Här är ett utdrag ur 'show interfaces status'. Tre portar har trafik. En av dem kommer att fungera sämre än de andra. Vilken, och vad skulle du kontrollera härnäst?
<img width="592" height="157" alt="Screenshot 2026-09-01 154151" src="https://github.com/user-attachments/assets/e78d761a-81e8-4523-bdc9-4eeea9c13367" />

Port Gi0/2. Den kör a-half och 100 megabit, medan de andra kör a-full och a-1000. Bokstaven 'a' innan värdet betyder att switchen förhandlat fram det automatiskt. Att förhandlingen hamnade i halv duplex på en gigabitport innebär nästan alltid att motparten har ett fast värde inställt.
Nästa steg är 'show interfaces Gi0/2' och räknarna. Stiger 'late collisions' har du en duplex missmatch. Då får man kontrollera båda ändarnas inställningar, inte bara switchens. Saknas 'a' helt är värdet istället fast inställt på switchen. 

# 13 Skriv fem meningar till en kollega som aldrig hört talas om en switch, där du förklarar varför switchen skickar en ram till alla portar första gången. Använda inga engelska termer utom switch.

Switchen skickar ram till alla portar första gången för att lista ut var mottagaren är, när den får svar på ramen sparar den ner dess adress i fem minuter. Den skickar till alla för att svaret ska lära dem var mottagaren sitter.
