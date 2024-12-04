from funkcije.fajlovi import citajFajl, upisFajl

def ucitajPrograme(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, naziv, idVrsteTreninga, trajanje, idInstruktora, potrebanPaket, opis = red.split('|')
            podaci[id] = {
                'id': eval(id),
                'naziv': naziv,
                'idVrsteTreninga': eval(idVrsteTreninga),
                'trajanje': eval(trajanje),
                'idInstruktora': eval(idInstruktora),
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
            idInstruktora = int(input("Unesite ID instruktora: "))
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
            print(f"Trenutni podaci za program sa ID {id}:")
            print(f"Naziv: {programi[id]['naziv']}")
            print(f"ID vrste treninga: {programi[id]['idVrsteTreninga']}")
            print(f"Trajanje (u minutima): {programi[id]['trajanje']}")
            print(f"ID instruktora: {programi[id]['idInstruktora']}")
            print(f"Potreban paket: {programi[id]['potrebanPaket']}")
            print(f"Opis: {programi[id]['opis']}")
            
            while True:
                odgovor = input("1. Naziv\n2. ID vrste treninga\n3. Trajanje\n4. ID instruktora\n5. Potreban paket\n6. Opis\n0. Izlaz\nIzaberite podatak koji zelite da izmenite: ")
                
                match odgovor:
                    case '1':
                        programi[id]['naziv'] = input("Unesite novi naziv: ")
                    case '2':
                        programi[id]['idVrsteTreninga'] = int(input("Unesite novi ID vrste treninga: "))
                    case '3':
                        programi[id]['trajanje'] = int(input("Unesite novo trajanje (u minutima): "))
                    case '4':
                        programi[id]['idInstruktora'] = int(input("Unesite novi ID instruktora: "))
                    case '5':
                        programi[id]['potrebanPaket'] = int(input("Unesite novi potreban paket: "))
                    case '6':
                        programi[id]['opis'] = input("Unesite novi opis: ")
                    case '0':
                        return True
        else:
            print("Program sa ovim ID ne postoji.")
            continue

def pretraziProgram(programi, kriterijum = ''):
    pretraga = {}
    kljuc = input('Unesite kljucnu rec za pretragu: ').lower()

    for id, podaci in programi.items():
        for vrednost in podaci.values():
            if kriterijum:
                if kriterijum == 'naziv' and kljuc in str(podaci['naziv']).lower():
                    pretraga[id] = podaci
                    break
                elif kriterijum == 'idVrsteTreninga' and str(podaci['idVrsteTreninga']).lower() == kljuc:
                    pretraga[id] = podaci
                    break
                elif kriterijum == 'trajanje' and str(podaci['trajanje']).lower() == kljuc:
                    pretraga[id] = podaci
                    break
                elif kriterijum == 'idInstruktora' and str(podaci['idInstruktora']).lower() == kljuc:
                    pretraga[id] = podaci
                    break
                elif kriterijum == 'potrebanPaket' and str(podaci['potrebanPaket']).lower() == kljuc:
                    pretraga[id] = podaci
                    break
                else:
                    break
            else:
                if kljuc in str(vrednost).lower():
                    pretraga[id] = podaci
    
    if not pretraga:
        return {}
    else:
        return pretraga

def pretraziProgramKriterijum(programi):
    while True:
        pretraga = {}
        kriterijum = input("Odaberite kriterijum pretrage:\n1. Naziv\n2. ID vrste treninga\n3. Trajanje\n4. ID instruktora\n5. Potreban paket\n0. Izlaz\nIzaberite kriterijum: ")
        
        match kriterijum:
            case '1':
                pretraga |= pretraziProgram(programi, 'naziv')
                break
            case '2':
                pretraga |= pretraziProgram(programi, 'idVrsteTreninga')
                break
            case '3':
                pretraga |= pretraziProgram(programi, 'trajanje')
                break
            case '4':
                pretraga |= pretraziProgram(programi, 'idInstruktora')
                break
            case '5':
                pretraga |= pretraziProgram(programi, 'potrebanPaket')
                break
            case _:
                print("Neispravan unos. Ponovite.")
                continue
        
    if not pretraga:
        return {}
    else:
        return pretraga