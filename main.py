# -*- coding: utf-8 -*-
"""Lanceur - Exécute l'application depuis src/."""

import sys
import os

if __name__ == "__main__":
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
    from main import main
    main()
