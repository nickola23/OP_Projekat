from datetime import date, time

def pretvoriuTekst(podaci):
    if podaci:
        tekst = ''
        for kljuc, podatak in podaci.items():
            linija = []
            for vrednost in podatak.values():
                if isinstance(vrednost, list):
                    linija.append(','.join(vrednost))
                elif isinstance(vrednost, time):
                    linija.append(vrednost.strftime('%H:%M')) 
                else:
                    linija.append(str(vrednost).strip())
            tekst += '|'.join(linija) + '\n'
        return tekst
    else:
        print('Nema podataka za upis')
        return None

def citajFajl(putanja):
    try:
        with open(putanja, 'r', encoding='utf-8') as fajl:
            return fajl.read()
    except Exception as e:
        print('Greska prilikom citanja fajla:\n', e)
        return None
    
def upisFajl(putanja, podaci):
    try:
        with open(putanja, 'w', encoding='utf-8') as fajl:
            fajl.write(pretvoriuTekst(podaci))
    except:
        print('Greska prilikom upisa u fajl.')