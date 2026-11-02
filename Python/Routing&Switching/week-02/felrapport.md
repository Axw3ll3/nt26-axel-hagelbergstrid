# Observation
Saknad Ip route mellan routrar

# Hypotes
Saknad IP Routing

# Test
Testade pinga 192.168.2.10 från Filservern, fick inget svar. Testade pinga 192.168.1.10 från PC-Boras, fick inget svar.

# Slutsats
Saknad IP Routing

# Åtgärd
Pekade rätt IP routing efter direktiv, så ekrarna hade sin ip routing mot navet men oavsett vart trafiken skulle (0.0.0.0 0.0.0.0 mot då 10.0.0.1 från Borås och 0.0.0.0 0.0.0.0 10.0.0.5 från Mölndal).

Från navet pekade jag ut ip routing till Mölndal och Borås till deras nät. Så 192.168.2.0 255.255.255.192 10.0.0.1 (från Nordvik till Borås) och 192.168.3.0 255.255.255.192 10.0.0.6 (från Nordvik till Mölndal)

Säkrade att de funka genom att pinga fram och tillbaka samt följde pingen med tracert.