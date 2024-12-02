from funkcije.fajloviFunkcije import citajFajl, upisFajl

programi = {}
putanja = './data/Program.txt'

def ucitajPrograme(putanja):
    fajl = citajFajl(putanja)
    if fajl is None:
        return {}
    
    podaci = {}
    for red in fajl.split('\n'):
        if red:
            id = red.split('|')[0]
            podaci[id] = {
                'id': eval(id),
                'naziv': red.split('|')[1],
                'idVrsteTreninga': eval(red.split('|')[2]),
                'trajanje': eval(red.split('|')[3]),
                'idInstruktora': eval(red.split('|')[4]),
                'potrebanPaket': eval(red.split('|')[5]),
                'opis': red.split('|')[6]
            }
            
    return podaci

programi = ucitajPrograme(putanja)

#upis programa u fajl
