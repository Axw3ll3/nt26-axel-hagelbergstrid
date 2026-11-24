# Felrapport – Labb 01B

## Observation
Vid ping från 'fil' (10.10.110.10) till 'eko' (10.10.120.10) med kommandot 'sudo ip netns exec fil ping -c 2 -W 1 10.10.120.10' blir resultatet '100% packet loss' (0 mottagna paket).

## Hypotes
Någon länk mellan 'fil', 'sw0', 'r' och 'eko' är nere, någon switchport sitter i fel VLAN, eller så vidarebefordrar routern 'r' inte IP-paket mellan subnäten.

## Test
1. Kontroll av länkar ('ip -br link' på värden och i namnrymderna):
   - Kommando: 'ip -br link', 'sudo ip netns exec fil ip -br link', 'sudo ip netns exec r ip -br link', 'sudo ip netns exec eko ip -br link'.
   - Svar: Alla berörda gränssnitt ('v-fil', 'v-eko', 'v-r110', 'v-r120', 'eth0' i 'fil' och 'eko', samt 'r110' och 'r120' i 'r') hade status 'UP'.

2. Kontroll av VLAN-taggar på switchen ('sudo ovs-vsctl show'):
   - Kommando: 'sudo ovs-vsctl show'
   - Svar: Porten 'v-eko' visade 'tag: 110' i stället för 'tag: 120' (övriga portar hade rätt taggar: 'v-fil' 'tag: 110', 'v-r110' 'tag: 110', 'v-r120' 'tag: 120').

*(Felsökningen stannade vid steg 2 i kontrollordningen eftersom orsaken hittades direkt.)*

## Slutsats
Switchporten 'v-eko' var felkonfigurerad med 'tag: 110' i stället för 'tag: 120', vilket gjorde att ekonomisystemet hamnade i fel VLAN och inte kunde kommunicera med routerns gränssnitt 'r120' i VLAN 120.

## Åtgärd
Ändrade VLAN-taggen på port 'v-eko' tillbaka till VLAN 120 med:
'sudo ovs-vsctl set port v-eko tag=120'.

Verifierade därefter att kommunikationen fungerade genom att köra:
'sudo ip netns exec fil ping -c 2 -W 1 10.10.120.10'
Resultatet blev '0% packet loss' och svar med 'ttl=63'.