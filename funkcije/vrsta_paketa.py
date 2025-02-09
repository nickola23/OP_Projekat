"""
Modul za upravljanje vrstama paketa.

Sadrži funkcije za ucitavanje
promenu i aktivaciju paketa.
"""
from funkcije.fajlovi import ucitaj_podatke

def ucitaj_vrste_paketa(putanja):
    kljucevi = ['id', 'naziv']
    return ucitaj_podatke(putanja, kljucevi)


def promeni_paket(podaci, korisnicko_ime, novi_paket):
    if korisnicko_ime in podaci:
        podaci[korisnicko_ime]['uplaceni_paket'] = novi_paket
        print(f"Paket za korisnika {korisnicko_ime} je uspešno promenjen.")
    else:
        print(f"Korisnik sa korisničkim imenom '{korisnicko_ime}' ne postoji.")


def aktivacija_premium_paketa(podaci):
    korisnicko_ime = input('Unesite korisnicko ime clana za aktivaciju: ')
    promeni_paket(podaci, korisnicko_ime, 1)
