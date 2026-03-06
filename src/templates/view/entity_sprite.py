# -*- coding: utf-8 -*-
"""Sprite d'entité - Représentation visuelle des éléments du jeu.

Ne dépend pas du modèle : reçoit les données nécessaires en paramètres.
"""

import pygame
from random import choice, randint

from templates.view.animation import AnimateSprite


class EntitySprite(AnimateSprite):
    """Sprite Pygame représentant une entité (animal, ressource, etc.).

    Lie le modèle (Element) à sa représentation visuelle.
    Gère le déplacement (Humain au clavier, autres animaux aléatoires).

    Attributes:
        entity: Instance de Element (Animal, Resource, etc.).
        name: Nom de l'entité.
        position: Coordonnées [x, y] en pixels.
    """

    def __init__(self, entity, x, y, grille, no_temp=True, grid_size=48, world_size=None):
        super().__init__(entity, grille)

        self.entity = entity
        self.name = entity.get_name()
        self.no_temp = no_temp
        self._grid_size = grid_size
        self._world_size = world_size or (1440, 1440)
        if self.no_temp:
            offset = 500
            self.position = [x * self._grid_size + offset, y * self._grid_size + offset]
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
        speed = getattr(self.entity, "get_speed", lambda: 1)()
        move_size = getattr(self.entity, "get_move_size", lambda: 10)()
        for _ in range(speed):
            if self.name == "Humain":
                self.human_move()
            offset = 500
            max_x = self._world_size[0] - 40 + offset
            max_y = self._world_size[1] - 40 + offset
            if offset < self.position[0] + self.pos[0] < max_x and offset < self.position[1] + self.pos[1] < max_y:
                self.change_anim_dir()
                self.position[0] += self.pos[0]
                self.position[1] += self.pos[1]
            else:
                self.pos = [self.pos[0] * -1, self.pos[1] * -1]

        self.clock -= move_size
        if self.clock <= 0:
            self.clock = 500
            if self.name != "Humain":
                self.pos = [choice([-1, 0, 0, 1]), choice([-1, 0, 0, 1])]
