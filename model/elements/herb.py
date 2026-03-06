# -*- coding: utf-8 -*-
"""Ressource herbe, consommable par les herbivores."""

from model.elements.resource import Resource


class Herb(Resource):
    """Ressource herbe, consommable par les herbivores."""

    __slots__ = ()

    def __init__(self):
        super().__init__("Herb", "\U0001F33F")
