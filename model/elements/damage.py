# -*- coding: utf-8 -*-
"""Représente un animal blessé (état temporaire après une attaque)."""

from model.elements.animal import Animal


class Damage(Animal):
    """Représente un animal blessé (état temporaire après une attaque)."""

    __slots__ = ()

    def __init__(self):
        super().__init__("Damage", "\U0001F4A2", 10)
