import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import patch
from funkcije.korisnik import prijava, dodaj_korisnika

@pytest.fixture
def mock_korisnici():
    return {
        "marko123": {
            'korisnicko_ime': 'marko123',
            'lozinka': 'Marko123',
            'ime': 'Marko',
            'prezime': 'Markovic',
            'uloga': '0',
            'status': '1',
            'uplaceni_paket': '1',
            'datum_registracije': '01.12.2024'
        }
    }

def test_prijava_uspesna(mock_korisnici):
    with patch("builtins.input", side_effect=["marko123", "Marko123"]):
        assert prijava(mock_korisnici, None) == mock_korisnici["marko123"]

def test_prijava_vec_prijavljen(mock_korisnici):
    with patch("builtins.input", side_effect=["marko123", "Marko123"]):
        assert prijava(mock_korisnici, mock_korisnici['marko123']) is mock_korisnici['marko123']

def test_prijava_pogresno_ime(mock_korisnici):
    with patch("builtins.input", side_effect=["pogresno_ime", "marko123", "Marko123"]):
        assert prijava(mock_korisnici, mock_korisnici['marko123']) is mock_korisnici['marko123']

def test_prijava_pogresna_sifra(mock_korisnici):
    with patch("builtins.input", side_effect=["marko123", "pogresna_sifra", "marko123", "Marko123"]):
        assert prijava(mock_korisnici, mock_korisnici['marko123']) is mock_korisnici['marko123']

def test_registracija_uspesna(mock_korisnici):
    with patch("builtins.input", side_effect=["nikola123", "Nikola123", "Nikola", "Nikolic"]):
        assert dodaj_korisnika(mock_korisnici) == True

def test_registracija_pogresna_sifra(mock_korisnici):
    with patch("builtins.input", side_effect=["nikola123", "Nikola", "Nik12", "Nikola123", "Nikola", "Nikolic"]):
        assert dodaj_korisnika(mock_korisnici) == True

def test_registracija_vec_registrovan(mock_korisnici):
    with patch("builtins.input", side_effect=["marko123", "nikola123", "Nikola123", "Nikola", "Nikolic"]):
        assert dodaj_korisnika(mock_korisnici) == True