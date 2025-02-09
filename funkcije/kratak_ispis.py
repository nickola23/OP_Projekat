def ispis_vrste_treninga(vrste_treninga):
    for _, podaci in vrste_treninga.items():
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
    for _, podaci in vrste_paketa.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_programi(programi):
    for _, podaci in programi.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_sale(sale):
    for _, podaci in sale.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")


def ispis_treninzi(treninzi):
    for _, podaci in treninzi.items():
        print(f"ID: {podaci['id']} - od {podaci['vreme_pocetka'].strftime('%H:%M')} "
                                   f"do {podaci['vreme_kraja'].strftime('%H:%M')}")


def ispis_mesta(rezervacije):
    for _, podaci in rezervacije.items():
        print(f"ID: {podaci['oznaka_reda_kolone']} - {podaci['id_korisnika']} "
                                                 f"- {podaci['id_termina']} - {podaci['datum']}")
