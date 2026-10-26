# 1 Vad är en zon, och vad är skillnaden mot ett nät?

# 2 Vad är en DMZ till för, och varför får den inte nå insidan?

# 3 I vilken ordning läser routern en ACL, och när slutar den läsa?

# 4 Vad kan en extended ACL som en standard-ACL inte kan?

# 5 Vad är implict deny, och hur mpnga rader måste en ACL ha för att den ska finnas?

# 6 Vad betyder wildcard-masken 0.0.0.63, och vilket prefix motsvarar den?

# 7 Räknas riktningen in från trafikens eller routerns synvinkel?

# 8 Vilket kommando visar om en regel faktiskt träffat något?

# 9 Vad skyddar port security mot som en ACL inte ser?

# 10 Vad är skillnaden mellan violation restrict och violation shutdown?

# 11 Skriv den engelska termen för vart och ett av följande: zon, riktning, inplicit deny och port security. Provet frågar efter dem.

# 12 Skriv wildcard-masken för vart och ett av följande: 192.168.1.0/26, 192.168.2.0/24, 10.0.0.0/30 och en enda värd. Räkna fram varje mask genom att dra nätmasken från 255, och visa mellanledet.

# 13 En kollega har skrivit 'deny ip 192.168.1.0 0.0.0.128 any'. Vilka adresser täcker den raden? Vilka två av Nordviks fyra nät hamnar innanför, och vilket blir det oväntade resultatet?

# 14 Här är en ACL. Kontoret når fortfarande ekonomiservern trorts att raden finns. lägg märkte till att den nekande raden saknar räknare helt. Vad är fel?

# 15 Här är ett utdrag från ett interface där en ACL nyss satts. Ingenting fungerar längre. Vad hände?

# 16 Skriv den fullständiga konfigurationen som stoppar gästnätet från allt inne i huset men släpper ut det mot internet: listan, alla rader i rätt ordning, och raden som sätter den på rätt interface i rätt riktning.

# 17 Skriv konfigurationen för port security på Gi0/5 till Gi0/9: högst en adress per port, inlärd och sparad automatiskt, och porten ska stängas av vid överträdelse.

# 18 Ny beställning, som ersätter den i genomgången: "Ekonomiavdelningen kan inte nå utvecklingsservern (192.168.1.15 i kontorsnätet). Utvecklarna ska däremot kunna nå ekonomisystemet. Skriv listan, säg vilket interface och vilken riktning den ska ha, och beskriv hur du bevisar båda halvorna.

# 19 "Ingen utifrån ska kunna nå något i huset, utom vår webbserver." Nordvikhar ingen webbserver idag men ska köpa en. Beskriv var den ska stå, vilken zon den hör hemma i och vad som händer om du ställer den i kontorsnätet.

# 20 "Konsulten som kommer på tisdag ska bara komma åt sin egen dator och skrivaren, ingenting annat". Beskriv två helt olika sätt att lösa det, och säg vilket du väljer och varför.

# Skriv fem meningar till en kollega som aldrig hört talas om implicit deny, där du förklarar varför en ACL med en enda nekande rad kan ta ner ett helt nät.

# 22 Vad är baseline, och varflr måste den mästas innan felet?

# 23 Vad gör PAT som statsik NAT inte gör?

# 24 En ping ger inget svar. Vilka två saker kan ha gått fel?