"""
Modul za upravljanje funkcijama za ispis.

Sadrži funkcije za ispis
programa, treninga, termina, rezervacija.
"""
from datetime import datetime

def programi_za_ispis(programi, instruktori, vrste_treninga, vrste_paketa):
    """
    Ispisuje podatke o programima sa instruktorima, vrstama treninga i paketa.

    Args:
        programi (dict): recnik sa podacima o programima
        instruktori (dict): recnik sa podacima o instruktorima
        vrste_treninga (dict): recnik sa podacima o vrstama treninga
        vrste_paketa (dict): recnik sa podacima o vrstama paketa

    Returns:
        dict: recnik sa podacima za ispis
    """
    podaci = {}
    for id_programa, program in programi.items():
        vrsta_treninga = vrste_treninga.get(str(program['idvrste_treninga']), {}).get('naziv', 'Nepoznato')
        vrsta_paketa = vrste_paketa.get(str(program['potreban_paket']), {}).get('naziv', 'Nepoznato')
        instruktor = instruktori.get(str(program['id_instruktora']), {})
        ime_instruktora = f"{instruktor.get('ime', 'Nepoznato')} {instruktor.get('prezime', '')}"

        podaci[id_programa] = {
            'id': program['id'],
            'naziv': program['naziv'],
            'vrsta_treninga': vrsta_treninga,
            'trajanje': program['trajanje'],
            'instruktor': ime_instruktora,
            'potreban_paket': vrsta_paketa,
            'opis': program['opis']
        }
    return podaci


def trening_za_ispis(treninzi, sale, programi):
    """
    Ispisuje podatke o treningima sa salama i programima.

    Args:
        treninzi (dict): recnik sa podacima o treningima
        sale (dict): recnik sa podacima o salama
        programi (dict): recnik sa podacima o programima

    Returns:
        dict: recnik sa podacima za ispis
    """
    podaci = {}
    for id_treninga, trening in treninzi.items():
        sala = sale.get(str(trening['id_sale']), {}).get('naziv', 'Nepoznato')
        program = programi.get(str(trening['id_programa']), {}).get('naziv', 'Nepoznato')

        podaci[id_treninga] = {
            'id': trening['id'],
            'id_sale': sala,
            'vreme_pocetka': trening['vreme_pocetka'],
            'vreme_kraja': trening['vreme_kraja'],
            'dani_nedelje': trening['dani_nedelje'],
            'id_programa': program,
        }
    return podaci


def spojeni_termini_za_ispis(termini, sale, programi):
    """
    Ispisuje podatke o terminima sa salama, programima.

    Args:
        termini (dict): recnik sa podacima o terminima
        sale (dict): recnik sa podacima o salama
        programi (dict): recnik sa podacima o programima

    Returns:
        dict: recnik sa podacima za ispis
    """
    dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja']

    if not termini or not isinstance(termini, dict):
        return {}

    podaci = {}
    for id, trening in termini.items():
        sala = sale.get(str(trening['id_sale']), {}).get('naziv', 'Nepoznato')
        program = programi.get(str(trening['id_programa']), {}).get('naziv', 'Nepoznato')
        dan_u_nedelji = dani[datetime.strptime(trening['datum'], '%d.%m.%Y').date().weekday()]

        if dan_u_nedelji in trening['dani_nedelje']:
            trening_dan = dan_u_nedelji
        else:
            trening_dan = 'Neodgovarajuci dan'

        podaci[id] = {
            'id': trening['id_termina'],
            'datum': trening['datum'],
            'id_treninga': trening['id_treninga'],
            'id_sale': sala,
            'vreme_pocetka': trening['vreme_pocetka'],
            'vreme_kraja': trening['vreme_kraja'],
            'dani_nedelje': trening_dan,
            'id_programa': program
        }
    return podaci


def rezervacije_za_ispis(rezervacije, termini, treninzi, programi):
    """
    Ispisuje podatke o rezervacijama sa terminima, treninzima i programima.

    Args:
        rezervacije (dict): recnik sa podacima o rezervacijama
        termini (dict): recnik sa podacima o terminima
        treninzi (dict): recnik sa podacima o treninzima
        programi (dict): recnik sa podacima o programima

    Returns:
        dict: recnik sa podacima za ispis

    """
    spojeni_podaci = {}

    for id_rezervacije, rezervacija in rezervacije.items():
        id_termina = rezervacija['id_termina']
        id_korisnika = rezervacija['id_korisnika']

        termin = termini.get(id_termina)
        if not termin:
            continue

        id_treninga = termin['id_treninga']

        trening = treninzi.get(id_treninga)
        if not trening:
            continue

        id_programa = trening['id_programa']

        program = programi.get(id_programa)
        if not program:
            continue

        spojeni_podaci[id_rezervacije] = {
            'id_rezervacije': id_rezervacije,
            'id_korisnika': id_korisnika,
            'datum_rezervacije': rezervacija['datum'],
            'id_termina': id_termina,
            'datum_termina': termin['datum'],
            'vreme_pocetka': trening['vreme_pocetka'].strftime('%H:%M'),
            'vreme_kraja': trening['vreme_kraja'].strftime('%H:%M'),
            'dani_nedelje': ', '.join(trening['dani_nedelje']),
            'naziv_programa': program['naziv'],
            'opis_programa': program['opis']
        }

    return spojeni_podaci
