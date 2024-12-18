from datetime import datetime
from funkcije.fajlovi import citajFajl, upisFajl
from funkcije.tabela import ispisTabele

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

def dodajTrening(treninzi, sale, programi):
    dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja']

    while True:
        id = input("Unesite ID treninga: ")
        if id not in treninzi.keys():
            break
        else:
           print("ID treninga vec postoji. Pokusajte ponovo.")
    
    while True:
        idSale = input("Unesite ID sale: ")
        if idSale in sale:
            break
        else:
            print(f'Sala sa ovim ID ne postoji. Pokusajte ponovo.')

    while True:
        try:
            vremePocetka = datetime.strptime(input("Unesite vreme početka (HH:MM): "), '%H:%M').time()
            break
        except Exception:
            print("Pogresan format vremena. Pokusajte ponovo.")

    while True:
        try:
            vremeKraja = datetime.strptime(input("Unesite vreme kraja (HH:MM): "), '%H:%M').time()
            break
        except Exception:
            print("Pogresan format vremena. Pokusajte ponovo.")
    
    while True:
        daniNedelje = input("Unesite dane u nedelji (ponedeljak,sreda) sa zarezom bez razmaka: ").split(',')
        if all(dan in dani for dan in daniNedelje):
            break
        else:
            print("Niste uneli validne dane u nedelji. Pokušajte ponovo.")

    while True:
        idPrograma = input("Unesite ID programa: ")
        if idPrograma in programi:
            break
        else:
            print(f'Program sa ovim ID ne postoji. Pokusajte ponovo.')
    
    treninzi[id] = {
        'id': id,
        'idSale': idSale,
        'vremePocetka': vremePocetka,
        'vremeKraja': vremeKraja,
        'daniNedelje': daniNedelje,
        'idPrograma': idPrograma
    }
    return True

def izmeniTrening(treninzi, sale, programi):
    dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja']

    while True:
        id = input("Unesite ID treninga za izmenu: ")
        if id in treninzi.keys():
            break
        else:
           print("ID treninga ne postoji. Pokusajte ponovo.")

    ispisTabele({id: treninzi[id]})

    while True:
        odgovor = input("1. ID sale\n2. Vreme pocetka\n3. Vreme kraja\n4. Dani u nedelji\n5. ID programa\nb. Nazad\nIzaberite podatak koji zelite da izmenite: ")
        match odgovor:
            case '1':
                
                while True:
                    idSale = input("Unesite novi ID sale: ")
                    if idSale in sale:
                        treninzi[id]['idSale'] = idSale
                        break
                    else:
                        print(f'Sala sa ovim ID ne postoji. Pokusajte ponovo.')
            case '2':
                while True:
                    try:
                        vremePocetka = datetime.strptime(input("Unesite novo vreme početka (HH:MM): "), '%H:%M').time()
                        treninzi[id]['vremePocetka'] = vremePocetka
                        break
                    except Exception:
                        print("Pogresan format vremena. Pokusajte ponovo.")
            case '3':
                while True:
                    try:
                        vremeKraja = datetime.strptime(input("Unesite novo vreme kraja (HH:MM): "), '%H:%M').time()
                        treninzi[id]['vremeKraja'] = vremeKraja
                        break
                    except Exception:
                        print("Pogresan format vremena. Pokusajte ponovo.")
            case '4':
                while True:
                    daniNedelje = input("Unesite nove dane u nedelji (ponedeljak,sreda) sa zarezom bez razmaka: ").split(',')
                    if all(dan in dani for dan in daniNedelje):
                        treninzi[id]['daniNedelje'] = daniNedelje
                        break
                    else:
                        print("Niste uneli validne dane u nedelji. Pokušajte ponovo.")
            case '5':
                while True:
                    idPrograma = input("Unesite novi ID programa: ")
                    if idPrograma in programi:
                        treninzi[id]['idPrograma'] = idPrograma
                        break
                    else:
                        print(f'Program sa ovim ID ne postoji. Pokusajte ponovo.')
            case 'b':
                return True

def brisiTrening(treninzi):
    while True:
        id = input("Unesite ID treninga za brisanje: ")
        if id in treninzi.keys():
            del treninzi[id]
            return True
        else:
            print("ID treninga ne postoji.")
            continue