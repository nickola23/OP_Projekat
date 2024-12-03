from datetime import datetime
from funkcije.fajlovi import citajFajl, upisFajl

def ucitajTermie(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, datum, idTreninga = red.split('|')
            podaci[id]({
                'id': id,
                'datum': datetime.strptime(datum, '%d.%m.%Y'),
                'idTreninga': eval(idTreninga)
            })
    
    return podaci
