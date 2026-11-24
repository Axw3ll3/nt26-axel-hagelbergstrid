# Labb 01A

### 'ip -br link show ka' före:

<img width="950" height="94" alt="image" src="https://github.com/user-attachments/assets/79f61ef3-a590-40dd-994c-a27d852a07e6" />


### 'ip -br link show ka' efter:

<img width="950" height="82" alt="image" src="https://github.com/user-attachments/assets/68889f22-f44b-46f7-8bbe-b4782e33a6ac" />

### Skillnaden mellan dessa 2 screenshots är att den första så ligger länken nere, medan på den andra ser vi länken är uppe.

### 'bridge link show':

<img width="950" height="82" alt="image" src="https://github.com/user-attachments/assets/93c12666-9f9f-4c5f-a8fe-f53c8b079b46" />

### Utdata från pingen och tabellen:

<img width="961" height="265" alt="image" src="https://github.com/user-attachments/assets/7302df17-dcd5-45ae-aaa6-ad07176719f8" />

### 'bridge fdb show' i veth motsvarar 'show mac address-table' i Cisco iOS.

### Trafik på bryggan vs. fysiskt nätverkskort:

Observation: På bryggan br0 ser vi ICMP-trafiken 'echo request' och 'echo reply' mellan '192.168.10.1' och '192.168.10.2', medan 'tcpdump' på datorns eget nätverkskort (wlo1) fångade '0 packets'.

Varför: Bryggan 'br0' fungerar som en virtuell L2-switch som kopplar samman 'v-a' och 'v-b' och skickar trafiken direkt mellan dessa portar i Linux-kärnan. Då mottagaren finns lokalt bakom bryggan och inte ens är ansluten till 'wlo1', skickas paketen aldrig ut på det fysiska nätverkskortet.

Betydelsen av detta: För att fånga trafik mellan två virtuella maskiner på samma värd räcker det inte att lyssna på värdens fysiska nätverkskort, eftersom den interna trafiken aldrig når dit. Man måste istället fånga trafiken på den virtuella bryggan/switchen, på respektive VM:s virtuella nätverksgränssnitt (veth) eller inne i gästsystemen.

# Labb 01B

### Utdata av 'sudo ovs-vsctl show':

<img width="955" height="365" alt="image" src="https://github.com/user-attachments/assets/fb1bc1db-c6de-47da-b61a-3e08ab94d7a4" />

### Utdata av steg 5:

<img width="961" height="189" alt="image" src="https://github.com/user-attachments/assets/efdb00ce-d750-4229-80ab-6d31578e39fe" />

<img width="952" height="226" alt="image" src="https://github.com/user-attachments/assets/96cf7904-c94a-4be1-acb6-edd19c9ee928" />

### Det står ttl=63 nu istället för ttl=64 eftersom när pingen hoppar router minskar ttl (time to live) med 1. Det minskade inte i steg 4 eftersom hoppet är inom samma VLAN/paketet inte routras.

### Utdata av 'sudo ovs-appctl fdb/show sw0':

<img width="957" height="151" alt="image" src="https://github.com/user-attachments/assets/1aaa9be4-2467-465d-b0a3-382a2f137ad9" />

### Kolumnen VLAN visar vilket virtuell nät som respektive MAC-adress tillhör, vilket gör att switchen håller MAC-adresstabellerna åtskilda per VLAN och endast vidarebefodrar ramar inom samma VLAN.

### Utdata om porten "upp":

<img width="959" height="421" alt="image" src="https://github.com/user-attachments/assets/254d5176-31bf-4159-b22d-04cc59a064f9" />


### För att maskinerna i VLAN 110 och 120 ska nå resten av näten måste porten på den fysiska switchen i andra änden vara konfigurerad som en trunkport som tillåter VLAN 110 och VLAN 120 (samt att VLAN:en är definierade i den fysiska switchens VLAN-databas).

