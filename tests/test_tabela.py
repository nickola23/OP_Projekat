import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import time
from funkcije.tabela import max_duzina, kreiraj_tabelu, ispis_tabele

@pytest.fixture
def sample_podaci():
    return {
        "1": {"ID": 1, "Naziv": "Joga", "Trajanje": 60, "Instruktor": "Marko"},
        "2": {"ID": 2, "Naziv": "Snaga", "Trajanje": 45, "Instruktor": "Jovan"},
        "3": {"ID": 3, "Naziv": "Kardio", "Trajanje": 30, "Instruktor": "Ana"}
    }

@pytest.fixture
def sample_podaci_sa_listom():
    return {
        "1": {"ID": 1, "Naziv": "Joga", "Trajanje": 60, "Instruktori": ["Marko", "Jovan"]},
        "2": {"ID": 2, "Naziv": "Snaga", "Trajanje": 45, "Instruktori": ["Jovan"]},
    }

@pytest.fixture
def sample_podaci_sa_vremenom():
    return {
        "1": {"ID": 1, "Naziv": "Joga", "Trajanje": 60, "Vreme": time(8, 30)},
        "2": {"ID": 2, "Naziv": "Snaga", "Trajanje": 45, "Vreme": time(10, 15)},
    }

def test_max_duzina(sample_podaci):
    expected_output = {"ID": 2, "Naziv": 6, "Trajanje": 8, "Instruktor": 10}
    assert max_duzina(sample_podaci) == expected_output

def test_max_duzina_empty():
    assert max_duzina({}) == {}

def test_max_duzina_invalid():
    assert max_duzina([]) == {}

def test_kreiraj_tabelu(sample_podaci):
    duzine = max_duzina(sample_podaci)
    tabela = kreiraj_tabelu(sample_podaci, duzine)
    assert " | 1  | Joga   | 60       | Marko     \n | 2  | Snaga  | 45       | Jovan     \n | 3  | Kardio | 30       | Ana       \n" in tabela

def test_kreiraj_tabelu_sa_listom(sample_podaci_sa_listom):
    duzine = max_duzina(sample_podaci_sa_listom)
    tabela = kreiraj_tabelu(sample_podaci_sa_listom, duzine)
    assert " | 1  | Joga  | 60       | Marko, jovan      \n | 2  | Snaga | 45       | Jovan             \n" in tabela

def test_kreiraj_tabelu_sa_vremenom(sample_podaci_sa_vremenom):
    duzine = max_duzina(sample_podaci_sa_vremenom)
    tabela = kreiraj_tabelu(sample_podaci_sa_vremenom, duzine)
    assert " | 08:30" in tabela
    assert " | 10:15" in tabela

def test_ispis_tabele(sample_podaci, capsys):
    ispis_tabele(sample_podaci)
    captured = capsys.readouterr()
    assert "\n\n | ID | Naziv  | Trajanje | Instruktor\n-+----+--------+----------+-----------\n | 1  | Joga   | 60       | Marko     \n | 2  | Snaga  | 45       | Jovan     \n | 3  | Kardio | 30       | Ana       \n\n" in captured.out
