# -*- coding: utf-8 -*-
"""État de vue du jeu - DTO pour la communication Controller → View.

La vue ne reçoit que ces données, jamais le modèle directement.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Any


@dataclass
class StatsPanelData:
    """Données du panneau de stats d'une entité sélectionnée."""

    entity_image: Any  # pygame.Surface
    entity_name: str
    is_prop: bool
    # Props
    bar_value: Optional[tuple] = None  # (current, max)
    # Animaux
    bar_life: Optional[tuple] = None
    bar_food: Optional[tuple] = None
    bar_drink: Optional[tuple] = None
    age: int = 0
    virus: bool = False
    gender: int = 0  # 0 ou 1
    damage: int = 0
    speed: int = 0
    weight: int = 0
    move_size: int = 0
    prey: List[str] = field(default_factory=list)
    parents: List[int] = field(default_factory=list)


@dataclass
class GameViewState:
    """État complet pour le rendu du jeu. Passé par le contrôleur à la vue."""

    entity_group: Any  # pygame.sprite.Group pour le dessin
    stats_panel: Optional[StatsPanelData] = None
    entities_count: int = 0
    props_count: int = 0
