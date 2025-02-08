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
        str: tekstualni podatak iz fajla ili None ako dođe do greške.
    """
    try:
        with open(putanja, 'r', encoding='utf-8') as fajl:
            return fajl.read()
    except FileNotFoundError:
        print(f"Greska: Fajl '{putanja}' nije pronadjen.")
    except PermissionError:
        print(f"Greska: Nemate dozvolu za pristup fajlu '{putanja}'.")
    except UnicodeDecodeError:
        print(f"Greska: Problem sa enkodiranjem pri čitanju fajla '{putanja}'.")
    return None


def upis_fajl(putanja, podaci):
    """
    Upis podataka u .txt fajl.

    Args:
        putanja (str): putanja do .txt fajla.
        podaci (dict): podaci za upis u fajl.
    """
    try:
        with open(putanja, 'w', encoding='utf-8') as fajl:
            fajl.write(pretvori_u_tekst(podaci))
    except FileNotFoundError:
        print(f"Greska: Fajl '{putanja}' nije pronadjen.")
    except PermissionError:
        print(f"Greska: Nemate dozvolu za pisanje u fajl '{putanja}'.")
    except OSError as e:
        print(f"Greska pri upisu u fajl '{putanja}': {e}")


def ucitaj_podatke(putanja, kljucevi, separator='|'):
    """
    Ucitava podatke iz fajla i pretvara ih u recnik.

    Args:
        putanja (str): Putanja do fajla.
        kljucevi (list): Lista kljuceva koji ce biti korisceni za recnik.
        separator (str): Separator koji razdvaja podatke u fajlu (podrazumevano '|').

    Returns:
        dict: Recnik sa ucitanim podacima.
    """
    fajl = citaj_fajl(putanja)
    if fajl is None:
        return {}

    podaci = {}
    for red in fajl.strip().split('\n'):
        vrednosti = red.split(separator)
        if len(vrednosti) == len(kljucevi):
            podaci[vrednosti[0]] = {}
            for i, kljuc in enumerate(kljucevi):
                podaci[vrednosti[0]][kljuc] = vrednosti[i]


    return podaci
