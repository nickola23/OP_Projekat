"""
Modul za upravljanje tabelama.

Sadrži funkcije za odredjivanje
maksimalne duzine, kreiranje i ispis tabela.
"""
from datetime import time

def max_duzina(podaci):
    if not podaci or not isinstance(podaci, dict):
        return {}

    max_duzine = {}

    prvi_unos = next(iter(podaci))
    for kljuc in podaci[prvi_unos].keys():
        max_duzine[kljuc] = len(kljuc)

    for red in podaci.values():
        for kljuc, vrednost in red.items():
            trenutna_duzina = len(str(vrednost))
            if trenutna_duzina > max_duzine[kljuc]:
                max_duzine[kljuc] = trenutna_duzina

    return max_duzine


def kreiraj_tabelu(podaci, duzine):
    vrednosti = ''
    for red in podaci.values():
        for kljuc in duzine.keys():
            if isinstance(red[kljuc], list):
                spojeni_podaci = ", ".join(map(str, red[kljuc]))
                vrednosti += " | " + f"{spojeni_podaci.capitalize():<{duzine[kljuc]}}"
            elif isinstance(red[kljuc], time):
                vrednosti += " | " + f"{str(red[kljuc].strftime('%H:%M')):<{duzine[kljuc]}}"
            else:
                vrednosti += " | " + f"{str(red[kljuc]):<{duzine[kljuc]}}"
        vrednosti += '\n'
    return vrednosti


def ispis_tabele(podaci):

    zaglavlje = linija = vrednosti = ''

    if not podaci or not isinstance(podaci, dict):
        print("Nema podataka za prikaz.")
        return

    duzine = max_duzina(podaci)

    if not duzine:
        print("Nema podataka za prikaz.")
        return

    for kljuc, vrednost in duzine.items():
        zaglavlje += " | " + f"{kljuc:<{vrednost}}"
        linija += "-+-" + "-" * vrednost

    print('\n')
    print(zaglavlje)
    print(linija)

    vrednosti = kreiraj_tabelu(podaci, duzine)
    print(vrednosti)
