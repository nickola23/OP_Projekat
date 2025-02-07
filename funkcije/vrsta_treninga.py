"""
Modul za upravljanje vrstama treninga.

Sadrži funkcije za ucitavanje
vrsta treninga.
"""
from funkcije.fajlovi import citaj_fajl

def ucitaj_vrste_treninga(putanja):
    """
    Ucitava vrste treninga iz fajla.

    Args:
        putanja (string): putanja do .txt fajla

    Returns:
        dict: sve vrste treninga
    """
    fajl = citaj_fajl(putanja)
    if fajl is None:
        return {}

    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id_vrste_treninga, naziv = red.split('|')
            podaci[id_vrste_treninga] = {
                'id': int(id_vrste_treninga),
                'naziv': naziv
            }

    return podaci
