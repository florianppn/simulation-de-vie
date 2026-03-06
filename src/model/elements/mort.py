# -*- coding: utf-8 -*-
"""Cadavre laissé après la mort d'un animal."""

from model.elements.animal import Animal


class Mort(Animal):
    """Cadavre laissé après la mort d'un animal."""

    __slots__ = ()

    def __init__(self):
        super().__init__("Mort", "\U0001f480", 10)
