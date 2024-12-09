

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