def ispis_vrste_treninga(vrste_treninga):
    for id, podaci in vrste_treninga.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_korisnika(korisnici, uloga=3):
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
    for id, podaci in vrste_paketa.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_programi(programi):
    for id, podaci in programi.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_sale(sale):
    for id, podaci in sale.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_treninzi(treninzi):
    for id, podaci in treninzi.items():
        print(f"ID: {podaci['id']} - od {podaci['vreme_pocetka'].strftime('%H:%M')} do {podaci['vreme_kraja'].strftime('%H:%M')}")


def ispis_mesta(rezervacije):
    for id, podaci in rezervacije.items():
        print(f"ID: {podaci['oznaka_reda_kolone']} - {podaci['id_korisnika']} - {podaci['id_termina']} - {podaci['datum']}")
