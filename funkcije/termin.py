from datetime import datetime
from funkcije.fajlovi import citaj_fajl, upis_fajl
from funkcije.tabela import ispis_tabele

def ucitaj_termin(putanja):
    fajl = citaj_fajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, datum, id_treninga = red.split('|')
            podaci[id] = {
                'id': id,
                'datum': datetime.strptime(datum, '%d.%m.%Y').date().strftime('%d.%m.%Y'),
                'id_treninga': id_treninga
            }
    
    return podaci

def dodaj_termin(termini):
    while True:
        id = input("Unesite ID termina: ")
        if id not in termini.keys():
            datum = input("Unesite datum termina (dd.mm.yyyy): ")
            id_treninga = input("Unesite ID treninga: ")
            termini[id] = {
                'id': id,
                'datum': datetime.strptime(datum, '%d.%m.%Y').date().strftime('%d.%m.%Y'),
                'id_treninga': id_treninga
            }
            return True
        else:
            print("Termin sa unesenim ID-em već postoji.")
            continue

def brisi_termin(termini):
    while True:
        id = input("Unesite ID termina za brisanje: ")
        if id in termini.keys():
            del termini[id]
            return True
        else:
            print("Termin sa unesenim ID-em ne postoji.")
            continue

def izmeni_termin(termini):
    while True:
        id = input("Unesite ID termina za izmenu: ")
        if id in termini.keys():
            ispis_tabele({id: termini[id]})

            while True:
                odgovor = input("1. Datum\n2. ID treninga\nb. Nazad\nIzaberite podatak koji zelite da izmenite: ")

                match odgovor:
                    case '1':
                        termini[id]['datum'] = datetime.strptime(input("Unesite novi datum (dd.mm.yyyy): "), '%d.%m.%Y').date().strftime('%d.%m.%Y')
                    case '2':
                        termini[id]['id_treninga'] = input("Unesite novi ID treninga: ")
                    case 'b':
                        return True
        else:  
            print("Termin sa unesenim ID-em ne postoji.")
            continue

def spoji_termine(treninzi, termini):
    spojeni_podaci = {}

    for termin in termini.values():
        trening = treninzi.get(termin['id_treninga'])
        if trening:
            spojeni_podaci[termin['id']] = {
                'id_termina': termin['id'],
                'datum': datetime.strptime(termin['datum'], '%d.%m.%Y').date().strftime('%d.%m.%Y'),
                'id_treninga': termin['id_treninga'],
                'id_sale': trening['id_sale'],
                'vreme_pocetka': trening['vreme_pocetka'],
                'vreme_kraja': trening['vreme_kraja'],
                'dani_nedelje': trening['dani_nedelje'],
                'id_programa': trening['id_programa']
            }
    return spojeni_podaci

def pretrazi_termine(termini, sale, programi, kriterijum=''):
    pretraga = {}
    if kriterijum == 'id_sale':
        print("Dostupni ID sale:")
        for id, podaci in sale.items():
            print(f"ID: {podaci.get('id', 'Nepoznato')} - {podaci.get('naziv', 'Nepoznato')}")
        
    elif kriterijum == 'id_programa':
        print("Dostupni ID programa:")
        for id, podaci in programi.items():
            print(f"ID: {podaci.get('id', 'Nepoznato')} - {podaci.get('naziv', 'Nepoznato')}")
        
    kljuc = input('Unesite ključnu reč za pretragu: ').strip().lower()

    for id, podaci in termini.items():
        if kriterijum:
            if kriterijum == 'id_sale' and str(podaci['id_sale']).lower() == kljuc:
                pretraga[id] = podaci
            elif kriterijum == 'id_programa' and str(podaci['id_programa']).lower() == kljuc:
                pretraga[id] = podaci
            elif kriterijum == 'datum' and podaci['datum'] == kljuc:
                pretraga[id] = podaci
            elif kriterijum == 'vreme_pocetka' and podaci['vreme_pocetka'].strftime('%H:%M') == kljuc:
                pretraga[id] = podaci
            elif kriterijum == 'vreme_kraja' and podaci['vreme_kraja'].strftime('%H:%M') == kljuc:
                pretraga[id] = podaci
        else:
            for vrednost in podaci.values():
                if isinstance(vrednost, list):
                    if kljuc in [str(v).lower() for v in vrednost]:
                        pretraga[id] = podaci
                        break
                elif kljuc in str(vrednost).lower():
                    pretraga[id] = podaci
                    break
    
    if not pretraga:
        print('Nema podataka iz pretrage.')
        return {}
    else:
        return pretraga
