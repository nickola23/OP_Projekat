from datetime import datetime
from funkcije.fajlovi import citajFajl, upisFajl
from funkcije.tabela import ispisTabele

def ucitajTermin(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, datum, idTreninga = red.split('|')
            podaci[id] = {
                'id': id,
                'datum': datetime.strptime(datum, '%d.%m.%Y').date().strftime('%d.%m.%Y'),
                'idTreninga': idTreninga
            }
    
    return podaci

def dodajTermin(termini):
    while True:
        id = input("Unesite ID termina: ")
        if id not in termini.keys():
            datum = input("Unesite datum termina (dd.mm.yyyy): ")
            idTreninga = input("Unesite ID treninga: ")
            termini[id] = {
                'id': id,
                'datum': datetime.strptime(datum, '%d.%m.%Y').date().strftime('%d.%m.%Y'),
                'idTreninga': idTreninga
            }
            return True
        else:
            print("Termin sa unesenim ID-em već postoji.")
            continue

def brisiTermin(termini):
    while True:
        id = input("Unesite ID termina za brisanje: ")
        if id in termini.keys():
            del termini[id]
            return True
        else:
            print("Termin sa unesenim ID-em ne postoji.")
            continue

def izmeniTermin(termini):
    while True:
        id = input("Unesite ID termina za izmenu: ")
        if id in termini.keys():
            ispisTabele({id: termini[id]})
            
            while True:
                odgovor = input("1. Datum\n2. ID treninga\nb. Nazad\nIzaberite podatak koji zelite da izmenite: ")
                
                match odgovor:
                    case '1':
                        termini[id]['datum'] = datetime.strptime(input("Unesite novi datum (dd.mm.yyyy): "), '%d.%m.%Y').date().strftime('%d.%m.%Y')
                    case '2':
                        termini[id]['idTreninga'] = input("Unesite novi ID treninga: ")
                    case 'b':
                        return True
        else:  
            print("Termin sa unesenim ID-em ne postoji.")
            continue

def spojiTermine(treninzi, termini):
    spojeniPodaci = {}

    for termin in termini.values():
        trening = treninzi.get(termin['idTreninga'])
        if trening:
            spojeniPodaci[termin['id']] = {
                'idTermina': termin['id'],
                'datum': datetime.strptime(termin['datum'], '%d.%m.%Y').date().strftime('%d.%m.%Y'),
                'idTreninga': termin['idTreninga'],
                'idSale': trening['idSale'],
                'vremePocetka': trening['vremePocetka'],
                'vremeKraja': trening['vremeKraja'],
                'daniNedelje': trening['daniNedelje'],
                'idPrograma': trening['idPrograma']
            }
    return spojeniPodaci

def pretraziTermine(termini, sale, programi, kriterijum=''):
    pretraga = {}
    if kriterijum == 'idSale':
        print("Dostupni ID sale:")
        for id, podaci in sale.items():
            print(f"ID: {podaci.get('id', 'Nepoznato')} - {podaci.get('naziv', 'Nepoznato')}")
        
    elif kriterijum == 'idPrograma':
        print("Dostupni ID programa:")
        for id, podaci in programi.items():
            print(f"ID: {podaci.get('id', 'Nepoznato')} - {podaci.get('naziv', 'Nepoznato')}")
        
    kljuc = input('Unesite ključnu reč za pretragu: ').strip().lower()

    for id, podaci in termini.items():
        if kriterijum:
            if kriterijum == 'idSale' and str(podaci['idSale']).lower() == kljuc:
                pretraga[id] = podaci
            elif kriterijum == 'idPrograma' and str(podaci['idPrograma']).lower() == kljuc:
                pretraga[id] = podaci
            elif kriterijum == 'datum' and podaci['datum'] == kljuc:
                pretraga[id] = podaci
            elif kriterijum == 'vremePocetka' and podaci['vremePocetka'].strftime('%H:%M') == kljuc:
                pretraga[id] = podaci
            elif kriterijum == 'vremeKraja' and podaci['vremeKraja'].strftime('%H:%M') == kljuc:
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
