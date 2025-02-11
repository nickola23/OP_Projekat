"""
Modul za upravljanje salama.

Sadrži funkcije za ucitavanje sala.
"""
from funkcije.fajlovi import ucitaj_podatke

def ucitaj_sale(putanja):
    """
    Učitava podatke sala iz fajla.

    Args:
        putanja (str): Putanja do .txt fajla.

    Returns:
        dict: Rečnik sa podacima o salama.
    """
    kljucevi = ['id', 'naziv', 'broj_redova', 'oznaka_mesta']
    podaci = ucitaj_podatke(putanja, kljucevi)

    # Dodatna obrada podataka
    for sala in podaci.values():
        sala['id'] = int(sala['id'])
        sala['broj_redova'] = int(sala['broj_redova'])
        sala['oznaka_mesta'] = sala['oznaka_mesta'].strip()

    return podaci
