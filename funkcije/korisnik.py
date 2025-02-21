"""
Modul za upravljanje korisnicima.

Sadrži funkcije za ucitavanje,
dodavanje, prijavu, registraciju i odjavu korisnika. 
"""
from datetime import datetime
import re
from funkcije.fajlovi import ucitaj_podatke

def ucitaj_korisnike(putanja):
    """
    Učitava podatke korisnika iz fajla.

    Args:
        putanja (str): Putanja do .txt fajla.

    Returns:
        dict: Rečnik sa podacima o korinicima.
    """
    kljucevi = ['korisnicko_ime', 'lozinka', 'ime', 'prezime', 'uloga',
                'status', 'uplaceni_paket', 'datum_registracije']
    podaci = ucitaj_podatke(putanja, kljucevi)

    # Dodatna obrada podataka
    for korisnik in podaci.values():
        korisnik['uloga'] = int(korisnik['uloga'])
        korisnik['status'] = int(korisnik['status'])
        korisnik['uplaceni_paket'] = int(korisnik['uplaceni_paket'])
        korisnik['datum_registracije']=(datetime.strptime(korisnik['datum_registracije'],"%d.%m.%Y")
                                                  .date().strftime('%d.%m.%Y'))

    return podaci


def dodaj_korisnika(korisnici):
    """
    Dodaje novog korisnika u sistem.

    Args:
        korisnici (dict): Rečnik sa korisnicima.

    Returns:
        bool: Vraća True ako je korisnik uspešno dodat.
    """
    while True:
        korisnicko_ime = input('Unesite korisnicko ime: ')
        if korisnicko_ime not in korisnici.keys():
            while True:
                lozinka = input('Unesite lozinku (barem 6 karaktera i 1 cifra): ').strip()
                if len(lozinka) < 6 or not re.search(r'\d', lozinka):
                    print('Lozinka nije validna. Pokušajte ponovo.')
                else:
                    break
            ime = input('Unesite ime: ')
            prezime = input('Unesite prezime: ')
            korisnici[korisnicko_ime] = {
                'korisnicko_ime': korisnicko_ime,
                'lozinka': lozinka,
                'ime': ime,
                'prezime': prezime,
                'uloga': 0,                 #registrovan, instruktor, admin - 0, 1, 2
                'status': 0,                #neaktivan, aktivan - 0, 1
                'uplaceni_paket': 0,        #standard, premium  - 0, 1
                'datum_registracije': datetime.now().date().strftime('%d.%m.%Y'),
            }

            return True
        print('Korisnicko ime je vec zauzeto.')
        continue


def registracija_instruktora(korisnici):
    """
    Dodaje novog instruktora u sistem.

    Args:
        korisnici (dict): Rečnik sa korisnicima.

    Returns:
        bool: Vraća True ako je instruktor uspešno registrovan.
    """
    while True:
        korisnicko_ime = input('Unesite korisnicko ime instruktora: ')
        if korisnicko_ime not in korisnici.keys():
            while True:
                lozinka = input('Unesite lozinku (barem 6 karaktera i 1 cifra): ').strip()
                if len(lozinka) < 6 or not re.search(r'\d', lozinka):
                    print('Lozinka nije validna. Pokušajte ponovo.')
                else:
                    break
            ime = input('Unesite ime: ')
            prezime = input('Unesite prezime: ')
            while True:
                try:
                    uloga = input('1. Instruktor\n2. Admin\nUnesite ulogu: ').strip()
                    match uloga:
                        case '1' | '2':
                            break
                        case _:
                            print('Pogrešan unos. Unesite broj 1 ili 2.')
                            continue
                except ValueError:
                    print("Greška prilikom unosa")

            korisnici[korisnicko_ime] = {
                'korisnicko_ime': korisnicko_ime,
                'lozinka': lozinka,
                'ime': ime,
                'prezime': prezime,
                'uloga': uloga,
                'status': 0,                
                'uplaceni_paket': 0,         
                'datum_registracije': datetime.now().date().strftime('%d.%m.%Y'),
            }
            print(f'Uspesno ste registrovali korisnika {korisnicko_ime}')
            return True
        print('Korisnicko ime je vec zauzeto.')
        continue


def prijava(korisnici, trenutni_korisnik):
    """
    Funkcija za prijavu korisnika.

    Args:
        korisnici (dict): Rečnik sa korisnicima.
        trenutni_korisnik (dict): Trenutno prijavljeni korisnik.

    Returns:
        dict: Podaci o korisniku koji je uspešno prijavljen.
    """
    if not trenutni_korisnik:
        while True:
            korisnicko_ime = input('Unesite korisnicko ime: ')
            if korisnicko_ime in korisnici.keys():
                lozinka = input('Unesite lozinku: ')
                if lozinka == korisnici[korisnicko_ime]['lozinka']:
                    print('Uspesna prijava.')
                    return korisnici[korisnicko_ime]
                print('Pogresna lozinka.')
                continue
            print('Korisnicko ime ne postoji.')
            continue
    print("Već ste prijavljeni.")
    return trenutni_korisnik


def registracija(korisnici):
    """
    Funkcija za registraciju korisnika.

    Args:
        korisnici (dict): Rečnik sa postojećim korisnicima.

    Returns:
        dict: Podaci o korisniku koji se uspešno registrovao i prijavio.
    """
    while True:
        if dodaj_korisnika(korisnici):
            print('Uspesna registracija. Sada se mozete prijaviti.')
            return prijava(korisnici, None)
        print('Neuspesna registracija.')
        continue


def odjava():
    """
    Funkcija za odjavu korisnika. Ispisuje poruku o uspešnoj odjavi.

    Returns:
        None
    """
    print('Odjava uspesna.')
