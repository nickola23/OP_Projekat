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

def dodajKorisnika():
    korisnickoIme = input('Unesite korisnicko ime: ')

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
    while True:
        korisnickoIme = input('Unesite korisnicko ime: ')

        if korisnickoIme in korisnici.keys():
            lozinka = input('Unesite lozinku: ')
            if lozinka == korisnici[korisnickoIme]['lozinka']:
                print('Uspesna prijava.')
                break
            else:
                print('Pogresna lozinka.')
                continue
        else:   
            print('Korisnicko ime ne postoji.')
            continue
    return True

def registracija():
    while True:
        if dodajKorisnika():
            print('Uspesna registracija.')
            zavrsi(putanja, korisnici)    #ukloniti kasnije sada sluzi za upis u fajl
            break
        else: 
            print('Neuspesna registracija.')
            continue
    return True
    
    