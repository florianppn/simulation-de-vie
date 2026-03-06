# -*- coding: utf-8 -*-

from random import randint, choice
from model.config import animals, props


class Element:
    __ids_count = 0

    @classmethod
    def get_ids_count(cls) -> int:
        return cls.__ids_count

    @classmethod
    def incr_ids_count(cls) -> None:
        cls.__ids_count += 1

    @classmethod
    def decr_ids_count(cls) -> None:
        cls.__ids_count -= 1

    def __init__(self, name: str, char_repr: str):
        Element.incr_ids_count()
        self.__id = Element.get_ids_count()
        self.__name = name
        self.__char_repr = char_repr

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.__id

    def get_char_repr(self) -> str:
        return self.__char_repr

    def __repr__(self) -> str:
        return f"{self.get_char_repr()}"


class Animal(Element):
    def __init__(self, name: str, char_repr: str, life_max: int):
        Element.__init__(self, name, char_repr)
        self.__time_life = 0
        self.__gender = randint(0, 1)
        self.__bar_life = [animals[name]['weight'], animals[name]['weight']]
        self.__current_direction = [choice([-1, 0, 1]), choice([-1, 0, 1])]
        self.__bar_drink = [animals[name]['drink'], animals[name]['drink']]
        self.__bar_food = [animals[name]['food'], animals[name]['food']]
        self.__speed = animals[name]['speed']
        self.__move_size = animals[name]['move_size']
        self.__damage = animals[name]['damage']
        self.__weight = animals[name]['weight']
        self.__prey = animals[name]['prey']
        self.__parents = [None, None]
        self.__virus = False

    def get_time_life(self) -> int:
        return self.__time_life

    def set_time_life(self) -> None:
        self.__time_life += 1

    def get_gender(self) -> int:
        return self.__gender

    def get_life_max(self) -> int:
        return self.__bar_life[1]

    def get_life(self) -> int:
        return self.__bar_life[0]

    def get_bar_life(self) -> list:
        return self.__bar_life

    def is_dead(self) -> bool:
        return self.get_life() <= 0

    def recovering_life(self, value: int) -> None:
        if self.get_life() + value <= self.get_life_max():
            self.__bar_life[0] += value
        else:
            self.__bar_life[0] = self.get_life_max()

    def losing_life(self, value: int) -> None:
        if self.__bar_life[0] - value >= 0:
            self.__bar_life[0] -= value
        else:
            self.__bar_life[0] = 0

    def get_current_direction(self) -> list:
        return self.__current_direction

    def set_direction(self, line_direction: int, column_direction: int) -> None:
        self.__current_direction = [line_direction, column_direction]

    def get_drink(self) -> list:
        return self.__bar_drink

    def decr_drink(self, value: int) -> None:
        if self.__bar_drink[0] - value >= 0:
            self.__bar_drink[0] -= value
        else:
            self.__bar_drink[0] = 0

    def incr_drink(self, value: int) -> None:
        if self.__bar_drink[0] + value <= self.__bar_drink[1]:
            self.__bar_drink[0] += value
        else:
            self.__bar_drink[0] = self.__bar_drink[1]

    def reset_drink(self) -> None:
        self.__bar_drink[0] = self.__bar_drink[1]

    def is_thirsty(self) -> bool:
        return self.__bar_drink[0] == 0

    def get_food(self) -> list:
        return self.__bar_food

    def decr_food(self, value: int) -> None:
        if self.__bar_food[0] - value >= 0:
            self.__bar_food[0] -= value
        else:
            self.__bar_food[0] = 0

    def incr_food(self, value: int) -> None:
        if self.__bar_food[0] + value <= self.__bar_food[1]:
            self.__bar_food[0] += value
        else:
            self.__bar_food[0] = self.__bar_food[1]

    def is_hungry(self) -> bool:
        return self.__bar_food[0] == 0

    def get_damage(self) -> int:
        return self.__damage

    def get_prey(self) -> list:
        return self.__prey

    def is_prey(self, name: str) -> bool:
        return name in self.__prey

    def get_parents(self) -> list:
        return self.__parents

    def set_parents(self, mother=None, father=None) -> None:
        self.__parents[0] = mother
        self.__parents[1] = father

    def get_virus(self) -> bool:
        return self.__virus

    def set_virus(self, state: bool) -> None:
        self.__virus = state


class Resource(Element):
    def __init__(self, name: str, char_repr: str):
        Element.__init__(self, name, char_repr)
        self.__bar_value = [props[name]['value'], props[name]['value']]

    def get_bar_value(self) -> list:
        return self.__bar_value

    def decr_bar_value(self, value: int) -> None:
        if self.__bar_value[0] - value >= 0:
            self.__bar_value[0] -= value

    def reset_bar_value(self) -> None:
        self.__bar_value[0] = self.__bar_value[1]

    def is_available(self) -> bool:
        return self.__bar_value[0] != 0


class Ground(Element):
    def __init__(self):
        Element.__init__(self, "Ground", ".")


class Herb(Resource):
    def __init__(self):
        Resource.__init__(self, "Herb", "\U0001F33F")


class Water(Resource):
    def __init__(self):
        Resource.__init__(self, "Water", "\U0001F4A7")


class Humain(Animal):
    def __init__(self):
        Animal.__init__(self, "Humain", "\U0001F600", 100)


class Souris(Animal):
    def __init__(self):
        Animal.__init__(self, "Souris", "\U0001F42D", 2)


class Dragon(Animal):
    def __init__(self):
        Animal.__init__(self, "Dragon", "\U0001F432", 20)


class Vache(Animal):
    def __init__(self):
        Animal.__init__(self, "Vache", "\U0001F42E", 5)


class Autruche(Animal):
    def __init__(self):
        Animal.__init__(self, "Autruche", "\U0001F983", 5)


class Bizon(Animal):
    def __init__(self):
        Animal.__init__(self, "Bizon", "\U0001F9AC", 5)


class Bouc(Animal):
    def __init__(self):
        Animal.__init__(self, "Bouc", "\U0001F40F", 5)


class Bouctin(Animal):
    def __init__(self):
        Animal.__init__(self, "Bouctin", "\U0001F40F", 5)


class Buffle(Animal):
    def __init__(self):
        Animal.__init__(self, "Buffle", "\U0001F403", 5)


class Canard(Animal):
    def __init__(self):
        Animal.__init__(self, "Canard", "\U0001F986", 5)


class Chameau(Animal):
    def __init__(self):
        Animal.__init__(self, "Chameau", "\U0001F42A", 5)


class Chat(Animal):
    def __init__(self):
        Animal.__init__(self, "Chat", "\U0001F431", 5)


class Cheval(Animal):
    def __init__(self):
        Animal.__init__(self, "Cheval", "\U0001F434", 5)


class Chevre(Animal):
    def __init__(self):
        Animal.__init__(self, "Chevre", "\U0001F410", 5)


class Chien(Animal):
    def __init__(self):
        Animal.__init__(self, "Chien", "\U0001F436", 5)


class Chinchila(Animal):
    def __init__(self):
        Animal.__init__(self, "Chinchila", "\U0001F429", 5)


class Cochon(Animal):
    def __init__(self):
        Animal.__init__(self, "Cochon", "\U0001F437", 5)


class Fennec(Animal):
    def __init__(self):
        Animal.__init__(self, "Fennec", "\U0001F98A", 5)


class Licorne(Animal):
    def __init__(self):
        Animal.__init__(self, "Licorne", "\U0001F984", 5)


class Mouton(Animal):
    def __init__(self):
        Animal.__init__(self, "Mouton", "\U0001F411", 5)


class Oie(Animal):
    def __init__(self):
        Animal.__init__(self, "Oie", "\U0001F9A2", 5)


class Ours(Animal):
    def __init__(self):
        Animal.__init__(self, "Ours", "\U0001F43B", 5)


class Pingoin(Animal):
    def __init__(self):
        Animal.__init__(self, "Pingoin", "\U0001F427", 5)


class Poney(Animal):
    def __init__(self):
        Animal.__init__(self, "Poney", "\U0001F40E", 5)


class Raton(Animal):
    def __init__(self):
        Animal.__init__(self, "Raton", "\U0001F99D", 5)


class Renard(Animal):
    def __init__(self):
        Animal.__init__(self, "Renard", "\U0001F98A", 5)


class Renardeau(Animal):
    def __init__(self):
        Animal.__init__(self, "Renardeau", "\U0001F98A", 5)


class Sanglier(Animal):
    def __init__(self):
        Animal.__init__(self, "Sanglier", "\U0001F417", 5)


class Singe(Animal):
    def __init__(self):
        Animal.__init__(self, "Singe", "\U0001F435", 5)


class Tigre(Animal):
    def __init__(self):
        Animal.__init__(self, "Tigre", "\U0001F42F", 5)


class Mort(Animal):
    def __init__(self):
        Animal.__init__(self, "Mort", "\U0001F480", 10)


class Damage(Animal):
    def __init__(self):
        Animal.__init__(self, "Damage", "\U0001F4A2", 10)
