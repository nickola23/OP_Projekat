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
                'id': id,
                'naziv': naziv
            }
            
    return podaci

def promeniPaket(podaci, korisnicko_ime, noviPaket):
    if korisnicko_ime in podaci:
        podaci[korisnicko_ime]['uplaceniPaket'] = noviPaket
        print(f"Paket za korisnika {korisnicko_ime} je uspešno promenjen.")
    else:
        print(f"Korisnik sa korisničkim imenom '{korisnicko_ime}' ne postoji.")

def aktivacijaPremiumPaketa(podaci):
    korisnicko_ime = input('Unesite korisnicko ime clana za aktivaciju: ')
    promeniPaket(podaci, korisnicko_ime, 1)
