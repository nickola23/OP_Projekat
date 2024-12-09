from datetime import datetime
from funkcije.fajlovi import citajFajl, upisFajl

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
            print(f"Trenutni podaci za termin sa ID {id}:")
            print(f"Datum: {termini[id]['datum']}")
            print(f"ID treninga: {termini[id]['idTreninga']}")
            
            while True:
                odgovor = input("1. Datum\n2. ID treninga\n0. Izlaz\nIzaberite podatak koji zelite da izmenite: ")
                
                match odgovor:
                    case '1':
                        termini[id]['datum'] = datetime.strptime(input("Unesite novi datum (dd.mm.yyyy): "), '%d.%m.%Y').date().strftime('%d.%m.%Y')
                    case '2':
                        termini[id]['idTreninga'] = input("Unesite novi ID treninga: ")
                    case '0':
                        return True
        else:  
            print("Termin sa unesenim ID-em ne postoji.")
            continue

def pretraziTermin(termini, kriterijum = ''):
    pretraga = {}
    kljuc = input('Unesite kljucnu rec za pretragu: ').lower()

    for id, podaci in termini.items():
        for vrednost in podaci.values():
            if kriterijum:
                if kriterijum == 'id' and str(podaci['id']).lower() == kljuc:
                    pretraga[id] = podaci
                elif kriterijum == 'datum' and str(datetime.strptime(podaci['datum'], '%d.%m.%Y')) == kljuc:    #sta???
                    pretraga[id] = podaci
                elif kriterijum == 'idTreninga' and str(podaci['idTreninga']).lower() == kljuc:
                    pretraga[id] = podaci
                else:
                    break
            else:
                if kljuc in str(vrednost).lower():
                    pretraga[id] = podaci
    
    if not pretraga:
        return {}
    else:
        return pretraga
