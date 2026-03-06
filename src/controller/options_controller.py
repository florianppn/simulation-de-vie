# -*- coding: utf-8 -*-
"""Contrôleur des options/paramètres - Orchestration Model/View (MVC)."""

import pygame

import model.config as config
from model.elements import entity_factory
from templates.view.options_view import OptionsView
from templates.view_state import OptionsViewState


class OptionsController:
    """Contrôleur des paramètres : modification des stats et lancement du jeu."""

    def __init__(self, game_model):
        self.model = game_model
        self.view = OptionsView(
            config.MOVABLE_ELEMENT,
            config.ENTITY_PARAM,
            config.HUMAN_PARAM,
        )
        self.selected_entity = 1

    def handle_events(self):
        """Gère les événements et retourne la prochaine interface."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click(event.pos)
                if self._is_click_launch(event.pos):
                    self._create_entity()
                    return "game"
        return "param"

    def _handle_click(self, pos):
        """Traite les clics sur les boutons."""
        for i in range(len(config.MOVABLE_ELEMENT)):
            if config.MOVABLE_ELEMENT[i] != "Humain" and self.view.liste_button_animal[i-1].x_button <= pos[0] <= self.view.liste_button_animal[i-1].x_button + self.view.liste_button_animal[i-1].largeur_bouton and self.view.liste_button_animal[i-1].y_button <= pos[1] <= self.view.liste_button_animal[i-1].y_button + self.view.liste_button_animal[i-1].hauteur_bouton:
                self.selected_entity = i

        for i in range(len(config.ENTITY_PARAM)):
            if self.view.liste_button_param_1[i].x_button <= pos[0] <= self.view.liste_button_param_1[i].x_button + self.view.liste_button_param_1[i].largeur_bouton and self.view.liste_button_param_1[i].y_button <= pos[1] <= self.view.liste_button_param_1[i].y_button + self.view.liste_button_param_1[i].hauteur_bouton:
                config.animals[config.MOVABLE_ELEMENT[self.selected_entity]][self.view.liste_button_param_1[i].name] += 1
            if self.view.liste_button_param_10[i].x_button <= pos[0] <= self.view.liste_button_param_10[i].x_button + self.view.liste_button_param_10[i].largeur_bouton and self.view.liste_button_param_10[i].y_button <= pos[1] <= self.view.liste_button_param_10[i].y_button + self.view.liste_button_param_10[i].hauteur_bouton:
                config.animals[config.MOVABLE_ELEMENT[self.selected_entity]][self.view.liste_button_param_10[i].name] += 10
            if self.view.liste_button_param_n10[i].x_button <= pos[0] <= self.view.liste_button_param_n10[i].x_button + self.view.liste_button_param_n10[i].largeur_bouton and self.view.liste_button_param_n10[i].y_button <= pos[1] <= self.view.liste_button_param_n10[i].y_button + self.view.liste_button_param_n10[i].hauteur_bouton:
                config.animals[config.MOVABLE_ELEMENT[self.selected_entity]][self.view.liste_button_param_n10[i].name] -= 10
            if self.view.liste_button_param_0[i].x_button <= pos[0] <= self.view.liste_button_param_0[i].x_button + self.view.liste_button_param_0[i].largeur_bouton and self.view.liste_button_param_0[i].y_button <= pos[1] <= self.view.liste_button_param_0[i].y_button + self.view.liste_button_param_0[i].hauteur_bouton:
                config.animals[config.MOVABLE_ELEMENT[self.selected_entity]][self.view.liste_button_param_0[i].name] = 0

        for i in range(len(config.HUMAN_PARAM)):
            if self.view.liste_button_param_humain_1[i].x_button <= pos[0] <= self.view.liste_button_param_humain_1[i].x_button + self.view.liste_button_param_humain_1[i].largeur_bouton and self.view.liste_button_param_humain_1[i].y_button <= pos[1] <= self.view.liste_button_param_humain_1[i].y_button + self.view.liste_button_param_humain_1[i].hauteur_bouton:
                config.animals["Humain"][self.view.liste_button_param_humain_1[i].name] += 1
            if self.view.liste_button_param_humain_10[i].x_button <= pos[0] <= self.view.liste_button_param_humain_10[i].x_button + self.view.liste_button_param_humain_10[i].largeur_bouton and self.view.liste_button_param_humain_10[i].y_button <= pos[1] <= self.view.liste_button_param_humain_10[i].y_button + self.view.liste_button_param_humain_10[i].hauteur_bouton:
                config.animals["Humain"][self.view.liste_button_param_humain_10[i].name] += 10
            if self.view.liste_button_param_humain_n10[i].x_button <= pos[0] <= self.view.liste_button_param_humain_n10[i].x_button + self.view.liste_button_param_humain_n10[i].largeur_bouton and self.view.liste_button_param_humain_n10[i].y_button <= pos[1] <= self.view.liste_button_param_humain_n10[i].y_button + self.view.liste_button_param_humain_n10[i].hauteur_bouton:
                config.animals["Humain"][self.view.liste_button_param_humain_n10[i].name] -= 10
            if self.view.liste_button_param_humain_0[i].x_button <= pos[0] <= self.view.liste_button_param_humain_0[i].x_button + self.view.liste_button_param_humain_0[i].largeur_bouton and self.view.liste_button_param_humain_0[i].y_button <= pos[1] <= self.view.liste_button_param_humain_0[i].y_button + self.view.liste_button_param_humain_0[i].hauteur_bouton:
                config.animals["Humain"][self.view.liste_button_param_humain_0[i].name] = 0

        if 674 <= pos[0] <= 724 and 115 <= pos[1] <= 165:
            config.HUMAIN_CP = (config.HUMAIN_CP + 1) % 78
        elif 445 <= pos[0] <= 495 and 115 <= pos[1] <= 165:
            config.HUMAIN_CP = (config.HUMAIN_CP - 1) % 78

    def _is_click_launch(self, pos):
        return 742 <= pos[0] <= 895 and 823 <= pos[1] <= 895

    def _create_entity(self):
        """Initialise le monde au lancement du jeu."""
        for animal_type, count in config.animals.items():
            for _ in range(count["count"]):
                animal = entity_factory.create_animal(animal_type)
                self.model.place_animals([animal])

        for props_type, count in config.props.items():
            for _ in range(count["count"]):
                prop = entity_factory.create_resource(props_type)
                self.model.place_resources([prop])

    def render(self, screen):
        """Affiche les options. Le contrôleur récupère les données et les passe à la vue."""
        view_state = OptionsViewState(
            movable_elements=config.MOVABLE_ELEMENT,
            entity_params=config.ENTITY_PARAM,
            human_params=config.HUMAN_PARAM,
            animals=config.animals,
            human_cp=config.HUMAIN_CP,
            human_name=config.HUMAIN_NAME[config.HUMAIN_CP],
            selected_entity_index=self.selected_entity,
        )
        self.view.render(screen, view_state)
