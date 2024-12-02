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
    zaglavlje = linija = vrednosti = ''

    if not podaci:
        print("Nema podataka za prikaz.")
        return
    
    duzine = maxDuzina(podaci)

    for kljuc in duzine.keys():
        zaglavlje += " | " + f"{kljuc:<{duzine[kljuc]}}" 
        linija += "-+-" + "-" * duzine[kljuc]

    print('\n')
    print(zaglavlje)
    print(linija)

    for red in podaci.values():
        for kljuc in duzine.keys():
            vrednosti += " | " + f"{str(red[kljuc]):<{duzine[kljuc]}}"
        vrednosti += '\n'
    print(vrednosti)
