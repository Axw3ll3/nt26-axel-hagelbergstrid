from getpass import getpass

from netmiko import ConnectHandler

def main():
    enhet = {
        "device_type": "cisco_ios",
        "host": "192.168.1.193"
        "username: drift",
        "password": getpass("Losenord: "),
    }

    with ConnectHandler (**enhet) as anslutning:
        svar = anslutning.send_command ("show ip interface brief")
    
    print (svar)

    with open("status.txt", "w") as f:
        f.write(svar)

    print("Sparade svaret i status.txt")

if __name__ == "__main__":
    main()