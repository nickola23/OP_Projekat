from datetime import time, date

def maxDuzina(podaci):

    if not podaci or not isinstance(podaci, dict):
        return {}
    
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

    if not podaci or not isinstance(podaci, dict):
        print("Nema podataka za prikaz. ili podaci nisu u obliku recnika")
        return
    
    duzine = maxDuzina(podaci)

    if not duzine:
        print("Nema podataka za prikaz. ili podaci nisu u obliku recnika")
        return

    for kljuc in duzine.keys():
        zaglavlje += " | " + f"{kljuc:<{duzine[kljuc]}}" 
        linija += "-+-" + "-" * duzine[kljuc]

    print('\n')
    print(zaglavlje)
    print(linija)

    for red in podaci.values():
        for kljuc in duzine.keys():
            if isinstance(red[kljuc], list):
                spojeni_podaci = ", ".join(map(str, red[kljuc]))
                vrednosti += " | " + f"{spojeni_podaci.capitalize():<{duzine[kljuc]}}"
            elif isinstance(red[kljuc], time):
                vrednosti += " | " + f"{str(red[kljuc].strftime("%H:%M")):<{duzine[kljuc]}}"
            else:
                vrednosti += " | " + f"{str(red[kljuc]):<{duzine[kljuc]}}"
        vrednosti += '\n'
    print(vrednosti)
