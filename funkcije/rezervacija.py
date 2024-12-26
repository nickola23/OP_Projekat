from datetime import datetime, timedelta
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

    if pretraga:
        return pretraga
    else:
        print(f"Nema rezervacija za korisnika '{korisnickoIme}'.")
        return pretraga
    
def pretraziRezervacijeInstruktor(rezervacije, treninzi, termini, programi, korisnickoIme):
    pretraga = {}
    
    for podaci in rezervacije.values():
        idTermina = podaci['idTermina']
        trening = treninzi.get(termini.get(idTermina, {}).get('idTreninga', ''))
        if trening:
            idPrograma = trening.get('idPrograma')
            if idPrograma and programi.get(idPrograma, {}).get('idInstruktora') == korisnickoIme:
                pretraga[podaci['id']] = podaci

    if pretraga:
        return pretraga
    else:
        print(f"Nema rezervacija za instruktora '{korisnickoIme}'.")
        return pretraga

    
def pretraziRezervacije(rezervacije, termini, treninzi, korisnici):
    while True:
        print("Opcije pretrage rezervacija:\n1. ID treninga\n2. Ime člana\n3. Prezime člana\n4. Datumu rezervacije\n5. Vreme početka treninga\n6. Vreme kraja treninga\nb. Nazad")

        izbor = input("Izaberite opciju za pretragu: ")

        match izbor:
            case "1":
                idTreninga = input("Unesite ID treninga: ").strip()
                pretraga = {
                    idRezervacije: rezervacija
                    for idRezervacije, rezervacija in rezervacije.items()
                    if treninzi[termini[rezervacija['idTermina']]['idTreninga']]['id'] == idTreninga
                }

            case "2":
                ime = input("Unesite ime člana: ").strip().lower()
                pretraga = {
                    idRezervacije: rezervacija
                    for idRezervacije, rezervacija in rezervacije.items()
                    if any(korisnik['ime'].lower() == ime for korisnik in korisnici.values() if korisnik['korisnickoIme'] == rezervacija['idKorisnika'])
                }

            case "3":
                prezime = input("Unesite prezime člana: ").strip().lower()
                pretraga = {
                    idRezervacije: rezervacija
                    for idRezervacije, rezervacija in rezervacije.items()
                    if any(korisnik['prezime'].lower() == prezime for korisnik in korisnici.values() if korisnik['korisnickoIme'] == rezervacija['idKorisnika'])
                }

            case "4":
                datum = input("Unesite datum rezervacije: ").strip()
                try:
                    datetime.strptime(datum, '%d.%m.%Y')
                    pretraga = {
                        idRezervacije: rezervacija
                        for idRezervacije, rezervacija in rezervacije.items()
                        if rezervacija['datum'] == datum
                    }
                except Exception:
                    print("Uneli ste nevažeći datum. Pokušajte ponovo.")
                    continue

            case "5":
                vremePocetka = input("Unesite vreme početka treninga (hh:mm): ").strip()
                try:
                    pocetak = datetime.strptime(vremePocetka, '%H:%M').time()
                    pretraga = {
                        idRezervacije: rezervacija
                        for idRezervacije, rezervacija in rezervacije.items()
                        if treninzi[termini[rezervacija['idTermina']]['idTreninga']]['vremePocetka'] == pocetak
                    }
                except ValueError:
                    print("Uneli ste nevažeće vreme. Pokušajte ponovo.")
                    continue

            case "6":
                vreme_kraja = input("Unesite vreme kraja treninga (hh:mm): ").strip()
                try:
                    kraj = datetime.strptime(vreme_kraja, '%H:%M').time()
                    pretraga = {
                        idRezervacije: rezervacija
                        for idRezervacije, rezervacija in rezervacije.items()
                        if treninzi[termini[rezervacija['idTermina']]['idTreninga']]['vremeKraja'] == kraj
                    }
                except ValueError:
                    print("Uneli ste nevažeće vreme. Pokušajte ponovo.")
                    continue

            case "b":
                print("Izlaz iz pretrage.")
                break

            case _:
                print("Nevažeća opcija. Pokušajte ponovo.")
                continue

        if pretraga:
            print("Rezultati pretrage:")
            ispisTabele(pretraga)
        else:
            print("Nema rezultata za zadatu pretragu.")



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
                trenutniRed.append("X")         # Zauzeto mesto
            else:
                trenutniRed.append(mesto[0])    # Slobodno mesto
        matrica.append(trenutniRed)

    print(f"Raspored mesta za termin {idTermina}:")
    for i, red in enumerate(matrica, 1):
        print(f"Red {i}: {' '.join(red)}")
    
def rezervacijaMesta(rezervacije, termini, treninzi, programi, korisnici, korisnickoIme):
    sviRedovi = "ABCDEF"
    brojKolona = 6

    korisnik = korisnici.get(korisnickoIme)
    if korisnik['status'] != 1:
        print(f"{korisnik['korisnickoIme']} status je 'neaktivan'. Ne možete rezervisati mesta.")
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

        danTreninga = datetime.strptime(termin['datum'], '%d.%m.%Y').weekday()

        if danTreninga != 4 and program['potrebanPaket'] == 1 and korisnik['uplaceniPaket'] != 1: 
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
            print("Uneto mesto nije slobodno ili ne postoji. Pokusajte ponovo.")
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

def rezervacijaMestaInstruktor(rezervacije, termini, treninzi, programi, korisnici, korisnickoImeInstruktora):
    while True:
        terminiInstruktora = {
            idTermina: termin
            for idTermina, termin in termini.items()
            if programi[treninzi[termin['idTreninga']]['idPrograma']]['idInstruktora'] == korisnickoImeInstruktora
        }

        if not terminiInstruktora:
            print("Nemate termine za koje možete rezervisati mesta.")
            break

        korisnickoImeClana = input("Unesite korisničko ime člana za kojeg rezervišete mesto: ").strip()
        if korisnickoImeClana not in korisnici:
            print("Uneto korisničko ime člana ne postoji. Pokušajte ponovo.")
            continue

        rezervacijaMesta(rezervacije, terminiInstruktora, treninzi, programi, korisnici, korisnickoImeClana)
        break

def ponistiRezervaciju(rezervacije, termini):
    while True:
        print("Vaše trenutne rezervacije:")
    
        aktivneRezeracije = {
            idRezervacije: rezervacija
            for idRezervacije, rezervacija in rezervacije.items()
            if datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date() >= datetime.now().date()
        }

        if not aktivneRezeracije:
            print("Nemate aktivnih rezervacija za poništavanje.")
            break

        ispisTabele(aktivneRezeracije)

        idRezervacije = input("Unesite ID rezervacije koju želite da poništite: ")
        if idRezervacije not in aktivneRezeracije:
            print("Nevažeći ID rezervacije. Pokušajte ponovo.")
            continue

        del rezervacije[idRezervacije]
        print(f"Rezervacija {idRezervacije} je uspešno poništena.")

        nastavak = input("Da li želite da poništite još neku rezervaciju? (da/ne): ").lower()
        if nastavak != 'da':
            break

def ponistiRezervacijuInstruktor(rezervacije, termini, treninzi, programi, korisnici, korisnickoIme):
    while True:
        terminiInstruktora = {
                idTermina: termin
                for idTermina, termin in termini.items()
                if programi[treninzi[termin['idTreninga']]['idPrograma']]['idInstruktora'] == korisnickoIme
            }

        if not terminiInstruktora:
            print("Nemate termine za koje možete poništiti rezervaciju.")
            break

        aktivneRezeracije = {
            idRezervacije: rezervacija
            for idRezervacije, rezervacija in rezervacije.items()
            if datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date() >= datetime.now().date()
        }

        if not aktivneRezeracije:
            print("Nemate aktivnih rezervacija za poništavanje.")
            break

        ponistiRezervaciju(rezervacije, termini)
        break

def izmeniRezervacijuInstruktor(rezervacije, termini, treninzi, programi, korisnici, korisnickoImeInstruktora):
    while True:
        terminiInstruktora = {
            idTermina: termin
            for idTermina, termin in termini.items()
            if programi[treninzi[termin['idTreninga']]['idPrograma']]['idInstruktora'] == korisnickoImeInstruktora
        }

        if not terminiInstruktora:
            print("Nemate termine za koje možete menjati rezervacije.")
            break

        print("Dostupni termini za koje ste odgovorni:")
        ispisTabele(terminiInstruktora)
        idTermina = input("Unesite šifru termina treninga (b. za Nazad): ").strip()
        if idTermina == 'b':
            break
        elif idTermina not in terminiInstruktora:
            print("Uneti termin nije vaš. Pokušajte ponovo.")
            continue

        korisniciSaRezervacijama = {
            rezervacija['idKorisnika']
            for rezervacija in rezervacije.values()
            if rezervacija['idTermina'] == idTermina
        }

        if korisniciSaRezervacijama:
            print(f"Korisnici sa rezervacijama za termin {idTermina}:")
            print(", ".join(korisniciSaRezervacijama))
        else:
            print("Nema korisnika sa rezervacijama za ovaj termin.")
            continue

        korisnickoImeClana = input("Unesite korisničko ime člana: ").strip()
        if korisnickoImeClana not in korisnici:
            print("Uneto korisničko ime člana ne postoji. Pokušajte ponovo.")
            continue

        zauzetaMestaKorisnika = {
            rezervacija['oznakaRedaKolone']
            for rezervacija in rezervacije.values()
            if rezervacija['idTermina'] == idTermina and rezervacija['idKorisnika'] == korisnickoImeClana
        }

        if zauzetaMestaKorisnika:
            print(f"Korisnik {korisnickoImeClana} je rezervisao sledeća mesta za termin {idTermina}:")
            print(", ".join(zauzetaMestaKorisnika))
        else:
            print(f"Korisnik '{korisnickoImeClana}' nema rezervisana mesta za ovaj termin.")
            continue

        oznakaRedaKolone = input("Unesite oznaku mesta koje želite da izmenite: ").strip()
        rezervacijaZaIzmenu = None
        for rezervacija in rezervacije.values():
            if (
                rezervacija['idTermina'] == idTermina
                and rezervacija['idKorisnika'] == korisnickoImeClana
                and rezervacija['oznakaRedaKolone'] == oznakaRedaKolone
            ):
                rezervacijaZaIzmenu = rezervacija
                break

        if not rezervacijaZaIzmenu:
            print("Rezervacija nije pronađena. Pokušajte ponovo.")
            continue

        print(f"Pronađena rezervacija: ")
        ispisTabele({rezervacijaZaIzmenu['id']: rezervacijaZaIzmenu})
        print("Opcije izmene:\n1. Promena termina\n2. Promena korisnika\n3. Promena mesta\nb. Nazad")

        izbor = input("Unesite opciju za izmenu: ").strip()
        if izbor == "1":
            print("Dostupni termini za koje ste odgovorni:")
            ispisTabele(terminiInstruktora)

            noviIdTermina = input("Unesite novi termin: ").strip()
            if noviIdTermina not in terminiInstruktora:
                print("Novi termin nije validan za vas. Pokušajte ponovo.")
                continue
            rezervacijaZaIzmenu['idTermina'] = noviIdTermina
            print("Termin uspešno izmenjen.")
        elif izbor == "2":
            noviKorisnik = input("Unesite korisničko ime novog korisnika: ").strip()
            if noviKorisnik not in korisnici:
                print("Novi korisnik ne postoji. Pokušajte ponovo.")
                continue
            rezervacijaZaIzmenu['idKorisnika'] = noviKorisnik
            print("Korisnik uspešno izmenjen.")
        elif izbor == "3":
            print("Dostupna mesta za dati termin:")
            prikazMestaUMatrici(idTermina, rezervacije)

            novaOznaka = input("Unesite novu oznaku mesta: ").strip()
            zauzetaMesta = {
                rezervacija['oznakaRedaKolone']
                for rezervacija in rezervacije.values()
                if rezervacija['idTermina'] == idTermina
            }
            if novaOznaka in zauzetaMesta:
                print("Novo mesto je već zauzeto. Pokušajte ponovo.")
                continue
            rezervacijaZaIzmenu['oznakaRedaKolone'] = novaOznaka
            print("Mesto uspešno izmenjeno.")
        elif izbor == "b":
            break
        else:
            print("Pogresan unos. Pokušajte ponovo.")
            continue

        nastavak = input("Da li želite da izmenite još neku rezervaciju? (da/ne): ").strip().lower()
        if nastavak != "da":
            break

def mesecnaNagradaLojalnosti(rezervacije, korisnici):
    danas = datetime.now().date()
    prosliMesec = danas - timedelta(days=30)
    
    mesecneRezervacije = {}
    for rezervacija in rezervacije.values():
        datumRezervacije = datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date()
        if datumRezervacije > prosliMesec:
            idKorisnika = rezervacija['idKorisnika']
            if idKorisnika not in mesecneRezervacije:
                mesecneRezervacije[idKorisnika] = []
            mesecneRezervacije[idKorisnika].append(rezervacija)
    
    for idKorisnika, rezervacijeKorisnika in mesecneRezervacije.items():
        if len(rezervacijeKorisnika) > 27:
            korisnik = korisnici.get(idKorisnika)
            if korisnik:
                korisnik['status'] = 1
                korisnik['uplaceniPaket'] = 1
    
    print("Raspodela mesečnih nagrada lojalnosti je završena.")