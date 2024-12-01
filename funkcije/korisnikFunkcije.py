from datetime import datetime
from funkcije.fajloviFunkcije import citajFajl, upisFajl

korisnici = {}
putanja = './data/Korisnici.txt'

def zavrsi(putanja, podaci):
    upisFajl(putanja, podaci)

def ucitajKorisnike(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            korisnickoIme = red.split('|')[0]
            podaci[korisnickoIme] = {
                'korisnickoIme': korisnickoIme,
                'lozinka': red.split('|')[1],
                'ime': red.split('|')[2],
                'prezime': red.split('|')[3],
                'uloga': eval(red.split('|')[4]),
                'status': eval(red.split('|')[5]),
                'uplaceniPaket': eval(red.split('|')[6]),
                'datumRegistracije': datetime.strptime(red.split('|')[7], "%d.%m.%Y").date().strftime('%d.%m.%Y'),
            }
            
    return podaci

korisnici = ucitajKorisnike(putanja)

def dodajKorisnika(korisnickoIme):
    if korisnickoIme not in korisnici.keys():
        lozinka = input('Unesite lozinku: ')
        ime = input('Unesite ime: ')
        prezime = input('Unesite prezime: ')
        korisnici[korisnickoIme] = {
            'korisnickoIme': korisnickoIme,
            'lozinka': lozinka,
            'ime': ime,
            'prezime': prezime,
            'uloga': 0,
            'status': 0,
            'uplaceniPaket': 0,
            'datumRegistracije': datetime.now().date().strftime('%d.%m.%Y'),
        } 

        return True
    else:
        print('Korisnicko ime je vec zauzeto.')
        return  False

def prijava():
    korisnickoIme = input('Unesite korisnicko ime: ')

    if korisnickoIme in korisnici.keys():
        lozinka = input('Unesite lozinku: ')
        if lozinka == korisnici[korisnickoIme]['lozinka']:
            print('Uspesna prijava.')
            return True
        else:
            print('Pogresna lozinka.')
            return False
    else:   
        print('Korisnicko ime ne postoji.')
        return False

def registracija():
    korisnickoIme = input('Unesite korisnicko ime: ')

    if dodajKorisnika(korisnickoIme):
        print('Uspesna registracija.')
        zavrsi(putanja, korisnici)    #ukloniti kasnije sada sluzi za upis u fajl
        return True
    else: 
        print('Neuspesna registracija.')
        return False
    
    