from datetime import datetime
import re
from funkcije.fajlovi import citajFajl, upisFajl

def ucitajKorisnike(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            korisnickoIme, lozinka, ime, prezime, uloga, status, uplaceniPaket, datumRegistracije = red.split('|')
            podaci[korisnickoIme] = {
                'korisnickoIme': korisnickoIme,
                'lozinka': lozinka,
                'ime': ime,
                'prezime': prezime,
                'uloga': eval(uloga),
                'status': eval(status),
                'uplaceniPaket': eval(uplaceniPaket),
                'datumRegistracije': datetime.strptime(datumRegistracije, "%d.%m.%Y").date().strftime('%d.%m.%Y'),
            }
            
    return podaci

def dodajKorisnika(korisnici):
    while True:
        korisnickoIme = input('Unesite korisnicko ime: ')
        if korisnickoIme not in korisnici.keys():
            while True:
                lozinka = input('Unesite lozinku (barem 6 karaktera i 1 cifra): ').strip()
                if len(lozinka) < 6 or not re.search(r'\d', lozinka):
                    print('Greška: Lozinka nije validna. Pokušajte ponovo.')
                else:
                    break
            ime = input('Unesite ime: ')
            prezime = input('Unesite prezime: ')
            korisnici[korisnickoIme] = {
                'korisnickoIme': korisnickoIme,
                'lozinka': lozinka,
                'ime': ime,
                'prezime': prezime,
                'uloga': 0,                 #registrovan, instruktor, admin - 0, 1, 2
                'status': 0,                #neaktivan, aktivan - 0, 1
                'uplaceniPaket': 0,         #standard, premium  - 0, 1
                'datumRegistracije': datetime.now().date().strftime('%d.%m.%Y'),
            } 

            return True
        else:
            print('Korisnicko ime je vec zauzeto.')
            continue

def prijava(korisnici, trenutniKorisnik):
    if not trenutniKorisnik:
        while True:
            korisnickoIme = input('Unesite korisnicko ime: ')
            if korisnickoIme in korisnici.keys():
                lozinka = input('Unesite lozinku: ')
                if lozinka == korisnici[korisnickoIme]['lozinka']:
                    print('Uspesna prijava.')
                    return korisnici[korisnickoIme]
                else:
                    print('Pogresna lozinka.')
                    continue
            else:   
                print('Korisnicko ime ne postoji.')
                continue
    else:
        print("Već ste prijavljeni.")
        return trenutniKorisnik

def registracija(korisnici):
    while True:
        if dodajKorisnika(korisnici):
            print('Uspesna registracija. Sada se mozete prijaviti.')
            return prijava(korisnici, None)
        else: 
            print('Neuspesna registracija.')
            continue
    
def odjava():
    print('Odjava uspesna.')
    return None