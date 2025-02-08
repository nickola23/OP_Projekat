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
    except Exception as e:
        print(f"Greska: {e}")
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
    except Exception as e:
        print(f"Greska: {e}")
