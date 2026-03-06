# -*- coding: utf-8 -*-
"""Vue du jeu - Affichage de la carte, entités et statistiques."""

import pygame

from model.config import PROPS_ELEMENT, animals


class GameView:
    """Vue responsable de l'affichage du jeu."""

    def __init__(self, screen_size):
        self.screen_width, self.screen_height = screen_size
        self.rect_width, self.rect_height = 175, 250
        self.rect_x = self.screen_width - self.rect_width
        self.rect_y = 0
        self.rect_width_G, self.rect_height_G = 175, 216

        self.sprite_sheet_stats = pygame.image.load("images/stats_icons/Stats.png").convert_alpha()
        self.sprite_sheet_stats = pygame.transform.scale(self.sprite_sheet_stats, (self.rect_width, self.rect_height))

        self.sprite_sheet_stats_G = pygame.image.load("images/stats_icons/global.png").convert_alpha()
        self.sprite_sheet_stats_G = pygame.transform.scale(self.sprite_sheet_stats_G, (self.rect_width_G, self.rect_height_G))

    def render(self, screen, model):
        """Affiche le jeu complet."""
        model.entity_group.draw(screen)
        self._draw_stats(screen, model)
        self._draw_global_stats(screen, model)

    def _draw_stats(self, screen, model):
        """Affiche les statistiques de l'entité sélectionnée."""
        if model.stats_entity is None or model.stats_entity.name in ["Mort", "Damage"]:
            return

        screen.blit(self.sprite_sheet_stats, (self.rect_x, self.rect_y))

        if model.stats_entity.name in PROPS_ELEMENT:
            entity_name = pygame.font.Font(None, 25).render(str(model.stats_entity.name), True, (255, 255, 255))
            screen.blit(entity_name, (866, 25))
            valeur_life = 44 - ((model.stats_entity.entity.get_bar_value()[1] - model.stats_entity.entity.get_bar_value()[0]) / model.stats_entity.entity.get_bar_value()[1] * 44)
            pygame.draw.rect(screen, "#FF0000", (837, 88, valeur_life, 2))
        else:
            valeur_life = 44 - ((model.stats_entity.entity.get_life_max() - model.stats_entity.entity.get_bar_life()[0]) / model.stats_entity.entity.get_life_max() * 44)
            valeur_food = 44 - ((model.stats_entity.entity.get_food()[1] - model.stats_entity.entity.get_food()[0]) / model.stats_entity.entity.get_food()[1] * 44)
            valeur_drink = 44 - ((model.stats_entity.entity.get_drink()[1] - model.stats_entity.entity.get_drink()[0]) / model.stats_entity.entity.get_drink()[1] * 44)

            pygame.draw.rect(screen, "#FF0000", (837, 88, valeur_life, 2))
            pygame.draw.rect(screen, "#F07800", (837, 109, valeur_food, 2))
            pygame.draw.rect(screen, "#0088E6", (837, 131, valeur_drink, 2))

            entity_name = pygame.font.Font(None, 25).render(str(model.stats_entity.name), True, (255, 255, 255))
            screen.blit(entity_name, (866, 25))
            entity_parent = pygame.font.Font(None, 25).render(str([p.entity.get_id() if p is not None else 0 for p in model.stats_entity.entity.get_parents()]), True, (255, 255, 255))
            screen.blit(entity_parent, (891, 53))
            entity_age = pygame.font.Font(None, 25).render(str(model.stats_entity.entity.get_time_life()), True, (255, 255, 255))
            screen.blit(entity_age, (832, 147))
            entity_virus = pygame.font.Font(None, 25).render(str(model.stats_entity.entity.get_virus()), True, (255, 255, 255))
            screen.blit(entity_virus, (835, 173))
            entity_genre = pygame.font.Font(None, 25).render(str(model.stats_entity.entity.get_gender()), True, (255, 255, 255))
            screen.blit(entity_genre, (833, 201))
            entity_damage = pygame.font.Font(None, 25).render(str(model.stats_entity.entity.get_damage()), True, (255, 255, 255))
            screen.blit(entity_damage, (905, 147))
            entity_speed = pygame.font.Font(None, 25).render(str(animals[model.stats_entity.name]['speed']), True, (255, 255, 255))
            screen.blit(entity_speed, (903, 171))
            entity_weight = pygame.font.Font(None, 25).render(str(animals[model.stats_entity.name]['weight']), True, (255, 255, 255))
            screen.blit(entity_weight, (902, 200))

        screen.blit(model.stats_entity.image, (815, 18))

    def _draw_global_stats(self, screen, model):
        """Affiche les statistiques globales du monde."""
        screen.blit(self.sprite_sheet_stats_G, (795, 250))
        entity_nb = pygame.font.Font(None, 18).render(f"Entity = {model.get_current_animals_count()}", True, (255, 255, 255))
        screen.blit(entity_nb, (819, 295))
        props_nb = pygame.font.Font(None, 18).render(f"Props = {model.entity_count(PROPS_ELEMENT)}", True, (255, 255, 255))
        screen.blit(props_nb, (819, 310))
