# Quelques extraits du cours : "Le typage statique signifie que le type d’une variable est déterminé au moment de la compilation, avant l’exécution du programme. Cela permet de détecter les erreurs de type avant que le code ne soit exécuté, ce qui peut améliorer la sécurité et la fiabilité du code. Les langages à typage statique incluent Java, C, Rust…"

# "A contrario, le typage dynamique détermine le type d’une variable au moment de l’exécution. Cela offre plus de flexibilité, mais peut également entraîner des erreurs de type qui ne sont détectées qu’à l’exécution. Les langages à typage dynamique incluent Python, Ruby, JavaScript…"

# Qualité du code

Ce dépôt contient mon travail sur le chapitre « Qualité du code » de Python 2 à ESIEE Paris.

J’ai étudié les annotations de type, les noms explicites, les docstrings, la responsabilité unique des fonctions, la gestion des exceptions et les tests.

J’ai ensuite repris mon Test technique sur les populations pour compléter les statistiques départementales et ajouter les annotations nécessaires à une validation stricte avec mypy.

## Contenu

- `règles.py` : exemples comparant différentes façons d’écrire le code.
- `main.py` : premiers exemples de fonctions typées.
- `typing_exemples.py` : générateur de Fibonacci annoté et accompagné de doctests.
- `test_technique.py` : traitement des populations, avec annotations et doctests.
- `population.csv` : données utilisées par le Test technique.
- `pyproject.toml` et `uv.lock` : configuration et dépendances du projet.

## Installation

Après avoir cloné le dépôt, installer les dépendances :

    uv sync

## Exécution des exemples

    uv run python main.py
    uv run python typing_exemples.py

## Vérification des types

    uv run mypy --strict typing_exemples.py
    uv run mypy --strict test_technique.py

Les deux fichiers passent la vérification stricte sans erreur.

Le fichier `règles.py` conserve volontairement des exemples non annotés pour les comparer aux versions améliorées. Il n’est pas inclus dans cette validation stricte.

## Doctests

    uv run python -m doctest -v typing_exemples.py
    uv run python -m doctest -v test_technique.py

Résultats obtenus :

- Générateur de Fibonacci : 3 doctests réussis.
- Test technique : 96 doctests réussis.

Les données de population sont lues avec leurs codes sous forme de chaînes pour conserver les zéros initiaux.

Pour les statistiques départementales, la ligne la plus récente de chaque couple code–nom de commune est conservée avant le comptage et l’addition des populations. Ce regroupement reproduit les résultats attendus par les doctests du cours.

## Ce que j’ai retenu

Les annotations indiquent les types attendus, mais Python ne les impose pas automatiquement à l’exécution.

Mypy vérifie la cohérence des types sans exécuter le programme. Les doctests vérifient les exemples et les résultats : ces deux contrôles sont complémentaires.

## Sources et accompagnement

Les exercices, exemples et résultats attendus proviennent du cours de Python d’ESIEE Paris.

J’ai utilisé ChatGPT pour obtenir des explications, être accompagnée dans les corrections et préparer la documentation. Les vérifications ont été exécutées localement.

## Autrice

Célya Bakala-Yame — bakalayc

