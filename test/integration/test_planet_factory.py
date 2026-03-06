# -*- coding: utf-8 -*-
"""Tests d'intégration PlanetAlpha + entity_factory."""

import pytest

from model.planet import PlanetAlpha
from model.elements import entity_factory


class TestPlanetPlacement:
    """Placement d'entités sur la planète via la factory."""

    def test_planet_init_grille_ground(self):
        planet = PlanetAlpha()
        ground = planet.get_ground()
        assert ground.get_name() == "Ground"
        assert planet.get_count(ground) == planet.longitude_cells_count * planet.latitude_cells_count

    def test_place_animals_diminue_places_libres(self):
        planet = PlanetAlpha()
        ground = planet.get_ground()
        count_before = planet.get_count(ground)
        animals = [entity_factory.create_animal("Vache") for _ in range(3)]
        planet.place_animals(animals)
        assert planet.get_count(ground) == count_before - 3
        assert planet.get_current_animals_count() == 3

    def test_place_resources_diminue_places_libres(self):
        planet = PlanetAlpha()
        ground = planet.get_ground()
        count_before = planet.get_count(ground)
        resources = [entity_factory.create_resource("Herb"), entity_factory.create_resource("Water")]
        planet.place_resources(resources)
        assert planet.get_count(ground) == count_before - 2

    def test_get_random_free_place_retourne_numero_valide(self):
        planet = PlanetAlpha()
        place = planet.get_random_free_place()
        assert place >= 0
        assert place < planet.longitude_cells_count * planet.latitude_cells_count
