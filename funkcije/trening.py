from datetime import datetime
from funkcije.fajlovi import citaj_fajl
from funkcije.tabela import ispis_tabele
from funkcije.kratak_ispis import ispis_sale, ispis_programi, ispis_treninzi

def ucitaj_trening(putanja):
    fajl = citaj_fajl(putanja)
    if fajl is None:
        return {}

    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id_treninga, id_sale, vreme_pocetka, vreme_kraja, dani_nedelje, id_programa= red.split('|')
            podaci[id_treninga] = {
                'id': id_treninga,
                'id_sale': id_sale,
                'vreme_pocetka': datetime.strptime(vreme_pocetka, '%H:%M').time(),
                'vreme_kraja': datetime.strptime(vreme_kraja, '%H:%M').time(),
                'dani_nedelje': dani_nedelje.split(','),
                'id_programa': id_programa
            }

    return podaci


def dodaj_trening(treninzi, sale, programi):
    dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja']
    novi_id = str(max([int(id_treninga) for id_treninga in treninzi.keys()], default=0) + 1)

    while True:
        print('Opcije za sale:')
        ispis_sale(sale)

        id_sale = input("Unesite ID sale (b. za Nazad): ")
        if id_sale == 'b':
            break
        elif id_sale not in sale:
            print('Sala sa ovim ID ne postoji. Pokusajte ponovo.')
            continue

        while True:
            try:
                vreme_pocetka = datetime.strptime(input("Unesite vreme početka (HH:MM): "), '%H:%M').time()
                break
            except Exception:
                print("Pogresan format vremena. Pokusajte ponovo.")

        while True:
            try:
                vreme_kraja = datetime.strptime(input("Unesite vreme kraja (HH:MM): "), '%H:%M').time()
                break
            except Exception:
                print("Pogresan format vremena. Pokusajte ponovo.")

        while True:
            dani_nedelje = input("Unesite dane u nedelji (odvojeni zarezom, npr. ponedeljak,sreda): ").strip().split(',')

            dani_nedelje = [dan.strip().lower() for dan in dani_nedelje]
            nevalidni_dani = [dan for dan in dani_nedelje if dan not in dani]

            if nevalidni_dani:
                print("Niste uneli validne dane u nedelji. Pokušajte ponovo.")
                continue
            else:
                break

        while True:
            print('Opcije za programe:')
            ispis_programi(programi)

            id_programa = input("Unesite ID programa: ")
            if id_programa in programi:
                break
            print('Program sa ovim ID ne postoji. Pokusajte ponovo.')

        treninzi[novi_id] = {
            'id': novi_id,
            'id_sale': id_sale,
            'vreme_pocetka': vreme_pocetka,
            'vreme_kraja': vreme_kraja,
            'dani_nedelje': dani_nedelje,
            'id_programa': id_programa
        }
        print("Uspesno ste dodali trening sa sledecim podacima:")
        ispis_tabele({novi_id: treninzi[novi_id]})
        return True
    return False


def izmeni_trening(treninzi, sale, programi):
    dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja']

    while True:
        print('Opcije za treninge:')
        ispis_treninzi(treninzi)

        id = input("Unesite ID treninga za izmenu (b. za Nazad): ")
        if id == 'b':
            break
        elif id not in treninzi.keys():
            print("ID treninga ne postoji. Pokusajte ponovo.")
            continue

        while True:
            print('Trenutni trening za izmenu:')
            ispis_tabele({id: treninzi[id]})

            odgovor = input("Ponuđene opcije za izmenu:\n1. ID sale\n2. Vreme pocetka\n3. Vreme kraja\n4. Dani u nedelji\n5. ID programa\nb. Nazad\nUnesite zeljenu opciju: ")
            match odgovor:
                case '1':
                    while True:
                        print('Opcije za sale:')
                        ispis_sale(sale)

                        id_sale = input("Unesite novi ID sale: ")
                        if id_sale in sale:
                            treninzi[id]['id_sale'] = id_sale
                            break
                        print('Sala sa ovim ID ne postoji. Pokusajte ponovo.')
                case '2':
                    while True:
                        try:
                            vreme_pocetka = datetime.strptime(input("Unesite novo vreme početka (HH:MM): "), '%H:%M').time()
                            treninzi[id]['vreme_pocetka'] = vreme_pocetka
                            break
                        except Exception:
                            print("Pogresan format vremena. Pokusajte ponovo.")
                case '3':
                    while True:
                        try:
                            vreme_kraja = datetime.strptime(input("Unesite novo vreme kraja (HH:MM): "), '%H:%M').time()
                            treninzi[id]['vreme_kraja'] = vreme_kraja
                            break
                        except Exception:
                            print("Pogresan format vremena. Pokusajte ponovo.")
                case '4':
                    while True:
                        dani_nedelje = input("Unesite nove dane u nedelji (ponedeljak,sreda) sa zarezom bez razmaka: ").split(',')
                        if all(dan in dani for dan in dani_nedelje):
                            treninzi[id]['dani_nedelje'] = dani_nedelje
                            break
                        print("Niste uneli validne dane u nedelji. Pokušajte ponovo.")
                case '5':
                    while True:
                        print('Opcije za programe:')
                        ispis_programi(programi)

                        id_programa = input("Unesite novi ID programa: ")
                        if id_programa in programi:
                            treninzi[id]['id_programa'] = id_programa
                            break
                        print('Program sa ovim ID ne postoji. Pokusajte ponovo.')
                case 'b':
                    print('Trening uspesno izmenjen.')
                    return True
    return False


def brisi_trening(treninzi):
    while True:
        print('Opcije postojecih treninga za brisanje:')
        ispis_treninzi(treninzi)

        id = input("Unesite ID treninga za brisanje (b. za Nazad): ")
        if id == 'b':
            break
        if id in treninzi.keys():
            del treninzi[id]
            print('Trening uspesno izbrisan.')
            return True
        print("ID treninga ne postoji.")
        continue
    return False
