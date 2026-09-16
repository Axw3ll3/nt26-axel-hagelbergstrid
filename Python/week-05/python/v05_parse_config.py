from pathlib import Path
def main():
    filnamn = Path("Python") / "week-05" / "python" / "configs" / "r1-show-run.txt"
    routes = []
    interfaces = []
    
    with open(filnamn) as f:
        for rad in f:
            rad = rad.strip()
            if rad.startswith("ip route "):
                routes.append(rad)
            if rad.startswith("interface "):
                interfaces.append(rad)

    print(f"Hittade {len(routes)} statiska rutter:")
    for rad in routes:
        print(f" {rad}")
    print(f"Hittade {len(interfaces)} gränssnitt:")
    for rad in interfaces:
        print(f" {rad}")
            
if __name__ == "__main__":
    main()
