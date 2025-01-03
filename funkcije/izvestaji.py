from datetime import datetime, date, time, timedelta
from funkcije.tabela import maxDuzina
from funkcije.tabela import ispisTabele
from funkcije.kratakIspis import ispisKorisnika

def sacuvajIzvestaj(podaci, nazivFajla):
    while True:
        opcija = input("Da li želite da sačuvate podatke u tekstualni fajl? (da/ne): ").strip().lower()
        
        if opcija == "da":
            try:
                with open(nazivFajla, "w", encoding="utf-8") as fajl:
                    if not podaci:
                        fajl.write("Nema podataka za čuvanje.\n")
                        break
                    
                    zaglavlje = linija = vrednosti = ''
                    duzine = maxDuzina(podaci)

                    for kljuc in duzine.keys():
                        zaglavlje += " | " + f"{kljuc:<{duzine[kljuc]}}"
                        linija += "-+-" + "-" * duzine[kljuc]

                    fajl.write(zaglavlje + "\n")
                    fajl.write(linija + "\n")

                    for red in podaci.values():
                        for kljuc in duzine.keys():
                            if isinstance(red[kljuc], list):
                                spojeni_podaci = ", ".join(map(str, red[kljuc]))
                                vrednosti += " | " + f"{spojeni_podaci.capitalize():<{duzine[kljuc]}}"
                            elif isinstance(red[kljuc], time):
                                vrednosti += " | " + f"{str(red[kljuc].strftime('%H:%M')):<{duzine[kljuc]}}"
                            else:
                                vrednosti += " | " + f"{str(red[kljuc]):<{duzine[kljuc]}}"
                        vrednosti += '\n'
                    fajl.write(vrednosti)

                print(f"Podaci su uspešno sačuvani u fajl: {nazivFajla}")
                break
            except Exception as e:
                print(f"Došlo je do greške prilikom čuvanja podataka: {e}")
                break
        elif opcija == "ne":
            print("Podaci nisu sačuvani u fajl.")
            break
        else:
            print("Neispravan unos. Pokusajte ponovo.")
            continue

def izvestajA(rezervacije):
    while True:
        odabraniDatum = input("Unesite datum rezervacije: ").strip()
        pretraga = {}
        try:
            datum = datetime.strptime(odabraniDatum, '%d.%m.%Y').date()
        except ValueError:
            print("Neispravan format datuma. Pokušajte ponovo.")
            continue
        for idx, rezervacija in enumerate(rezervacije.values(), start=1):
            if rezervacija['datum'] == odabraniDatum:
                pretraga[idx] = {
                    'ID Rezervacije': rezervacija['id'],
                    'Korisnicko ime': rezervacija['idKorisnika'],
                    'ID Termina': rezervacija['idTermina'],
                    'Oznaka Mesta': rezervacija['oznakaRedaKolone'],
                    'Datum': rezervacija['datum']
                }
        ispisTabele(pretraga)
        sacuvajIzvestaj(pretraga, 'izvestaji/izvestajA.txt')
        return pretraga

def izvestajB(rezervacije, termini):
    while True:
        odabraniDatum = input("Unesite datum termina treninga: ").strip()
        try:
            datum = datetime.strptime(odabraniDatum, '%d.%m.%Y').date()
        except ValueError:
            print("Neispravan format datuma. Pokušajte ponovo.")
            continue

        terminiZaDatum = {id: termin for id, termin in termini.items() if datetime.strptime(termin['datum'], '%d.%m.%Y').date() == datum}

        if not terminiZaDatum:
            return {}

        pretraga = {}
        for idRezervacije, rezervacija in rezervacije.items():
            if rezervacija['idTermina'] in terminiZaDatum:
                pretraga[idRezervacije] = {
                    'ID Rezervacije': idRezervacije,
                    'Korisnicko ime': rezervacija['idKorisnika'],
                    'ID Termina': rezervacija['idTermina'],
                    'Oznaka Mesta': rezervacija['oznakaRedaKolone'],
                    'Datum': rezervacija['datum'],
                }

        ispisTabele(pretraga)
        sacuvajIzvestaj(pretraga, 'izvestaji/izvestajB.txt')
        return pretraga

def izvestajC(rezervacije, korisnici, programi, termini, treninzi):
    while True:
        odabraniDatum = input("Unesite datum rezervacije: ").strip()
        try:
            datum = datetime.strptime(odabraniDatum, '%d.%m.%Y').date()
        except ValueError:
            print("Neispravan format datuma. Pokušajte ponovo.")
            continue
        
        while True:
            print('Opcije za instruktore:')
            ispisKorisnika(korisnici, 1)

            odabraniInstruktor = input("Unesite korisnicko ime instruktora: ").strip()
            if odabraniInstruktor not in korisnici:
                print("Ne postoji instruktor sa datim korisnickim imenom. Pokušajte ponovo.")
                continue
            else: break

        pretraga = {}
        for idx, rezervacija in enumerate(rezervacije.values(), start=1):
            idTermina = rezervacija['idTermina']
            idTreninga = termini[idTermina]['idTreninga']
            idInstruktora = programi[treninzi[idTreninga]['idPrograma']]['idInstruktora']

            if rezervacija['datum'] == odabraniDatum and idInstruktora.lower() == odabraniInstruktor.lower():
                pretraga[idx] = {
                    'ID Rezervacije': rezervacija['id'],
                    'Korisnicko ime': rezervacija['idKorisnika'],
                    'ID Termina': idTermina,
                    'Instruktor': idInstruktora,
                    'Oznaka Mesta': rezervacija['oznakaRedaKolone'],
                    'Datum': rezervacija['datum']
                }

                if not pretraga:
                    print("Nema rezervacija za odabrani datum i instruktora.")
                    continue

        ispisTabele(pretraga)
        sacuvajIzvestaj(pretraga, 'izvestaji/izvestajC.txt')
        return pretraga
    
def izvestajD(rezervacije):
    while True:
        validniDani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja']
        odabraniDan = input("Unesite dan u nedelji (npr. ponedeljak): ").strip().lower()
        engleskiUDani = {
            'monday': 'ponedeljak',
            'tuesday': 'utorak',
            'wednesday': 'sreda',
            'thursday': 'cetvrtak',
            'friday': 'petak',
            'saturday': 'subota',
            'sunday': 'nedelja'
        }

        if odabraniDan not in validniDani:
            print("Neispravan unos. Pokušajte ponovo.")
            continue

        pretraga = {}
        brojac = 0
        for idx, rezervacija in enumerate(rezervacije.values(), start=1):
            datum = datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date()
            danUNedeljiEngleski = datum.strftime('%A').lower()
            danUNedeljiSrpski = engleskiUDani[danUNedeljiEngleski]

            if danUNedeljiSrpski == odabraniDan:
                brojac += 1
                pretraga[idx] = {
                    'ID Rezervacije': rezervacija['id'],
                    'Korisnicko ime': rezervacija['idKorisnika'],
                    'ID Termina': rezervacija['idTermina'],
                    'Oznaka Mesta': rezervacija['oznakaRedaKolone'],
                    'Datum': rezervacija['datum']
                }

        print(f"Ukupan broj rezervacija za {odabraniDan} je: {brojac}. To su:")
        ispisTabele(pretraga)
        sacuvajIzvestaj(pretraga, 'izvestaji/izvestajD.txt')
        return pretraga

def izvestajE(rezervacije, termini, treninzi, programi):
    danasnjiDatum = datetime.now().date()
    poslednjih30Dana = danasnjiDatum - timedelta(days=30)
    brojRezervacijaPoInstruktoru = {}

    for rezervacija in rezervacije.values():
        datumRezervacije = datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date()
        if datumRezervacije >= poslednjih30Dana:
            idTermina = rezervacija['idTermina']
            if idTermina in termini:
                idTreninga = termini[idTermina]['idTreninga']
                if idTreninga in treninzi:
                    idPrograma = treninzi[idTreninga]['idPrograma']
                    if idPrograma in programi:
                        idInstruktora = programi[idPrograma]['idInstruktora']
                        if idInstruktora not in brojRezervacijaPoInstruktoru:
                            brojRezervacijaPoInstruktoru[idInstruktora] = 0
                        brojRezervacijaPoInstruktoru[idInstruktora] += 1

    sortiraniInstruktori = sorted(
        brojRezervacijaPoInstruktoru.items(), 
        key=lambda x: x[1], 
        reverse=True
    )

    pretraga = {}
    for id, (instruktor, brojRezervacija) in enumerate(sortiraniInstruktori, start=1):
        pretraga[id] = {
            'Instruktor': instruktor,
            'Broj rezervacija': brojRezervacija
        }

    ispisTabele(pretraga)
    sacuvajIzvestaj(pretraga, 'izvestaji/izvestajE.txt')
    return pretraga

def izvestajF(rezervacije, termini, treninzi, programi):
    danasnjiDatum = datetime.now().date()
    poslednjih30Dana = danasnjiDatum - timedelta(days=30)

    premiumRezervacije = 0
    standardRezervacije = 0

    for rezervacija in rezervacije.values():
        datumRezervacije = datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date()
        if datumRezervacije >= poslednjih30Dana:
            idTermina = rezervacija['idTermina']
            if idTermina in termini:
                idTreninga = termini[idTermina]['idTreninga']
                if idTreninga in treninzi:
                    idPrograma = treninzi[idTreninga]['idPrograma']
                    if idPrograma in programi:
                        potrebanPaket = programi[idPrograma]['potrebanPaket']
                        if potrebanPaket == 1:
                            premiumRezervacije += 1
                        elif potrebanPaket == 0:
                            standardRezervacije += 1

    pretraga = {
        1: {'Tip paketa': 'Premium', 'Broj rezervacija': premiumRezervacije},
        2: {'Tip paketa': 'Standard', 'Broj rezervacija': standardRezervacije},
    }

    ispisTabele(pretraga)
    sacuvajIzvestaj(pretraga, 'izvestaji/izvestajF.txt')
    return pretraga

def izvestajG(rezervacije, termini, treninzi, programi):
    danasnjiDatum = datetime.now().date()
    poslednjihGodinuDana = danasnjiDatum - timedelta(days=365)

    popularnostPrograma = {}

    for rezervacija in rezervacije.values():
        datumRezervacije = datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date()
        if datumRezervacije >= poslednjihGodinuDana:
            idTermina = rezervacija['idTermina']
            if idTermina in termini:
                idTreninga = termini[idTermina]['idTreninga']
                if idTreninga in treninzi:
                    idPrograma = treninzi[idTreninga]['idPrograma']
                    if idPrograma in programi:
                        if idPrograma not in popularnostPrograma:
                            popularnostPrograma[idPrograma] = 0
                        popularnostPrograma[idPrograma] += 1

    najpopularnijiProgrami = sorted(
        popularnostPrograma.items(),
        key=lambda x: x[1], 
        reverse=True
    )[:3]

    pretraga = {}
    for idx, (idPrograma, brojRezervacija) in enumerate(najpopularnijiProgrami, start=1):
        pretraga[idx] = {
            'Naziv Programa': programi[idPrograma]['naziv'],
            'Broj Rezervacija': brojRezervacija,
        }

    ispisTabele(pretraga)
    sacuvajIzvestaj(pretraga, 'izvestaji/izvestajG.txt')
    return pretraga

def izvestajH(rezervacije, termini):
    popularnostDana = {}

    for rezervacija in rezervacije.values():
        idTermina = rezervacija['idTermina']
        if idTermina in termini:
            datumTermina = datetime.strptime(termini[idTermina]['datum'], '%d.%m.%Y').date()
            danUNedelji = datumTermina.strftime('%A').lower()

            daniNaSrpskom = {
                'monday': 'ponedeljak',
                'tuesday': 'utorak',
                'wednesday': 'sreda',
                'thursday': 'četvrtak',
                'friday': 'petak',
                'saturday': 'subota',
                'sunday': 'nedelja',
            }

            danNaSrpskom = daniNaSrpskom[danUNedelji]

            if danNaSrpskom not in popularnostDana:
                popularnostDana[danNaSrpskom] = 0
            popularnostDana[danNaSrpskom] += 1

    najpopularnijiDan = max(popularnostDana.items(), key=lambda x: x[1])

    pretraga = {
        1: {
            'Dan u Nedelji': najpopularnijiDan[0].capitalize(),
            'Broj Rezervacija': najpopularnijiDan[1],
        }
    }

    ispisTabele(pretraga)
    sacuvajIzvestaj(pretraga, 'izvestaji/izvestajH.txt')
    return pretraga
