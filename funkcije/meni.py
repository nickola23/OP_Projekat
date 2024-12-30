from funkcije.rezervacija import ucitajRezervacije, pretraziRezervacije, pretraziRezervacijeKorisnik, rezervacijaMesta, ponistiRezervaciju, mesecnaNagradaLojalnosti, rezervacijaMestaInstruktor, pretraziRezervacijeInstruktor, ponistiRezervacijuInstruktor, izmeniRezervacijuInstruktor
from funkcije.zaIspis import programiZaIspis, treningZaIspis, spojeniTerminiZaIspis, rezervacijeZaIspis
from funkcije.program import ucitajPrograme, dodajProgram, izmeniProgram, brisiProgram, pretraziProgram
from funkcije.korisnik import prijava, registracija, odjava, ucitajKorisnike, registracijaInstruktora
from funkcije.trening import ucitajTrening, dodajTrening, izmeniTrening, brisiTrening
from funkcije.vrstaPaketa import ucitajVrstePaketa, aktivacijaPremiumPaketa
from funkcije.termin import ucitajTermin, pretraziTermine, spojiTermine
from funkcije.clanarina import ucitajClanarine, validacijaClanarina
from funkcije.upravljanjeKorisnicima import aktivacijaClana
from funkcije.vrstaTreninga import ucitajVrsteTreninga
from funkcije.tabela import ispisTabele
from funkcije.fajlovi import upisFajl
from funkcije.sala import ucitajSale

putanjaVrsteTreninga = './data/VrstaTreninga.txt'
putanjaRezervacije = './data/Rezervacija.txt'
putanjaVrstePaketa = './data/VrstaPaketa.txt'
putanjaKorisnici = './data/Korisnici.txt'
putanjaClanarine = './data/Clanarina.txt'
putanjaProgrami = './data/Program.txt'
putanjaTrening = './data/Trening.txt'
putanjaTermin = './data/Termin.txt'
putanjaSala = './data/Sala.txt'

vrsteTreninga = ucitajVrsteTreninga(putanjaVrsteTreninga)
rezervacije = ucitajRezervacije(putanjaRezervacije)
vrstePaketa = ucitajVrstePaketa(putanjaVrstePaketa)
korisnici = ucitajKorisnike(putanjaKorisnici)
clanarine = ucitajClanarine(putanjaClanarine)
programi = ucitajPrograme(putanjaProgrami)
treninzi = ucitajTrening(putanjaTrening)
termini =  ucitajTermin(putanjaTermin)
sale = ucitajSale(putanjaSala)

trenutniKorisnik = None
menii = {}

def prijavaKorisnik(korisnici):
    global trenutniKorisnik
    trenutniKorisnik = prijava(korisnici, trenutniKorisnik)
    glavniMeni()

def registracijaKorisnik(korisnici):
    global trenutniKorisnik
    trenutniKorisnik = registracija(korisnici)
    glavniMeni()

def odjavaKorisnik():
    global trenutniKorisnik
    trenutniKorisnik = odjava()
    glavniMeni()

def upisiFajlove():
    upisFajl(putanjaVrsteTreninga, vrsteTreninga)
    upisFajl(putanjaRezervacije, rezervacije)
    upisFajl(putanjaVrstePaketa, vrstePaketa)
    upisFajl(putanjaKorisnici, korisnici)
    upisFajl(putanjaClanarine, clanarine)
    upisFajl(putanjaProgrami, programi)
    upisFajl(putanjaTrening, treninzi)
    upisFajl(putanjaTermin, termini)
    upisFajl(putanjaSala, sale)

def izlaz():
    upisiFajlove()
    print('Izlaz iz programa.')

def nazad():
    print('Povratak nazad.')

def pokreniMeni(trenutniMeni):
    meni = menii[trenutniMeni]
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
                pokreniMeni(funkcija)

            if meni["nazad"] and unos == 'b':
                return
            if meni["izlaz"] and unos == '0':
                exit()
        else:
            print("Odabrali ste nepostojeću opciju")
    

def meniNeregistrovan():

    meniFunkcije = {
        '1': lambda: prijavaKorisnik(korisnici),
        '2': lambda: registracijaKorisnik(korisnici),
        '3': lambda: ispisTabele(programiZaIspis(programi, korisnici, vrsteTreninga, vrstePaketa)),
        '4': lambda: ispisTabele(programiZaIspis(pretraziProgram(programi, vrsteTreninga, vrstePaketa), korisnici, vrsteTreninga, vrstePaketa)),
        '5': lambda: ispisTabele(spojiTermine(treningZaIspis(treninzi, sale, programi), termini)),
        '6': lambda: pokreniMeni('meniPretraziTermin'),
        '0': lambda: izlaz()
    }

    meniOpcije = {
        'naziv': "neregistrovan",
        'nazivIspis': "Neregistrovani Meni",
        'opcijeIspis': "1. Prijava\n2. Registracija\n3. Pregled dostupnih programa treninga\n4. Pretrazi programe\n5. Pregled dostupnih termina\n6. Pretrazi termine\n0. Izlaz",
        'opcijeUnos': meniFunkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meniNeregistrovan'] = meniOpcije

def meniRegistrovan():

    meniFunkcije = {
        '1': lambda: odjavaKorisnik(),
        '2': lambda: ispisTabele(programiZaIspis(programi, korisnici, vrsteTreninga, vrstePaketa)),
        '3': lambda: ispisTabele(programiZaIspis(pretraziProgram(programi, vrsteTreninga, vrstePaketa), korisnici, vrsteTreninga, vrstePaketa)),
        '4': lambda: ispisTabele(spojiTermine(treningZaIspis(treninzi, sale, programi), termini)),
        '5': lambda: pokreniMeni('meniPretraziTermin'),
        '6': lambda: rezervacijaMesta(rezervacije, termini, treninzi, programi, sale, korisnici, trenutniKorisnik['korisnickoIme']),
        '7': lambda: ispisTabele(rezervacijeZaIspis(pretraziRezervacijeKorisnik(rezervacije, trenutniKorisnik['korisnickoIme']), termini, treninzi, programi)),
        '8': lambda: ponistiRezervaciju(rezervacije, termini),
        '0': lambda: izlaz()
    }

    meniOpcije = {
        'naziv': "registrovan",
        'nazivIspis': "Registrovan Meni",
        'opcijeIspis': "1. Odjava\n2. Pregled dostupnih programa treninga\n3. Pretrazi programe\n4. Pregled dostupnih termina\n5. Pretrazi termine\n6. Rezervisi mesto\n7. Pregled rezervacija\n8. Ponisti rezervaciju\n0. Izlaz",
        'opcijeUnos': meniFunkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meniRegistrovan'] = meniOpcije

def meniInstruktor():

    meniFunkcije = {
        '1': lambda: odjavaKorisnik(),
        '2': lambda: ispisTabele(programiZaIspis(programi, korisnici, vrsteTreninga, vrstePaketa)),
        '3': lambda: ispisTabele(programiZaIspis(pretraziProgram(programi, vrsteTreninga, vrstePaketa), korisnici, vrsteTreninga, vrstePaketa)),
        '4': lambda: ispisTabele(spojiTermine(treningZaIspis(treninzi, sale, programi), termini)),
        '5': lambda: pokreniMeni('meniPretraziTermin'),
        '6': lambda: rezervacijaMestaInstruktor(rezervacije, termini, treninzi, programi, sale, korisnici, trenutniKorisnik['korisnickoIme']),
        '7': lambda: ispisTabele(rezervacijeZaIspis(pretraziRezervacijeInstruktor(rezervacije, treninzi, termini, programi, trenutniKorisnik['korisnickoIme']), termini, treninzi, programi)),
        '8': lambda: ponistiRezervacijuInstruktor(rezervacije, termini, treninzi, programi, korisnici, trenutniKorisnik['korisnickoIme']),
        '9': lambda: pretraziRezervacije(rezervacije, termini, treninzi, korisnici),
        '10': lambda: aktivacijaClana(korisnici, clanarine),
        '11': lambda: aktivacijaPremiumPaketa(korisnici),
        '12': lambda: izmeniRezervacijuInstruktor(rezervacije, termini, treninzi, programi, korisnici, trenutniKorisnik['korisnickoIme']),
        '0': lambda: izlaz()
    }

    meniOpcije = {
        'naziv': "instruktor",
        'nazivIspis': "Instruktor Meni",
        'opcijeIspis': "1. Odjava\n2. Pregled dostupnih programa treninga\n3. Pretrazi programe\n4. Pregled dostupnih termina\n5. Pretrazi termine\n6. Rezervisi mesto\n7. Pregled rezervacija\n8. Ponisti rezervaciju\n9. Pretraga rezervacija\n10. Aktivacija clana\n11. Aktivacija premium clana\n12. Izmeni rezervacije\n0. Izlaz",
        'opcijeUnos': meniFunkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meniInstruktor'] = meniOpcije

def meniAdmin():

    submenu2_dict = {
        '1': lambda: odjavaKorisnik(),
        '2': lambda: ispisTabele(programiZaIspis(programi, korisnici, vrsteTreninga, vrstePaketa)),
        '3': lambda: ispisTabele(programiZaIspis(pretraziProgram(programi, vrsteTreninga, vrstePaketa), korisnici, vrsteTreninga, vrstePaketa)),
        '4': lambda: ispisTabele(spojiTermine(treningZaIspis(treninzi, sale, programi), termini)),
        '5': lambda: pokreniMeni('meniPretraziTermin'),
        '6': lambda: registracijaInstruktora(korisnici),
        '7': lambda: print('izvestavanje'),
        '8': lambda: mesecnaNagradaLojalnosti(rezervacije, korisnici),
        '9': lambda: pokreniMeni('meniUnosIzmenaBrisanjeProgram'),
        '10': lambda: pokreniMeni('meniUnosIzmenaBrisanjeTrening'),
        '0': lambda: izlaz()
    }

    meniOpcije = {
        'naziv': "admin",
        'nazivIspis': "Admin Meni",
        'opcijeIspis': "1. Odjava\n2. Pregled dostupnih programa treninga\n3. Pretrazi programe\n4. Pregled dostupnih termina\n5. Pretrazi termine\n6. Registracija novih instruktora\n7. Izvestavanje\n8. Mesecna nagrada lojalnosti\n9. Unos Izmena Brisanje Programa\n10. Unos Izmena Brisanje Treninga\n0. Izlaz",
        'opcijeUnos': submenu2_dict,
        'nazad': False,
        'izlaz': True
    }

    menii['meniAdmin'] = meniOpcije

def meniPretraziTermin():

    meniFunkcije = {
        '1': lambda: ispisTabele(spojeniTerminiZaIspis(pretraziTermine(spojiTermine(treninzi, termini), sale, programi, 'idSale'), sale, programi)),
        '2': lambda: ispisTabele(spojeniTerminiZaIspis(pretraziTermine(spojiTermine(treninzi, termini), sale, programi, 'idPrograma'), sale, programi)),
        '3': lambda: ispisTabele(spojeniTerminiZaIspis(pretraziTermine(spojiTermine(treninzi, termini), sale, programi, 'datum'), sale, programi)),
        '4': lambda: ispisTabele(spojeniTerminiZaIspis(pretraziTermine(spojiTermine(treninzi, termini), sale, programi, 'vremePocetka'), sale, programi)),
        '5': lambda: ispisTabele(spojeniTerminiZaIspis(pretraziTermine(spojiTermine(treninzi, termini), sale, programi, 'vremeKraja'), sale, programi)),
        'b': lambda: nazad()
    }

    meniOpcije = {
        'naziv': "pretraziTermin",
        'nazivIspis': "Pretrazi Termin Meni",
        'opcijeIspis': "1. ID Sale\n2. ID programa\n3. Datum\n4. Vreme pocetka\n5. Vreme kraja\nb. Nazad",
        'opcijeUnos': meniFunkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meniPretraziTermin'] = meniOpcije

def meniUnosIzmenaBrisanjeProgram():

    meniFunkcije = {
        '1': lambda: dodajProgram(programi, vrsteTreninga, korisnici, vrstePaketa),
        '2': lambda: izmeniProgram(programi, vrsteTreninga, korisnici, vrstePaketa),
        '3': lambda: brisiProgram(programi),
        'b': lambda: nazad()
    }

    meniOpcije = {
        'naziv': "UnosIzmenaBrisanjePrograma",
        'nazivIspis': "Unos Izmena Brisanje Programa Meni",
        'opcijeIspis': "1. Unos programa treninga\n2. Izmena programa treninga\n3. Brisanje programa treninga\nb. Nazad",
        'opcijeUnos': meniFunkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meniUnosIzmenaBrisanjeProgram'] = meniOpcije

def meniUnosIzmenaBrisanjeTrening():

    meniFunkcije = {
        '1': lambda: dodajTrening(treninzi, sale, programi),
        '2': lambda: izmeniTrening(treninzi, sale, programi),
        '3': lambda: brisiTrening(treninzi),
        'b': lambda: nazad()
    }

    meniOpcije = {
        'naziv': "meniUnosIzmenaBrisanjeTrening",
        'nazivIspis': "Unos Izmena Brisanje Treminga Meni",
        'opcijeIspis': "1. Unos treninga\n2. Izmena treninga\n3. Brisanje treninga\nb. Nazad",
        'opcijeUnos': meniFunkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meniUnosIzmenaBrisanjeTrening'] = meniOpcije

def initiate():
    meniNeregistrovan()
    meniRegistrovan()
    meniInstruktor()
    meniAdmin()
    meniPretraziTermin()
    meniUnosIzmenaBrisanjeProgram()
    meniUnosIzmenaBrisanjeTrening()

def glavniMeni():
    global trenutniKorisnik
    initiate()
    validacijaClanarina(korisnici, clanarine)   #azuriraj clanarine

    if trenutniKorisnik is None:                #nije prijavljen
        pokreniMeni('meniNeregistrovan')
    elif trenutniKorisnik['uloga'] == 0:        #registrovan
        pokreniMeni('meniRegistrovan')
    elif trenutniKorisnik['uloga'] == 1:        #instruktor
        pokreniMeni('meniInstruktor')
    elif trenutniKorisnik['uloga'] == 2:        #admin
        pokreniMeni('meniAdmin')