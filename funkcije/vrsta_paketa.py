from funkcije.fajlovi import citaj_fajl

def ucitaj_vrste_paketa(putanja):
    fajl = citaj_fajl(putanja)
    if fajl is None:
        return {}

    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id_vrste_paketa, naziv = red.split('|')
            podaci[id_vrste_paketa] = {
                'id': id_vrste_paketa,
                'naziv': naziv
            }

    return podaci


def promeni_paket(podaci, korisnicko_ime, novi_paket):
    if korisnicko_ime in podaci:
        podaci[korisnicko_ime]['uplaceni_paket'] = novi_paket
        print(f"Paket za korisnika {korisnicko_ime} je uspešno promenjen.")
    else:
        print(f"Korisnik sa korisničkim imenom '{korisnicko_ime}' ne postoji.")


def aktivacija_premium_paketa(podaci):
    korisnicko_ime = input('Unesite korisnicko ime clana za aktivaciju: ')
    promeni_paket(podaci, korisnicko_ime, 1)
