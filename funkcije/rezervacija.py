"""
Modul za upravljanje rezervacijama.

Sadrži funkcije za pretragu, izmenu, ponistavanje rezervacija kao i
ucitavanje, prikaz mesta u matrici, rezervisanje i dodelu mesecne nagrade lojalnosti
"""
from datetime import datetime, timedelta
from funkcije.fajlovi import ucitaj_podatke
from funkcije.tabela import ispis_tabele
from funkcije.termin import spoji_termine
from funkcije.kratak_ispis import ispis_korisnika, ispis_treninzi, ispis_mesta

def ucitaj_rezervacije(putanja):
    kljucevi = ['id', 'id_korisnika', 'id_termina', 'oznaka_reda_kolone', 'datum']
    podaci = ucitaj_podatke(putanja, kljucevi)

    # Dodatna obrada za datum
    for rezervacija in podaci.values():
        rezervacija['datum'] = (datetime.strptime(rezervacija['datum'].strip(), '%d.%m.%Y')
                                        .date().strftime('%d.%m.%Y'))

    return podaci


def pretrazi_rezervacije_korisnik(rezervacije, korisnicko_ime):
    pretraga = {}

    if korisnicko_ime:
        for podaci in rezervacije.values():
            if podaci['id_korisnika'] == korisnicko_ime:
                pretraga[podaci['id']] = podaci

    if pretraga:
        return pretraga
    print(f"Nema rezervacija za korisnika '{korisnicko_ime}'.")
    return pretraga


def pretrazi_rezervacije_instruktor(rezervacije, treninzi, termini, programi, korisnicko_ime):
    pretraga = {}

    for podaci in rezervacije.values():
        id_termina = podaci['id_termina']
        trening = treninzi.get(termini.get(id_termina, {}).get('id_treninga', ''))
        if trening:
            id_programa = trening.get('id_programa')
            if id_programa and programi.get(id_programa, {}).get('id_instruktora') == korisnicko_ime:
                pretraga[podaci['id']] = podaci

    if pretraga:
        return pretraga
    print(f"Nema rezervacija za instruktora '{korisnicko_ime}'.")
    return pretraga


def pretrazi_rezervacije(rezervacije, termini, treninzi, korisnici):
    while True:
        print("Ponuđene opcije:\n1. ID treninga\n2. Ime člana\n3. Prezime člana\n4. Datumu rezervacije\n5. Vreme početka treninga\n6. Vreme kraja treninga\nb. Nazad")

        izbor = input("Unesite zeljenu opciju: ")

        match izbor:
            case "1":
                print('Opcije postojecih treninga:')
                ispis_treninzi(treninzi)

                id_treninga = input("Unesite ID treninga: ").strip()
                pretraga = {
                    id_rezervacije: rezervacija
                    for id_rezervacije, rezervacija in rezervacije.items()
                    if treninzi[termini[rezervacija['id_termina']]['id_treninga']]['id'] == id_treninga
                }

            case "2":
                ime = input("Unesite ime člana: ").strip().lower()
                pretraga = {
                    id_rezervacije: rezervacija
                    for id_rezervacije, rezervacija in rezervacije.items()
                    if any(korisnik['ime'].lower() == ime for korisnik in korisnici.values() if korisnik['korisnicko_ime'] == rezervacija['id_korisnika'])
                }

            case "3":
                prezime = input("Unesite prezime člana: ").strip().lower()
                pretraga = {
                    id_rezervacije: rezervacija
                    for id_rezervacije, rezervacija in rezervacije.items()
                    if any(korisnik['prezime'].lower() == prezime for korisnik in korisnici.values() if korisnik['korisnicko_ime'] == rezervacija['id_korisnika'])
                }

            case "4":
                datum = input("Unesite datum rezervacije: ").strip()
                try:
                    datetime.strptime(datum, '%d.%m.%Y')
                    pretraga = {
                        id_rezervacije: rezervacija
                        for id_rezervacije, rezervacija in rezervacije.items()
                        if rezervacija['datum'] == datum
                    }
                except ValueError:
                    print("Uneli ste nevažeći datum. Pokušajte ponovo.")
                    continue

            case "5":
                vreme_pocetka = input("Unesite vreme početka treninga (hh:mm): ").strip()
                try:
                    pocetak = datetime.strptime(vreme_pocetka, '%H:%M').time()
                    pretraga = {
                        id_rezervacije: rezervacija
                        for id_rezervacije, rezervacija in rezervacije.items()
                        if treninzi[termini[rezervacija['id_termina']]['id_treninga']]['vreme_pocetka'] == pocetak
                    }
                except ValueError:
                    print("Uneli ste nevažeće vreme. Pokušajte ponovo.")
                    continue

            case "6":
                vreme_kraja = input("Unesite vreme kraja treninga (hh:mm): ").strip()
                try:
                    kraj = datetime.strptime(vreme_kraja, '%H:%M').time()
                    pretraga = {
                        id_rezervacije: rezervacija
                        for id_rezervacije, rezervacija in rezervacije.items()
                        if treninzi[termini[rezervacija['id_termina']]['id_treninga']]['vreme_kraja'] == kraj
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
            ispis_tabele(pretraga)
        else:
            print("Nema rezultata za zadatu pretragu.")


def prikaz_mesta_u_matrici(id_termina, rezervacije, termini, treninzi, sale):
    id_treninga = termini[id_termina]['id_treninga']
    id_sale = treninzi[id_treninga]['id_sale']
    sala = sale[id_sale]
    oznaka_mesta = sala['oznaka_mesta']
    broj_kolona = sala['broj_redova']

    svi_redovi = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indeks = svi_redovi.index(oznaka_mesta) + 1
    svi_redovi = svi_redovi[:indeks]

    #sva_mesta = {f"{red}{kolona}" for kolona in range(1, broj_kolona + 1) for red in svi_redovi}

    zauzeta_mesta = {rezervacija['oznaka_reda_kolone'] for rezervacija in rezervacije.values() if rezervacija['id_termina'] == id_termina}

    matrica = []
    for kolona in range(1, broj_kolona + 1):
        trenutni_red = []
        for red in svi_redovi:
            mesto = f"{red}{kolona}"
            if mesto in zauzeta_mesta:
                trenutni_red.append("X")         # Zauzeto mesto
            else:
                trenutni_red.append(mesto[0])    # Slobodno mesto
        matrica.append(trenutni_red)

    print(f"Raspored mesta za termin {id_termina}:")
    for i, red in enumerate(matrica, 1):
        print(f"Red {i}: {' '.join(red)}")


def rezervacija_mesta(rezervacije, termini, treninzi, programi, sale, korisnici, korisnicko_ime):
    korisnik = korisnici.get(korisnicko_ime)
    if korisnik['status'] != 1:
        print(f"{korisnik['korisnicko_ime']} status je 'neaktivan'. Ne možete rezervisati mesta.")
        return

    while True:
        print("Dostupni termini:")
        ispis_tabele(spoji_termine(treninzi, termini))

        id_termina = input("Unesite ID željenog termina (b. za Nazad): ")
        if id_termina == 'b':
            break
        if id_termina not in termini:
            print("Uneti termin ne postoji. Pokušajte ponovo.")
            continue

        termin = termini[id_termina]
        trening = treninzi.get(termin['id_treninga'])
        if not trening:
            print("Trening za izabrani termin nije pronađen.")
            continue

        program = programi.get(trening['id_programa'])
        if not program:
            print("Program za izabrani trening nije pronađen.")
            continue

        dan_treninga = datetime.strptime(termin['datum'], '%d.%m.%Y').weekday()

        if dan_treninga != 4 and program['potreban_paket'] == 1 and korisnik['uplaceni_paket'] != 1:
            print("Ovaj program zahteva premium članstvo. Ne možete rezervisati mesto.")
            continue

        if id_termina not in termini:
            print(f"Termin sa ID {id_termina} nije pronađen.")
            return

        id_treninga = termini[id_termina]['id_treninga']

        if id_treninga not in treninzi:
            print(f"Trening sa ID {id_treninga} nije pronađen.")
            return

        id_sale = treninzi[id_treninga]['id_sale']

        if id_sale not in sale:
            print(f"Sala sa ID {id_sale} nije pronađena.")
            return

        sala = sale[id_sale]
        oznaka_mesta = sala['oznaka_mesta']
        broj_kolona = sala['broj_redova']

        svi_redovi = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        indeks = svi_redovi.index(oznaka_mesta) + 1
        svi_redovi = svi_redovi[:indeks]

        zauzeta_mesta = {rezervacija['oznaka_reda_kolone'] for rezervacija in rezervacije.values() if rezervacija['id_termina'] == id_termina}
        slobodna_mesta = {f"{red}{kolona}" for kolona in range(1, broj_kolona + 1) for red in svi_redovi} - zauzeta_mesta

        if not slobodna_mesta:
            print("Nema slobodnih mesta za izabrani termin.")
            continue

        prikaz_mesta_u_matrici(id_termina, rezervacije, termini, treninzi, sale)

        oznaka_reda_kolone = input("Unesite oznaku reda i kolone željenog mesta (npr. A1): ")
        if oznaka_reda_kolone not in slobodna_mesta:
            print("Uneto mesto nije slobodno ili ne postoji. Pokusajte ponovo.")
            continue

        novi_id = str(len(rezervacije) + 1)
        datum = datetime.now().strftime('%d.%m.%Y')
        rezervacije[novi_id] = {
            'id': novi_id,
            'id_korisnika': korisnicko_ime,
            'id_termina': id_termina,
            'oznaka_reda_kolone': oznaka_reda_kolone,
            'datum': datum,
        }
        print(f"Uspešno rezervisano mesto {oznaka_reda_kolone} za termin {id_termina}.")

        nastavak = input("Da li želite da rezervišete još mesta? (da/ne): ").lower()
        if nastavak != 'da':
            break


def rezervacija_mesta_instruktor(rezervacije, termini, treninzi, programi, sale, korisnici, korisnicko_ime_instruktora):
    while True:
        termini_instruktora = {
            id_termina: termin
            for id_termina, termin in termini.items()
            if programi[treninzi[termin['id_treninga']]['id_programa']]['id_instruktora'] == korisnicko_ime_instruktora
        }

        if not termini_instruktora:
            print("Nemate termine za koje možete rezervisati mesta.")
            break

        korisnicko_ime_clana = input("Unesite korisničko ime člana za kojeg rezervišete mesto: ").strip()
        if korisnicko_ime_clana not in korisnici:
            print("Uneto korisničko ime člana ne postoji. Pokušajte ponovo.")
            continue

        rezervacija_mesta(rezervacije, termini_instruktora, treninzi, programi, sale, korisnici, korisnicko_ime_clana)
        break


def ponisti_rezervaciju(rezervacije):
    while True:
        print("Vaše trenutne rezervacije:")

        aktivne_rezeracije = {
            id_rezervacije: rezervacija
            for id_rezervacije, rezervacija in rezervacije.items()
            if datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date() >= datetime.now().date()
        }

        if not aktivne_rezeracije:
            print("Nemate aktivnih rezervacija za poništavanje.")
            break

        ispis_tabele(aktivne_rezeracije)

        id_rezervacije = input("Unesite ID rezervacije koju želite da poništite (b. za Nazad): ")
        if id_rezervacije == 'b':
            break
        if id_rezervacije not in aktivne_rezeracije:
            print("Nevažeći ID rezervacije. Pokušajte ponovo.")
            continue

        del rezervacije[id_rezervacije]
        print(f"Rezervacija {id_rezervacije} je uspešno poništena.")

        nastavak = input("Da li želite da poništite još neku rezervaciju? (da/ne): ").lower()
        if nastavak != 'da':
            break


def ponisti_rezervaciju_instruktor(rezervacije, termini, treninzi, programi, korisnicko_ime):
    while True:
        termini_instruktora = {
                id_termina: termin
                for id_termina, termin in termini.items()
                if programi[treninzi[termin['id_treninga']]['id_programa']]['id_instruktora'] == korisnicko_ime
            }

        if not termini_instruktora:
            print("Nemate termine za koje možete poništiti rezervaciju.")
            break

        aktivne_rezeracije = {
            id_rezervacije: rezervacija
            for id_rezervacije, rezervacija in rezervacije.items()
            if datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date() >= datetime.now().date()
        }

        if not aktivne_rezeracije:
            print("Nemate aktivnih rezervacija za poništavanje.")
            break

        ponisti_rezervaciju(rezervacije, termini)
        break


def izmeni_rezervaciju_instruktor(rezervacije, termini, treninzi, programi, korisnici, korisnicko_ime_instruktora):
    while True:
        termini_instruktora = {
            id_termina: termin
            for id_termina, termin in termini.items()
            if programi[treninzi[termin['id_treninga']]['id_programa']]['id_instruktora'] == korisnicko_ime_instruktora
        }

        if not termini_instruktora:
            print("Nemate termine za koje možete menjati rezervacije.")
            break

        print("Dostupni termini za koje ste odgovorni:")
        ispis_tabele(termini_instruktora)

        id_termina = input("Unesite šifru termina treninga (b. za Nazad): ").strip()
        if id_termina == 'b':
            break
        if id_termina not in termini_instruktora:
            print("Uneti termin nije vaš. Pokušajte ponovo.")
            continue

        korisnici_sa_rezervacijama = {
            rezervacija['id_korisnika']
            for rezervacija in rezervacije.values()
            if rezervacija['id_termina'] == id_termina
        }

        filtrirani_korisnici = {
            korisnicko_ime: korisnici[korisnicko_ime]
            for korisnicko_ime in korisnici_sa_rezervacijama
            if korisnicko_ime in korisnici
        }

        if korisnici_sa_rezervacijama:
            print('Opcije korisnika sa rezervacijama:')
            ispis_korisnika(filtrirani_korisnici)
        else:
            print("Nema korisnika sa rezervacijama za ovaj termin.")
            continue

        korisnicko_ime_clana = input("Unesite korisničko ime člana: ").strip()
        if korisnicko_ime_clana not in korisnici:
            print("Uneto korisničko ime člana ne postoji. Pokušajte ponovo.")
            continue

        izabrane_rezervacije = {
            id_rezervacije: rezervacija
            for id_rezervacije, rezervacija in rezervacije.items()
            if (rezervacija['id_termina'] == id_termina
                and rezervacija['id_korisnika'] == korisnicko_ime_clana)
        }

        if izabrane_rezervacije:
            print('Opcije rezervisanih mesta korisnika:')
            ispis_mesta(izabrane_rezervacije)
        else:
            print(f"Korisnik '{korisnicko_ime_clana}' nema rezervisana mesta za ovaj termin.")
            continue

        oznaka_reda_kolone = input("Unesite ID mesta koje želite da izmenite: ").strip()
        rezervacija_za_izmenu = None
        for rezervacija in rezervacije.values():
            if (
                rezervacija['id_termina'] == id_termina
                and rezervacija['id_korisnika'] == korisnicko_ime_clana
                and rezervacija['oznaka_reda_kolone'] == oznaka_reda_kolone
            ):
                rezervacija_za_izmenu = rezervacija
                break

        if not rezervacija_za_izmenu:
            print("Rezervacija nije pronađena. Pokušajte ponovo.")
            continue

        print("Pronađena rezervacija: ")
        ispis_tabele({rezervacija_za_izmenu['id']: rezervacija_za_izmenu})
        print("Opcije izmene:\n1. Promena termina\n"
              "2. Promena korisnika\n3. Promena mesta\nb. Nazad")

        izbor = input("Unesite opciju za izmenu: ").strip()
        if izbor == "1":
            print("Dostupni termini za koje ste odgovorni:")
            ispis_tabele(termini_instruktora)

            novi_id_termina = input("Unesite novi termin: ").strip()
            if novi_id_termina not in termini_instruktora:
                print("Novi termin nije validan za vas. Pokušajte ponovo.")
                continue
            rezervacija_za_izmenu['id_termina'] = novi_id_termina
            print("Termin uspešno izmenjen.")
        elif izbor == "2":
            novi_korisnik = input("Unesite korisničko ime novog korisnika: ").strip()
            if novi_korisnik not in korisnici:
                print("Novi korisnik ne postoji. Pokušajte ponovo.")
                continue
            rezervacija_za_izmenu['id_korisnika'] = novi_korisnik
            print("Korisnik uspešno izmenjen.")
        elif izbor == "3":
            print("Dostupna mesta za dati termin:")
            prikaz_mesta_u_matrici(id_termina, rezervacije)

            nova_oznaka = input("Unesite novu oznaku mesta: ").strip()
            zauzeta_mesta = {
                rezervacija['oznaka_reda_kolone']
                for rezervacija in rezervacije.values()
                if rezervacija['id_termina'] == id_termina
            }
            if nova_oznaka in zauzeta_mesta:
                print("Novo mesto je već zauzeto. Pokušajte ponovo.")
                continue
            rezervacija_za_izmenu['oznaka_reda_kolone'] = nova_oznaka
            print("Mesto uspešno izmenjeno.")
        elif izbor == "b":
            break
        else:
            print("Pogresan unos. Pokušajte ponovo.")
            continue

        nastavak = input("Da li želite da izmenite još neku rezervaciju? (da/ne): ").strip().lower()
        if nastavak != "da":
            break


def mesecna_nagrada_lojalnosti(rezervacije, korisnici):
    danas = datetime.now().date()
    prosli_mesec = danas - timedelta(days=30)

    mesecne_rezervacije = {}
    for rezervacija in rezervacije.values():
        datum_rezervacije = datetime.strptime(rezervacija['datum'], '%d.%m.%Y').date()
        if datum_rezervacije > prosli_mesec:
            id_korisnika = rezervacija['id_korisnika']
            if id_korisnika not in mesecne_rezervacije:
                mesecne_rezervacije[id_korisnika] = []
            mesecne_rezervacije[id_korisnika].append(rezervacija)

    for id_korisnika, rezervacije_korisnika in mesecne_rezervacije.items():
        if len(rezervacije_korisnika) > 27:
            korisnik = korisnici.get(id_korisnika)
            if korisnik:
                korisnik['status'] = 1
                korisnik['uplaceni_paket'] = 1

    print("Raspodela mesečnih nagrada lojalnosti je uspešno završena.")
