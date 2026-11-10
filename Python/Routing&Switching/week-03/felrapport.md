# Felrapport Vecka 03

# Labb 03A – Fel 1
Observation: R-Boras-1 får inget grannskap upp mot R-Nordvik-1 på Gi0/2.
Hypotes: IP-adressering eller nätmask matchar inte på länken.
Test: Körde 'show ip interface brief' och 'show run interface Gi0/2' på båda routrarna.
Slutsats: Felaktig IP-mask konfigurerad på R-Boras-1.
Åtgärd: Korrigerade IP-adress och mask på Gi0/2 till rätt poddnät.

# Labb 03A – Fel 2
Observation: R-Boras-1 skickar inte OSPF-uppdateringar på Gi0/1.
Hypotes: Network-kommandot saknas eller täcker inte gränssnittets IP.
Test: Kontrollerade 'show running-config | section router ospf'.
Slutsats: Wildcard-masken i OSPF-konfigurationen var felaktig.
Åtgärd: Uppdaterade network-raden med korrekt wildcard-mask (0.0.0.3).

# Labb 03A – Fel 3
Observation: Länken mellan R-Nordvik-1 och R-Molndal-1 visar inte FULL grannskap.
Hypotes: Passive-interface har aktiverats på den seriella länken av misstag.
Test: Körde `show ip ospf interface 'Se0/0/0'.
Slutsats: Gränssnittet var markerat som passive-interface.
Åtgärd: Tog bort passive-interface på Se0/0/0 med 'no passive-interface Serial0/0/0'.

# Labb 03B – Fel 1
Observation: eBGP-sessionen mot ISP-A blir aldrig etablerad.
Hypotes: Fel remote-as angivet för ISP-A.
Test: Kontrollerade konsolloggarna (%BGP-5-ADJCHANGE) och running-config.
Slutsats: Neighbor-kommandot pekade på fel AS-nummer.
Åtgärd: Korrigerade 'neighbor 203.0.113.1 remote-as 64500'.

# Labb 03B – Fel 2
Observation: Borås kan nå Göteborg men inte internet/webbservern.
Hypotes: Saknad NAT-översättning för Borås nät på R-Nordvik-1.
Test: Granskade 'ip nat inside' markeringar samt ACL för NAT-översättningen.
Slutsats: Interfacet Gi0/2 saknade kommandot 'ip nat inside'.
Åtgärd: Lade till 'ip nat inside' under gränssnittet Gi0/2 på R-Nordvik-1.