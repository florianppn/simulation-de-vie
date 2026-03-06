# PlanetGame

[![Tests](https://github.com/florianppn/simulation-de-vie/workflows/Tests/badge.svg)](https://github.com/florianppn/simulation-de-vie/actions/workflows/tests.yml)

Simulation de vie en Python avec Pygame. Architecture **MVC** (Model-View-Controller).

## Structure du projet

```
simulation-de-vie/
├── main.py              # Lanceur (exécute src.main)
├── src/                 # Code de l'application
│   ├── main.py          # Point d'entrée
│   ├── model/           # Modèle - Données et logique métier
│   ├── templates/       # Vues et états d'affichage
│   └── controller/      # Contrôleur - Gestion des entrées
├── test/                # Tests unitaires et d'intégration
│   ├── conftest.py      # Config pytest (path src/)
│   ├── unit/            # Tests unitaires (Element, Grid, factory, Animal)
│   └── integration/     # Tests d'intégration (Planet + factory)
├── pyproject.toml       # Config Ruff (lint)
├── .github/workflows/   # CI/CD (tests, Ruff, pip-audit sur push/PR)
└── assets/              # Ressources graphiques
    ├── animaux/         # Sprites des entités
    ├── Animaux/         # Sprites additionnels
    ├── menu/            # Images du menu
    ├── font/            # Polices
    └── map/              # Carte Tiled (.tmx, .tsx)
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

## Tests

### Installer les dépendances de test

```bash
pip install pytest
```

### Lancer les tests

```bash
# Depuis la racine du projet
pytest test/ -v

# Uniquement les tests unitaires
pytest test/unit/ -v

# Uniquement les tests d'intégration
pytest test/integration/ -v
```

## CI/CD

À chaque push ou pull request sur `main`/`master`, GitHub Actions exécute :

- **Lint** : Ruff (vérification du code + formatage) et pip-audit (sécurité des dépendances)
- **Tests** : pytest sur Ubuntu, Windows et macOS

Le badge en haut du README indique le statut du dernier run.

## Dépendances

- **Jeu** : pygame, pytmx, pyscroll
- **Tests** : pytest
- **Lint / format** : ruff
