from funkcije.fajlovi import citajFajl, upisFajl
from funkcije.tabela import ispisTabele
from funkcije.kratakIspis import ispisKorisnika, ispisVrstePaketa, ispisVrsteTreninga, ispisProgrami

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

def dodajProgram(programi, vrsteTreninga, korisnici, vrstePaketa):
    id = str(max([int(idPrograma) for idPrograma in programi.keys()], default=0) + 1)

    while True:
        naziv = input("Unesite naziv programa (b. za Nazad): ")
        if naziv == 'b':
            break

        while True:
            print('Opcije za vrste treninga:')
            ispisVrsteTreninga(vrsteTreninga)

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
            print('Opcije za instruktore:')
            ispisKorisnika(korisnici, 1)

            idInstruktora = input("Unesite Korisnicko ime instruktora: ")
            if idInstruktora in korisnici:
                break
            else:
                print(f'Instruktor sa ovim korisnickim imenom ne postoji. Pokusajte ponovo.')
        
        while True:
            print('Opcije za vrste paketa:')
            ispisVrstePaketa(vrstePaketa)
            
            potrebanPaket = input("Unesite ID potrebnog paketa: ")
            if potrebanPaket in vrstePaketa:
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
        print("Uspesno ste dodali program sa sledecim podacima:")
        ispisTabele({id: programi[id]})
        return True
    return False

def izmeniProgram(programi, vrsteTreninga, korisnici, vrstePaketa):
    while True:
        print('Opcije programa za izmenu:')
        ispisProgrami(programi)
        
        id = input("Unesite ID programa za izmenu (b. za Nazad): ")
        if id == 'b':
            break
        elif id not in programi.keys():
            print("Program sa ovim ID ne postoji.")
            continue

        ispisTabele({id: programi[id]})
                
        while True:
            odgovor = input("Ponuđene opcije:\n1. Naziv\n2. ID vrste treninga\n3. Trajanje\n4. ID instruktora\n5. Potreban paket\n6. Opis\nb. Nazad\nUnesite zeljenu opciju: ")
            
            match odgovor:
                case '1':
                    programi[id]['naziv'] = input("Unesite novi naziv: ")
                case '2':
                    while True:
                        print('Opcije za vrste treninga:')
                        ispisVrsteTreninga(vrsteTreninga)

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
                        print('Opcije za instruktore:')
                        ispisKorisnika(korisnici, 1)

                        idInstruktora = input("Unesite novo Korisnicko ime instruktora: ")
                        if idInstruktora in korisnici:
                            programi[id]['idInstruktora'] = idInstruktora
                            break
                        else:
                            print(f'Instruktor sa ovim korisnickim imenom ne postoji. Pokusajte ponovo.')
                case '5':
                    while True:
                        print('Opcije za vrste paketa:')
                        ispisVrstePaketa(vrstePaketa)

                        potrebanPaket = input("Unesite novi ID potrebnog paketa: ")
                        if potrebanPaket in vrstePaketa:
                            programi[id]['potrebanPaket'] = potrebanPaket
                            break
                        else:
                            print(f'Paket sa ovim ID ne postoji. Pokusajte ponovo.')
                case '6':
                    programi[id]['opis'] = input("Unesite novi opis: ")
                case 'b':
                    return True
    return False

def brisiProgram(programi):
    while True:
        print('Opcije postojecih programa za brisanje:')
        ispisProgrami(programi)

        id = input("Unesite ID programa za brisanje (b. za Nazad): ")
        if id == 'b':
            return False
        elif id in programi.keys():
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
        ispisVrsteTreninga(vrsteTreninga)
        
        kljuc = input('Unesite ID vrste treninga za pretragu: ').strip().lower()
    elif kriterijum == 'potrebanPaket':
        print("Dostupni paketi:")
        ispisVrstePaketa(vrstePaketa)
        
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