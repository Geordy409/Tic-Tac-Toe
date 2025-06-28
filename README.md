# Jeu du Pendule (Jeu du Pendu)

## Description

Ce projet est une implémentation simple du jeu du pendule (ou jeu du pendu) en Python.  
Le joueur doit deviner un mot secret lettre par lettre.  
Le joueur dispose d'un nombre limité de vies (9) avant de perdre la partie.

## Fonctionnement

- Le jeu choisit un mot au hasard parmi une liste prédéfinie.
- Le joueur entre une lettre à chaque tour.
- Si la lettre est dans le mot, elle est dévoilée dans la position correspondante.
- Sinon, le joueur perd une vie.
- Le jeu continue jusqu'à ce que le mot soit entièrement découvert ou que le joueur n'ait plus de vies.

## Comment jouer

1. Lancez le script Python.
2. Entrez une lettre à chaque tour lorsque vous êtes invité.
3. Essayez de deviner le mot secret avant d'épuiser toutes vos vies.

## Exemple d'exécution

**\_\_\_\_** | vies : 9
Entrez une lettre : a
a**\_\_\_** | vies : 9
Entrez une lettre : e
a**\_e**e | vies : 9
Entrez une lettre : x
a**\_e**e | vies : 8

## Prérequis

- Python 3.x

## Lancer le jeu

```bash
python ton_script.py
```
