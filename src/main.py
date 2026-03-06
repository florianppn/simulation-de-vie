# -*- coding: utf-8 -*-
"""
PlanetGame - Simulation de vie
Architecture MVC
"""

from random import seed

from controller.main_controller import MainController


def main():
    """Point d'entrée de l'application PlanetGame."""
    seed(1000)
    controller = MainController()
    controller.run()


if __name__ == "__main__":
    main()
