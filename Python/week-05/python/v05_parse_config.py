filnamn = "r1-show-run.txt"

routes = []

with open(filnamn) as f:
    for rad in f:
        rad = rad.strip()
        if rad.startswith("ip route "):
            routes.append(rad)

print(f"Hittade {len(routes)} statiska rutter:")
for rad in routes:
    print(f" {rad}")