"""
Modul za upravljanje salama.

Sadrži funkcije za ucitavanje sala.
"""
from funkcije.fajlovi import citaj_fajl

def ucitaj_sale(putanja):
    """
    Ucitava sale iz .txt fajla i vraca ih u obliku recnika.

    Args:
        putanja (str): putanja do .txt fajla

    Returns:
        dict: recnik sa svim salama
    """
    fajl = citaj_fajl(putanja)
    if fajl is None:
        return {}

    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id_sale, naziv, broj_redova, oznaka_mesta = red.split('|')
            podaci[id_sale] = {
                'id': int(id_sale),
                'naziv': naziv,
                'broj_redova': int(broj_redova),
                'oznaka_mesta': oznaka_mesta.strip()
            }

    return podaci
