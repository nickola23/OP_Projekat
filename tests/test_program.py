import pytest
from unittest.mock import patch
from funkcije.program import dodaj_program

@pytest.fixture
def mock_programi():
    return {
        "1": {
            'id': "1",
            'naziv': "Snaga i Kondicija",
            'id_vrste_treninga': "2",
            'trajanje': 60,
            'id_instruktora': "marko123",
            'potreban_paket': "1",
            'opis': "Program za jačanje tela i poboljšanje kondicije."
        }
    }

@pytest.fixture
def mock_vrste_treninga():
    return {
    '1': {'id': 1, 'naziv': 'Joga'},
    '2': {'id': 2, 'naziv': 'Snaga i Kondicija'},
    '3': {'id': 3, 'naziv': 'Kardio'}
}


@pytest.fixture
def mock_korisnici():
    return {
        "marko123": {
            'korisnicko_ime': 'marko123',
            'ime': 'Marko',
            'prezime': 'Markovic',
            'uloga': '1'
        }
    }

@pytest.fixture
def mock_vrste_paketa():
    return {
        '1': {'id': '1', 'naziv': "Standard"},
        '2': {'id': '2', 'naziv': "Premium"}
    }

def test_dodaj_program_uspesno(mock_programi, mock_vrste_treninga, mock_korisnici, mock_vrste_paketa):
    unos_podataka = [
        "HIIT",
        "2",
        "45",
        "marko123",
        "1",
        "Intenzivan program za sagorevanje kalorija"
    ]

    with patch("builtins.input", side_effect=unos_podataka):
        rezultat = dodaj_program(mock_programi, mock_vrste_treninga, mock_korisnici, mock_vrste_paketa)

    assert rezultat is True
    assert "2" in mock_programi

def test_dodaj_program_povratak_na_meni(mock_programi, mock_vrste_treninga, mock_korisnici, mock_vrste_paketa):
    with patch("builtins.input", side_effect=["b"]):
        rezultat = dodaj_program(mock_programi, mock_vrste_treninga, mock_korisnici, mock_vrste_paketa)

    assert rezultat is False

def test_dodaj_program_nevalidno_trajanje(mock_programi, mock_vrste_treninga, mock_korisnici, mock_vrste_paketa):
    unos_podataka = [
        "HIIT",
        "2",
        "-10",
        "30",
        "marko123",
        "1",
        "Test opis"
    ]

    with patch("builtins.input", side_effect=unos_podataka):
        rezultat = dodaj_program(mock_programi, mock_vrste_treninga, mock_korisnici, mock_vrste_paketa)

    assert rezultat is True
    assert "2" in mock_programi

def test_dodaj_program_nevalidan_instruktor(mock_programi, mock_vrste_treninga, mock_korisnici, mock_vrste_paketa):
    unos_podataka = [
        "HIIT",
        "2",
        "30",
        "nepoznati_instruktor",
        "marko123",
        "1",
        "Test opis"
    ]

    with patch("builtins.input", side_effect=unos_podataka):
        rezultat = dodaj_program(mock_programi, mock_vrste_treninga, mock_korisnici, mock_vrste_paketa)

    assert rezultat is True
    assert "2" in mock_programi

def test_dodaj_program_nevalidan_paket(mock_programi, mock_vrste_treninga, mock_korisnici, mock_vrste_paketa):
    unos_podataka = [
        "HIIT",
        "2",
        "30",
        "marko123",
        "99",
        "1",
        "Test opis"
    ]

    with patch("builtins.input", side_effect=unos_podataka):
        rezultat = dodaj_program(mock_programi, mock_vrste_treninga, mock_korisnici, mock_vrste_paketa)

    assert rezultat is True
    assert "2" in mock_programi
