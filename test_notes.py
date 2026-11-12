import pytest
from notes import moyenne_ponderee


def test_moyenne_simple():
    assert moyenne_ponderee([10, 14], [1, 1]) == 12


def test_coefficients():
    assert moyenne_ponderee([10, 16], [1, 2]) == 14


def test_listes_incoherentes():
    with pytest.raises(ValueError):
        moyenne_ponderee([10], [1, 2])


def test_liste_vide():
    with pytest.raises(ValueError):
        moyenne_ponderee([], [])


def test_note_hors_bornes():
    with pytest.raises(ValueError):
        moyenne_ponderee([25, 10], [1, 1])


def test_coefficients_nuls():
    with pytest.raises(ValueError):
        moyenne_ponderee([10, 12], [0, 0])