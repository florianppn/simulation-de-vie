# -*- coding: utf-8 -*-
"""Ressource eau, régénère la soif des animaux à proximité."""

from model.elements.resource import Resource


class Water(Resource):
    """Ressource eau, régénère la soif des animaux à proximité."""

    __slots__ = ()

    def __init__(self):
        super().__init__("Water", "\U0001F4A7")
