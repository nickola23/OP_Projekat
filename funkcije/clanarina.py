from funkcije.fajlovi import citajFajl, upisFajl
from datetime import datetime, timedelta

def ucitajClanarine(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, idKorisnika, datumUplate = red.split('|')
            podaci[id] = {
                'id': eval(id),
                'idKorisnika': idKorisnika,
                'datumUplate': datetime.strptime(datumUplate.strip(), '%d.%m.%Y').date().strftime('%d.%m.%Y'),
            }
            
    return podaci

def dodajClanarinu(korisnici, clanarine, korisnickoIme):
    if korisnickoIme not in korisnici:
        print(f"Korisnik sa korisničkim imenom {korisnickoIme} ne postoji.")
        return False

    if clanarine:
        noviId = max(map(int, clanarine.keys())) + 1
    else:
        noviId = 1
    
    datumUplate = datetime.now().strftime('%d.%m.%Y')

    clanarine[str(noviId)] = {
        'id': noviId,
        'idKorisnika': korisnickoIme,
        'datumUplate': datumUplate,
    }

    print(f"Uspešno dodata članarina za korisnika {korisnickoIme}.")
    return True

def validacijaClanarina(korisnici, clanarine):
    danasnjiDatum = datetime.now().date()

    for korisnickoIme, podaci in korisnici.items():
        aktivnaClanarina = None
        for clanarina in clanarine.values():
            if clanarina['idKorisnika'] == korisnickoIme:
                datumUplate = datetime.strptime(clanarina['datumUplate'], '%d.%m.%Y').date()
                if (datumUplate + timedelta(days=30)) >= danasnjiDatum:
                    aktivnaClanarina = True
                    break

        if not aktivnaClanarina:
            korisnici[korisnickoIme]['status'] = 0
            korisnici[korisnickoIme]['uplaceniPaket'] = 0

    return korisnici