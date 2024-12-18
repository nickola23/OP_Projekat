from datetime import datetime
from funkcije.fajlovi import citajFajl, upisFajl
from funkcije.tabela import ispisTabele

def ucitajRezervacije(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, idKorisnika, idTermina, oznakaRedaKolone, datum = red.split('|')
            podaci[id] = {
                'id': id,
                'idKorisnika': idKorisnika,
                'idTermina': idTermina,
                'oznakaRedaKolone': oznakaRedaKolone,
                'datum': datetime.strptime(datum.strip(), '%d.%m.%Y').date().strftime('%d.%m.%Y'),
            }
    
    return podaci

def pretraziRezervacijeKorisnik(rezervacije, korisnickoIme):
    pretraga = {}
    if korisnickoIme:
        for podaci in rezervacije.values():
            if podaci['idKorisnika'] == korisnickoIme:
                pretraga[podaci['id']] = podaci

    if podaci:
        return pretraga
    else:
        print(f"Nema rezervacija za korisnika '{korisnickoIme}'.")
        return pretraga