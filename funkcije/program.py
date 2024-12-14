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

def dodajProgram(programi):
    while True:
        id = input("Unesite ID programa: ")
        if id not in programi.keys():
            naziv = input("Unesite naziv programa: ")
            idVrsteTreninga = int(input("Unesite ID vrste treninga: "))
            trajanje = int(input("Unesite trajanje programa (u minutima): "))
            idInstruktora = input("Unesite Korisnicko ime instruktora: ")
            potrebanPaket = int(input("Unesite potreban paket: "))
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
        else:
            print("Program sa ovim ID vec postoji.")
            continue

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

def izmeniProgram(programi):
    while True:
        id = input("Unesite ID programa za izmenu: ")
        if id in programi.keys():
            ispisTabele({id: programi[id]})
            
            while True:
                odgovor = input("1. Naziv\n2. ID vrste treninga\n3. Trajanje\n4. ID instruktora\n5. Potreban paket\n6. Opis\nb. Nazad\nIzaberite podatak koji zelite da izmenite: ")
                
                match odgovor:
                    case '1':
                        programi[id]['naziv'] = input("Unesite novi naziv: ")
                    case '2':
                        programi[id]['idVrsteTreninga'] = int(input("Unesite novi ID vrste treninga: "))
                    case '3':
                        programi[id]['trajanje'] = int(input("Unesite novo trajanje (u minutima): "))
                    case '4':
                        programi[id]['idInstruktora'] = input("Unesite Korisnicko ime instruktora: ")
                    case '5':
                        programi[id]['potrebanPaket'] = int(input("Unesite novi potreban paket: "))
                    case '6':
                        programi[id]['opis'] = input("Unesite novi opis: ")
                    case 'b':
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
        min = eval(input('Unesite minimalno trajanje treninga u minutima: '))
        max = eval(input('Unesite maksimalno trajanje treninga u minutima: '))
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