# 1
Kom fram till svaret genom att kolla fw-nordvik-1-syslog.txt filen, och där hittade jag 172.16.10.10 som sedan blev ompekad/översatt till ip adressen 203.0.113.12 som stod senare på raden inom paranteser.

# 2
Svaret är 50-nej, webbservern ligger i säkerhetsszon 50 (där 50 kommer in). Det är ett nej, då om vi tar bort DMZ accesslistan kommer inte någon ny anslutning från internet komma åt filservern i kontorsnätet.

# 3
Svaret är port 3389 eftersom i fw-nordvik-1-syslog.txt hänvisas försök att ansluta mot den, så ... --> dmz/172.16.10.10(3389). Så först hänvisar den inom vilken säkerhetszon (dmz), adressen den försöker nå (172.16.10.10) och sist, inom parantesen, står vilken port (3389), vilket också är svaret.

# 4
Svaret var '198.51.100.30', vilket är för att 198.51.100.30 (Mölndalssidan) inte kan komma överens med kryptering som inte matchar. Man kan även se i syslog att det är upprepade misslyckade attacker mot port 3389 då det har VPN fel i fas 1. Utöver detta ser man att DMZ försöker nå inside vilket inte är något man vill (fel i konfiguration), syns vid 8:23 i syslog.

# 5
Söker man efter policy genom CTRL-F, där hittade man fas-1. I dem när man kollar uppifrån ner ser man group på R-Molndal-1 är 2 och på FW-Nordvik-1 är det group 5. Enda som på rak arm som skiljer

# 6
Svaret är 192.168.2.64/26. Detta då man ser trafik mellan 192.168.1.42 till 192.168.2.10 fungerade innan kl. 9:05 och matchade NAT-undantaget för VPN tunneln. Efter kl. 9:05 går user 'kalle' in och ändrar object network BORAS-NET, och ändrar subnet 192.168.2.64 255.255.255.192. Då 192.168.2.10 inte ligger inom detta spann/nätverk kommer det framöver nekas då det inte matchar VPN tunnelns kriterier.

# 7
Svaret är 3 gånger. Även fast det uppkommer 6 gånger så ser man att 198.51.100.77 har 3st "Teardown TCP connection" och 3st "Built inbound TCP connection". Den senare med "Built inbound" innebär att en koppling skapats, vilekt är vad frågan frågar om.