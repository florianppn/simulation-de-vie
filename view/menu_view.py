# -*- coding: utf-8 -*-
"""Vue du menu principal."""

import pygame
import os

from model.config import WINDOW_SIZES


class MenuView:
    """Vue du menu principal (Start, Option, Quit)."""

    def __init__(self):
        self.gap = 30
        self.image_fond = pygame.image.load("Menu/images/fond.png").convert()

        self.largeur_bouton = 240
        self.hauteur_bouton = 126
        repertoire_images = "Menu/images/"
        self.image_bouton_start = pygame.image.load(os.path.join(repertoire_images, "start.png")).convert_alpha()
        self.image_bouton_start = pygame.transform.scale(self.image_bouton_start, (self.largeur_bouton, self.hauteur_bouton))

        self.image_bouton_option = pygame.image.load(os.path.join(repertoire_images, "option.png")).convert_alpha()
        self.image_bouton_option = pygame.transform.scale(self.image_bouton_option, (self.largeur_bouton, self.hauteur_bouton))

        self.image_bouton_quit = pygame.image.load(os.path.join(repertoire_images, "quit.png")).convert_alpha()
        self.image_bouton_quit = pygame.transform.scale(self.image_bouton_quit, (self.largeur_bouton, self.hauteur_bouton))

        centre_x = WINDOW_SIZES["menu"][0] // 2
        centre_y = WINDOW_SIZES["menu"][0] // 2 + 50

        self.x_bouton_start = centre_x - (self.largeur_bouton // 2)
        self.y_bouton_start = centre_y - (self.hauteur_bouton // 2) - (self.hauteur_bouton + self.gap)

        self.x_bouton_option = centre_x - (self.largeur_bouton // 2)
        self.y_bouton_option = centre_y - (self.hauteur_bouton // 2)

        self.x_bouton_quit = centre_x - (self.largeur_bouton // 2)
        self.y_bouton_quit = centre_y - (self.hauteur_bouton // 2) + (self.hauteur_bouton + self.gap)

    def render(self, screen):
        """Affiche le menu."""
        screen.blit(pygame.transform.scale(self.image_fond, WINDOW_SIZES["menu"]), (0, 0))
        screen.blit(self.image_bouton_start, (self.x_bouton_start, self.y_bouton_start))
        screen.blit(self.image_bouton_option, (self.x_bouton_option, self.y_bouton_option))
        screen.blit(self.image_bouton_quit, (self.x_bouton_quit, self.y_bouton_quit))
