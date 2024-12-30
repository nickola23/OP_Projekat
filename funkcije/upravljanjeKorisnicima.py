from datetime import datetime
from funkcije.clanarina import dodajClanarinu

def dodajInstruktora(korisnici):
    while True:
        korisnickoIme = input("Unesite korisnicko ime: ")
        if korisnickoIme not in korisnici.keys():
            lozinka = input("Unesite lozinku: ")
            ime = input("Unesite ime: ")
            prezime = input("Unesite prezime: ")
            uloga = input("Izaberite jednu od uloga:\n0. Instruktor\n1. Administrator\nUnesite ulogu:")

            korisnici[korisnickoIme] = {
                'korisnickoIme': korisnickoIme,
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
        
def promeniStatusClana(korisnici, clanarine, korisnickoIme, noviStatus):
    if korisnickoIme in korisnici:
        dodajClanarinu(korisnici, clanarine, korisnickoIme)
        korisnici[korisnickoIme]['status'] = noviStatus
        print(f"Status korisnika {korisnickoIme} je uspešno promenjen.")
    else:
        print(f"Korisnik sa korisničkim imenom {korisnickoIme} ne postoji.")

def aktivacijaClana(korisnici, clanarine):
    korisnickoIme = input('Unesite korisnicko ime clana za aktivaciju: ')
    promeniStatusClana(korisnici, clanarine, korisnickoIme, 1)
