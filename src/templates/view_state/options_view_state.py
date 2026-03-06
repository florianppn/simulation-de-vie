# -*- coding: utf-8 -*-
"""État de vue des options - DTO pour Controller → View."""

from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class OptionsViewState:
    """Données pour l'affichage de l'écran options."""

    movable_elements: List[str]
    entity_params: List[str]
    human_params: List[str]
    animals: Dict[str, Dict[str, Any]]
    human_cp: int
    human_name: str
    selected_entity_index: int
