"""
Modul za upravljanje .txt fajlovima.

Sadrži funkcije za upis, citanje fajlova i 
pretvaranja podataka u tekst pogodan za upis.
"""
from datetime import time

def pretvori_u_tekst(podaci):
    """
    Pretvara podatke u oblik koji se prikazuje u fajlu.

    Args:
        podaci (dict): podaci za upis u fajl.

    Returns:
        str: tekstualni podatak za upis u fajl.
    """
    if podaci:
        tekst = ''
        for podatak in podaci.values():
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
    print('Nema podataka za upis')
    return None


def citaj_fajl(putanja):
    """
    Cita podatke iz .txt fajla.

    Args:
        putanja (str): putanja do fajla.

    Returns:
        str: tekstualni podatak iz fajla.
    """
    try:
        with open(putanja, 'r', encoding='utf-8') as fajl:
            return fajl.read()
    except Exception as e:
        print('Greska prilikom citanja fajla:\n', e)
        return None


def upis_fajl(putanja, podaci):
    """
    Upis podataka u.txt fajl.

    Args:
        putanja (str): putanja do .txt fajla.
        podaci (dict): podaci za upis u fajl.
    """
    try:
        with open(putanja, 'w', encoding='utf-8') as fajl:
            fajl.write(pretvori_u_tekst(podaci))
    except Exception as e:
        print('Greska prilikom upisa u fajl.')
