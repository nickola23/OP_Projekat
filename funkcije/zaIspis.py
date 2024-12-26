from datetime import datetime

def programiZaIspis(programi, instruktori, vrsteTreninga, vrstePaketa):
    podaci = {}
    for id, program in programi.items():
        vrstaTreninga = vrsteTreninga.get(str(program['idVrsteTreninga']), {}).get('naziv', 'Nepoznato')
        vrstaPaketa = vrstePaketa.get(str(program['potrebanPaket']), {}).get('naziv', 'Nepoznato')
        instruktor = instruktori.get(str(program['idInstruktora']), {})
        imeInstruktora = f"{instruktor.get('ime', 'Nepoznato')} {instruktor.get('prezime', '')}"
        
        podaci[id] = {
            'id': program['id'],
            'naziv': program['naziv'],
            'vrstaTreninga': vrstaTreninga,
            'trajanje': program['trajanje'],
            'instruktor': imeInstruktora,
            'potrebanPaket': vrstaPaketa,
            'opis': program['opis']
        }
    return podaci

def treningZaIspis(treninzi, sale, programi):
    podaci = {}
    for id, trening in treninzi.items():
        sala = sale.get(str(trening['idSale']), {}).get('naziv', 'Nepoznato')
        program = programi.get(str(trening['idPrograma']), {}).get('naziv', 'Nepoznato')

        podaci[id] = {
            'id': trening['id'],
            'idSale': sala,
            'vremePocetka': trening['vremePocetka'],
            'vremeKraja': trening['vremeKraja'],
            'daniNedelje': trening['daniNedelje'],
            'idPrograma': program,
        }
    return podaci

def spojeniTerminiZaIspis(termini, sale, programi):
    dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja']

    if not termini or not isinstance(termini, dict):
        return {}

    podaci = {}
    for id, trening in termini.items():
        sala = sale.get(str(trening['idSale']), {}).get('naziv', 'Nepoznato')
        program = programi.get(str(trening['idPrograma']), {}).get('naziv', 'Nepoznato')
        danUNedelji = dani[datetime.strptime(trening['datum'], '%d.%m.%Y').date().weekday()]

        if danUNedelji in trening['daniNedelje']:
            treningDan = danUNedelji
        else:
            treningDan = 'Neodgovarajuci dan'

        podaci[id] = {
            'id': trening['idTermina'],
            'datum': trening['datum'],
            'idTreninga': trening['idTreninga'],
            'idSale': sala,
            'vremePocetka': trening['vremePocetka'],
            'vremeKraja': trening['vremeKraja'],
            'daniNedelje': treningDan,
            'idPrograma': program
        }
    return podaci

def rezervacijeZaIspis(rezervacije, termini, treninzi, programi):
    spojeniPodaci = {}

    for idRezervacije, rezervacija in rezervacije.items():
        idTermina = rezervacija['idTermina']
        idKorisnika = rezervacija['idKorisnika']

        termin = termini.get(idTermina)
        if not termin:
            continue

        idTreninga = termin['idTreninga']

        trening = treninzi.get(idTreninga)
        if not trening:
            continue

        idPrograma = trening['idPrograma']

        program = programi.get(idPrograma)
        if not program:
            continue

        spojeniPodaci[idRezervacije] = {
            'idRezervacije': idRezervacije,
            'idKorisnika': idKorisnika,
            'datumRezervacije': rezervacija['datum'],
            'idTermina': idTermina,
            'datumTermina': termin['datum'],
            'vremePocetka': trening['vremePocetka'].strftime('%H:%M'),
            'vremeKraja': trening['vremeKraja'].strftime('%H:%M'),
            'daniNedelje': ', '.join(trening['daniNedelje']),
            'nazivPrograma': program['naziv'],
            'opisPrograma': program['opis']
        }

    return spojeniPodaci