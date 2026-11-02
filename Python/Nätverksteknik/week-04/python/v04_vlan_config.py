def vlan_config(number, name):
    rader = []
    rader.append(f"vlan: {number}")
    rader.append(f"name: {name}")
    return rader

vlans = {}
for i in range(1, 41):
    vlans[i] = f"NAT{i:02d}"
    

for number in vlans:
    for rad in vlan_config(number, vlans[number]):
        print (rad)
