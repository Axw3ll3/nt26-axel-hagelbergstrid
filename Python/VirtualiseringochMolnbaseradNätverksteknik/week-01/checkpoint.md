# Labb 01A

'ip -br link show ka' före:

<img width="950" height="94" alt="image" src="https://github.com/user-attachments/assets/79f61ef3-a590-40dd-994c-a27d852a07e6" />


'ip -br link show ka' efter:

<img width="950" height="82" alt="image" src="https://github.com/user-attachments/assets/68889f22-f44b-46f7-8bbe-b4782e33a6ac" />

Skillnaden mellan dessa 2 screenshots är att den första så ligger länken nere, medan på den andra ser vi länken är uppe.

'bridge link show':

<img width="950" height="82" alt="image" src="https://github.com/user-attachments/assets/93c12666-9f9f-4c5f-a8fe-f53c8b079b46" />

Utdata från pingen och tabellen:

<img width="961" height="265" alt="image" src="https://github.com/user-attachments/assets/7302df17-dcd5-45ae-aaa6-ad07176719f8" />

'bridge fdb show' i veth motsvarar 'show mac address-table' i Cisco iOS.

Trafik på bryggan vs. fysiskt nätverkskort:
Observation: På bryggan br0 ser vi ICMP-trafiken 'echo request' och 'echo reply' mellan '192.168.10.1' och '192.168.10.2', medan 'tcpdump' på datorns eget nätverkskort (wlo1) fångade '0 packets'.
Varför: Bryggan 'br0' fungerar som en virtuell L2-switch som kopplar samman 'v-a' och 'v-b' och skickar trafiken direkt mellan dessa portar i Linux-kärnan. Då mottagaren finns lokalt bakom bryggan och inte ens är ansluten till 'wlo1', skickas paketen aldrig ut på det fysiska nätverkskortet.
Betydelsen av detta: För att fånga trafik mellan två virtuella maskiner på samma värd räcker det inte att lyssna på värdens fysiska nätverkskort, eftersom den interna trafiken aldrig når dit. Man måste istället fånga trafiken på den virtuella bryggan/switchen, på respektive VM:s virtuella nätverksgränssnitt (veth) eller inne i gästsystemen.
