from funkcije.fajlovi import citajFajl, upisFajl

def ucitajVrstePaketa(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, naziv = red.split('|')
            podaci[id] = {
                'id': eval(id),
                'naziv': naziv
            }
            
    return podaci

def promeniPaket(podaci, korisnickoIme, noviPaket):
    if korisnickoIme in podaci:
        podaci[korisnickoIme]['uplaceniPaket'] = noviPaket
        print(f"Paket za korisnika '{korisnickoIme}' je uspešno promenjen.")
    else:
        print(f"Korisnik sa korisničkim imenom '{korisnickoIme}' ne postoji.")
