"""
Modul za upravljanje kratkim ispisom podataka.

Sadrži funkcije za kratak ispis:
korisnika, programa, sale, treninga, mesta, vrste treninga, vrste paketa.
"""
def ispis_vrste_treninga(vrste_treninga):
    """
    Ispisuje sve vrste treninga sa njihovim ID-jem i nazivom.

    Args:
        vrste_treninga (dict): Rečnik sa podacima o vrstama treninga
    """
    for _, podaci in vrste_treninga.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_korisnika(korisnici, uloga=3):
    """
    Ispisuje korisnike na osnovu njihove uloge.

    Args:
        korisnici (dict): Rečnik sa podacima o korisnicima
        uloga (int, opcionalno): Filtrira korisnike prema ulozi.
    """
    if uloga == 3:
        for korisnicko_ime, podaci in korisnici.items():
            ime = podaci['ime']
            prezime = podaci['prezime']
            print(f"{korisnicko_ime} - {ime} {prezime}")
    else:
        for korisnicko_ime, podaci in korisnici.items():
            if podaci['uloga'] == uloga:
                ime = podaci['ime']
                prezime = podaci['prezime']
                print(f"{korisnicko_ime} - {ime} {prezime}")


def ispis_vrste_paketa(vrste_paketa):
    """
    Ispisuje sve vrste paketa sa njihovim ID-jem i nazivom.

    Args:
        vrste_paketa (dict): Rečnik sa podacima o vrstama paketa.
    """
    for _, podaci in vrste_paketa.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_programi(programi):
    """
    Ispisuje sve programe sa njihovim ID-jem i nazivom.

    Args:
        programi (dict): Rečnik sa podacima o programima.
    """
    for _, podaci in programi.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_sale(sale):
    """
    Ispisuje sve sale sa njihovim ID-jem i nazivom.

    Args:
        sale (dict): Rečnik sa podacima o salama.
    """
    for _, podaci in sale.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_treninzi(treninzi):
    """
    Ispisuje sve treninge sa njihovim ID-jem, vremenom početka i kraja.

    Args:
        treninzi (dict): Rečnik sa podacima o treninzima.
    """
    for _, podaci in treninzi.items():
        print(f"ID: {podaci['id']} - od {podaci['vreme_pocetka'].strftime('%H:%M')} "
                                   f"do {podaci['vreme_kraja'].strftime('%H:%M')}")


def ispis_mesta(rezervacije):
    """
    Ispisuje sve rezervacije sa njihovim ID-jem mesta, ID-jem korisnika, ID-jem termina i datumom.

    Args:
        rezervacije (dict): Rečnik sa podacima o rezervacijama.
    """
    for _, podaci in rezervacije.items():
        print(f"ID: {podaci['oznaka_reda_kolone']} - {podaci['id_korisnika']} "
                                                 f"- {podaci['id_termina']} - {podaci['datum']}")
