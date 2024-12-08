from funkcije.tabela import ispisTabele
from funkcije.korisnik import prijava, registracija, odjava, ucitajKorisnike
from funkcije.program import ucitajPrograme, izmeniProgram, pretraziProgram, pretraziProgramKriterijum
from funkcije.trening import ucitajTrening
from funkcije.termin import ucitajTermin
from funkcije.fajlovi import upisFajl

putanjaKorisnici = './data/Korisnici.txt'
putanjaProgrami = './data/Program.txt'
putanjaTrening = './data/Trening.txt'
putanjaTermin = './data/Termin.txt'

korisnici = ucitajKorisnike(putanjaKorisnici)
programi = ucitajPrograme(putanjaProgrami)
treninzi = ucitajTrening(putanjaTrening)
termini =  ucitajTermin(putanjaTermin)

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
    print('Izlaz iz programa')

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
        '3': lambda: ispisTabele(programi),
        '4': lambda: ispisTabele(pretraziProgram(programi)),
        '5': lambda: ispisTabele(pretraziProgramKriterijum(programi)),
        '6': lambda: print('pretragaTermina'),
        '0': lambda: izlaz()
    }

    meniOpcije = {
        'naziv': "neregistrovan",
        'nazivIspis': "Neregistrovani Meni",
        'opcijeIspis': "1. Prijava\n2. Registracija\n3. Ispis tabele\n4. Pretrazi programe\n5. Pretrazi programe po Kriterijumu\n6. Pretrazi termine\n0. Izlaz",
        'opcijeUnos': meniFunkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meniNeregistrovan'] = meniOpcije

def meniRegistrovan():

    meniFunkcije = {
        '1': lambda: odjavaKorisnik(),
        '2': lambda: ispisTabele(programi),
        '3': lambda: ispisTabele(pretraziProgram(programi)),
        '4': lambda: ispisTabele(pretraziProgramKriterijum(programi)),
        '5': lambda: print('pretragaTermina'),
        '6': lambda: print('rezervacijaMesta'),
        '7': lambda: print('pregledRezervacija'),
        '8': lambda: print('ponistavanjeRezervacije'),
        '0': lambda: izlaz()
    }

    meniOpcije = {
        'naziv': "registrovan",
        'nazivIspis': "Registrovan Meni",
        'opcijeIspis': "1. Odjava\n2. Ispis tabele\n3. Pretrazi programe\n4. Pretrazi programe po Kriterijumu\n5. Pretrazi termine\n6. Rezervisi mesto\n7. Pregled rezervacija\n8. Ponisti rezervaciju\n0. Izlaz",
        'opcijeUnos': meniFunkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meniRegistrovan'] = meniOpcije

def meniInstruktor():

    meniFunkcije = {
        '1': lambda: odjavaKorisnik(),
        '2': lambda: ispisTabele(programi),
        '3': lambda: ispisTabele(pretraziProgram(programi)),
        '4': lambda: ispisTabele(pretraziProgramKriterijum(programi)),
        '5': lambda: print('pretragaTermina'),
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
        'opcijeIspis': "1. Odjava\n2. Ispis tabele\n3. Pretrazi programe\n4. Pretrazi programe po Kriterijumu\n5. Pretrazi termine\n6. Rezervisi mesto\n7. Pregled rezervacija\n8. Ponisti rezervaciju\n9. Pretraga rezervacija\n10. Aktivacija clana\n11. Aktivacija premium clana\n12. Izmeni rezervacije\n0. Izlaz",
        'opcijeUnos': meniFunkcije,
        'nazad': False,
        'izlaz': True
    }

    menii['meniInstruktor'] = meniOpcije

def meniAdmin():

    submenu2_dict = {
        '1': lambda: odjavaKorisnik(),
        '2': lambda: ispisTabele(programi),
        '3': lambda: ispisTabele(pretraziProgram(programi)),
        '4': lambda: ispisTabele(pretraziProgramKriterijum(programi)),
        '5': lambda: print('pretragaTermina'),
        '6': lambda: print('registracijaNovihInstruktora.'),
        '7': lambda: print('izvestavanje'),
        '8': lambda: print('mesecnNagradaLojalnosti'),
        '9': lambda: print('prikazMestaMatrica'),
        '10': lambda: print('promenaPaketaClana'),
        '11': lambda: print('UnosizmenaBrisanjeProgramaTreninga'),
        '12': lambda: print('UnosizmenaBrisanjeTreninga'),
        '0': lambda: izlaz()
    }

    meniOpcije = {
        'naziv': "admin",
        'nazivIspis': "Admin Meni",
        'opcijeIspis': "1. Odjava\n2. Ispis tabele\n3. Pretrazi programe\n4. Pretrazi programe po Kriterijumu\n5. Pretrazi termine\n6. Registracija novih instruktora\n7. Izvestavanje\n8. Mesecna nagrada lojalnosti\n9. Prikaz mesta matrica\n10. Promena paketa clana\n11. Unos Izmena Brisanje programa treninga\n12. Unos izmena brisanje treninga\n0. Izlaz",
        'opcijeUnos': submenu2_dict,
        'nazad': False,
        'izlaz': True
    }

    menii['meniAdmin'] = meniOpcije

def initiate():
    meniNeregistrovan()
    meniRegistrovan()
    meniInstruktor()
    meniAdmin()

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