def main():
    vendors = {
        "a4:c3:f0": "Intel",
        "3c:d9:2b": "Hewlett-Packard",
        "00:1a:a1": "Cisco Systems",
        #Own MAC Addresses
        "a0:ad:9f": "ASUSTek COMPUTER INC",
        "28:95:29": "Intel Corporate",
        "E8:78:65": "Apple Inc",
    
    }
    
    addresses = [
        "a4:c3:f0:11:3a:b7",
        "3c:d9:2b:d2:11:88",
        "8c:85:90:44:12:0e",
        #Own MAC Addresses
        "a0:ad:9f:52:03:e3",
        "28:95:29:c0:50:30",
        "E8:78:65:04:C5:25",
    ]
    
    for address in addresses:
        prefix = address [0:8]
        
    
        if prefix in vendors:
            name = vendors [prefix]
        else:
            name = "Okänd tillverkare"
    
        print(f"{address} -> {name}")
        
if __name__ == "__main__":
    main()