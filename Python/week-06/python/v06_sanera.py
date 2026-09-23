from pathlib import Path

def main():
    hemligt = ["secret", "password", "snmp-server community"]
    
    filnamn = Path("Python") / "week-06" / "python" / "r1-rakonfig.txt"
    ut_filnamn = filnamn.parent / "r1-show-run.txt"
    routes = []
    rensade = []
    borttagna = 0
    
    with open (filnamn) as f:
        for rad in f:
            if any (ord_ in rad for ord_ in hemligt):
                borttagna = borttagna + 1
            else:
                rensade.append(rad)
    
                
    with open (ut_filnamn, "w") as f:
        for rad in rensade:
            f.write (rad)
            
    print (f"Tog borg {borttagna} rader. Resultatet ligger i r1-show-run.txt.")
    
if __name__ == "__main__":
    main()