# 1 Vad säger en IP-adress som inte en MAC-adress säger?

IP-adressen säger vart enheten finns. MAC-adressen säger vem enheten är och ändras aldrig i normalfall. IP-adressen säger var den bor just nu, och byts så fort enheten byter nät.

# 2 Vad gör nätmasken?

Nätmasken talar om hur stor del av adressen som är nätet och hur stor del som är enheten. Utan den går det inte att avgöra om två adresser ligger i samma nät.

# 3 Vilken adress i ett nät får ingen enhet ha, och varför är det två stycken?

De adresser i ett nät ingen får ha är nätadressen och broadcastadressen. Detta eftersom nätadressen är namnet på nätet, och broadcastadressen når alla i nätet. Ingen enhet i nätet får ha dessa och därför är antalet enheter alltid två färre än antalet adresser.

# 4  Vad är blocksteget för /26, och vad använder du den till?

Blocksteget för /26 är 64, och det används för att hitta närmaste nät genom att räkna 0, 64, 128, 192 tills du passerar din adress.

# 5 Varför måste gatewayen ligga i samma nät som du?

Gatewayen måste ligga i samma nät som du eftersom du bara kan skicka direkt till enheter i ditt egna nät. Ligger gatewayen utanför ditt nät når du den aldrig, och då hjälper den dig inte.

# 6 Vad händer med en dator som har rätt adress men ingen gateway?

Datorn fungerar bra inom sitt egna nät, men når ingenting utanför. Skrivaren och filservern fungerar, men inte internet. Det är därför det är så svårt att hitta felet.

# 7 Vilka fyra saker får en dator av DHCP, och vilken av dem säger hur länge det gäller?

De fyra saker en dator får av DHCP är IP-adress, nätmask, default gateway och DNS-server.

# 8 Vilka enheter ska ha statisk adress, och varför?

De enheter som ska ha statisk adress är routrar, switchar, servrar och skrivare. Detta för att andra ska kunna hitta dem på en känd adress, och för att lätt nå för att felsöka.

# 9 Hur skiljer du ett DNS-problem från ett DHCP-problem?

DNS-problem uppstår om man kan pinga en resurs men inte når adressen till samma resurs. Fungerar inget av det är det något annat, och då börjar du felsöka din egna adress.

# 10 Vad betyder det att en dator har en adress som börjar på 169.254?

Om en dator har en adress som börjar på 169.254 är det för att datorn frågade efter en adress, fick inget svar och hittade på en egen, då det inte fungerar utanför den egna kabeln.

# 11 Räkna ut nätadress, broadcast och adressintervall för 192.168.1.200/26. Visa alla fyra stegen.

1. Blocksteg för /26 är 64
2. 0, 64, 128, 192. Talet ligger efter 192. Nätet är 192.168.1.192.
3. Nästa nät efter 192 är 256, vilket inte finns i det sista talet. Nätet slutar på 255, och broadcast blir då 192.168.1.255.
4. Enherna är från 192.168.1.193 till 192.168.1.254, alltså 62 stycken då boadcast och nätet i sig ockuperar 192 och 255. 

# 12 Räkna ut samma sak för 10.0.0.6/30. Hur många enheter får plats?

Blocksteget är 4. Det räknas då 0, 4, 8. Talet 6 ligger mellan 4 och 8. Nätet är 10.0.0.4, broadcast är 10.0.0.7, och enheterna är 10.0.0.5 och 10.0.0.6, vilket blir 2 st.

# 13 Nordviks lager i Borås har fått 192.168.2.0/24 och behöver 3 nät: lager, trådlöst gäst och drift. Föreslå en uppdelning i /26 och skriv ut nät, broadcast och intervall för varje.

Lagerns nät blir 192.168.2.0/26, broadcast på 192.168.2.63, och enheterna däremellan blir på 192.168.2.1 till 192.168.2.62

Trådlöst gäst nätet blir på 192.168.2.64/26, broadcast på 192.168.2.127 och enheterna blir mellan 192.168.2.65 till 192.168.2.126.

Drift nätet ligger på 192.168.2.192/26, broadcast på 192.168.2.255. Enheterna hamnar på adresserna mellan 192.168.2.193 och 192.168.2.254.

# 14 Här är ett utdrag från en dator som inte kommer ut på nätet, men som når filservern på 192.168.1.10. Vad är fel?
<img width="560" height="124" alt="Screenshot 2026-09-02 132017" src="https://github.com/user-attachments/assets/d154e729-f243-4883-9d92-9a127d24551a" />

Gatewayen ligger i fel nät. Datorn har 192.168.1.42 med masken 255.255.255.192, alltså i /26. Datorns nät är 192.168.1.0/26 med adresserna 192.168.1.1 till 192.168.1.62. Gatewayen ligger på 192.168.1.65 vilket är utanför nätet. Rätt gateway adress är 192.168.1.1.

# 15 Här är ett utdrag från routern. En student säger att DHCP inte fungerar, för hens dator får ingen adress. Vad frågar du härnäst?
<img width="579" height="227" alt="Screenshot 2026-09-02 132022" src="https://github.com/user-attachments/assets/2cd8110e-3be2-4ba8-acae-ecdf002e231f" />


Bara Gi0/0 har adress och är igång. De andra gigabitportarna är nere (administratively down). Sitter studenten i frågans dator bakom någon av gigaportarna som är nere når DHCP-frågan aldrig ett konfigurerat interface, och då får personen i fråga ingen adress hur rätt poolen än är. 

Vanligt att kolla om porten är rätt konfigurerad, utdatan säger den funkar även fast man inte kört ett enda DHCP-kommando. Därför det är viktigt att kolla 'show ip interface brief' tidigt och inte sist.

# 16 Skriv fem meningar till en kollega som aldrig hört talas om nätsmask, där du förklarar varför två datorer med samma adressbörjan ändå kan hamna i olika nät.

Varje IP-adress består alltid av två delar: en nätverksdel som visar vilket nätverk den tillhör och en enhetsdel för att specificera datorn. Datorer läser adresser binärt som ettor och nollor, vilket betyder att gränsen inte måste ligga snyggt mellan de synliga siffrorna utan kan ligga mitt inne i sista talet. Om två datorer har samma adressbörjan men olika nätmasker dras gränserna på olika ställen. Detta gör att ena datorns adressdel tolkas som ett nätverk, medan andras hamnar i ett helt annat nätverk.
