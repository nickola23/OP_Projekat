"""
Modul za upravljanje vrstama paketa.

Sadrži funkcije za ucitavanje
promenu i aktivaciju paketa.
"""
from funkcije.fajlovi import ucitaj_podatke

def ucitaj_vrste_paketa(putanja):
    """
    Učitava vrste paketa iz fajla.

    Args:
        putanja (str): Putanja do .txt fajla.

    Returns:
        dict: Rečnik sa podacima o vrstama paketa.
    """
    kljucevi = ['id', 'naziv']
    return ucitaj_podatke(putanja, kljucevi)


def promeni_paket(podaci, korisnicko_ime, novi_paket):
    """
    Menja uplaćeni paket korisnika.

    Args:
        podaci (dict): Rečnik sa podacima o korisnicima.
        korisnicko_ime (str): Korisničko ime korisnika kojem se menja paket.
        novi_paket (str): ID novog paketa koji se dodeljuje korisniku.
    """
    if korisnicko_ime in podaci:
        podaci[korisnicko_ime]['uplaceni_paket'] = novi_paket
        print(f"Paket za korisnika {korisnicko_ime} je uspešno promenjen.")
    else:
        print(f"Korisnik sa korisničkim imenom '{korisnicko_ime}' ne postoji.")


def aktivacija_premium_paketa(podaci):
    """
    Aktivira premium paket za određenog korisnika.

    Args:
        podaci (dict): Rečnik sa podacima o korisnicima.
    """
    korisnicko_ime = input('Unesite korisnicko ime clana za aktivaciju: ')
    promeni_paket(podaci, korisnicko_ime, 1)
