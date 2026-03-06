# -*- coding: utf-8 -*-
"""Sol par défaut des cellules vides."""

from model.elements.element import Element


class Ground(Element):
    """Sol par défaut des cellules vides."""

    __slots__ = ()

    def __init__(self):
        super().__init__("Ground", ".")
