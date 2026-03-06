# -*- coding: utf-8 -*-
"""Configuration pytest - Ajoute src/ au path pour les imports."""

import sys
import os

# Permettre l'import des modules de l'application (model, controller, templates)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
