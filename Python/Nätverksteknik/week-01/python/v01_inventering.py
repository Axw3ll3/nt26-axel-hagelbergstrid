def main():
    
    device_1 = "SW-Nordvik-1"
    model_1 = "WS-C3560-48TS"
    role_1 = "Switch, access"
    
    device_2 = "R-Nordvik-1"
    model_2 = "CISCO2951"
    role_2 = "Router, lager 3"
    
    device_3 = "SW-AxelStrid-2"
    model_3 = "WS-C2960-24TT-L"
    role_3 = "Switch, access"

    print ("UTRUSTNINGSLISTA")
    print ("-" * 52)
    
    print (f"{device_1:<16} {model_1:<20} {role_1}")
    print (f"{device_2:<16} {model_2:<20} {role_2}")
    print (f"{device_3:<16} {model_3:<20} {role_3}")

    print ("-" * 52)
    print (f"Antal enheter: 3")
        
if __name__ == "__main__":
    main()