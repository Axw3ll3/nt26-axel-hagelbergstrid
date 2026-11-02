import ipaddress

from jaraco import text

def main():

    text = "192.168.1.128/26"

    net = ipaddress.ip_network(text, strict=False)

    usable = list(net.hosts())

    print (f"Network: {net.network_address}")
    print (f"Netmask: {net.netmask}")
    print (f"Broadcast: {net.broadcast_address}")
    print (f"First Address: {usable[0]}")
    print (f"Last Address: {usable[-1]}")
    print (f"Total Usable Devices: {len(usable)}")

if __name__ == "__main__":
    main()