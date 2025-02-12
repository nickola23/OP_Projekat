"""
Modul sa menijem za upravljanje aplikacijom.

Sadrži sve funkcije glavnog menija programa.
"""
import sys
from funkcije.rezervacija import (
    ucitaj_rezervacije, pretrazi_rezervacije, pretrazi_rezervacije_korisnik,
    rezervacija_mesta, ponisti_rezervaciju, mesecna_nagrada_lojalnosti,
    rezervacija_mesta_instruktor, pretrazi_rezervacije_instruktor,
    ponisti_rezervaciju_instruktor, izmeni_rezervaciju_instruktor
)
from funkcije.za_ispis import (
    programi_za_ispis, trening_za_ispis,
    spojeni_termini_za_ispis, rezervacije_za_ispis
)
from funkcije.program import (
    ucitaj_programe, dodaj_program, izmeni_program,
    brisi_program, pretrazi_program
)
from funkcije.izvestaji import (
    izvestaj_a, izvestaj_b, izvestaj_c,izvestaj_d, izvestaj_e,
    izvestaj_f, izvestaj_g, izvestaj_h
)
from funkcije.korisnik import (
    prijava, registracija, odjava, ucitaj_korisnike,
    registracija_instruktora
)
from funkcije.trening import (
    ucitaj_trening, dodaj_trening, izmeni_trening, brisi_trening
)
from funkcije.vrsta_paketa import ucitaj_vrste_paketa, aktivacija_premium_paketa
from funkcije.termin import ucitaj_termin, pretrazi_termine, spoji_termine
from funkcije.clanarina import ucitaj_clanarine, validacija_clanarina
from funkcije.upravljanje_korisnicima import aktivacija_clana
from funkcije.vrsta_treninga import ucitaj_vrste_treninga
from funkcije.tabela import ispis_tabele
from funkcije.fajlovi import upis_fajl
from funkcije.sala import ucitaj_sale

PUTANJA_VRSTE_TRENINGA = './data/vrsta_treninga.txt'
PUTANJA_REZERVACIJE = './data/Rezervacija.txt'
PUTANJA_VRSTE_PAKETA = './data/vrsta_paketa.txt'
PUTANJA_KORISNICI = './data/Korisnici.txt'
PUTANJA_CLANARINE = './data/Clanarina.txt'
PUTANJA_PROGRAMI = './data/Program.txt'
PUTANJA_TRENING = './data/Trening.txt'
PUTANJA_TERMIN = './data/Termin.txt'
PUTANJA_SALA = './data/Sala.txt'

vrste_treninga = ucitaj_vrste_treninga(PUTANJA_VRSTE_TRENINGA)
rezervacije = ucitaj_rezervacije(PUTANJA_REZERVACIJE)
vrste_paketa = ucitaj_vrste_paketa(PUTANJA_VRSTE_PAKETA)
korisnici = ucitaj_korisnike(PUTANJA_KORISNICI)
clanarine = ucitaj_clanarine(PUTANJA_CLANARINE)
programi = ucitaj_programe(PUTANJA_PROGRAMI)
treninzi = ucitaj_trening(PUTANJA_TRENING)
termini =  ucitaj_termin(PUTANJA_TERMIN)
sale = ucitaj_sale(PUTANJA_SALA)

TRENUTNI_KORISNIK = None
menii = {}

def prijava_korisnik():
    """
    Funkcija za prijavu korisnika.

    Prijavljeni korisnik postaje 
    aktivan korisnik u globalnoj promenljivoj TRENUTNI_KORISNIK.
    """
    global TRENUTNI_KORISNIK
    TRENUTNI_KORISNIK = prijava(korisnici, TRENUTNI_KORISNIK)
    glavni_meni()


def registracija_korisnik():
    """
    Funkcija za registraciju korisnika.

    Novi korisnik se registruje i postaje aktivan korisnik 
    u globalnoj promenljivoj TRENUTNI_KORISNIK.
    """
    global TRENUTNI_KORISNIK
    TRENUTNI_KORISNIK = registracija(korisnici)
    glavni_meni()


def odjava_korisnik():
    """
    Funkcija za odjavu korisnika.

    Korisnik se odjavljuje, a globalna promenljiva TRENUTNI_KORISNIK se postavlja na None.
    """
    global TRENUTNI_KORISNIK
    odjava()
    TRENUTNI_KORISNIK = None
    glavni_meni()


def upisi_fajlove():
    """
    Funkcija za upis podataka u fajlove.

    Upisuje različite vrste podataka u odgovarajuće fajlove koristeći funkciju upis_fajl.
    """
    upis_fajl(PUTANJA_VRSTE_TRENINGA, vrste_treninga)
    upis_fajl(PUTANJA_REZERVACIJE, rezervacije)
    upis_fajl(PUTANJA_VRSTE_PAKETA, vrste_paketa)
    upis_fajl(PUTANJA_KORISNICI, korisnici)
    upis_fajl(PUTANJA_CLANARINE, clanarine)
    upis_fajl(PUTANJA_PROGRAMI, programi)
    upis_fajl(PUTANJA_TRENING, treninzi)
    upis_fajl(PUTANJA_TERMIN, termini)
    upis_fajl(PUTANJA_SALA, sale)


def izlaz():
    """
    Funkcija za izlaz iz programa.

    Pre izlaska, podaci se upisuju u fajlove i ispisuje se poruka.
    """
    upisi_fajlove()
    print('Izlaz iz programa.')


def nazad():
    """
    Ispisuje poruku 'Povratak nazad' kao potvrdu akcije.
    """
    print('Povratak nazad.')


def pokreni_meni(trenutni_meni):
    """
    Funkcija za prikaz i navigaciju kroz trenutni meni.

    Args:
        trenutni_meni (str): Ključ trenutnog menija koji se prikazuje korisniku.
    """
    meni = menii[trenutni_meni]
    while True:
        print("=" * 30)
        print("Odabrali ste", meni["nazivIspis"])
        print("=" * 30)
        print("Ponuđene opcije:")
        print(meni["opcijeIspis"])

        unos = input("Unesite zeljenu opciju: ")

        if unos in meni["opcijeUnos"]:
            funkcija = meni["opcijeUnos"][unos]
            if meni["opcijeUnos"][unos] not in menii:
                funkcija()
            else:
                pokreni_meni(funkcija)

            if meni["nazad"] and unos == 'b':
                return
            if meni["izlaz"] and unos == '0':
                sys.exit()
        else:
            print("Odabrali ste nepostojeću opciju")


def meni_neregistrovan():
    """
    Prikazuje meni za neregistrovane korisnike i omogućava izbor funkcija.

    Opcije:
        1. Prijava korisnika.
        2. Registracija korisnika.
        3. Pregled dostupnih programa treninga.
        4. Pretraga programa treninga.
        5. Pregled dostupnih termina.
        6. Pretraga termina.
        0. Izlaz iz aplikacije.
    """
    meni_funkcije = {
        '1': lambda: prijava_korisnik(),
        '2': lambda: registracija_korisnik(),
        '3': lambda: ispis_tabele(programi_za_ispis
                                  (programi, korisnici, vrste_treninga, vrste_paketa)),

        '4': lambda: ispis_tabele(programi_za_ispis
                                  (pretrazi_program(programi, vrste_treninga, vrste_paketa),
                                   korisnici, vrste_treninga, vrste_paketa)),

        '5': lambda: ispis_tabele(spoji_termine
                                  (trening_za_ispis(treninzi, sale, programi), termini)),

        '6': lambda: pokreni_meni('meni_pretrazi_termin'),
        '0': lambda: izlaz()
    }

    meni_opcije = {
        'naziv': "neregistrovan",
        'nazivIspis': "Neregistrovani Meni",
        'opcijeIspis':  "1. Prijava\n"
                        "2. Registracija\n"
                        "3. Pregled dostupnih programa treninga\n"
                        "4. Pretrazi programe\n"
                        "5. Pregled dostupnih termina\n"
                        "6. Pretrazi termine\n"
                        "0. Izlaz",
        'opcijeUnos': meni_funkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meni_neregistrovan'] = meni_opcije


def meni_registrovan():
    """
    Prikazuje meni za registrovane korisnike i omogućava izbor funkcija.

    Opcije:
        1. Odjava korisnika.
        2. Pregled dostupnih programa treninga.
        3. Pretraga programa treninga.
        4. Pregled dostupnih termina.
        5. Pretraga termina.
        6. Rezervacija mesta.
        7. Pregled rezervacija.
        8. Poništavanje rezervacije.
        0. Izlaz iz programa.
    """
    meni_funkcije = {
        '1': lambda: odjava_korisnik(),
        '2': lambda: ispis_tabele(programi_za_ispis
                                  (programi, korisnici, vrste_treninga, vrste_paketa)),

        '3': lambda: ispis_tabele(programi_za_ispis
                                  (pretrazi_program(programi, vrste_treninga, vrste_paketa),
                                   korisnici, vrste_treninga, vrste_paketa)),

        '4': lambda: ispis_tabele(spoji_termine
                                  (trening_za_ispis(treninzi, sale, programi), termini)),

        '5': lambda: pokreni_meni('meni_pretrazi_termin'),
        '6': lambda: rezervacija_mesta(rezervacije, termini, treninzi, programi,
                                       sale, korisnici, TRENUTNI_KORISNIK['korisnicko_ime']),

        '7': lambda: ispis_tabele(rezervacije_za_ispis
                (pretrazi_rezervacije_korisnik(rezervacije, TRENUTNI_KORISNIK['korisnicko_ime']),

                termini, treninzi, programi)),
        '8': lambda: ponisti_rezervaciju(rezervacije),
        '0': lambda: izlaz()
    }

    meni_opcije = {
        'naziv': "registrovan",
        'nazivIspis': "Registrovan Meni",
        'opcijeIspis':  "1. Odjava\n"
                        "2. Pregled dostupnih programa treninga\n"
                        "3. Pretrazi programe\n"
                        "4. Pregled dostupnih termina\n"
                        "5. Pretrazi termine\n"
                        "6. Rezervisi mesto\n"
                        "7. Pregled rezervacija\n"
                        "8. Ponisti rezervaciju\n"
                        "0. Izlaz",
        'opcijeUnos': meni_funkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meni_registrovan'] = meni_opcije


def meni_instruktor():
    """
    Prikazuje meni za instruktore i omogućava izbor funkcija.

    Opcije:
        1. Odjava korisnika.
        2. Pregled dostupnih programa treninga.
        3. Pretraga programa treninga.
        4. Pregled dostupnih termina.
        5. Pretraga termina.
        6. Rezervacija mesta za korisnika.
        7. Pregled rezervacija instruktora.
        8. Poništavanje rezervacije instruktora.
        9. Pretraga svih rezervacija.
        10. Aktivacija člana.
        11. Aktivacija premium člana.
        12. Izmena rezervacija instruktora.
        0. Izlaz iz programa.
    """
    meni_funkcije = {
        '1': lambda: odjava_korisnik(),
        '2': lambda: ispis_tabele(programi_za_ispis
                                  (programi, korisnici, vrste_treninga, vrste_paketa)),

        '3': lambda: ispis_tabele(programi_za_ispis(pretrazi_program
            (programi, vrste_treninga, vrste_paketa), korisnici, vrste_treninga, vrste_paketa)),

        '4': lambda: ispis_tabele(spoji_termine(trening_za_ispis(treninzi,sale,programi),termini)),
        '5': lambda: pokreni_meni('meni_pretrazi_termin'),
        '6': lambda: rezervacija_mesta_instruktor
            (rezervacije, termini, treninzi, programi, sale,
             korisnici, TRENUTNI_KORISNIK['korisnicko_ime']),

        '7': lambda: ispis_tabele(rezervacije_za_ispis(pretrazi_rezervacije_instruktor
            (rezervacije, treninzi, termini, programi, TRENUTNI_KORISNIK['korisnicko_ime']),
              termini, treninzi, programi)),

        '8': lambda: ponisti_rezervaciju_instruktor
            (rezervacije, termini, treninzi, programi, TRENUTNI_KORISNIK['korisnicko_ime']),

        '9': lambda: pretrazi_rezervacije(rezervacije, termini, treninzi, korisnici),
        '10': lambda: aktivacija_clana(korisnici, clanarine),
        '11': lambda: aktivacija_premium_paketa(korisnici),
        '12': lambda: izmeni_rezervaciju_instruktor
            (rezervacije, termini, treninzi, programi, korisnici,
             TRENUTNI_KORISNIK['korisnicko_ime']),

        '0': lambda: izlaz()
    }

    meni_opcije = {
        'naziv': "instruktor",
        'nazivIspis': "Instruktor Meni",
        'opcijeIspis':  "1. Odjava\n"
                        "2. Pregled dostupnih programa treninga\n"
                        "3. Pretrazi programe\n"
                        "4. Pregled dostupnih termina\n"
                        "5. Pretrazi termine\n"
                        "6. Rezervisi mesto\n"
                        "7. Pregled rezervacija\n"
                        "8. Ponisti rezervaciju\n"
                        "9. Pretraga rezervacija\n"
                        "10. Aktivacija clana\n"
                        "11. Aktivacija premium clana\n"
                        "12. Izmeni rezervacije\n"
                        "0. Izlaz",
        'opcijeUnos': meni_funkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meni_instruktor'] = meni_opcije


def meni_admin():
    """
    Prikazuje meni za administratore i omogućava izbor funkcija.

    Opcije:
        1. Odjava korisnika.
        2. Pregled dostupnih programa treninga.
        3. Pretraga programa treninga.
        4. Pregled dostupnih termina.
        5. Pretraga termina.
        6. Registracija novih instruktora.
        7. Izveštavanje.
        8. Mesečna nagrada lojalnosti.
        9. Unos, izmena i brisanje programa.
        10. Unos, izmena i brisanje treninga.
        0. Izlaz iz programa.
    """
    submenu2_dict = {
        '1': lambda: odjava_korisnik(),
        '2': lambda: ispis_tabele(programi_za_ispis
            (programi, korisnici, vrste_treninga, vrste_paketa)),

        '3': lambda: ispis_tabele(programi_za_ispis
            (pretrazi_program(programi, vrste_treninga, vrste_paketa),
              korisnici, vrste_treninga, vrste_paketa)),

        '4': lambda: ispis_tabele(spoji_termine(trening_za_ispis(treninzi,sale,programi),termini)),
        '5': lambda: pokreni_meni('meni_pretrazi_termin'),
        '6': lambda: registracija_instruktora(korisnici),
        '7': lambda: pokreni_meni('meni_izvestaji'),
        '8': lambda: mesecna_nagrada_lojalnosti(rezervacije, korisnici),
        '9': lambda: pokreni_meni('meni_unos_izmena_brisanje_program'),
        '10': lambda: pokreni_meni('meni_unos_izmena_brisanje_trening'),
        '0': lambda: izlaz()
    }

    meni_opcije = {
        'naziv': "admin",
        'nazivIspis': "Admin Meni",
        'opcijeIspis':  "1. Odjava\n"
                        "2. Pregled dostupnih programa treninga\n"
                        "3. Pretrazi programe\n"
                        "4. Pregled dostupnih termina\n"
                        "5. Pretrazi termine\n"
                        "6. Registracija novih instruktora\n"
                        "7. Izvestavanje\n"
                        "8. Mesecna nagrada lojalnosti\n"
                        "9. Unos Izmena Brisanje Programa\n"
                        "10. Unos Izmena Brisanje Treninga\n"
                        "0. Izlaz",
        'opcijeUnos': submenu2_dict,
        'nazad': False,
        'izlaz': True
    }

    menii['meni_admin'] = meni_opcije


def meni_pretrazi_termin():
    """
    Prikazuje meni za pretragu termina i omogućava izbor kriterijuma pretrage.

    Opcije:
        1. Pretraga po ID-u sale.
        2. Pretraga po ID-u programa.
        3. Pretraga po datumu.
        4. Pretraga po vremenu početka.
        5. Pretraga po vremenu kraja.
        b. Povratak na prethodni meni.
    """
    meni_funkcije = {
        '1': lambda: ispis_tabele(spojeni_termini_za_ispis(pretrazi_termine
            (spoji_termine(treninzi, termini), sale, programi, 'id_sale'), sale, programi)),

        '2': lambda: ispis_tabele(spojeni_termini_za_ispis(pretrazi_termine
            (spoji_termine(treninzi, termini), sale, programi, 'id_programa'), sale, programi)),

        '3': lambda: ispis_tabele(spojeni_termini_za_ispis(pretrazi_termine
            (spoji_termine(treninzi, termini), sale, programi, 'datum'), sale, programi)),

        '4': lambda: ispis_tabele(spojeni_termini_za_ispis(pretrazi_termine
            (spoji_termine(treninzi, termini), sale, programi, 'vreme_pocetka'), sale, programi)),

        '5': lambda: ispis_tabele(spojeni_termini_za_ispis(pretrazi_termine
            (spoji_termine(treninzi, termini), sale, programi, 'vreme_kraja'), sale, programi)),

        'b': lambda: nazad()
    }

    meni_opcije = {
        'naziv': "pretraziTermin",
        'nazivIspis': "Pretrazi Termin Meni",
        'opcijeIspis': "1. ID Sale\n"
                       "2. ID programa\n"
                       "3. Datum\n"
                       "4. Vreme pocetka\n"
                       "5. Vreme kraja\n"
                       "b. Nazad",
        'opcijeUnos': meni_funkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meni_pretrazi_termin'] = meni_opcije


def meni_unos_izmena_brisanje_program():
    """
    Prikazuje meni za unos, izmenu i brisanje programa treninga i omogućava izbor.

    Opcije:
        1. Unos novog programa treninga.
        2. Izmena postojećeg programa treninga.
        3. Brisanje programa treninga.
        b. Povratak na prethodni meni.
    """
    meni_funkcije = {
        '1': lambda: dodaj_program(programi, vrste_treninga, korisnici, vrste_paketa),
        '2': lambda: izmeni_program(programi, vrste_treninga, korisnici, vrste_paketa),
        '3': lambda: brisi_program(programi),
        'b': lambda: nazad()
    }

    meni_opcije = {
        'naziv': "UnosIzmenaBrisanjePrograma",
        'nazivIspis': "Unos Izmena Brisanje Programa Meni",
        'opcijeIspis': "1. Unos programa treninga\n"
                       "2. Izmena programa treninga\n"
                       "3. Brisanje programa treninga\n"
                       "b. Nazad",
        'opcijeUnos': meni_funkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meni_unos_izmena_brisanje_program'] = meni_opcije


def meni_unos_izmena_brisanje_trening():
    """
    Prikazuje meni za unos, izmenu i brisanje treninga i omogućava izbor.

    Opcije:
        1. Unos novog treninga.
        2. Izmena postojećeg treninga.
        3. Brisanje treninga.
        b. Povratak na prethodni meni.
    """
    meni_funkcije = {
        '1': lambda: dodaj_trening(treninzi, sale, programi),
        '2': lambda: izmeni_trening(treninzi, sale, programi),
        '3': lambda: brisi_trening(treninzi),
        'b': lambda: nazad()
    }

    meni_opcije = {
        'naziv': "meni_unos_izmena_brisanje_trening",
        'nazivIspis': "Unos Izmena Brisanje Treminga Meni",
        'opcijeIspis': "1. Unos treninga\n"
                       "2. Izmena treninga\n"
                       "3. Brisanje treninga\n"
                       "b. Nazad",
        'opcijeUnos': meni_funkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meni_unos_izmena_brisanje_trening'] = meni_opcije


def meni_izvestaji():
    """
    Prikazuje meni za različite izveštaje o rezervacijama i terminima i omogućava izbor.

    Opcije:
        1. Lista rezervacija za odabran datum rezervacije.
        2. Lista rezervacija za odabran datum termina treninga.
        3. Lista rezervacija za odabran datum rezervacije i odabranog instruktora.
        4. Ukupan broj rezervacija za izabran dan (u nedelji) održavanja treninga.
        5. Ukupan broj rezervacija po instruktorima u poslednjih 30 dana.
        6. Ukupan broj realizovanih rezervacija (Standard i Premium) u poslednjih 30 dana.
        7. Najpopularniji programi treninga.
        8. Najpopularniji dan u nedelji.
        b. Povratak na prethodni meni.
    """
    meni_funkcije = {
        '1': lambda: izvestaj_a(rezervacije),
        '2': lambda: izvestaj_b(rezervacije, termini),
        '3': lambda: izvestaj_c(rezervacije, korisnici, programi, termini, treninzi),
        '4': lambda: izvestaj_d(rezervacije),
        '5': lambda: izvestaj_e(rezervacije, termini, treninzi, programi),
        '6': lambda: izvestaj_f(rezervacije, termini, treninzi, programi),
        '7': lambda: izvestaj_g(rezervacije, termini, treninzi, programi),
        '8': lambda: izvestaj_h(rezervacije, termini),
        'b': lambda: nazad()
    }

    meni_opcije = {
        'naziv': "meni_izvestaji",
        'nazivIspis': "Izvestaji Meni",
        'opcijeIspis': 
            "1. Lista rezervacija za odabran datum rezervacije\n"
            "2. Lista rezervacija za odabran datum termina treninga\n"
            "3. Lista rezervacija za odabran datum rezervacije i odabranog instruktora\n"
            "4. Ukupan broj rezervacija za izabran dan (u nedelji) održavanja treninga\n"
            "5. Ukupan broj rezervacije po instruktorima u poslednjih 30 dana\n"
            "6. Ukupan broj rezervacija realizovanih (Standard i Premium) u poslednjih 30 dana.\n"
            "7. Najpopularniji programi treninga.\n"
            "8. Najpopularniji dan u nedelji.\n"
            "b. Nazad",
        'opcijeUnos': meni_funkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meni_izvestaji'] = meni_opcije


def definisi():
    """
    Poziva sve funkcije koje inicijalizuju menije.
    """
    meni_neregistrovan()
    meni_registrovan()
    meni_instruktor()
    meni_admin()
    meni_pretrazi_termin()
    meni_unos_izmena_brisanje_program()
    meni_unos_izmena_brisanje_trening()
    meni_izvestaji()


def glavni_meni():
    """
    Glavni meni koji pokreće odgovarajući meni na osnovu statusa korisnika.
    """
    definisi()
    validacija_clanarina(korisnici, clanarine)   # azuriraj clanarine

    if TRENUTNI_KORISNIK is None:                # nije prijavljen
        pokreni_meni('meni_neregistrovan')
    elif TRENUTNI_KORISNIK['uloga'] == 0:        # registrovan
        pokreni_meni('meni_registrovan')
    elif TRENUTNI_KORISNIK['uloga'] == 1:        # instruktor
        pokreni_meni('meni_instruktor')
    elif TRENUTNI_KORISNIK['uloga'] == 2:        # admin
        pokreni_meni('meni_admin')
