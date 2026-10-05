from getpass import getpass
from netmiko import ConnectHandler
import os
from pathlib import Path

skript_mapp = Path(__file__).parent
os.chdir(skript_mapp)

losenord = getpass("Losenord: ")

# En rad per enhet. Lagg till fler efter samma monster.
enheter = [
    {"namn": "R-Nordvik-1", "host": "192.168.1.193"},
    {"namn": "SW-Nordvik-1", "host": "192.168.1.197"},
    {"namn": "SW-Nordvik-2", "host": "192.168.1.196"},
]

rader = ["# Inventarierapport", ""]

for enhet in enheter:
    anslutning = ConnectHandler(
        device_type="cisco_ios",
        host=enhet["host"],
        username="drift",
        password=losenord,
    )
    version = anslutning.send_command("show version | include uptime")
    anslutning.disconnect()

    rader.append(f"## {enhet['namn']} ({enhet['host']})")
    rader.append(version)
    rader.append("")

with open("inventarie.md", "w") as f:
    f.write("\n".join(rader))

print(f"Skrev rapport for {len(enheter)} enheter till inventarie.md")
