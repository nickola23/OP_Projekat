"""
Modul za upravljanje clanarinama.

Sadrži funkcije za ucitavanje,
dodavanje i validaciju clanarine.
"""
from datetime import datetime, timedelta
from funkcije.fajlovi import citaj_fajl

def ucitaj_clanarine(putanja):
    """
    Ucitava clanarine iz .txt fajla

    Args:
        putanja (string): putanja do .txt fajla.

    Returns:
        dict: sve clanarine
    """
    fajl = citaj_fajl(putanja)
    if fajl is None:
        return {}

    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id_clanarine, id_korisnika, datum_uplate = red.split('|')
            podaci[id_clanarine] = {
                'id': int(id_clanarine),
                'id_korisnika': id_korisnika,
                'datum_uplate': datetime.strptime(datum_uplate.strip(), '%d.%m.%Y').date().strftime('%d.%m.%Y'),
            }

    return podaci


def dodaj_clanarinu(korisnici, clanarine, korisnicko_ime):
    """
    Dodaje clanarinu u recnik

    Args:
        korisnici (dict): trenutni recnik korisnika,
        clanarine (dict): trenutni recnik clanarina,
        korisnicko_ime (string): ime korisnika kome se dodaje clanarina.

    Returns:
        boolean: da li je uspesno izvrseno
    """
    if korisnicko_ime not in korisnici:
        print(f"Korisnik sa korisničkim imenom {korisnicko_ime} ne postoji.")
        return False

    if clanarine:
        novi_id = max(map(int, clanarine.keys())) + 1
    else:
        novi_id = 1

    datum_uplate = datetime.now().strftime('%d.%m.%Y')

    clanarine[str(novi_id)] = {
        'id': novi_id,
        'id_korisnika': korisnicko_ime,
        'datum_uplate': datum_uplate,
    }

    print(f"Uspešno dodata članarina za korisnika {korisnicko_ime}.")
    return True


def validacija_clanarina(korisnici, clanarine):
    """
    Proverava da li su clanarine istekle i ako jesu menja status i uplaceni_paket korisniku

    Args:
        korisnici (dict): trenutni recnik korisnika,
        clanarine (dict): trenutni recnik clanarina.

    Returns:
        dict: novi recnik korisnika
    """
    danasnji_datum = datetime.now().date()

    for korisnicko_ime in korisnici.keys():
        aktivna_clanarina = None
        for clanarina in clanarine.values():
            if clanarina['id_korisnika'] == korisnicko_ime:
                datum_uplate = datetime.strptime(clanarina['datum_uplate'], '%d.%m.%Y').date()
                if (datum_uplate + timedelta(days=30)) >= danasnji_datum:
                    aktivna_clanarina = True
                    break

        if not aktivna_clanarina:
            korisnici[korisnicko_ime]['status'] = 0
            korisnici[korisnicko_ime]['uplaceni_paket'] = 0

    return korisnici
