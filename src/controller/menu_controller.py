# -*- coding: utf-8 -*-
"""Contrôleur du menu principal."""

import pygame

from model.config import WINDOW_SIZES, animals, props
from model.elements import entity_factory
from templates.view.menu_view import MenuView


class MenuController:
    """Contrôleur du menu principal : gestion des clics et création des entités."""

    def __init__(self, game_model):
        self.model = game_model
        from model.config import WINDOW_SIZES
        self.view = MenuView(WINDOW_SIZES["menu"])

    def handle_events(self):
        """Gère les événements et retourne la prochaine interface."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._is_click_start(event.pos):
                    self._create_entity()
                    return "game"
                elif self._is_click_option(event.pos):
                    return "param"
                elif self._is_click_quit(event.pos):
                    return "quit"
            elif event.type == pygame.QUIT:
                return "quit"
        return "menu"

    def _is_click_start(self, pos):
        return (self.view.x_bouton_start <= pos[0] <= self.view.x_bouton_start + self.view.largeur_bouton and
                self.view.y_bouton_start <= pos[1] <= self.view.y_bouton_start + self.view.hauteur_bouton)

    def _is_click_option(self, pos):
        return (self.view.x_bouton_option <= pos[0] <= self.view.x_bouton_option + self.view.largeur_bouton and
                self.view.y_bouton_option <= pos[1] <= self.view.y_bouton_option + self.view.hauteur_bouton)

    def _is_click_quit(self, pos):
        return (self.view.x_bouton_quit <= pos[0] <= self.view.x_bouton_quit + self.view.largeur_bouton and
                self.view.y_bouton_quit <= pos[1] <= self.view.y_bouton_quit + self.view.hauteur_bouton)

    def _create_entity(self):
        """Initialise le monde au lancement."""
        for animal_type, count in animals.items():
            for _ in range(count["count"]):
                animal = entity_factory.create_animal(animal_type)
                self.model.place_animals([animal])

        for props_type, count in props.items():
            for _ in range(count["count"]):
                prop = entity_factory.create_resource(props_type)
                self.model.place_resources([prop])

    def render(self, screen):
        """Affiche le menu."""
        self.view.render(screen)
