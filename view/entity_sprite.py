# -*- coding: utf-8 -*-
"""Sprite d'entité - Représentation visuelle des éléments du jeu."""

import pygame
from random import choice, randint

from view.animation import AnimateSprite
from model.config import *


class EntitySprite(AnimateSprite):
    """Sprite Pygame représentant une entité (animal, ressource, etc.).

    Lie le modèle (Element) à sa représentation visuelle.
    Gère le déplacement (Humain au clavier, autres animaux aléatoires).

    Attributes:
        entity: Instance de Element (Animal, Resource, etc.).
        name: Nom de l'entité.
        position: Coordonnées [x, y] en pixels.
    """

    def __init__(self, entity, x, y, grille, no_temp=True):
        super().__init__(entity, grille)

        self.entity = entity
        self.name = entity.get_name()
        self.no_temp = no_temp
        if self.no_temp:
            self.position = [x * PLANET_PYGAME_SIZE_GRID + 500, y * PLANET_PYGAME_SIZE_GRID + 500]
        else:
            self.position = [x, y]

        self.pos = [randint(-1, 1), randint(-1, 1)]

        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.clock = randint(0, 1000)

    def update(self):
        """Met à jour les coordonnées du sprite."""
        self.rect.topleft = self.position

    def change_anim_dir(self):
        """Change l'animation selon la direction."""
        if self.pos[0] == 1:
            self.change_animation("right")
        elif self.pos[0] == -1:
            self.change_animation("left")
        elif self.pos[1] == 1:
            self.change_animation("down")
        elif self.pos[1] == -1:
            self.change_animation("up")

    def human_move(self):
        """Gère les mouvements du joueur humain."""
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.pos[0] = 1
        elif pressed[pygame.K_LEFT]:
            self.pos[0] = -1
        else:
            self.pos[0] = 0

        if pressed[pygame.K_DOWN]:
            self.pos[1] = 1
        elif pressed[pygame.K_UP]:
            self.pos[1] = -1
        else:
            self.pos[1] = 0

    def move(self):
        """Déplace le sprite selon la direction."""
        for i in range(animals[self.name]["speed"]):
            if self.name == "Humain":
                self.human_move()
            if self.position[0] + self.pos[0] > 500 and self.position[0] + self.pos[0] < WORLD_SIZE[0] - 40 + 500:
                if self.position[1] + self.pos[1] > 500 and self.position[1] + self.pos[1] < WORLD_SIZE[1] - 40 + 500:
                    self.change_anim_dir()
                    self.position[0] += self.pos[0]
                    self.position[1] += self.pos[1]
                else:
                    self.pos = [self.pos[0] * -1, self.pos[1] * -1]
            else:
                self.pos = [self.pos[0] * -1, self.pos[1] * -1]

        self.clock -= animals[self.name]["move_size"]
        if self.clock <= 0:
            self.clock = 500
            if self.name != "Humain":
                self.pos = [choice([-1, 0, 0, 1]), choice([-1, 0, 0, 1])]
