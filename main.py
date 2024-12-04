from funkcije.tabela import ispisTabele
from funkcije.korisnik import prijava, registracija, odjava, ucitajKorisnike
from funkcije.program import ucitajPrograme, izmeniProgram, pretraziProgram, pretraziProgramKriterijum
from funkcije.trening import ucitajTrening
from funkcije.termin import ucitajTermin

putanjaKorisnici = './data/Korisnici.txt'
putanjaProgrami = './data/Program.txt'
putanjaTrening = './data/Trening.txt'
putanjaTermin = './data/Termin.txt'

korisnici = ucitajKorisnike(putanjaKorisnici)
programi = ucitajPrograme(putanjaProgrami)
treninzi = ucitajTrening(putanjaTrening)
termini =  ucitajTermin(putanjaTermin)

trenutniKorisnik = None

def prijavaKorisnik(korisnici):
    global trenutniKorisnik
    trenutniKorisnik = prijava(korisnici, trenutniKorisnik)

def registracijaKorisnik(korisnici):
    global trenutniKorisnik
    trenutniKorisnik = registracija(korisnici)

def odjavaKorisnik():
    global trenutniKorisnik
    trenutniKorisnik = odjava()

def izlaz():
    print("Izlaz iz programa.")
    exit(0)

menii = {
    "pocetni": {
        "prijava": lambda: prijavaKorisnik(korisnici, trenutniKorisnik),
        "registracija": lambda: registracijaKorisnik(korisnici),
        "pregledPrograma": lambda: ispisTabele(programi),
        "pretragaPrograma": lambda: ispisTabele(pretraziProgram(programi)),
        "naprednaPretraga": lambda: ispisTabele(pretraziProgramKriterijum(programi)),
        "pretragaTermina": lambda: print('pretragaTermina'),
        "izlaz": lambda: izlaz
    },
    "neregistrovan": 'ispisiMeni(neregistrovan)',
    "registrovanClan": 'ispisiMeni(registrovanClan)',
    "registrovanInstruktor": 'ispisiMeni(registrovanInstruktor)',
    "registrovanAdmin": 'ispisiMeni(registrovanAdmin)',
}

def ispisiMeni(meni):
    print('Izaberite stavku iz menija: ')
    for i, (naziv, _) in enumerate(meni.items()):
        print(f'{i}: {naziv}')

def unosMeni(meni):
    try:
        izbor = int(input('Izaberite broj stavke >>> '))
        if izbor < 0 or izbor >= len(meni):
            print('Nevazeci unos, pokušajte ponovo.')
        else:
            stavka = list(meni.values())[izbor]
            stavka()
    except Exception as e: 
        print('Greska prilikom izbora\n', e)

def main():
    trenutniMeni = menii['pocetni']

    ispisiMeni(trenutniMeni)
    unosMeni(trenutniMeni)

if __name__ == '__main__':
    main()