# -*- coding: utf-8 -*-
"""Modèle du jeu - Logique métier (collisions, reproduction, virus, etc.)."""

import pytmx
import pyscroll
from random import choice

from model.planet import PlanetAlpha
from model.grid import Grid
from model.config import *
from model.elements import entity_factory
from view.entity_sprite import EntitySprite


class GameModel(PlanetAlpha):
    """Modèle du jeu contenant la logique métier.

    Gère les collisions, la reproduction, les virus, la prédation,
    la faim et la soif. Utilise la carte Tiled et pyscroll pour le rendu.

    Attributes:
        entity_group: Groupe pyscroll des sprites affichés.
        player: Référence au sprite du joueur (Humain).
        stats_entity: Entité sélectionnée pour afficher ses stats.
    """

    def __init__(self, screen_size):
        PlanetAlpha.__init__(self)

        tmx_data = pytmx.util_pygame.load_pygame('./assets/map/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen_size)
        map_layer.zoom = ZOOM

        self.entity_group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.player = None
        self.stats_entity = None
        self.clock = 0
        self.fps = FPS

        self.zoom = ZOOM
        if self.zoom == 1:
            self.render_distance = 950
        elif self.zoom == 2:
            self.render_distance = 350
        elif self.zoom == 3:
            self.render_distance = 250

    def entity_add(self):
        """Ajoute toutes les entités au groupe de rendu."""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].get_name() != 'Ground':
                    entity = EntitySprite(
                        self.grid[i][j], i, j,
                        Grid.get_neighborhood(self, i, j, WIND_ROSE) if self.grid[i][j].get_name() == 'Water' else None
                    )
                    if self.grid[i][j].get_name() == "Humain":
                        self.player = entity
                    if self.grid[i][j].get_name() in MOVABLE_ELEMENT:
                        self.entity_group.add(entity, layer=3)
                    elif self.grid[i][j].get_name() in PROPS_ELEMENT:
                        self.entity_group.add(entity, layer=2)
                    else:
                        self.entity_group.add(entity, layer=1)

    def get_collision(self, element):
        """Détecte les collisions et renvoie la liste des entités en contact."""
        collisions_list = []
        for cible in self.entity_group:
            if element.entity.get_id() != cible.entity.get_id():
                if (cible.position[0] > element.position[0] - 48 and cible.position[0] < element.position[0] + 48):
                    if (cible.position[1] > element.position[1] - 48 and cible.position[1] < element.position[1] + 48):
                        collisions_list.append(cible)
        return collisions_list

    def is_render(self, cible):
        """Détermine si l'entité est dans la zone de rendu."""
        if cible.position[0] > self.player.position[0] - self.render_distance and cible.position[0] < self.player.position[0] + self.render_distance:
            if cible.position[1] > self.player.position[1] - self.render_distance and cible.position[1] < self.player.position[1] + self.render_distance:
                return True
        return False

    def entity_count(self, tipe=None):
        counter = 0
        entity_dict = {}
        if tipe == MOVABLE_ELEMENT:
            for elt in self.entity_group:
                if elt.name in MOVABLE_ELEMENT:
                    counter += 1
            return counter
        elif tipe == PROPS_ELEMENT:
            for elt in self.entity_group:
                if elt.name in PROPS_ELEMENT:
                    counter += 1
            return counter
        elif tipe is None:
            for elt in self.entity_group:
                counter += 1
                if elt.name in entity_dict:
                    entity_dict[elt.name] += 1
                else:
                    entity_dict[elt.name] = 1
            return entity_dict

    def kill(self, elt):
        """Supprime l'entité et la remplace par Mort si nécessaire."""
        if elt.entity.get_name() not in ["Mort", "Damage"]:
            self.entity_group.remove(elt)
            entity = EntitySprite(entity_factory.create_mort(), elt.position[0], elt.position[1], [], False)
            self.entity_group.add(entity, layer=2)
        else:
            self.entity_group.remove(elt)

    def percentage_chance(self, chance: int) -> bool:
        """Retourne True avec une probabilité de chance%."""
        if chance >= 100:
            return True
        return choice([False if i != int(chance/2) or chance == 0 else True for i in range(100-chance)])

    def random_attack(self, elt, collision_list: list) -> None:
        """Gère les attaques aléatoires des animaux."""
        list_neighbors = [animal for animal in collision_list if animal.name != 'Water']
        if elt.name != 'Humain' and len(list_neighbors) > 0:
            alea = choice(list_neighbors)
            if elt.entity.is_prey(alea.name):
                if alea.name != 'Herb':
                    alea.entity.losing_life(elt.entity.get_damage())
                    if alea.entity.is_dead():
                        elt.entity.incr_food(alea.entity.get_life_max())
                        self.kill(alea)
                    else:
                        entity = EntitySprite(entity_factory.create_damage(), elt.position[0], elt.position[1], [], False)
                        self.entity_group.add(entity, layer=3)
                else:
                    alea.entity.decr_bar_value(1)
                    elt.entity.incr_food(1)

    def neighboring_water(self, elt, collision_list: list) -> None:
        """Régénère la soif si l'animal est à côté de l'eau."""
        for entite in collision_list:
            if entite.name == 'Water':
                elt.entity.reset_drink()
                break

    def entity_event(self, elt) -> None:
        """Exécute les événements pour une entité."""
        collision_entity = self.get_collision(elt)
        self.birth(elt, collision_entity)
        elt.entity.set_time_life()
        self.catch_virus(elt)
        self.lose_virus(elt)
        if elt.entity.get_drink()[0] <= elt.entity.get_drink()[1] and elt.entity.get_food()[0] <= elt.entity.get_food()[1]:
            self.neighboring_water(elt, collision_entity)
            self.random_attack(elt, collision_entity)
            self.dying_hunger_thirst(elt)

    def dying_hunger_thirst(self, elt) -> None:
        """L'animal perd de la vie s'il a faim ou soif."""
        if elt.entity.is_hungry() or elt.entity.is_thirsty():
            elt.entity.losing_life(1)

    def birth(self, elt, collision_list) -> None:
        """Reproduction : 25% de chance si deux animaux de même espèce et sexe différent."""
        if self.percentage_chance(25):
            for entite in collision_list:
                if entite.name == elt.name and entite.entity.get_gender() != elt.entity.get_gender():
                    newAnimal = entity_factory.create_animal(elt.name)
                    newAnimal.set_parents(entite if entite.entity.get_gender() == 0 else elt, entite if entite.entity.get_gender() == 1 else elt)
                    entity = EntitySprite(newAnimal, elt.position[0], elt.position[1], [], False)
                    self.entity_group.add(entity, layer=3)
                    break

    def catch_virus(self, elt) -> None:
        """10% de chance d'attraper un virus."""
        if self.percentage_chance(10) and elt.entity.get_virus() is False and elt.name != 'Humain':
            elt.entity.set_virus(True)

    def lose_virus(self, elt) -> None:
        """2% de chance de guérir du virus."""
        if self.percentage_chance(2) and elt.entity.get_virus() is True:
            elt.entity.set_virus(False)

    def virus_damage(self, elt) -> None:
        """L'animal avec virus perd de la vie."""
        if elt.entity.get_virus() is True:
            elt.entity.losing_life(1)

    def get_entity_at_click(self, pos):
        """Retourne l'entité à la position du clic."""
        for elt in self.entity_group:
            if self.is_render(elt):
                calc = [pos[0] - 485 + self.player.position[0], pos[1] - 485 + self.player.position[1]]
                if (elt.position[0] > calc[0] - 24 and elt.position[0] < calc[0] + 24):
                    if (elt.position[1] > calc[1] - 24 and elt.position[1] < calc[1] + 24):
                        return elt
        return None

    def select_entity(self, pos):
        """Sélectionne l'entité au clic."""
        entity = self.get_entity_at_click(pos)
        self.stats_entity = entity

    def update(self):
        """Boucle d'actualisation de la logique du jeu."""
        self.clock -= 1
        for elt in self.entity_group:
            if self.is_render(elt):
                if elt.name in MOVABLE_ELEMENT:
                    elt.move()

                    if self.clock % (self.fps / 4) == 0:
                        if elt.name == "Damage":
                            self.kill(elt)

                    if self.clock % self.fps == 0:
                        self.entity_event(elt)

                    if self.clock % (self.fps * 5) == 0:
                        elt.entity.decr_drink(1)
                        elt.entity.decr_food(1)
                        self.virus_damage(elt)

                else:
                    if self.clock % (self.fps * 5) == 0:
                        if elt.entity.get_name() == 'Herb':
                            elt.entity.reset_bar_value()

        if self.clock <= 0:
            self.clock = 3600
            for elt in self.entity_group:
                if elt.name == "Mort":
                    if self.is_render(elt):
                        self.kill(elt)

        self.entity_group.update()
        self.entity_group.center(self.player.rect.center)
