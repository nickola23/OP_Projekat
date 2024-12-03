from datetime import datetime
from funkcije.fajlovi import citajFajl, upisFajl

def ucitajTrening(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, idSale, vremePocetka, vremeKraja, daniNedelje, idPrograma= red.split('|')
            podaci[id] = {
                'id': id,
                'idSale': idSale,
                'vremePocetka': datetime.strptime(vremePocetka, '%H:%M').time(),
                'vremeKraja': datetime.strptime(vremeKraja, '%H:%M').time(),
                'daniNedelje': daniNedelje.split(','),
                'idPrograma': idPrograma
            }
    
    return podaci

def dodajTrening(treninzi):
    while True:
        id = input("Unesite ID treninga: ")
        if id not in treninzi.keys():
            idSale = input("Unesite ID sale: ")
            vremePocetka = datetime.strptime(input("Unesite vreme početka (HH:MM): "), '%H:%M').time()
            vremeKraja = datetime.strptime(input("Unesite vreme kraja (HH:MM): "), '%H:%M').time()
            daniNedelje = input("Unesite dane u nedelji (ponedeljak,sreda): ").split(',')
            idPrograma = int(input("Unesite ID programa: "))
            
            treninzi[id] = {
                'id': id,
                'idSale': idSale,
                'vremePocetka': vremePocetka,
                'vremeKraja': vremeKraja,
                'daniNedelje': daniNedelje,
                'idPrograma': idPrograma
            }
            return True
        else:
            print("ID treninga je vec zauzet.")
            continue

def brisiTrening(treninzi):
    while True:
        id = input("Unesite ID treninga za brisanje: ")
        if id in treninzi.keys():
            del treninzi[id]
            return True
        else:
            print("ID treninga ne postoji.")
            continue

def izmeniTrening(treninzi):
    while True:
        id = input("Unesite ID treninga za izmenu: ")
        if id in treninzi.keys():
            print(f'Trenutni podaci za trening sa ID {id}:')
            print(f'ID sale: {treninzi[id]["idSale"]}')
            print(f'Vreme početka: {treninzi[id]["vremePocetka"].strftime("%H:%M")}')
            print(f'Vreme kraja: {treninzi[id]["vremeKraja"].strftime("%H:%M")}')
            print(f'Dani u nedelji: {", ".join(treninzi[id]["daniNedelje"])}')
            print(f'ID programa: {treninzi[id]["idPrograma"]}')
            
            odgovor = input("1. ID sale\n 2. Vreme pocetka\n 3. Vreme kraja\n4. Dani u nedelji\n 5. ID programa\n0. Izlaz\nIzaberite podatak koji zelite da izmenite: ")

            match odgovor:
                case '1':
                    treninzi[id]['idSale'] = input("Unesite novi ID sale: ")
                case '2':
                    treninzi[id]['vremePocetka'] = datetime.strptime(input("Unesite novo vreme početka (HH:MM): "), '%H:%M').time()
                case '3':
                    treninzi[id]['vremeKraja'] = datetime.strptime(input("Unesite novo vreme kraja (HH:MM): "), '%H:%M').time()
                case '4':
                    treninzi[id]['daniNedelje'] = input("Unesite nove dane u nedelji (ponedeljak,sreda): ").split(',')
                case '5':
                    treninzi[id]['idPrograma'] = input("Unesite novi ID programa: ")
                case 0:
                    return True
        else:
            print("ID treninga ne postoji.")
            continue