# -*- coding: utf-8 -*-
"""Tests unitaires pour Element."""

from model.elements.element import Element


class TestElement:
    """Tests de la classe de base Element."""

    def test_init_attribue_nom_et_char_repr(self):
        elt = Element("Test", "T")
        assert elt.get_name() == "Test"
        assert elt.get_char_repr() == "T"

    def test_id_est_incrémenté(self):
        before = Element._ids_count
        elt1 = Element("A", "a")
        elt2 = Element("B", "b")
        assert elt1.get_id() == before + 1
        assert elt2.get_id() == before + 2

    def test_repr_retourne_char_repr(self):
        elt = Element("Foo", "F")
        assert repr(elt) == "F"
