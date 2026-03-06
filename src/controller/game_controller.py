# -*- coding: utf-8 -*-
"""Contrôleur du jeu - Orchestration Model/View (MVC)."""

import pygame

from model.config import WINDOW_SIZES, FPS
from model.game_model import GameModel
from templates.view.game_view import GameView
from templates.view_state import GameViewState, StatsPanelData


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
        """Affiche le jeu. Le contrôleur récupère les données du modèle et les passe à la vue."""
        data = self.model.get_view_data()
        stats_panel = None
        if data["stats"]:
            s = data["stats"]
            stats_panel = StatsPanelData(
                entity_image=s["entity_image"],
                entity_name=s["entity_name"],
                is_prop=s["is_prop"],
                bar_value=s.get("bar_value"),
                bar_life=s.get("bar_life"),
                bar_food=s.get("bar_food"),
                bar_drink=s.get("bar_drink"),
                age=s.get("age", 0),
                virus=s.get("virus", False),
                gender=s.get("gender", 0),
                damage=s.get("damage", 0),
                speed=s.get("speed", 0),
                weight=s.get("weight", 0),
                move_size=s.get("move_size", 0),
                prey=s.get("prey", []),
                parents=s.get("parents", []),
            )
        view_state = GameViewState(
            entity_group=data["entity_group"],
            stats_panel=stats_panel,
            entities_count=data["entities_count"],
            props_count=data["props_count"],
        )
        self.view.render(screen, view_state)

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
