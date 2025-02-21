"""
Modul za upravljanje korisnicima.

Sadrži funkcije za dodavanje instruktora,
aktivaciju i promenu statusa clana.
"""
from datetime import datetime
from funkcije.clanarina import dodaj_clanarinu

def dodaj_instruktora(korisnici):
    """
    Dodaje novog instruktora ili administratora.

    Args:
        korisnici (dict): Rečnik sa podacima o korisnicima.

    Returns:
        bool: True ako je instruktor uspešno dodat, False u suprotnom.
    """
    while True:
        korisnicko_ime = input("Unesite korisnicko ime: ")
        if korisnicko_ime not in korisnici.keys():
            lozinka = input("Unesite lozinku: ")
            ime = input("Unesite ime: ")
            prezime = input("Unesite prezime: ")
            uloga = input("Izaberite opciju:\n0. Instruktor\n1. Administrator\nUnesite ulogu:")

            korisnici[korisnicko_ime] = {
                'korisnicko_ime': korisnicko_ime,
                'ime': ime,
                'prezime': prezime,
                'lozinka': lozinka,
                'uloga': int(uloga),
                'status': 0,
                'uplaceni_paket': 0,
                'datum_registracije': datetime.now().date().strftime('%d.%m.%Y'),
            }

            print("Uspesno ste dodali instruktora.")
            return True


def promeni_status_clana(korisnici, clanarine, korisnicko_ime, novi_status):
    """
    Menja status člana u sistemu.

    Args:
        korisnici (dict): Rečnik sa podacima o korisnicima.
        clanarine (dict): Rečnik sa podacima o članarinama.
        korisnicko_ime (str): Korisničko ime člana čiji se status menja.
        novi_status (int): Novi status člana.
    """
    if korisnicko_ime in korisnici:
        dodaj_clanarinu(korisnici, clanarine, korisnicko_ime)
        korisnici[korisnicko_ime]['status'] = novi_status
        print(f"Status korisnika {korisnicko_ime} je uspešno promenjen.")
    else:
        print(f"Korisnik sa korisničkim imenom {korisnicko_ime} ne postoji.")


def aktivacija_clana(korisnici, clanarine):
    """
    Aktivira člana u sistemu promenom njegovog statusa.

    Args:
        korisnici (dict): Rečnik sa podacima o korisnicima.
        clanarine (dict): Rečnik sa podacima o članarinama.
    """
    korisnicko_ime = input('Unesite korisnicko ime člana za aktivaciju: ')
    promeni_status_clana(korisnici, clanarine, korisnicko_ime, 1)
