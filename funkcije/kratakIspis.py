def ispisVrsteTreninga(vrsteTreninga):
    for id, podaci in vrsteTreninga.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")

def ispisKorisnika(korisnici, uloga=3):
    if uloga == 3:
        for korisnickoIme, podaci in korisnici.items():
            ime = podaci['ime']
            prezime = podaci['prezime']
            print(f"{korisnickoIme} - {ime} {prezime}")
    else:
        for korisnickoIme, podaci in korisnici.items():
            if podaci['uloga'] == uloga:
                ime = podaci['ime']
                prezime = podaci['prezime']
                print(f"{korisnickoIme} - {ime} {prezime}")

def ispisVrstePaketa(vrstePaketa):
    for id, podaci in vrstePaketa.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")

def ispisProgrami(programi):
    for id, podaci in programi.items():
        print(f"ID: {podaci['id']} - {podaci['naziv']}")