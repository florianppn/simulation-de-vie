# -*- coding: utf-8 -*-
"""Tests unitaires pour Animal."""

from model.elements import entity_factory


class TestAnimal:
    """Tests des animaux créés via la factory (dépendent de model.config.animals)."""

    def test_animal_a_vie_et_barres(self):
        animal = entity_factory.create_animal("Vache")
        assert animal.get_life_max() > 0
        assert animal.get_bar_life()[0] == animal.get_bar_life()[1]
        assert animal.get_food()[0] == animal.get_food()[1]
        assert animal.get_drink()[0] == animal.get_drink()[1]

    def test_losing_life_diminue_la_vie(self):
        animal = entity_factory.create_animal("Souris")
        max_life = animal.get_life_max()
        animal.losing_life(1)
        assert animal.get_bar_life()[0] == max_life - 1
        animal.losing_life(10)
        assert animal.get_bar_life()[0] == 0

    def test_is_dead_apres_perte_totale(self):
        animal = entity_factory.create_animal("Souris")
        animal.losing_life(animal.get_life_max())
        assert animal.is_dead() is True

    def test_recovering_life_plafonne_au_max(self):
        animal = entity_factory.create_animal("Vache")
        animal.losing_life(2)
        animal.recovering_life(10)
        assert animal.get_bar_life()[0] == animal.get_life_max()

    def test_gender_est_0_ou_1(self):
        animal = entity_factory.create_animal("Humain")
        assert animal.get_gender() in (0, 1)

    def test_get_speed_et_move_size(self):
        animal = entity_factory.create_animal("Humain")
        assert animal.get_speed() >= 0
        assert animal.get_move_size() >= 0

    def test_set_parents(self):
        m = entity_factory.create_animal("Vache")
        f = entity_factory.create_animal("Vache")
        enfant = entity_factory.create_animal("Vache")
        enfant.set_parents(m, f)
        assert enfant.get_parents() == [m, f]
