def maxDuzina(podaci):
    maxDuzina = {}
    prvi_unos = next(iter(podaci))
    for kljuc in podaci[prvi_unos].keys():
        maxDuzina[kljuc] = len(kljuc)
    
    for red in podaci.values():
        for kljuc, vrednost in red.items():

            trenutna_duzina = len(str(vrednost))
            if trenutna_duzina > maxDuzina[kljuc]:
                maxDuzina[kljuc] = trenutna_duzina
    
    return maxDuzina

def ispisTabele(podaci):
    if not podaci:
        print("Nema podataka za prikaz.")
        return
    
    duzine = maxDuzina(podaci)

    zaglavlje = " | ".join(f"{kljuc:<{duzine[kljuc]}}" for kljuc in duzine.keys())
    linija = "-+-".join("-" * duzine[kljuc] for kljuc in duzine.keys())

    print(zaglavlje)
    print(linija)

    for red in podaci.values():
        vrednosti = " | ".join(f"{str(red[kljuc]):<{duzine[kljuc]}}" for kljuc in duzine.keys())
        print(vrednosti)
