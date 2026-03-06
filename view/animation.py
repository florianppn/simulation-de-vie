# -*- coding: utf-8 -*-

import pygame
import os
from random import choice


class AnimateSprite(pygame.sprite.Sprite):
    """Sprite animé avec sprite sheet."""

    def __init__(self, entity, grille):
        super().__init__()
        self.grille = grille
        self.sprite_sheet = None
        self.random_choice(entity)

        self.animation_index = 0
        self.sprite_size = 48
        self.images = {
            'down': self.get_images(0),
            'left': self.get_images(self.sprite_size),
            'right': self.get_images(self.sprite_size * 2),
            'up': self.get_images(self.sprite_size * 3),
        }
        self.time = 0
        self.speed = 2

    def random_choice(self, name):
        """Charge le sprite approprié (Water avec voisins, etc.)."""
        if name.get_name() == "Water":
            text = ""
            grid = [1 if elt is not None and elt.get_name() == "Water" else 0 for elt in self.grille]
            grid[0] = 0
            grid[2] = 0
            grid[4] = 0
            grid[6] = 0
            for elt in grid:
                text += str(elt)
            try:
                sprite_name = f"{text}.png"
                self.sprite_sheet = pygame.image.load(f"./assets/animaux/{name.get_name()}/{sprite_name}").convert_alpha()
            except FileNotFoundError:
                sprite_name = "11111111.png"
                self.sprite_sheet = pygame.image.load(f"./assets/animaux/{name.get_name()}/{sprite_name}").convert_alpha()
        else:
            sprite_name = choice(os.listdir(f"./assets/animaux/{name.get_name()}"))
            self.sprite_sheet = pygame.image.load(f"./assets/animaux/{name.get_name()}/{sprite_name}").convert_alpha()

    def change_animation(self, name):
        """Change l'animation courante."""
        self.image = self.images[name][self.animation_index]
        self.time += self.speed * 5

        if self.time >= 100:
            self.animation_index += 1
            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0
            self.time = 0

    def get_images(self, y):
        """Extrait les frames du sprite sheet."""
        images = []
        for i in range(0, 3):
            x = i * self.sprite_size
            image = self.get_image(x, y)
            images.append(image)
        return images

    def get_image(self, x, y):
        """Retourne une sous-image du sprite sheet."""
        image = pygame.Surface((self.sprite_size, self.sprite_size), pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (x, y, self.sprite_size, self.sprite_size))
        image = image.subsurface(image.get_bounding_rect())
        return image
