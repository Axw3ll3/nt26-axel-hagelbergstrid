OSPF Neighbors från R-Boras-1:

OSPF Routes & Interfaces från R-Nordvik-1:

OSPF väljer vägen via Borås då det är billigare/lägre kostnad jämfört med direktlänken (Serial), eftersom OSPF baserar sin metric på bandbredd.


Routingtabell med Gi0/2 avstängd:

BGP Summary & BGP Table från R-Nordvik-1:

Talen i Path-kolumnen visar ordningsföljden av de autonoma system (AS_PATH) som uppdateringen passerat för att nå routern.

Defaultrutt på R-Boras-1:

NAT Translations från R-Nordvik-1:

PAT använder unika källportnummer för att skilja mellan olika interna anslutningar som delar på samma outside-ip. Om två enheter använder samma källport översätter routerns port till en ny ledig port på utsidan