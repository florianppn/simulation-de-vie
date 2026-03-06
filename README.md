# PlanetGame

Simulation de vie en Python avec Pygame. Architecture **MVC** (Model-View-Controller).

## Structure du projet

```
simulation-de-vie/
├── main.py              # Point d'entrée
├── model/               # Modèle - Données et logique métier
│   ├── config.py        # Configuration (animaux, props, constantes)
│   ├── elements.py      # Element, Animal, Resource (entités du jeu)
│   ├── grid.py          # Grille 2D
│   ├── planet.py        # PlanetAlpha (monde)
│   └── game_model.py    # Logique du jeu (collisions, reproduction, virus)
├── view/                # Vue - Affichage
│   ├── animation.py     # Sprites animés
│   ├── entity_sprite.py # Représentation visuelle des entités
│   ├── game_view.py     # Affichage du jeu
│   ├── menu_view.py     # Affichage du menu
│   └── options_view.py  # Affichage des paramètres
├── controller/          # Contrôleur - Gestion des entrées
│   ├── main_controller.py    # Orchestration des écrans
│   ├── game_controller.py   # Contrôle du jeu
│   ├── menu_controller.py   # Contrôle du menu
│   └── options_controller.py # Contrôle des options
└── assets/              # Ressources graphiques
    ├── animaux/         # Sprites des entités (animaux, ressources, stats)
    ├── menu/            # Images du menu (fond, boutons)
    ├── font/            # Polices de caractères
    └── map/             # Carte Tiled (.tmx, .tsx)
```

## Lancer le jeu

### Créer l'environnement virtuel

```bash
python3 -m venv env-py
source env-py/bin/activate  # Linux/macOS
# ou : env-py\Scripts\activate  # Windows

pip install pygame pytmx pyscroll
```

### Lancer le jeu

```bash
source env-py/bin/activate
python main.py
```

## Dépendances

- pygame
- pytmx
- pyscroll
