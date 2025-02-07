from datetime import datetime
from funkcije.clanarina import dodaj_clanarinu

def dodajInstruktora(korisnici):
    while True:
        korisnicko_ime = input("Unesite korisnicko ime: ")
        if korisnicko_ime not in korisnici.keys():
            lozinka = input("Unesite lozinku: ")
            ime = input("Unesite ime: ")
            prezime = input("Unesite prezime: ")
            uloga = input("Izaberite jednu od uloga:\n0. Instruktor\n1. Administrator\nUnesite ulogu:")

            korisnici[korisnicko_ime] = {
                'korisnicko_ime': korisnicko_ime,
                'lozinka': lozinka,
                'ime': ime,
                'prezime': prezime,
                'uloga': eval(uloga),
                'status': 0,
                'uplaceniPaket': 0,
                'datumRegistracije': datetime.now().date().strftime('%d.%m.%Y'),
            }

            print("Uspesno ste dodali instruktora.")
            return True
        
def promeniStatusClana(korisnici, clanarine, korisnicko_ime, noviStatus):
    if korisnicko_ime in korisnici:
        dodaj_clanarinu(korisnici, clanarine, korisnicko_ime)
        korisnici[korisnicko_ime]['status'] = noviStatus
        print(f"Status korisnika {korisnicko_ime} je uspešno promenjen.")
    else:
        print(f"Korisnik sa korisničkim imenom {korisnicko_ime} ne postoji.")

def aktivacijaClana(korisnici, clanarine):
    korisnicko_ime = input('Unesite korisnicko ime clana za aktivaciju: ')
    promeniStatusClana(korisnici, clanarine, korisnicko_ime, 1)
