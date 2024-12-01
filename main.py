def izlaz():
    print("Izlaz iz programa.")

menii = {
    "pocetni": {
        "prijava": lambda: print('prijava'),
        "pregledPrograma": lambda: print('pregledPrograma'),
        "pretragaPrograma": lambda: print('pretragaPrograma'),
        "naprednaPretraga": lambda: print('naprednaPretraga'),
        "pretragaTermina": lambda: print('pretragaTermina'),
        "izlaz": izlaz
    },
    "neregistrovan": 'ispisiMeni(neregistrovan)',
    "registrovanClan": 'ispisiMeni(registrovanClan)',
    "registrovanInstruktor": 'ispisiMeni(registrovanInstruktor)',
    "registrovanAdmin": 'ispisiMeni(registrovanAdmin)',
}

def ispisiMeni(meni):
    print('Izaberite stavku iz menija: ')
    for i, (naziv, _) in enumerate(meni.items()):
        print(f'{i}: {naziv}')

def unosMeni(meni):
    try:
        izbor = int(input('Izaberite broj stavke >>> '))
        if izbor < 0 or izbor >= len(meni):
            print('Nevazeci unos, pokušajte ponovo.')
        else:
            stavka = list(meni.values())[izbor]
            stavka()
    except: 
        print('Morate uneti broj.')

def main():
    trenutniMeni = menii['pocetni']

    ispisiMeni(trenutniMeni)
    unosMeni(trenutniMeni)

if __name__ == '__main__':
    main()