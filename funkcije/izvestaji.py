from datetime import datetime, timedelta
from funkcije.tabela import max_duzina, kreiraj_tabelu
from funkcije.tabela import ispis_tabele
from funkcije.kratak_ispis import ispis_korisnika

def sacuvaj_izvestaj(podaci, naziv_fajla):
    while True:
        opcija = input("Da li želite da sačuvate podatke u fajl? (da/ne): ").strip().lower()

        if opcija == "da":
            try:
                with open(naziv_fajla, "w", encoding="utf-8") as fajl:
                    if not podaci:
                        fajl.write("Nema podataka za čuvanje.\n")
                        break

                    zaglavlje = linija = vrednosti = ''
                    duzine = max_duzina(podaci)

                    for kljuc, duzina in duzine.items():
                        zaglavlje += " | " + f"{kljuc:<{duzina}}"
                        linija += "-+-" + "-" * duzina

                    fajl.write(zaglavlje + "\n")
                    fajl.write(linija + "\n")

                    vrednosti = kreiraj_tabelu(podaci, duzine)
                    fajl.write(vrednosti)

                print(f"Podaci su uspešno sačuvani u fajl: {naziv_fajla}")
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


def izvestaj_a(rezervacije):
    while True:
        odabrani_datum = input("Unesite datum rezervacije: ").strip()
        pretraga = {}
        try:
            datetime.strptime(odabrani_datum, '%d.%m.%Y').date()
        except ValueError:
            print("Neispravan format datuma. Pokušajte ponovo.")
            continue
        for idx, rezervacija in enumerate(rezervacije.values(), start=1):
            if rezervacija['datum'] == odabrani_datum:
                pretraga[idx] = {
                    'ID Rezervacije': rezervacija['id'],
                    'Korisnicko ime': rezervacija['id_korisnika'],
                    'ID Termina': rezervacija['id_termina'],
                    'Oznaka Mesta': rezervacija['oznaka_reda_kolone'],
                    'Datum': rezervacija['datum']
                }
        ispis_tabele(pretraga)
        sacuvaj_izvestaj(pretraga, 'izvestaji/izvestaj_a.txt')
        return pretraga


def izvestaj_b(rezervacije, termini):
    while True:
        odabrani_datum = input("Unesite datum termina treninga: ").strip()
        try:
            datum = datetime.strptime(odabrani_datum, '%d.%m.%Y').date()
        except ValueError:
            print("Neispravan format datuma. Pokušajte ponovo.")
            continue

        termini_za_datum = {
                            id: termin for id, termin in termini.items()
                            if datetime.strptime(termin['datum'], '%d.%m.%Y').date() == datum
                        }

        if not termini_za_datum:
            return {}

        pretraga = {}
        for id_rezervacije, rezervacija in rezervacije.items():
            if rezervacija['id_termina'] in termini_za_datum:
                pretraga[id_rezervacije] = {
                    'ID Rezervacije': id_rezervacije,
                    'Korisnicko ime': rezervacija['id_korisnika'],
                    'ID Termina': rezervacija['id_termina'],
                    'Oznaka Mesta': rezervacija['oznaka_reda_kolone'],
                    'Datum': rezervacija['datum'],
                }

        ispis_tabele(pretraga)
        sacuvaj_izvestaj(pretraga, 'izvestaji/izvestaj_b.txt')
        return pretraga


def izvestaj_c(rezervacije, korisnici, programi, termini, treninzi):
    while True:
        odabrani_datum = input("Unesite datum rezervacije: ").strip()
        try:
            datetime.strptime(odabrani_datum, '%d.%m.%Y').date()
        except ValueError:
            print("Neispravan format datuma. Pokušajte ponovo.")
            continue

        while True:
            print('Opcije za instruktore:')
            ispis_korisnika(korisnici, 1)

            odabrani_instruktor = input("Unesite korisnicko ime instruktora: ").strip()
            if odabrani_instruktor not in korisnici:
                print("Ne postoji instruktor sa datim korisnickim imenom. Pokušajte ponovo.")
                continue
            break

        pretraga = {}
        for idx, rezervacija in enumerate(rezervacije.values(), start=1):
            id_termina = rezervacija['id_termina']
            id_treninga = termini[id_termina]['id_treninga']
            id_instruktora = programi[treninzi[id_treninga]['id_programa']]['id_instruktora']

            if (rezervacija['datum'] == odabrani_datum and 
                                        id_instruktora.lower() == odabrani_instruktor.lower()):

                pretraga[idx] = {
                    'ID Rezervacije': rezervacija['id'],
                    'Korisnicko ime': rezervacija['id_korisnika'],
                    'ID Termina': id_termina,
                    'Instruktor': id_instruktora,
                    'Oznaka Mesta': rezervacija['oznaka_reda_kolone'],
                    'Datum': rezervacija['datum']
                }

                if not pretraga:
                    print("Nema rezervacija za odabrani datum i instruktora.")
                    continue

        ispis_tabele(pretraga)
        sacuvaj_izvestaj(pretraga, 'izvestaji/izvestaj_c.txt')
        return pretraga


def izvestaj_d(rezervacije):
    while True:
        validni_dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja']
        odabrani_dan = input("Unesite dan u nedelji (npr. ponedeljak): ").strip().lower()
        engleski_u_dani = {
            'monday': 'ponedeljak',
            'tuesday': 'utorak',
            'wednesday': 'sreda',
            'thursday': 'cetvrtak',
            'friday': 'petak',
            'saturday': 'subota',
            'sunday': 'nedelja'
        }

        if odabrani_dan not in validni_dani:
            print("Neispravan unos. Pokušajte ponovo.")
            continue

        pretraga = {}
        brojac = 0
        for idx, rezervacija in enumerate(rezervacije.values(), start=1):
            datum = datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date()
            dan_u_nedelji_engleski = datum.strftime('%A').lower()
            dan_u_nedelji_srpski = engleski_u_dani[dan_u_nedelji_engleski]

            if dan_u_nedelji_srpski == odabrani_dan:
                brojac += 1
                pretraga[idx] = {
                    'ID Rezervacije': rezervacija['id'],
                    'Korisnicko ime': rezervacija['id_korisnika'],
                    'ID Termina': rezervacija['id_termina'],
                    'Oznaka Mesta': rezervacija['oznaka_reda_kolone'],
                    'Datum': rezervacija['datum']
                }

        print(f"Ukupan broj rezervacija za {odabrani_dan} je: {brojac}. To su:")
        ispis_tabele(pretraga)
        sacuvaj_izvestaj(pretraga, 'izvestaji/izvestaj_d.txt')
        return pretraga


def izvestaj_e(rezervacije, termini, treninzi, programi):
    danasnji_datum = datetime.now().date()
    poslednjih_30_dana = danasnji_datum - timedelta(days=30)
    broj_rezervacija_po_instruktoru = {}

    for rezervacija in rezervacije.values():
        datum_rezervacije = datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date()
        if datum_rezervacije >= poslednjih_30_dana:
            id_termina = rezervacija['id_termina']
            if id_termina in termini:
                id_treninga = termini[id_termina]['id_treninga']
                if id_treninga in treninzi:
                    id_programa = treninzi[id_treninga]['id_programa']
                    if id_programa in programi:
                        id_instruktora = programi[id_programa]['id_instruktora']
                        if id_instruktora not in broj_rezervacija_po_instruktoru:
                            broj_rezervacija_po_instruktoru[id_instruktora] = 0
                        broj_rezervacija_po_instruktoru[id_instruktora] += 1

    sortirani_instruktori = sorted(
        broj_rezervacija_po_instruktoru.items(),
        key=lambda x: x[1],
        reverse=True
    )

    pretraga = {}
    for id_instruktora, (instruktor, broj_rezervacija) in enumerate(sortirani_instruktori, start=1):
        pretraga[id_instruktora] = {
            'Instruktor': instruktor,
            'Broj rezervacija': broj_rezervacija
        }

    ispis_tabele(pretraga)
    sacuvaj_izvestaj(pretraga, 'izvestaji/izvestaj_e.txt')
    return pretraga

def izvestaj_f(rezervacije, termini, treninzi, programi):
    danasnji_datum = datetime.now().date()
    poslednjih_30_dana = danasnji_datum - timedelta(days=30)

    premium_rezervacije = 0
    standard_rezervacije = 0

    for rezervacija in rezervacije.values():
        datum_rezervacije = datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date()
        if datum_rezervacije >= poslednjih_30_dana:
            id_termina = rezervacija['id_termina']
            if id_termina in termini:
                id_treninga = termini[id_termina]['id_treninga']
                if id_treninga in treninzi:
                    id_programa = treninzi[id_treninga]['id_programa']
                    if id_programa in programi:
                        potreban_paket = programi[id_programa]['potreban_paket']
                        if potreban_paket == 1:
                            premium_rezervacije += 1
                        elif potreban_paket == 0:
                            standard_rezervacije += 1

    pretraga = {
        1: {'Tip paketa': 'Premium', 'Broj rezervacija': premium_rezervacije},
        2: {'Tip paketa': 'Standard', 'Broj rezervacija': standard_rezervacije},
    }

    ispis_tabele(pretraga)
    sacuvaj_izvestaj(pretraga, 'izvestaji/izvestaj_f.txt')
    return pretraga


def izvestaj_g(rezervacije, termini, treninzi, programi):
    danasnji_datum = datetime.now().date()
    poslednjih_godinu_dana = danasnji_datum - timedelta(days=365)

    popularnost_programa = {}

    for rezervacija in rezervacije.values():
        datum_rezervacije = datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date()
        if datum_rezervacije >= poslednjih_godinu_dana:
            id_termina = rezervacija['id_termina']
            if id_termina in termini:
                id_treninga = termini[id_termina]['id_treninga']
                if id_treninga in treninzi:
                    id_programa = treninzi[id_treninga]['id_programa']
                    if id_programa in programi:
                        if id_programa not in popularnost_programa:
                            popularnost_programa[id_programa] = 0
                        popularnost_programa[id_programa] += 1

    najpopularniji_programi = sorted(
        popularnost_programa.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    pretraga = {}
    for idx, (id_programa, broj_rezervacija) in enumerate(najpopularniji_programi, start=1):
        pretraga[idx] = {
            'Naziv Programa': programi[id_programa]['naziv'],
            'Broj Rezervacija': broj_rezervacija,
        }

    ispis_tabele(pretraga)
    sacuvaj_izvestaj(pretraga, 'izvestaji/izvestaj_g.txt')
    return pretraga


def izvestaj_h(rezervacije, termini):
    popularnost_dana = {}

    for rezervacija in rezervacije.values():
        id_termina = rezervacija['id_termina']
        if id_termina in termini:
            datum_termina = datetime.strptime(termini[id_termina]['datum'], '%d.%m.%Y').date()
            dan_u_nedelji = datum_termina.strftime('%A').lower()

            dani_na_srpskom = {
                'monday': 'ponedeljak',
                'tuesday': 'utorak',
                'wednesday': 'sreda',
                'thursday': 'četvrtak',
                'friday': 'petak',
                'saturday': 'subota',
                'sunday': 'nedelja',
            }

            dan_na_srpskom = dani_na_srpskom[dan_u_nedelji]

            if dan_na_srpskom not in popularnost_dana:
                popularnost_dana[dan_na_srpskom] = 0
            popularnost_dana[dan_na_srpskom] += 1

    najpopularniji_dan = max(popularnost_dana.items(), key=lambda x: x[1])

    pretraga = {
        1: {
            'Dan u Nedelji': najpopularniji_dan[0].capitalize(),
            'Broj Rezervacija': najpopularniji_dan[1],
        }
    }

    ispis_tabele(pretraga)
    sacuvaj_izvestaj(pretraga, 'izvestaji/izvestaj_h.txt')
    return pretraga
