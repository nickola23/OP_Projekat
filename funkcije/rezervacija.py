from datetime import datetime
from funkcije.fajlovi import citajFajl, upisFajl
from funkcije.tabela import ispisTabele
from funkcije.zaIspis import rezervacijeZaIspis
from funkcije.termin import spojiTermine

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

def prikazMestaUMatrici(idTermina, rezervacije): 
    sviRedovi = "ABCDEF"
    brojKolona = 6
    svaMesta = {f"{red}{kolona}" for kolona in range(1, brojKolona + 1) for red in sviRedovi}

    zauzetaMesta = {rezervacija['oznakaRedaKolone'] for rezervacija in rezervacije.values() if rezervacija['idTermina'] == idTermina}

    matrica = []
    for kolona in range(1, brojKolona + 1):
        trenutniRed = []
        for red in sviRedovi:
            mesto = f"{red}{kolona}"
            if mesto in zauzetaMesta:
                trenutniRed.append("X")  # Zauzeto mesto
            else:
                trenutniRed.append(mesto[0])  # Slobodno mesto
        matrica.append(trenutniRed)

    print(f"Raspored mesta za termin {idTermina}:")
    for i, red in enumerate(matrica, 1):
        print(f"Red {i}: {' '.join(red)}")
    
def rezervacijaMesta(rezervacije, termini, treninzi, programi, korisnici, korisnickoIme):
    sviRedovi = "ABCDEF"
    brojKolona = 6

    korisnik = korisnici.get(korisnickoIme)
    if korisnik['status'] != 1:
        print("Vaš status aktivnosti je 'neaktivan'. Ne možete rezervisati mesta.")
        return

    while True:
        print("Dostupni termini:")
        ispisTabele(spojiTermine(treninzi, termini))
        
        idTermina = input("Unesite ID željenog termina: ")
        if idTermina not in termini:
            print("Uneti termin ne postoji. Pokušajte ponovo.")
            continue
        
        termin = termini[idTermina]
        trening = treninzi.get(termin['idTreninga'])
        if not trening:
            print("Trening za izabrani termin nije pronađen.")
            continue
        
        program = programi.get(trening['idPrograma'])
        if not program:
            print("Program za izabrani trening nije pronađen.")
            continue

        if program['potrebanPaket'] == 1 and korisnik['uplaceniPaket'] != 1:
            print("Ovaj program zahteva premium članstvo. Ne možete rezervisati mesto.")
            continue
        
        zauzetaMesta = {rezervacija['oznakaRedaKolone'] for rezervacija in rezervacije.values() if rezervacija['idTermina'] == idTermina}
        slobodnaMesta = {f"{red}{kolona}" for kolona in range(1, brojKolona + 1) for red in sviRedovi} - zauzetaMesta

        if not slobodnaMesta:
            print("Nema slobodnih mesta za izabrani termin.")
            continue

        prikazMestaUMatrici(idTermina, rezervacije)

        oznakaRedaKolone = input("Unesite oznaku reda i kolone željenog mesta (npr. A1): ")
        if oznakaRedaKolone not in slobodnaMesta:
            print("Uneto mesto nije slobodno ili ne postoji. Pokušajte ponovo.")
            continue

        noviID = str(len(rezervacije) + 1)
        datum = datetime.now().strftime('%d.%m.%Y')
        rezervacije[noviID] = {
            'id': noviID,
            'idKorisnika': korisnickoIme,
            'idTermina': idTermina,
            'oznakaRedaKolone': oznakaRedaKolone,
            'datum': datum,
        }
        print(f"Uspešno rezervisano mesto {oznakaRedaKolone} za termin {idTermina}.")

        nastavak = input("Da li želite da rezervišete još mesta? (da/ne): ").lower()
        if nastavak != 'da':
            break

def ponistiRezervaciju(rezervacije, termini):
    while True:
        print("Vaše trenutne rezervacije:")
    
        aktivne_rezervacije = {
            idRezervacije: rezervacija
            for idRezervacije, rezervacija in rezervacije.items()
            if datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date() >= datetime.now().date()
        }

        if not aktivne_rezervacije:
            print("Nemate aktivnih rezervacija za poništavanje.")
            break

        ispisTabele(aktivne_rezervacije)

        idRezervacije = input("Unesite ID rezervacije koju želite da poništite: ")
        if idRezervacije not in aktivne_rezervacije:
            print("Nevažeći ID rezervacije. Pokušajte ponovo.")
            continue

        del rezervacije[idRezervacije]
        print(f"Rezervacija {idRezervacije} je uspešno poništena.")

        nastavak = input("Da li želite da poništite još neku rezervaciju? (da/ne): ").lower()
        if nastavak != 'da':
            break
