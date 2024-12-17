from funkcije.fajlovi import citajFajl, upisFajl
from funkcije.tabela import ispisTabele

def ucitajPrograme(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, naziv, idVrsteTreninga, trajanje, idInstruktora, potrebanPaket, opis = red.split('|')
            podaci[id] = {
                'id':id,
                'naziv': naziv,
                'idVrsteTreninga': eval(idVrsteTreninga),
                'trajanje': eval(trajanje),
                'idInstruktora': idInstruktora,
                'potrebanPaket': eval(potrebanPaket),
                'opis': opis
            }
            
    return podaci

def dodajProgram(programi, vrsteTreninga, korisnici, paketi):
    while True:
        id = input("Unesite ID programa: ")
        if id not in programi.keys():
            break
        else:
            print("Program sa ovim ID vec postoji. Pokusajte ponovo.")

    naziv = input("Unesite naziv programa: ")

    while True:
        idVrsteTreninga = input("Unesite ID vrste treninga: ")
        if idVrsteTreninga in vrsteTreninga:
            break
        else:
            print(f'Vrsta treninga sa ovim ID ne postoji. Pokusajte ponovo.')

    while True:
        try:
            trajanje = int(input("Unesite trajanje programa (u minutima): "))
            if trajanje > 0:
                break
            else:
                print("Trajanje mora biti vece od 0. Pokusajte ponovo.")
        except Exception:
            print("Trajanje mora biti ceo broj. Pokusajte ponovo.")
            continue

    while True:
        idInstruktora = input("Unesite Korisnicko ime instruktora: ")
        if idInstruktora in korisnici:
            break
        else:
            print(f'Instruktor sa ovim korisnickim imenom ne postoji. Pokusajte ponovo.')
    
    while True:
        potrebanPaket = input("Unesite ID potrebnog paketa: ")
        if potrebanPaket in paketi:
            break
        else:
            print(f'Paket sa ovim ID ne postoji. Pokusajte ponovo.')

    opis = input("Unesite opis programa: ")
    
    programi[id] = {
        'id': id,
        'naziv': naziv,
        'idVrsteTreninga': idVrsteTreninga,
        'trajanje': trajanje,
        'idInstruktora': idInstruktora,
        'potrebanPaket': potrebanPaket,
        'opis': opis
    }

    print("Uspesno ste dodali program.")
    return True

def izmeniProgram(programi, vrsteTreninga, korisnici, paketi):
    while True:
        id = input("Unesite ID programa za izmenu: ")
        if id in programi.keys():
            break
        else:
            print("Program sa ovim ID ne postoji.")

    ispisTabele({id: programi[id]})
            
    while True:
        odgovor = input("1. Naziv\n2. ID vrste treninga\n3. Trajanje\n4. ID instruktora\n5. Potreban paket\n6. Opis\nb. Nazad\nIzaberite podatak koji zelite da izmenite: ")
        
        match odgovor:
            case '1':
                programi[id]['naziv'] = input("Unesite novi naziv: ")
            case '2':
                while True:
                    idVrsteTreninga = input("Unesite novi ID vrste treninga: ")
                    if idVrsteTreninga in vrsteTreninga:
                        programi[id]['idVrsteTreninga'] = idVrsteTreninga
                        break
                    else:
                        print(f'Vrsta treninga sa ovim ID ne postoji. Pokusajte ponovo.')
            case '3':
                while True:
                    try:
                        trajanje = int(input("Unesite novo trajanje programa (u minutima): "))
                        if trajanje > 0:
                            programi[id]['trajanje'] = trajanje
                            break
                        else:
                            print("Trajanje mora biti vece od 0. Pokusajte ponovo.")
                    except Exception:
                        print("Trajanje mora biti ceo broj. Pokusajte ponovo.")
                
            case '4':
                while True:
                    idInstruktora = input("Unesite novo Korisnicko ime instruktora: ")
                    if idInstruktora in korisnici:
                        programi[id]['idInstruktora'] = idInstruktora
                        break
                    else:
                        print(f'Instruktor sa ovim korisnickim imenom ne postoji. Pokusajte ponovo.')
            case '5':
                while True:
                    potrebanPaket = input("Unesite novi ID potrebnog paketa: ")
                    if potrebanPaket in paketi:
                        programi[id]['potrebanPaket'] = potrebanPaket
                        break
                    else:
                        print(f'Paket sa ovim ID ne postoji. Pokusajte ponovo.')
            case '6':
                programi[id]['opis'] = input("Unesite novi opis: ")
            case 'b':
                return True

def brisiProgram(programi):
    while True:
        id = input("Unesite ID programa za brisanje: ")
        if id in programi.keys():
            del programi[id]
            print("Uspesno ste izbrisali program.")
            return True
        else:
            print("Program sa ovim ID ne postoji.")
            continue

def pretraziProgram(programi, vrsteTreninga, vrstePaketa, kriterijum = ''):
    pretraga = {}
    if kriterijum == 'idVrsteTreninga':
        print("Dostupne vrste treninga:")
        for id, podaci in vrsteTreninga.items():
            print(f"ID: {podaci.get('id', 'Nepoznato')} - {podaci.get('naziv', 'Nepoznato')}")
        
        kljuc = input('Unesite ID vrste treninga za pretragu: ').strip().lower()
    elif kriterijum == 'potrebanPaket':
        print("Dostupni paketi:")
        for id, podaci in vrstePaketa.items():
            print(f"ID: {podaci.get('id', 'Nepoznato')} - {podaci.get('naziv', 'Nepoznato')}")
        
        kljuc = input('Unesite ID paketa za pretragu: ').strip().lower()
    elif kriterijum == 'trajanje':
        while True:
            try:
                min = int(input('Unesite minimalno trajanje treninga u minutima: '))
                max = int(input('Unesite maksimalno trajanje treninga u minutima: '))
                break
            except Exception:
                print(f'Morate uneti ceo broj. Pokusajte ponovo.')
    else:
        kljuc = input('Unesite ključnu reč za pretragu: ').strip().lower()

    for id, podaci in programi.items():
        for vrednost in podaci.values():
            if kriterijum:
                if kriterijum == 'naziv' and kljuc in str(podaci['naziv']).lower():
                    pretraga[id] = podaci
                elif kriterijum == 'idVrsteTreninga' and str(podaci['idVrsteTreninga']).lower() == kljuc:
                    pretraga[id] = podaci
                elif kriterijum == 'trajanje' and podaci['trajanje'] >= min and podaci['trajanje'] <= max:
                    pretraga[id] = podaci
                elif kriterijum == 'potrebanPaket' and str(podaci['potrebanPaket']).lower() == kljuc:
                    pretraga[id] = podaci
            else:
                if kljuc in str(vrednost).lower():
                    pretraga[id] = podaci
    
    return pretraga