# -*- coding: utf-8 -*-
"""Tests unitaires pour l'Abstract Factory (entity_factory)."""

import pytest

from model.elements import entity_factory
from model.elements.animal import Animal
from model.elements.ground import Ground
from model.elements.herb import Herb
from model.elements.water import Water
from model.elements.mort import Mort
from model.elements.damage import Damage


class TestPlanetEntityFactory:
    """Tests de PlanetEntityFactory (singleton entity_factory)."""

    def test_create_animal_retourne_animal(self):
        animal = entity_factory.create_animal("Vache")
        assert isinstance(animal, Animal)
        assert animal.get_name() == "Vache"

    def test_create_animal_especes_connues(self):
        for name in ["Humain", "Souris", "Dragon", "Fennec"]:
            animal = entity_factory.create_animal(name)
            assert animal.get_name() == name
            assert animal.get_life_max() > 0

    def test_create_resource_herb(self):
        r = entity_factory.create_resource("Herb")
        assert isinstance(r, Herb)
        assert r.get_name() == "Herb"

    def test_create_resource_water(self):
        r = entity_factory.create_resource("Water")
        assert isinstance(r, Water)
        assert r.get_name() == "Water"

    def test_create_resource_inconnue_leve_value_error(self):
        with pytest.raises(ValueError, match="Ressource inconnue"):
            entity_factory.create_resource("Inconnu")

    def test_create_ground_retourne_ground(self):
        g = entity_factory.create_ground()
        assert isinstance(g, Ground)
        assert g.get_name() == "Ground"

    def test_create_mort_retourne_mort(self):
        m = entity_factory.create_mort()
        assert isinstance(m, Mort)
        assert m.get_name() == "Mort"

    def test_create_damage_retourne_damage(self):
        d = entity_factory.create_damage()
        assert isinstance(d, Damage)
        assert d.get_name() == "Damage"
