def pretvoriuTekst(podaci):
    if podaci:
        tekst = ''
        for kljuc, podatak in podaci.items():
            linija = list(podatak.values())
            for i, vrednost in enumerate(linija):
                if i > 0:
                    tekst += '|'
                tekst += str(vrednost).strip()
            tekst += '\n'
        return tekst
    else:
        print('Nema podataka za upis')
        return None

def citajFajl(putanja):
    try:
        with open(putanja, 'r') as fajl:
            return fajl.read()
    except:
        print('Greska prilikom citanja fajla.')
        return None
    
def upisFajl(putanja, podaci):
    try:
        with open(putanja, 'w') as fajl:
            fajl.write(pretvoriuTekst(podaci))
    except:
        print('Greska prilikom upisa u fajl.')