# -*- coding: utf-8 -*-
"""Contrôleur du jeu."""

import pygame

from model.config import WINDOW_SIZES, FPS
from model.game_model import GameModel
from view.game_view import GameView


class GameController:
    """Contrôleur du jeu : événements, mise à jour et rendu."""

    def __init__(self):
        screen_size = WINDOW_SIZES["game"]
        self.model = GameModel(screen_size)
        self.view = GameView(screen_size)
        self.clock = pygame.time.Clock()
        self.initialized = False

    def _initialize(self, screen):
        """Initialise le jeu au premier lancement."""
        if not self.initialized:
            print("Start Initialisation")
            self.model.entity_add()
            self.initialized = True

    def handle_events(self):
        """Gère les événements et retourne la prochaine interface."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.model.select_entity(event.pos)
        return "game"

    def update(self):
        """Met à jour la logique du jeu."""
        self.model.update()

    def render(self, screen):
        """Affiche le jeu."""
        self.view.render(screen, self.model)

    def run(self, screen):
        """Boucle principale du jeu. Retourne la prochaine interface ("game" ou "quit")."""
        # Traiter les événements en premier pour éviter les plantages à la fermeture
        next_interface = self.handle_events()
        if next_interface == "quit":
            return "quit"

        self._initialize(screen)
        self.update()
        self.render(screen)
        pygame.display.flip()
        self.clock.tick(FPS)
        return "game"
