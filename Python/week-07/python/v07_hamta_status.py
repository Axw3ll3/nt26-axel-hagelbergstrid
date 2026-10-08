from getpass import getpass
from netmiko import ConnectHandler
import os
from pathlib import Path

skript_mapp = Path(__file__).parent
os.chdir(skript_mapp)

enhet = {
    "device_type": "cisco_ios",
    "host": "192.168.2.193",
    "username": "drift",
    "password": getpass("Losenord: "),
}

with ConnectHandler(**enhet) as anslutning:
    svar = anslutning.send_command("show ip interface brief")

print(svar)

with open("status.txt", "w") as f:
    f.write(svar)

print("Sparade svaret i status.txt")