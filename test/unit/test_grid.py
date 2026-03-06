# -*- coding: utf-8 -*-
"""Tests unitaires pour Grid."""

import pytest
from model.grid import Grid


@pytest.fixture
def grid_3x3():
    return Grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def test_dimensions(grid_3x3):
    assert grid_3x3.lines_count == 3
    assert grid_3x3.columns_count == 3


def test_is_square(grid_3x3):
    assert grid_3x3.is_square() is True


def test_cell_number_coordinates_roundtrip(grid_3x3):
    assert grid_3x3.get_coordinates_from_cell_number(4) == (1, 1)
    assert grid_3x3.get_cell_number_from_coordinates(1, 1) == 4


def test_get_set_cell(grid_3x3):
    assert grid_3x3.get_cell(4) == 5
    grid_3x3.set_cell(4, 99)
    assert grid_3x3.get_cell(4) == 99


def test_get_neighbour_interieur(grid_3x3):
    assert grid_3x3.get_neighbour(1, 1, (0, 1)) == 6


def test_get_neighbour_exterieur_none(grid_3x3):
    assert grid_3x3.get_neighbour(0, 0, (-1, 0)) is None
