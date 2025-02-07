from funkcije.rezervacija import ucitaj_rezervacije, pretrazi_rezervacije, pretrazi_rezervacije_korisnik, rezervacija_mesta, ponisti_rezervaciju, mesecna_nagrada_lojalnosti, rezervacija_mesta_instruktor, pretrazi_rezervacije_instruktor, ponisti_rezervaciju_instruktor, izmeni_rezervaciju_instruktor
from funkcije.za_ispis import programi_za_ispis, trening_za_ispis, spojeni_termini_za_ispis, rezervacije_za_ispis
from funkcije.program import ucitaj_programe, dodaj_program, izmeni_program, brisi_program, pretrazi_program
from funkcije.korisnik import prijava, registracija, odjava, ucitaj_korisnike, registracija_instruktora
from funkcije.trening import ucitaj_trening, dodaj_trening, izmeni_trening, brisi_trening
from funkcije.vrsta_paketa import ucitaj_vrste_paketa, aktivacija_premium_paketa
from funkcije.termin import ucitaj_termin, pretrazi_termine, spoji_termine
from funkcije.clanarina import ucitaj_clanarine, validacija_clanarina
from funkcije.upravljanje_korisnicima import aktivacija_clana
from funkcije.vrsta_treninga import ucitaj_vrste_treninga
from funkcije.tabela import ispis_tabele
from funkcije.fajlovi import upis_fajl
from funkcije.sala import ucitaj_sale
from funkcije.izvestaji import izvestaj_a, izvestaj_b, izvestaj_c,izvestaj_d, izvestaj_e, izvestaj_f, izvestaj_g, izvestaj_h

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

trenutni_korisnik = None
menii = {}

def prijava_korisnik(korisnici):
    global trenutni_korisnik
    trenutni_korisnik = prijava(korisnici, trenutni_korisnik)
    glavni_meni()


def registracija_korisnik(korisnici):
    global trenutni_korisnik
    trenutni_korisnik = registracija(korisnici)
    glavni_meni()


def odjava_korisnik():
    global trenutni_korisnik
    trenutni_korisnik = odjava()
    glavni_meni()


def upisi_fajlove():
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
    upisi_fajlove()
    print('Izlaz iz programa.')


def nazad():
    print('Povratak nazad.')


def pokreni_meni(trenutni_meni):
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
                exit()
        else:
            print("Odabrali ste nepostojeću opciju")


def meni_neregistrovan():

    meni_funkcije = {
        '1': lambda: prijava_korisnik(korisnici),
        '2': lambda: registracija_korisnik(korisnici),
        '3': lambda: ispis_tabele(programi_za_ispis(programi, korisnici, vrste_treninga, vrste_paketa)),
        '4': lambda: ispis_tabele(programi_za_ispis(pretrazi_program(programi, vrste_treninga, vrste_paketa), korisnici, vrste_treninga, vrste_paketa)),
        '5': lambda: ispis_tabele(spoji_termine(trening_za_ispis(treninzi, sale, programi), termini)),
        '6': lambda: pokreni_meni('meni_pretrazi_termin'),
        '0': lambda: izlaz()
    }

    meni_opcije = {
        'naziv': "neregistrovan",
        'nazivIspis': "Neregistrovani Meni",
        'opcijeIspis': "1. Prijava\n2. Registracija\n3. Pregled dostupnih programa treninga\n4. Pretrazi programe\n5. Pregled dostupnih termina\n6. Pretrazi termine\n0. Izlaz",
        'opcijeUnos': meni_funkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meni_neregistrovan'] = meni_opcije


def meni_registrovan():

    meni_funkcije = {
        '1': lambda: odjava_korisnik(),
        '2': lambda: ispis_tabele(programi_za_ispis(programi, korisnici, vrste_treninga, vrste_paketa)),
        '3': lambda: ispis_tabele(programi_za_ispis(pretrazi_program(programi, vrste_treninga, vrste_paketa), korisnici, vrste_treninga, vrste_paketa)),
        '4': lambda: ispis_tabele(spoji_termine(trening_za_ispis(treninzi, sale, programi), termini)),
        '5': lambda: pokreni_meni('meni_pretrazi_termin'),
        '6': lambda: rezervacija_mesta(rezervacije, termini, treninzi, programi, sale, korisnici, trenutni_korisnik['korisnicko_ime']),
        '7': lambda: ispis_tabele(rezervacije_za_ispis(pretrazi_rezervacije_korisnik(rezervacije, trenutni_korisnik['korisnicko_ime']), termini, treninzi, programi)),
        '8': lambda: ponisti_rezervaciju(rezervacije, termini),
        '0': lambda: izlaz()
    }

    meni_opcije = {
        'naziv': "registrovan",
        'nazivIspis': "Registrovan Meni",
        'opcijeIspis': "1. Odjava\n2. Pregled dostupnih programa treninga\n3. Pretrazi programe\n4. Pregled dostupnih termina\n5. Pretrazi termine\n6. Rezervisi mesto\n7. Pregled rezervacija\n8. Ponisti rezervaciju\n0. Izlaz",
        'opcijeUnos': meni_funkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meni_registrovan'] = meni_opcije


def meni_instruktor():

    meni_funkcije = {
        '1': lambda: odjava_korisnik(),
        '2': lambda: ispis_tabele(programi_za_ispis(programi, korisnici, vrste_treninga, vrste_paketa)),
        '3': lambda: ispis_tabele(programi_za_ispis(pretrazi_program(programi, vrste_treninga, vrste_paketa), korisnici, vrste_treninga, vrste_paketa)),
        '4': lambda: ispis_tabele(spoji_termine(trening_za_ispis(treninzi, sale, programi), termini)),
        '5': lambda: pokreni_meni('meni_pretrazi_termin'),
        '6': lambda: rezervacija_mesta_instruktor(rezervacije, termini, treninzi, programi, sale, korisnici, trenutni_korisnik['korisnicko_ime']),
        '7': lambda: ispis_tabele(rezervacije_za_ispis(pretrazi_rezervacije_instruktor(rezervacije, treninzi, termini, programi, trenutni_korisnik['korisnicko_ime']), termini, treninzi, programi)),
        '8': lambda: ponisti_rezervaciju_instruktor(rezervacije, termini, treninzi, programi, korisnici, trenutni_korisnik['korisnicko_ime']),
        '9': lambda: pretrazi_rezervacije(rezervacije, termini, treninzi, korisnici),
        '10': lambda: aktivacija_clana(korisnici, clanarine),
        '11': lambda: aktivacija_premium_paketa(korisnici),
        '12': lambda: izmeni_rezervaciju_instruktor(rezervacije, termini, treninzi, programi, korisnici, trenutni_korisnik['korisnicko_ime']),
        '0': lambda: izlaz()
    }

    meni_opcije = {
        'naziv': "instruktor",
        'nazivIspis': "Instruktor Meni",
        'opcijeIspis': "1. Odjava\n2. Pregled dostupnih programa treninga\n3. Pretrazi programe\n4. Pregled dostupnih termina\n5. Pretrazi termine\n6. Rezervisi mesto\n7. Pregled rezervacija\n8. Ponisti rezervaciju\n9. Pretraga rezervacija\n10. Aktivacija clana\n11. Aktivacija premium clana\n12. Izmeni rezervacije\n0. Izlaz",
        'opcijeUnos': meni_funkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meni_instruktor'] = meni_opcije


def meni_admin():

    submenu2_dict = {
        '1': lambda: odjava_korisnik(),
        '2': lambda: ispis_tabele(programi_za_ispis(programi, korisnici, vrste_treninga, vrste_paketa)),
        '3': lambda: ispis_tabele(programi_za_ispis(pretrazi_program(programi, vrste_treninga, vrste_paketa), korisnici, vrste_treninga, vrste_paketa)),
        '4': lambda: ispis_tabele(spoji_termine(trening_za_ispis(treninzi, sale, programi), termini)),
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
        'opcijeIspis': "1. Odjava\n2. Pregled dostupnih programa treninga\n3. Pretrazi programe\n4. Pregled dostupnih termina\n5. Pretrazi termine\n6. Registracija novih instruktora\n7. Izvestavanje\n8. Mesecna nagrada lojalnosti\n9. Unos Izmena Brisanje Programa\n10. Unos Izmena Brisanje Treninga\n0. Izlaz",
        'opcijeUnos': submenu2_dict,
        'nazad': False,
        'izlaz': True
    }

    menii['meni_admin'] = meni_opcije


def meni_pretrazi_termin():

    meni_funkcije = {
        '1': lambda: ispis_tabele(spojeni_termini_za_ispis(pretrazi_termine(spoji_termine(treninzi, termini), sale, programi, 'id_sale'), sale, programi)),
        '2': lambda: ispis_tabele(spojeni_termini_za_ispis(pretrazi_termine(spoji_termine(treninzi, termini), sale, programi, 'id_programa'), sale, programi)),
        '3': lambda: ispis_tabele(spojeni_termini_za_ispis(pretrazi_termine(spoji_termine(treninzi, termini), sale, programi, 'datum'), sale, programi)),
        '4': lambda: ispis_tabele(spojeni_termini_za_ispis(pretrazi_termine(spoji_termine(treninzi, termini), sale, programi, 'vreme_pocetka'), sale, programi)),
        '5': lambda: ispis_tabele(spojeni_termini_za_ispis(pretrazi_termine(spoji_termine(treninzi, termini), sale, programi, 'vreme_kraja'), sale, programi)),
        'b': lambda: nazad()
    }

    meni_opcije = {
        'naziv': "pretraziTermin",
        'nazivIspis': "Pretrazi Termin Meni",
        'opcijeIspis': "1. ID Sale\n2. ID programa\n3. Datum\n4. Vreme pocetka\n5. Vreme kraja\nb. Nazad",
        'opcijeUnos': meni_funkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meni_pretrazi_termin'] = meni_opcije


def meni_unos_izmena_brisanje_program():

    meni_funkcije = {
        '1': lambda: dodaj_program(programi, vrste_treninga, korisnici, vrste_paketa),
        '2': lambda: izmeni_program(programi, vrste_treninga, korisnici, vrste_paketa),
        '3': lambda: brisi_program(programi),
        'b': lambda: nazad()
    }

    meni_opcije = {
        'naziv': "UnosIzmenaBrisanjePrograma",
        'nazivIspis': "Unos Izmena Brisanje Programa Meni",
        'opcijeIspis': "1. Unos programa treninga\n2. Izmena programa treninga\n3. Brisanje programa treninga\nb. Nazad",
        'opcijeUnos': meni_funkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meni_unos_izmena_brisanje_program'] = meni_opcije


def meni_unos_izmena_brisanje_trening():

    meni_funkcije = {
        '1': lambda: dodaj_trening(treninzi, sale, programi),
        '2': lambda: izmeni_trening(treninzi, sale, programi),
        '3': lambda: brisi_trening(treninzi),
        'b': lambda: nazad()
    }

    meni_opcije = {
        'naziv': "meni_unos_izmena_brisanje_trening",
        'nazivIspis': "Unos Izmena Brisanje Treminga Meni",
        'opcijeIspis': "1. Unos treninga\n2. Izmena treninga\n3. Brisanje treninga\nb. Nazad",
        'opcijeUnos': meni_funkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meni_unos_izmena_brisanje_trening'] = meni_opcije


def meni_izvestaji():

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
        'opcijeIspis': "1. Lista rezervacija za odabran datum rezervacije\n2. Lista rezervacija za odabran datum termina treninga\n3. Lista rezervacija za odabran datum rezervacije i odabranog instruktora\n4. Ukupan broj rezervacija za izabran dan (u nedelji) održavanja treninga\n5. Ukupan broj rezervacije po instruktorima u poslednjih 30 dana\n6. Ukupan broj rezervacija realizovanih (Standard i Premium) u poslednjih 30 dana.\n7. Najpopularniji programi treninga.\n8. Najpopularniji dan u nedelji.\nb. Nazad",
        'opcijeUnos': meni_funkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meni_izvestaji'] = meni_opcije


def definisi():
    meni_neregistrovan()
    meni_registrovan()
    meni_instruktor()
    meni_admin()
    meni_pretrazi_termin()
    meni_unos_izmena_brisanje_program()
    meni_unos_izmena_brisanje_trening()
    meni_izvestaji()


def glavni_meni():
    global trenutni_korisnik
    definisi()
    validacija_clanarina(korisnici, clanarine)   #azuriraj clanarine

    if trenutni_korisnik is None:                #nije prijavljen
        pokreni_meni('meni_neregistrovan')
    elif trenutni_korisnik['uloga'] == 0:        #registrovan
        pokreni_meni('meni_registrovan')
    elif trenutni_korisnik['uloga'] == 1:        #instruktor
        pokreni_meni('meni_instruktor')
    elif trenutni_korisnik['uloga'] == 2:        #admin
        pokreni_meni('meni_admin')
