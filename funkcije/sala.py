from funkcije.fajlovi import citajFajl, upisFajl

def ucitajSale(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, naziv, brojRedova, oznakaMesta = red.split('|')
            podaci[id] = {
                'id': eval(id),
                'naziv': naziv,
                'brojRedova': eval(brojRedova),
                'oznakaMesta': oznakaMesta.strip()
            }
            
    return podaci

