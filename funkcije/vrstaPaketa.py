from funkcije.fajlovi import citajFajl, upisFajl

def ucitajVrstePaketa(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, naziv = red.split('|')
            podaci[id] = {
                'id': eval(id),
                'naziv': naziv
            }
            
    return podaci