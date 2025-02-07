from funkcije.fajlovi import citaj_fajl, upis_fajl

def ucitaj_sale(putanja):
    fajl = citaj_fajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id, naziv, broj_redova, oznaka_mesta = red.split('|')
            podaci[id] = {
                'id': eval(id),
                'naziv': naziv,
                'broj_redova': eval(broj_redova),
                'oznaka_mesta': oznaka_mesta.strip()
            }
            
    return podaci

