import socket

mal = "192.168.1.10"
portar = [22, 23, 80, 443, 445]

try:
    adress = socket.gethostbyname(mal)
except socket.gaierror:
    print(f"Hittar ingen maskin som heter {mal}. Kontrollera stavningen.")
    
for port in portar:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((adress, port))
        print(f"Port {port}: OPPEN")
    except OSError:
        print(f"Port {port}: stangd eller filtrerad")
    
s.close