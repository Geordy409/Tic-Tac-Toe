# 🎮 Jeu du Morpion en Python

Un petit projet en Python pour jouer au **Morpion (Tic-Tac-Toe)** en mode console à deux joueurs.

## 🧠 Objectif

Deux joueurs s'affrontent à tour de rôle pour placer leur symbole (`X` pour Joueur 1, `O` pour Joueur 2) sur une grille 3x3. Le premier à aligner trois symboles horizontalement, verticalement ou en diagonale gagne la partie.

---

## ⚙️ Fonctionnalités

- Grille 3x3 initialisée avec des cases vides.
- Tour par tour entre Joueur 1 et Joueur 2.
- Détection automatique de :
  - ✅ Victoire
  - 🤝 Match nul (égalité)
- 🔒 Gestion des erreurs :
  - Empêche les joueurs de saisir une case déjà occupée
  - Empêche les entrées invalides (hors de 1 à 9)

---

## ▶️ Lancer le jeu

### Prérequis

- Python 3.x
- Bibliothèque `numpy`

```bash
pip install numpy
```
