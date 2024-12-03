from datetime import datetime

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