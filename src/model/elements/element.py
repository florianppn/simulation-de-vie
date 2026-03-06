# -*- coding: utf-8 -*-
"""Classe de base pour toute entité du monde."""


class Element:
    """Classe de base pour toute entité (animal, ressource, sol).

    Attributes:
        _id: Identifiant unique auto-incrémenté.
        _name: Nom de l'entité.
        _char_repr: Représentation caractère (emoji).
    """

    __slots__ = ("_id", "_name", "_char_repr")
    _ids_count = 0

    def __init__(self, name: str, char_repr: str):
        Element._ids_count += 1
        self._id = Element._ids_count
        self._name = name
        self._char_repr = char_repr

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._id

    def get_char_repr(self) -> str:
        return self._char_repr

    def __repr__(self) -> str:
        return self._char_repr
