def main():
    hemligt = ["secret", "password", "snmp-server community"]
    
    filnamn = "r1-rakonfig.txt"
    rensade = []
    borttagna = 0
    
    with open (filnamn) as f:
        for rad in f:
            if any (ord_ in rad for ord_ in hemligt):
                borttagna = borttagna + 1
            else:
                rensade.append(rad)
                
    with open ("r1-show-run.txt", "w") as f:
        for rad in rensade:
            f.write (rad)
            
    print (f"Tog borg {borttagna} rader. Resultatet ligger i r1-show-run.txt.")