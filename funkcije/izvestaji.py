from datetime import datetime, date, time
from funkcije.tabela import maxDuzina
from funkcije.tabela import ispisTabele

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