from funkcije.fajlovi import citaj_fajl, upis_fajl

def ucitaj_vrste_treninga(putanja):
    fajl = citaj_fajl(putanja)
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

