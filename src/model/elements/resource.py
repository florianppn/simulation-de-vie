# -*- coding: utf-8 -*-
"""Ressource consommable avec une valeur."""

from model.elements.element import Element
from model.config import props


class Resource(Element):
    """Ressource consommable avec une valeur (herbe, eau)."""

    __slots__ = ("_bar_value",)

    def __init__(self, name: str, char_repr: str):
        super().__init__(name, char_repr)
        val = props[name]["value"]
        self._bar_value = [val, val]

    def get_bar_value(self) -> list:
        return self._bar_value

    def decr_bar_value(self, value: int) -> None:
        self._bar_value[0] = max(0, self._bar_value[0] - value)

    def reset_bar_value(self) -> None:
        self._bar_value[0] = self._bar_value[1]

    def is_available(self) -> bool:
        return self._bar_value[0] != 0
