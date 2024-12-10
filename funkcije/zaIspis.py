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
    if not termini or not isinstance(termini, dict):
        print('Greska: termini nisu validni podaci.')
        return {}

    podaci = {}
    for id, trening in termini.items():
        sala = sale.get(str(trening['idSale']), {}).get('naziv', 'Nepoznato')
        program = programi.get(str(trening['idPrograma']), {}).get('naziv', 'Nepoznato')

        podaci[id] = {
            'id': trening['idTermina'],
            'datum': trening['datum'],
            'idTreninga': trening['idTreninga'],
            'idSale': sala,
            'vremePocetka': trening['vremePocetka'],
            'vremeKraja': trening['vremeKraja'],
            'daniNedelje': trening['daniNedelje'],
            'idPrograma': program
        }
    return podaci