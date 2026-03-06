# -*- coding: utf-8 -*-
"""Vue du jeu - Affichage de la carte, entités et statistiques.

La vue ne reçoit que des données (GameViewState), jamais le modèle.
"""

import pygame

from templates.view_state import GameViewState, StatsPanelData


def _barre(width: int, current: float, maximum: float) -> int:
    """Calcule la largeur de la barre (0 à width) selon current/maximum."""
    if maximum <= 0:
        return width
    return int(width * (current / maximum))


class GameView:
    """Vue responsable de l'affichage du jeu.

    Affiche la carte, les entités, les statistiques de l'entité
    sélectionnée et les statistiques globales du monde.
    Reçoit uniquement des données du contrôleur (MVC).
    """

    def __init__(self, screen_size):
        self.screen_width, self.screen_height = screen_size
        self.rect_width, self.rect_height = 175, 250
        self.rect_x = self.screen_width - self.rect_width
        self.rect_y = 0
        self.rect_width_G, self.rect_height_G = 175, 216

        self.sprite_sheet_stats = pygame.image.load("assets/animaux/stats_icons/Stats.png").convert_alpha()
        self.sprite_sheet_stats = pygame.transform.scale(self.sprite_sheet_stats, (self.rect_width, self.rect_height))

        self.sprite_sheet_stats_G = pygame.image.load("assets/animaux/stats_icons/global.png").convert_alpha()
        self.sprite_sheet_stats_G = pygame.transform.scale(self.sprite_sheet_stats_G, (self.rect_width_G, self.rect_height_G))

    def render(self, screen, view_state: GameViewState):
        """Affiche le jeu à partir des données fournies par le contrôleur."""
        view_state.entity_group.draw(screen)
        self._draw_stats(screen, view_state)
        self._draw_global_stats(screen, view_state)

    def _draw_stats(self, screen, view_state: GameViewState):
        """Affiche les statistiques de l'entité sélectionnée."""
        if view_state.stats_panel is None:
            return

        panel = view_state.stats_panel
        font = pygame.font.Font(None, 25)
        screen.blit(self.sprite_sheet_stats, (self.rect_x, self.rect_y))

        if panel.is_prop:
            entity_name = font.render(panel.entity_name, True, (255, 255, 255))
            screen.blit(entity_name, (866, 25))
            cur, max_val = panel.bar_value
            valeur_life = _barre(44, cur, max_val)
            pygame.draw.rect(screen, "#FF0000", (837, 88, valeur_life, 2))
        else:
            cur_life, max_life = panel.bar_life
            cur_food, max_food = panel.bar_food
            cur_drink, max_drink = panel.bar_drink
            valeur_life = _barre(44, cur_life, max_life)
            valeur_food = _barre(44, cur_food, max_food)
            valeur_drink = _barre(44, cur_drink, max_drink)

            pygame.draw.rect(screen, "#FF0000", (837, 88, valeur_life, 2))
            pygame.draw.rect(screen, "#F07800", (837, 109, valeur_food, 2))
            pygame.draw.rect(screen, "#0088E6", (837, 131, valeur_drink, 2))

            entity_name = font.render(panel.entity_name, True, (255, 255, 255))
            screen.blit(entity_name, (866, 25))
            screen.blit(font.render(str(panel.parents), True, (255, 255, 255)), (891, 53))
            screen.blit(font.render(str(panel.age), True, (255, 255, 255)), (832, 147))
            screen.blit(font.render(str(panel.virus), True, (255, 255, 255)), (835, 173))
            screen.blit(font.render(str(panel.gender), True, (255, 255, 255)), (833, 201))
            screen.blit(font.render(str(panel.damage), True, (255, 255, 255)), (905, 147))
            screen.blit(font.render(str(panel.speed), True, (255, 255, 255)), (903, 171))
            screen.blit(font.render(str(panel.weight), True, (255, 255, 255)), (902, 200))

        screen.blit(panel.entity_image, (815, 18))

    def _draw_global_stats(self, screen, view_state: GameViewState):
        """Affiche les statistiques globales du monde (temps réel)."""
        screen.blit(self.sprite_sheet_stats_G, (795, 250))
        font = pygame.font.Font(None, 18)
        entity_nb = font.render(f"Entity = {view_state.entities_count}", True, (255, 255, 255))
        props_nb = font.render(f"Props = {view_state.props_count}", True, (255, 255, 255))
        screen.blit(entity_nb, (819, 295))
        screen.blit(props_nb, (819, 310))
