from funkcije.tabela import ispisTabele
from funkcije.korisnik import prijava, registracija, odjava, ucitajKorisnike
from funkcije.program import ucitajPrograme, dodajProgram, izmeniProgram, brisiProgram, pretraziProgram
from funkcije.trening import ucitajTrening, dodajTrening, izmeniTrening, brisiTrening
from funkcije.termin import ucitajTermin, pretraziTermin, spojiPodatke
from funkcije.fajlovi import upisFajl
from funkcije.vrstaTreninga import ucitajVrsteTreninga
from funkcije.vrstaPaketa import ucitajVrstePaketa
from funkcije.sala import ucitajSale
from funkcije.zaIspis import programiZaIspis, treningZaIspis

putanjaVrsteTreninga = './data/VrstaTreninga.txt'
putanjaVrstePaketa = './data/VrstaPaketa.txt'
putanjaKorisnici = './data/Korisnici.txt'
putanjaProgrami = './data/Program.txt'
putanjaTrening = './data/Trening.txt'
putanjaTermin = './data/Termin.txt'
putanjaSala = './data/Sala.txt'

vrsteTreninga = ucitajVrsteTreninga(putanjaVrsteTreninga)
vrstePaketa = ucitajVrstePaketa(putanjaVrstePaketa)
korisnici = ucitajKorisnike(putanjaKorisnici)
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
    upisFajl(putanjaKorisnici, korisnici)
    upisFajl(putanjaProgrami, programi)
    upisFajl(putanjaTrening, treninzi)
    upisFajl(putanjaTermin, termini)

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
        '4': lambda: pokreniMeni('meniPretraziProgram'),
        '5': lambda: ispisTabele(spojiPodatke(treningZaIspis(treninzi, sale, programi), termini)),
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
        '3': lambda: pokreniMeni('meniPretraziProgram'),
        '4': lambda: ispisTabele(spojiPodatke(treningZaIspis(treninzi, sale, programi), termini)),
        '5': lambda: pokreniMeni('meniPretraziTermin'),
        '6': lambda: print('rezervacijaMesta'),
        '7': lambda: print('pregledRezervacija'),
        '8': lambda: print('ponistavanjeRezervacije'),
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
        '3': lambda: pokreniMeni('meniPretraziProgram'),
        '4': lambda: ispisTabele(spojiPodatke(treningZaIspis(treninzi, sale, programi), termini)),
        '5': lambda: pokreniMeni('meniPretraziTermin'),
        '6': lambda: print('rezervacijaMesta'),
        '7': lambda: print('pregledRezervacija'),
        '8': lambda: print('ponistavanjeRezervacije'),
        '9': lambda: print('preatragaRezervacija'),
        '10': lambda: print('aktivacijaClana'),
        '11': lambda: print('aktivacijaPremiumClana'),
        '12': lambda: print('izmenaRezervacije'),
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
        '3': lambda: pokreniMeni('meniPretraziProgram'),
        '4': lambda: ispisTabele(spojiPodatke(treningZaIspis(treninzi, sale, programi), termini)),
        '5': lambda: pokreniMeni('meniPretraziTermin'),
        '6': lambda: print('registracijaNovihInstruktora.'),
        '7': lambda: print('izvestavanje'),
        '8': lambda: print('mesecnNagradaLojalnosti'),
        '9': lambda: print('prikazMestaMatrica'),
        '10': lambda: print('promenaPaketaClana'),
        '11': lambda: dodajProgram(programi),                   #Unos, izmena, brisanje programa treninga - kreiraj podmeni
        '12': lambda: izmeniProgram(programi),
        '13': lambda: brisiProgram(programi),
        '14': lambda: dodajTrening(treninzi),                   #Unos, izmena, brisanje treninga - kreiraj podmeni
        '15': lambda: izmeniTrening(treninzi),
        '16': lambda: brisiTrening(treninzi),
        '0': lambda: izlaz()
    }

    meniOpcije = {
        'naziv': "admin",
        'nazivIspis': "Admin Meni",
        'opcijeIspis': "1. Odjava\n2. Pregled dostupnih programa treninga\n3. Pretrazi programe\n4. Pregled dostupnih termina\n5. Pretrazi termine\n6. Registracija novih instruktora\n7. Izvestavanje\n8. Mesecna nagrada lojalnosti\n9. Prikaz mesta matrica\n10. Promena paketa clana\n11. Unos programa treninga\n12. Izmena programa treninga\n13. Brisanje programa treninga\n14. Dodaj trening\n15. Izmeni trening\n16. Brisanje treninga\n0. Izlaz",
        'opcijeUnos': submenu2_dict,
        'nazad': False,
        'izlaz': True
    }

    menii['meniAdmin'] = meniOpcije

def meniPretraziProgram():

    meniFunkcije = {
        '1': lambda: pretraziProgram(programi, 'naziv'),
        '2': lambda: pretraziProgram(programi, 'idVrsteTreninga'),
        '3': lambda: pretraziProgram(programi, 'trajanje'),
        '4': lambda: pretraziProgram(programi, 'idInstruktora'),
        '5': lambda: pretraziProgram(programi, 'potrebanPaket'),
        'b': lambda: nazad()
    }

    meniOpcije = {
        'naziv': "pretraziProgram",
        'nazivIspis': "Pretrazi Program Meni",
        'opcijeIspis': "1. Naziv\n2. ID vrste treninga\n3. Trajanje\n4. ID instruktora\n5. Potreban paket\nb. Nazad",
        'opcijeUnos': meniFunkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meniPretraziProgram'] = meniOpcije

def meniPretraziTermin():

    meniFunkcije = {
        '1': lambda: pretraziTermin(termini, 'naziv'),
        '2': lambda: pretraziTermin(termini, 'idVrsteTreninga'),
        '3': lambda: pretraziTermin(termini, 'trajanje'),
        '4': lambda: pretraziTermin(termini, 'idInstruktora'),
        '5': lambda: pretraziTermin(termini, 'potrebanPaket'),
        'b': lambda: nazad()
    }

    meniOpcije = {
        'naziv': "pretraziTermin",
        'nazivIspis': "Pretrazi Termin Meni",
        'opcijeIspis': "1. Naziv\n2. ID vrste treninga\n3. Trajanje\n4. ID instruktora\n5. Potreban paket\nb. Nazad",
        'opcijeUnos': meniFunkcije,
        'nazad': True,
        'izlaz': False
    }

    menii['meniPretraziTermin'] = meniOpcije

def initiate():
    meniNeregistrovan()
    meniRegistrovan()
    meniInstruktor()
    meniAdmin()
    meniPretraziProgram()
    meniPretraziTermin()

def glavniMeni():
    initiate()
    global trenutniKorisnik

    if trenutniKorisnik is None:                #nije prijavljen
        pokreniMeni('meniNeregistrovan')
    elif trenutniKorisnik['uloga'] == 0:        #registrovan
        pokreniMeni('meniRegistrovan')
    elif trenutniKorisnik['uloga'] == 1:        #instruktor
        pokreniMeni('meniInstruktor')
    elif trenutniKorisnik['uloga'] == 2:        #admin
        pokreniMeni('meniAdmin')