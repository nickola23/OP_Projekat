from funkcije.fajlovi import citaj_fajl, upis_fajl
from funkcije.tabela import ispis_tabele
from funkcije.kratakIspis import ispis_korisnika, ispis_vrste_paketa, ispis_vrste_treninga, ispis_programi

def ucitaj_programe(putanja):
    fajl = citaj_fajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, naziv, idvrste_treninga, trajanje, id_instruktora, potreban_paket, opis = red.split('|')
            podaci[id] = {
                'id':id,
                'naziv': naziv,
                'idvrste_treninga': eval(idvrste_treninga),
                'trajanje': eval(trajanje),
                'id_instruktora': id_instruktora,
                'potreban_paket': eval(potreban_paket),
                'opis': opis
            }
            
    return podaci

def dodaj_program(programi, vrste_treninga, korisnici, vrste_paketa):
    id = str(max([int(id_programa) for id_programa in programi.keys()], default=0) + 1)

    while True:
        naziv = input("Unesite naziv programa (b. za Nazad): ")
        if naziv == 'b':
            break

        while True:
            print('Opcije za vrste treninga:')
            ispis_vrste_treninga(vrste_treninga)

            idvrste_treninga = input("Unesite ID vrste treninga: ")
            if idvrste_treninga in vrste_treninga:
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
            ispis_korisnika(korisnici, 1)

            id_instruktora = input("Unesite Korisnicko ime instruktora: ")
            if id_instruktora in korisnici:
                break
            else:
                print(f'Instruktor sa ovim korisnickim imenom ne postoji. Pokusajte ponovo.')
        
        while True:
            print('Opcije za vrste paketa:')
            ispis_vrste_paketa(vrste_paketa)
            
            potreban_paket = input("Unesite ID potrebnog paketa: ")
            if potreban_paket in vrste_paketa:
                break
            else:
                print(f'Paket sa ovim ID ne postoji. Pokusajte ponovo.')

        opis = input("Unesite opis programa: ")
        
        programi[id] = {
            'id': id,
            'naziv': naziv,
            'idvrste_treninga': idvrste_treninga,
            'trajanje': trajanje,
            'id_instruktora': id_instruktora,
            'potreban_paket': potreban_paket,
            'opis': opis
        }
        print("Uspesno ste dodali program sa sledecim podacima:")
        ispis_tabele({id: programi[id]})
        return True
    return False

def izmeni_program(programi, vrste_treninga, korisnici, vrste_paketa):
    while True:
        print('Opcije programa za izmenu:')
        ispis_programi(programi)
        
        id = input("Unesite ID programa za izmenu (b. za Nazad): ")
        if id == 'b':
            break
        elif id not in programi.keys():
            print("Program sa ovim ID ne postoji.")
            continue

        ispis_tabele({id: programi[id]})
                
        while True:
            odgovor = input("Ponuđene opcije:\n1. Naziv\n2. ID vrste treninga\n3. Trajanje\n4. ID instruktora\n5. Potreban paket\n6. Opis\nb. Nazad\nUnesite zeljenu opciju: ")
            
            match odgovor:
                case '1':
                    programi[id]['naziv'] = input("Unesite novi naziv: ")
                case '2':
                    while True:
                        print('Opcije za vrste treninga:')
                        ispis_vrste_treninga(vrste_treninga)

                        idvrste_treninga = input("Unesite novi ID vrste treninga: ")
                        if idvrste_treninga in vrste_treninga:
                            programi[id]['idvrste_treninga'] = idvrste_treninga
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
                        ispis_korisnika(korisnici, 1)

                        id_instruktora = input("Unesite novo Korisnicko ime instruktora: ")
                        if id_instruktora in korisnici:
                            programi[id]['id_instruktora'] = id_instruktora
                            break
                        else:
                            print(f'Instruktor sa ovim korisnickim imenom ne postoji. Pokusajte ponovo.')
                case '5':
                    while True:
                        print('Opcije za vrste paketa:')
                        ispis_vrste_paketa(vrste_paketa)

                        potreban_paket = input("Unesite novi ID potrebnog paketa: ")
                        if potreban_paket in vrste_paketa:
                            programi[id]['potreban_paket'] = potreban_paket
                            break
                        else:
                            print(f'Paket sa ovim ID ne postoji. Pokusajte ponovo.')
                case '6':
                    programi[id]['opis'] = input("Unesite novi opis: ")
                case 'b':
                    print('Program uspesno izmenjen.')
                    return True
    return False

def brisi_program(programi):
    while True:
        print('Opcije postojecih programa za brisanje:')
        ispis_programi(programi)

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

def pretrazi_program(programi, vrste_treninga, vrste_paketa):
    pretraga = programi

    kriterijumi = input("Ponuđene opcije:\n1. Vrsta treninga\n2. Trajanje treninga (u minutama)\n3. Potreban paket\n4. Naziv programa\nUnesite jedan ili više kriterijuma za pretragu (odvojeni zarezom, npr. 1,3):").strip().split(',')

    for kriterijum in kriterijumi:
        kriterijum = kriterijum.strip()
        
        if kriterijum == '1':
            print("Dostupne vrste treninga:")
            ispis_vrste_treninga(vrste_treninga)
            while True:
                idvrste_treninga = input("Unesite ID vrste treninga: ").strip()
                if idvrste_treninga not in vrste_treninga:
                    print(f"Vrsta treninga sa ID {idvrste_treninga} ne postoji. Pokušajte ponovo.")
                    continue
                pretraga = {
                    id: podaci
                    for id, podaci in pretraga.items()
                    if str(podaci['idvrste_treninga']) == idvrste_treninga
                }
                break

        elif kriterijum == '2':
            while True:
                try:
                    min_trajanje = int(input("Unesite minimalno trajanje treninga u minutima: "))
                    max_trajanje = int(input("Unesite maksimalno trajanje treninga u minutima: "))
                    if min_trajanje < 0 or max_trajanje < 0:
                        print('Trajanje mora biti vece od 0. Pokusajte ponovo.')
                        continue 
                    break 
                except ValueError: print("Trajanje mora biti ceo broj. Pokusajte ponovo.")
            pretraga = {
            id: podaci
            for id, podaci in pretraga.items()
            if min_trajanje <= podaci['trajanje'] <= max_trajanje
        }

        elif kriterijum == '3':
            print("Dostupni paketi:")
            ispis_vrste_paketa(vrste_paketa)
            while True:
                id_paketa = input("Unesite ID paketa: ").strip()
                if id_paketa not in vrste_paketa:
                    print(f"Paket sa ID {id_paketa} ne postoji. Pokušajte ponovo.")
                    continue
                pretraga = {
                    id: podaci
                    for id, podaci in pretraga.items()
                    if str(podaci['potreban_paket']) == id_paketa
                }
                break

        elif kriterijum == '4':
            naziv = input("Unesite ključnu reč za pretragu u nazivu programa: ").strip().lower()
            pretraga = {
                id: podaci
                for id, podaci in pretraga.items()
                if naziv in podaci['naziv'].lower()
            }

        else:
            print(f"Kriterijum '{kriterijum}' nije validan. Preskačem ga.")

    return pretraga