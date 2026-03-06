# -*- coding: utf-8 -*-
"""Tests d'intégration flux Model -> get_view_data -> ViewState."""

import pytest

from model.planet import PlanetAlpha
from model.elements import entity_factory
from model.config import PLANET_LONGITUDE_CELLS_COUNT, PLANET_LATITUDE_CELLS_COUNT


def test_planet_get_count_apres_placement():
    """Vérifie que get_count reflète bien les entités placées."""
    planet = PlanetAlpha()
    ground = planet.get_ground()
    herb = entity_factory.create_resource("Herb")
    planet.place_resources([herb])
    total_cells = PLANET_LONGITUDE_CELLS_COUNT * PLANET_LATITUDE_CELLS_COUNT
    assert planet.get_count(ground) == total_cells - 1
