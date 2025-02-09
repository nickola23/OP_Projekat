from funkcije.fajlovi import ucitaj_podatke
from funkcije.tabela import ispis_tabele
from funkcije.kratak_ispis import (
    ispis_korisnika, ispis_vrste_paketa, ispis_vrste_treninga, ispis_programi
)

def ucitaj_programe(putanja):
    kljucevi=['id','naziv','id_vrste_treninga','trajanje','id_instruktora','potreban_paket','opis']
    podaci = ucitaj_podatke(putanja, kljucevi)

    # Dodatna obrada podataka
    for program in podaci.values():
        program['id_vrste_treninga'] = int(program['id_vrste_treninga'])
        program['trajanje'] = int(program['trajanje'])
        program['potreban_paket'] = int(program['potreban_paket'])

    return podaci


def dodaj_program(programi, vrste_treninga, korisnici, vrste_paketa):
    novi_id = str(max((int(id_programa) for id_programa in programi.keys()), default=0) + 1)

    while True:
        naziv = input("Unesite naziv programa (b. za Nazad): ")
        if naziv == 'b':
            break

        while True:
            print('Opcije za vrste treninga:')
            ispis_vrste_treninga(vrste_treninga)

            id_vrste_treninga = input("Unesite ID vrste treninga: ")
            if id_vrste_treninga in vrste_treninga:
                break
            print('Vrsta treninga sa ovim ID ne postoji. Pokusajte ponovo.')

        while True:
            try:
                trajanje = int(input("Unesite trajanje programa (u minutima): "))
                if trajanje > 0:
                    break
                print("Trajanje mora biti vece od 0. Pokusajte ponovo.")
            except ValueError:
                print("Trajanje mora biti ceo broj. Pokusajte ponovo.")

        while True:
            print('Opcije za instruktore:')
            ispis_korisnika(korisnici, 1)

            id_instruktora = input("Unesite Korisnicko ime instruktora: ")
            if id_instruktora in korisnici:
                break
            print('Instruktor sa ovim korisnickim imenom ne postoji. Pokusajte ponovo.')

        while True:
            print('Opcije za vrste paketa:')
            ispis_vrste_paketa(vrste_paketa)

            potreban_paket = input("Unesite ID potrebnog paketa: ")
            if potreban_paket in vrste_paketa:
                break
            print('Paket sa ovim ID ne postoji. Pokusajte ponovo.')

        opis = input("Unesite opis programa: ")

        programi[novi_id] = {
            'id': novi_id,
            'naziv': naziv,
            'id_vrste_treninga': id_vrste_treninga,
            'trajanje': trajanje,
            'id_instruktora': id_instruktora,
            'potreban_paket': potreban_paket,
            'opis': opis
        }
        print("Uspesno ste dodali program sa sledecim podacima:")
        ispis_tabele({novi_id: programi[novi_id]})
        return True
    return False


def izmeni_program(programi, vrste_treninga, korisnici, vrste_paketa):
    while True:
        print('Opcije programa za izmenu:')
        ispis_programi(programi)

        id_programa = input("Unesite ID programa za izmenu (b. za Nazad): ")
        if id_programa == 'b':
            break
        if id_programa not in programi.keys():
            print("Program sa ovim ID ne postoji.")
            continue

        ispis_tabele({id_programa: programi[id_programa]})
   
        while True:
            odgovor = input("Ponuđene opcije:\n1. Naziv\n2. ID vrste treninga\n"
                            "3. Trajanje\n4. ID instruktora\n5. Potreban paket\n6. Opis\nb. Nazad\nUnesite zeljenu opciju: ")
            
            match odgovor:
                case '1':
                    programi[id_programa]['naziv'] = input("Unesite novi naziv: ")
                case '2':
                    while True:
                        print('Opcije za vrste treninga:')
                        ispis_vrste_treninga(vrste_treninga)

                        id_vrste_treninga = input("Unesite novi ID vrste treninga: ")
                        if id_vrste_treninga in vrste_treninga:
                            programi[id_programa]['id_vrste_treninga'] = id_vrste_treninga
                            break
                        print(f'Vrsta treninga sa ovim ID ne postoji. Pokusajte ponovo.')
                case '3':
                    while True:
                        try:
                            trajanje = int(input("Unesite novo trajanje programa (u minutima): "))
                            if trajanje > 0:
                                programi[id_programa]['trajanje'] = trajanje
                                break
                            print("Trajanje mora biti vece od 0. Pokusajte ponovo.")
                        except ValueError:
                            print("Trajanje mora biti ceo broj. Pokusajte ponovo.")
                case '4':
                    while True:
                        print('Opcije za instruktore:')
                        ispis_korisnika(korisnici, 1)

                        id_instruktora = input("Unesite novo Korisnicko ime instruktora: ")
                        if id_instruktora in korisnici:
                            programi[id_programa]['id_instruktora'] = id_instruktora
                            break
                        print('Instruktor sa ovim korisnickim '
                              'imenom ne postoji. Pokusajte ponovo.')
                case '5':
                    while True:
                        print('Opcije za vrste paketa:')
                        ispis_vrste_paketa(vrste_paketa)

                        potreban_paket = input("Unesite novi ID potrebnog paketa: ")
                        if potreban_paket in vrste_paketa:
                            programi[id_programa]['potreban_paket'] = potreban_paket
                            break
                        print('Paket sa ovim ID ne postoji. Pokusajte ponovo.')
                case '6':
                    programi[id_programa]['opis'] = input("Unesite novi opis: ")
                case 'b':
                    print('Program uspesno izmenjen.')
                    return True
    return False


def brisi_program(programi):
    while True:
        print('Opcije postojecih programa za brisanje:')
        ispis_programi(programi)

        id_programa = input("Unesite ID programa za brisanje (b. za Nazad): ")
        if id_programa == 'b':
            return False
        if id_programa in programi.keys():
            del programi[id_programa]
            print("Uspesno ste izbrisali program.")
            return True
        print("Program sa ovim ID ne postoji.")
        continue


def pretrazi_program(programi, vrste_treninga, vrste_paketa):
    pretraga = programi

    kriterijumi = (input("Ponuđene opcije:\n1. Vrsta treninga\n2. Trajanje treninga (u minutama)\n"
                        "3. Potreban paket\n4. Naziv programa\nUnesite "
                        "jedan ili više kriterijuma za pretragu (odvojeni zarezom, npr. 1,3):")
                        .strip().split(','))

    for kriterijum in kriterijumi:
        kriterijum = kriterijum.strip()

        if kriterijum == '1':
            print("Dostupne vrste treninga:")
            ispis_vrste_treninga(vrste_treninga)
            while True:
                id_vrste_treninga = input("Unesite ID vrste treninga: ").strip()
                if id_vrste_treninga not in vrste_treninga:
                    print(f"Vrsta treninga sa ID {id_vrste_treninga} ne postoji. Pokušajte ponovo.")
                    continue
                pretraga = {
                    novi_id: podaci
                    for novi_id, podaci in pretraga.items()
                    if str(podaci['id_vrste_treninga']) == id_vrste_treninga
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
                except ValueError: 
                    print("Trajanje mora biti ceo broj. Pokusajte ponovo.")
            pretraga = {
            id_programa: podaci
            for id_programa, podaci in pretraga.items()
            if min_trajanje <= podaci['trajanje'] and  podaci['trajanje'] <= max_trajanje
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
                    novi_id: podaci
                    for novi_id, podaci in pretraga.items()
                    if str(podaci['potreban_paket']) == id_paketa
                }
                break

        elif kriterijum == '4':
            naziv = input("Unesite ključnu reč za pretragu u nazivu programa: ").strip().lower()
            pretraga = {
                id_programa: podaci
                for id_programa, podaci in pretraga.items()
                if naziv in podaci['naziv'].lower()
            }

        else:
            print(f"Kriterijum '{kriterijum}' nije validan. Preskačem ga.")

    return pretraga
