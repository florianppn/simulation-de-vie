# -*- coding: utf-8 -*-
"""Entité vivante avec vie, faim, soif, reproduction et prédation."""

from random import randint, choice

from model.elements.element import Element
from model.config import animals


class Animal(Element):
    """Entité vivante avec vie, faim, soif, reproduction et prédation."""

    __slots__ = (
        "_time_life",
        "_gender",
        "_bar_life",
        "_current_direction",
        "_bar_drink",
        "_bar_food",
        "_speed",
        "_move_size",
        "_damage",
        "_weight",
        "_prey",
        "_parents",
        "_virus",
    )

    def __init__(self, name: str, char_repr: str, life_max: int):
        super().__init__(name, char_repr)
        cfg = animals[name]
        self._time_life = 0
        self._gender = randint(0, 1)
        self._bar_life = [cfg["weight"], cfg["weight"]]
        self._current_direction = [choice([-1, 0, 1]), choice([-1, 0, 1])]
        self._bar_drink = [cfg["drink"], cfg["drink"]]
        self._bar_food = [cfg["food"], cfg["food"]]
        self._speed = cfg["speed"]
        self._move_size = cfg["move_size"]
        self._damage = cfg["damage"]
        self._weight = cfg["weight"]
        self._prey = cfg["prey"]
        self._parents = [None, None]
        self._virus = False

    def get_time_life(self) -> int:
        return self._time_life

    def set_time_life(self) -> None:
        self._time_life += 1

    def get_gender(self) -> int:
        return self._gender

    def get_life_max(self) -> int:
        return self._bar_life[1]

    def get_life(self) -> int:
        return self._bar_life[0]

    def get_bar_life(self) -> list:
        return self._bar_life

    def is_dead(self) -> bool:
        return self._bar_life[0] <= 0

    def recovering_life(self, value: int) -> None:
        self._bar_life[0] = min(self._bar_life[0] + value, self._bar_life[1])

    def losing_life(self, value: int) -> None:
        self._bar_life[0] = max(0, self._bar_life[0] - value)

    def get_current_direction(self) -> list:
        return self._current_direction

    def set_direction(self, line_direction: int, column_direction: int) -> None:
        self._current_direction = [line_direction, column_direction]

    def get_drink(self) -> list:
        return self._bar_drink

    def decr_drink(self, value: int) -> None:
        self._bar_drink[0] = max(0, self._bar_drink[0] - value)

    def incr_drink(self, value: int) -> None:
        self._bar_drink[0] = min(self._bar_drink[0] + value, self._bar_drink[1])

    def reset_drink(self) -> None:
        self._bar_drink[0] = self._bar_drink[1]

    def is_thirsty(self) -> bool:
        return self._bar_drink[0] == 0

    def get_food(self) -> list:
        return self._bar_food

    def decr_food(self, value: int) -> None:
        self._bar_food[0] = max(0, self._bar_food[0] - value)

    def incr_food(self, value: int) -> None:
        self._bar_food[0] = min(self._bar_food[0] + value, self._bar_food[1])

    def is_hungry(self) -> bool:
        return self._bar_food[0] == 0

    def get_damage(self) -> int:
        return self._damage

    def get_speed(self) -> int:
        return self._speed

    def get_move_size(self) -> int:
        return self._move_size

    def get_prey(self) -> list:
        return self._prey

    def is_prey(self, name: str) -> bool:
        return name in self._prey

    def get_parents(self) -> list:
        return self._parents

    def set_parents(self, mother=None, father=None) -> None:
        self._parents = [mother, father]

    def get_virus(self) -> bool:
        return self._virus

    def set_virus(self, state: bool) -> None:
        self._virus = state
