# -*- coding: utf-8 -*-
"""Abstract Factory pour la création des entités du jeu."""

from abc import ABC, abstractmethod

from model.elements.element import Element
from model.elements.animal import Animal
from model.elements.resource import Resource
from model.elements.ground import Ground
from model.elements.herb import Herb
from model.elements.water import Water
from model.elements.mort import Mort
from model.elements.damage import Damage
from model.elements.specs import ANIMAL_SPECS


class AbstractEntityFactory(ABC):
    """Fabrique abstraite pour créer les entités du monde."""

    @abstractmethod
    def create_animal(self, name: str) -> Animal:
        """Crée un animal par son nom."""
        pass

    @abstractmethod
    def create_resource(self, name: str) -> Resource:
        """Crée une ressource par son nom."""
        pass

    @abstractmethod
    def create_ground(self) -> Element:
        """Crée le sol par défaut."""
        pass

    @abstractmethod
    def create_mort(self) -> Animal:
        """Crée une entité Mort (cadavre)."""
        pass

    @abstractmethod
    def create_damage(self) -> Animal:
        """Crée une entité Damage (animal blessé)."""
        pass


class PlanetEntityFactory(AbstractEntityFactory):
    """Implémentation concrète pour PlanetGame."""

    def create_animal(self, name: str) -> Animal:
        """Crée un animal configuré selon son espèce."""
        emoji, life_max = ANIMAL_SPECS[name]
        return Animal(name, emoji, life_max)

    def create_resource(self, name: str) -> Resource:
        """Crée une ressource (Herb ou Water)."""
        if name == "Herb":
            return Herb()
        if name == "Water":
            return Water()
        raise ValueError(f"Ressource inconnue: {name}")

    def create_ground(self) -> Element:
        """Crée le sol."""
        return Ground()

    def create_mort(self) -> Animal:
        """Crée un cadavre."""
        return Mort()

    def create_damage(self) -> Animal:
        """Crée un animal blessé."""
        return Damage()


# Instance singleton pour l'application
entity_factory: AbstractEntityFactory = PlanetEntityFactory()
