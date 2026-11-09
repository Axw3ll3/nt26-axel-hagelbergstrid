# 1
Svaret är att R-Nordvik-1 använder rutten 10.0.0.6 via interfacet Serial0/0/0, varav interfacet är svaret av frågan (vad som efterfrågas). Detta hittar man i filen "r-nordvik-1.txt"

# 2
Svaret är 64, vilket man ser i r-nordvik-1 filen. Under fliken där man får output för 'show ip ospf interface brief' ser man att interfacet Serial0/0/0 har en kostnad 64 under spalten "cost".

# 3
Svaret är att R-Nordvik-1 inte når BGP grannen mot ip adressen 198.51.100.1, vilket man ser i 'r-nordvik-1.txt' filen. Det må stå att state är active men ändå ser man att en del data saknas, exempelvis MsgRcvd, MsgSent och Up/Down står som never. Dessa värden ger en intrycket att kopplingen inte är uppe.

# 4
Svaret är att Mölndal har Hello-intervallet 5 och dead-intervallet 20. Detta hittar man i 'r-molndal-1.txt' filen under output för 'show ip ospf interface GigabitEthernet0/1'.

# 5
Svaret är kostnad 3 och via vägen 10.0.0.2. 3 eftersom kostnaden till Borås är 1, 1 för länken mellan Borås och Mölndal och 1 för kostnaden till Mölndals VLAN. 1+1+1=3. Vägen blir 10.0.0.2 då den pekas dit via ospf ip routen från Borås till Mölndal är pekad via den vägen.

# 6
Svaret är att pekandet mot neighbor för 198.51.110.1 remote-as är pekad fel (mot 64510) när den egentligen ska bli pekad mot 64501, vilket hänvisas i 'isp-b-valkomstbrev.txt' filen. Kollar man i 'r-nordvik-1.txt' filen i 'show running-config | section router' under 'router bgp 65010'. Där ser man raden: router bgp 65010 neighbor 198.51.100.1 remote-as 64510 neighbor 203.0.113.1 remote-as 64500 varav felet pekas ut.

# 7
Svaret är 5 olika datorer. Kollar man i 'r-nordvik-1.txt' filen längst ner under 'show ip nat translations' ser man vilka datorer som surfar via PAT. 
Kollar vi i detalj:
1. tcp 203.0.113.10:51022 - 192.168.1.42:51022 = Unik dator 1 (192.168.1.42)
2. tcp 203.0.113.10:51023 ... 192.168.1.42:51023 = Samma dator (192.168.1.42), räknas inte igen.
3. udp 203.0.113.10:53211 ... 192.168.1.20:53211 = Unik dator 2 (192.168.1.20)
4. tcp 203.0.113.10:49801 ... 192.168.1.70:49801 = Unik dator 3 (192.168.1.70)
5. tcp 203.0.113.10:1024 ... 192.168.1.23:49801 = Unik dator 4 (192.168.1.23)
6. icmp 203.0.113.10:7 ... 192.168.2.15:7 = Unik dator 5 (192.168.2.15)
7. tcp 203.0.113.10:50310 ... 192.168.1.42:50310 = Tillhör 192.168.1.42 (redan räknad).
8. tcp 203.0.113.11:49200 ... 192.168.1.10:49200 = Tillhör 192.168.1.10.
9. --- 203.0.113.11 ... 192.168.1.10 ... --- = Detta är en statisk NAT-mappning (ip nat inside source static 192.168.1.10 203.0.113.11). Statisk NAT räknas inte med. Dessutom har datorn (192.168.1.10) en statisk IP och räknas därför bort helt.