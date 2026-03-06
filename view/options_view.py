# -*- coding: utf-8 -*-
"""Vue des options/paramètres."""

import pygame
import os

import model.config as config


class Button:
    """Bouton réutilisable pour l'interface des options."""
    __bt_count = -1
    __last = "animal_list"

    @classmethod
    def bt_reset(cls) -> None:
        cls.__bt_count = 0

    @classmethod
    def get_bt_count(cls) -> int:
        return cls.__bt_count

    @classmethod
    def incr_bt_count(cls) -> None:
        cls.__bt_count += 1

    @classmethod
    def get_last(cls) -> str:
        return cls.__last

    @classmethod
    def set_last(cls, name) -> None:
        cls.__last = name

    def __init__(self, name, start, dim_button, gap, tipe):
        self.type = tipe
        if self.type != Button.get_last():
            Button.set_last(self.type)
            Button.bt_reset()
        else:
            Button.incr_bt_count()

        self.name = name
        self.largeur_bouton = dim_button[0]
        self.hauteur_bouton = dim_button[1]
        self.start = start
        self.gap = gap
        self.x_button = self.start[0]
        if Button.get_bt_count() != 0:
            self.y_button = self.start[1] + (self.hauteur_bouton + self.gap) * Button.get_bt_count()
        else:
            self.y_button = self.start[1]


class OptionsView:
    """Vue des paramètres (animaux, humain)."""

    def __init__(self):
        self.gap = 8
        self.image_fond = pygame.image.load("assets/menu/fond_config.png").convert()
        self.sprite_size = 48

        self.liste_button_animal = [Button(elt, (10, 20), (74, 22), 8, "animal_list") for elt in config.MOVABLE_ELEMENT]
        self.liste_button_param_1 = [Button(elt, (282, 149), (32, 31), 10, "param_1") for elt in config.ENTITY_PARAM]
        self.liste_button_param_10 = [Button(elt, (318, 149), (32, 31), 10, "param_10") for elt in config.ENTITY_PARAM]
        self.liste_button_param_n10 = [Button(elt, (353, 149), (32, 31), 10, "param_n10") for elt in config.ENTITY_PARAM]
        self.liste_button_param_0 = [Button(elt, (388, 149), (32, 31), 10, "param_0") for elt in config.ENTITY_PARAM]

        self.liste_button_param_humain_1 = [Button(elt, (596, 277), (32, 31), 10, "param__humain_1") for elt in config.HUMAN_PARAM]
        self.liste_button_param_humain_10 = [Button(elt, (632, 277), (32, 31), 10, "param__humain_10") for elt in config.HUMAN_PARAM]
        self.liste_button_param_humain_n10 = [Button(elt, (667, 277), (32, 31), 10, "param__humain_n10") for elt in config.HUMAN_PARAM]
        self.liste_button_param_humain_0 = [Button(elt, (702, 277), (32, 31), 10, "param__humain_0") for elt in config.HUMAN_PARAM]

        self.BLANC = (255, 255, 255)
        self.GREEN = (40, 180, 99)
        self.police_name = pygame.font.Font(None, 36)
        self.police_values = pygame.font.Font(None, 25)

    def render(self, screen, selected_entity):
        """Affiche l'écran des options."""
        screen.blit(pygame.transform.scale(self.image_fond, (900, 900)), (0, 0))
        self._humain_stat(screen)
        self._entity_stat(screen, selected_entity)

    def _entity_stat(self, screen, i):
        """Affiche les stats de l'entité sélectionnée."""
        entity = config.animals[self.liste_button_animal[i].name]
        entity_name = self.police_name.render(self.liste_button_animal[i].name, True, self.GREEN)
        screen.blit(entity_name, (187, 68))

        stats = [
            (str(entity["count"]), (202, 157)),
            (str(entity["speed"]), (206, 200)),
            (str(entity["move_size"]), (195, 240)),
            (str(entity["damage"]), (222, 283)),
            (str(entity["food"]), (195, 325)),
            (str(entity["drink"]), (196, 366)),
            (str(entity["weight"]), (220, 408)),
        ]

        for val, pos in stats:
            entity_stat = self.police_values.render(val, True, self.BLANC)
            screen.blit(entity_stat, pos)

    def _humain_stat(self, screen):
        """Affiche les stats de l'humain."""
        sprite_sheet = pygame.image.load(os.path.join(f"./assets/animaux/Humain/Humain ({config.HUMAIN_CP+1}).png")).convert_alpha()
        image = pygame.Surface((self.sprite_size, self.sprite_size), pygame.SRCALPHA)
        image.blit(sprite_sheet, (0, 0), (0, 0, self.sprite_size, self.sprite_size))
        image = image.subsurface(image.get_bounding_rect())

        entity_name = self.police_name.render(config.HUMAIN_NAME[config.HUMAIN_CP], True, self.GREEN)
        entity_speed = self.police_values.render(str(config.animals["Humain"]["speed"]), True, self.BLANC)
        entity_move_size = self.police_values.render(str(config.animals["Humain"]["move_size"]), True, self.BLANC)
        entity_damage = self.police_values.render(str(config.animals["Humain"]["damage"]), True, self.BLANC)
        entity_food = self.police_values.render(str(config.animals["Humain"]["food"]), True, self.BLANC)
        entity_drink = self.police_values.render(str(config.animals["Humain"]["drink"]), True, self.BLANC)

        screen.blit(image, (565, 90))
        screen.blit(entity_name, (528, 213))
        screen.blit(entity_speed, (548, 325))
        screen.blit(entity_move_size, (528, 367))
        screen.blit(entity_damage, (550, 284))
        screen.blit(entity_food, (525, 410))
        screen.blit(entity_drink, (534, 452))
