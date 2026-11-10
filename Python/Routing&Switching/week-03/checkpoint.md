OSPF Neighbors från R-Boras-1:

<img width="600" height="76" alt="image" src="https://github.com/user-attachments/assets/67aaace8-5388-49bf-8340-ac8ef2c2d03e" />


OSPF Routes & Interfaces från R-Nordvik-1:

<img width="600" height="201" alt="image" src="https://github.com/user-attachments/assets/57bab184-9207-4ba2-a0a8-3857c7e9523b" />


OSPF väljer vägen via Borås då det är billigare/lägre kostnad jämfört med direktlänken (Serial), eftersom OSPF baserar sin metric på bandbredd.


Routingtabell med Gi0/2 avstängd:

<img width="554" height="425" alt="image" src="https://github.com/user-attachments/assets/909b26ab-3e5a-4b3f-b798-d0d82ec8f7de" />


BGP Summary & BGP Table från R-Nordvik-1:

<img width="624" height="234" alt="image" src="https://github.com/user-attachments/assets/753927a6-e8bc-4189-b2c3-da83c15a4b0e" />

Talen i Path-kolumnen visar ordningsföljden av de autonoma system (AS_PATH) som uppdateringen passerat för att nå routern.

Defaultrutt på R-Boras-1:

<img width="617" height="386" alt="image" src="https://github.com/user-attachments/assets/394fa17d-c380-4e5b-9230-faba955271d6" />

NAT Translations från R-Nordvik-1:

<img width="561" height="86" alt="image" src="https://github.com/user-attachments/assets/4f5ae131-6b3a-4f40-b875-da75da656621" />

PAT använder unika källportnummer för att skilja mellan olika interna anslutningar som delar på samma outside-ip. Om två enheter använder samma källport översätter routerns port till en ny ledig port på utsidan
