# 1
Svaret är v-b, vilket man ser i filen 'vard-1-brygga.txt' filen. Kollar man i den ser man i tabellen under 'ip -br link show v-b' att dess status är down.

# 2
Svaret är v-eko, eftersom den ligger i vlan 110, ekonomi ligger inom vlan 120 (ser man på dess tagg). Går att hitta i 'vard-1-switch-fore.txt' filen.

# 3
Svaret är 1, det ser vi då TTL bara minskat med 1 (från 64 till 63). Detta ser vi i 'vard-1-switch-efter.txt' filen.

# 4
Svaret är att MAC adressen a6:13:db:8f:85:6f tillhör VLAN 120. Det ser vi i tabellen i filen 'vard-1-switch-efter.txt' filen.

# 5
Svaret är kb, vilket går att lista ut på första raden då man definierar ka's peer som kb. Då vi ser infon kring att ka har sin länk LOWERLAYERDOWN betyder det att andra sidan (kb) inte har sin port uppe. Syns i 'vard-1-kabel.txt' filen.

# 6
Svaret är VLAN 110 och VLAN 120. Dessa VLAN syns i filen 'vard-1-upplank.txt' filen efter trunk delen (att trunken innehåller/har tillgång dessa VLAN).

# 7
Svaret är att porten v-a@eth0 har värdet 55, vilket man ser i 'vard-1-portar.txt' filen då det står 55 före namnet på porten.