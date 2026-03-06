# -*- coding: utf-8 -*-
"""Contrôleur principal - Orchestration des écrans."""

import pygame

from model.config import WINDOW_SIZES
from model.game_model import GameModel
from controller.menu_controller import MenuController
from controller.options_controller import OptionsController
from controller.game_controller import GameController


class MainController:
    """Contrôleur principal orchestrant les écrans (menu, options, jeu).

    Gère les transitions entre les interfaces et la boucle principale.
    """

    def __init__(self):
        pygame.init()
        # Initialiser l'affichage pour permettre le chargement des ressources (carte TMX)
        pygame.display.set_mode(WINDOW_SIZES["menu"])
        screen_size = WINDOW_SIZES["game"]
        self.game_model = GameModel(screen_size)
        self.menu_controller = MenuController(self.game_model)
        self.options_controller = OptionsController(self.game_model)
        self.game_controller = GameController()
        self.game_controller.model = self.game_model

        self.current_interface = "menu"
        self.previous_interface = None

    def run(self):
        """Boucle principale de l'application."""
        screen = None
        while self.current_interface != "quit":
            if self.current_interface != self.previous_interface:
                screen = pygame.display.set_mode(WINDOW_SIZES[self.current_interface])
                pygame.display.set_caption(f"PlanetGame - {self.current_interface}")
                self.previous_interface = self.current_interface

            if self.current_interface == "menu":
                self.menu_controller.render(screen)
                self.current_interface = self.menu_controller.handle_events()
            elif self.current_interface == "param":
                self.options_controller.render(screen)
                self.current_interface = self.options_controller.handle_events()
            elif self.current_interface == "game":
                self.current_interface = self.game_controller.run(screen)

            if self.current_interface != "quit":
                pygame.display.flip()

        pygame.quit()
