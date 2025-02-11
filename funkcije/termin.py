"""
Modul za upravljanje terminima.

Sadrži funkcije za ucitavanje,
dodavanje, izmenu, brisanje i pretragu termina. 
"""
from datetime import datetime
from funkcije.fajlovi import ucitaj_podatke
from funkcije.tabela import ispis_tabele

def ucitaj_termin(putanja):
    """
    Učitava podatke termina iz fajla.

    Args:
        putanja (str): Putanja do .txt fajla.

    Returns:
        dict: Rečnik sa podacima o terminima.
    """
    kljucevi = ['id', 'datum', 'id_treninga']
    podaci = ucitaj_podatke(putanja, kljucevi)

    # Dodatna obrada podataka
    for termin in podaci.values():
        termin['datum'] = (datetime.strptime(termin['datum'], '%d.%m.%Y')
                                   .date().strftime('%d.%m.%Y'))

    return podaci


def dodaj_termin(termini):
    """
    Dodaje novi termin za trening u sistem.

    Args:
        termini (dict): Rečnik sa podacima o terminima.

    Returns:
        bool: True ako je termin uspešno dodat.
    """
    while True:
        id_termina = input("Unesite ID termina: ")
        if id_termina not in termini.keys():
            datum = input("Unesite datum termina (dd.mm.yyyy): ")
            id_treninga = input("Unesite ID treninga: ")
            termini[id_termina] = {
                'id': id_termina,
                'datum': datetime.strptime(datum, '%d.%m.%Y').date().strftime('%d.%m.%Y'),
                'id_treninga': id_treninga
            }
            return True
        print("Termin sa unesenim ID-em već postoji.")
        continue


def brisi_termin(termini):
    """
    Briše termin iz sistema na osnovu ID-a.

    Args:
        termini (dict): Rečnik sa podacima o terminima.

    Returns:
        bool: True ako je termin uspešno obrisan.
    """
    while True:
        id_termina = input("Unesite ID termina za brisanje: ")
        if id_termina in termini.keys():
            del termini[id_termina]
            return True
        print("Termin sa unesenim ID-em ne postoji.")
        continue


def izmeni_termin(termini):
    """
    Menja podatke o postojećem terminu.

    Args:
        termini (dict): Rečnik sa podacima o terminima.

    Returns:
        bool: True ako je termin uspešno izmenjen.
    """
    while True:
        id_termina = input("Unesite ID termina za izmenu: ")
        if id_termina in termini.keys():
            ispis_tabele({id_termina: termini[id_termina]})

            while True:
                odgovor = input("1. Datum\n2. ID treninga\nb. Nazad\n"
                                "Izaberite podatak koji zelite da izmenite: ")
                match odgovor:
                    case '1':
                        datum_input = input("Unesite novi datum (dd.mm.yyyy): ")
                        datum_obj = datetime.strptime(datum_input, '%d.%m.%Y').date()
                        termini[id_termina]['datum'] = datum_obj.strftime('%d.%m.%Y')
                    case '2':
                        termini[id_termina]['id_treninga'] = input("Unesite novi ID treninga: ")
                    case 'b':
                        return True
        else:
            print("Termin sa unesenim ID-em ne postoji.")
            continue


def spoji_termine(treninzi, termini):
    """
    Spaja podatke o terminima i treninzima u jedan rečnik.

    Args:
        treninzi (dict): Rečnik sa podacima o treninzima.
        termini (dict): Rečnik sa podacima o terminima.

    Returns:
        dict: Novi rečnik koji sadrži spajane podatke o terminima i treninzima.
    """
    spojeni_podaci = {}

    for termin in termini.values():
        trening = treninzi.get(termin['id_treninga'])
        if trening:
            spojeni_podaci[termin['id']] = {
                'id_termina': termin['id'],
                'datum': datetime.strptime(termin['datum'], '%d.%m.%Y').date().strftime('%d.%m.%Y'),
                'id_treninga': termin['id_treninga'],
                'id_sale': trening['id_sale'],
                'vreme_pocetka': trening['vreme_pocetka'],
                'vreme_kraja': trening['vreme_kraja'],
                'dani_nedelje': trening['dani_nedelje'],
                'id_programa': trening['id_programa']
            }
    return spojeni_podaci


def pretrazi_termine(termini, sale, programi, kriterijum=''):
    """
    Pretražuje termine na osnovu različitih kriterijuma.

    Args:
        termini (dict): Rečnik sa podacima o terminima.
        sale (dict): Rečnik sa podacima o salama.
        programi (dict): Rečnik sa podacima o programima.
        kriterijum (str, optional): Kriterijum za pretragu.

    Returns:
        dict: Rečnik sa rezultatima pretrage.
    """
    pretraga = {}
    if kriterijum == 'id_sale':
        print("Dostupni ID sale:")
        for _, podaci in sale.items():
            print(f"ID: {podaci.get('id', 'Nepoznato')} - {podaci.get('naziv', 'Nepoznato')}")

    elif kriterijum == 'id_programa':
        print("Dostupni ID programa:")
        for _, podaci in programi.items():
            print(f"ID: {podaci.get('id', 'Nepoznato')} - {podaci.get('naziv', 'Nepoznato')}")

    kljuc = input('Unesite ključnu reč za pretragu: ').strip().lower()

    for id_termina, podaci in termini.items():
        if kriterijum:
            if kriterijum == 'id_sale' and str(podaci['id_sale']).lower() == kljuc:
                pretraga[id_termina] = podaci
            elif kriterijum == 'id_programa' and str(podaci['id_programa']).lower() == kljuc:
                pretraga[id_termina] = podaci
            elif kriterijum == 'datum' and podaci['datum'] == kljuc:
                pretraga[id_termina] = podaci
            elif kriterijum == 'vreme_pocetka' and podaci['vreme_pocetka'].strftime('%H:%M')==kljuc:
                pretraga[id_termina] = podaci
            elif kriterijum == 'vreme_kraja' and podaci['vreme_kraja'].strftime('%H:%M') == kljuc:
                pretraga[id_termina] = podaci
        else:
            for vrednost in podaci.values():
                if isinstance(vrednost, list):
                    if kljuc in [str(v).lower() for v in vrednost]:
                        pretraga[id_termina] = podaci
                        break
                elif kljuc in str(vrednost).lower():
                    pretraga[id_termina] = podaci
                    break

    if not pretraga:
        print('Nema podataka iz pretrage.')
        return {}
    return pretraga
