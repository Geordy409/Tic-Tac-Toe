# 🎮 Jeu du Morpion en Python (avec interface graphique Tkinter)

Un projet en Python pour jouer au **Morpion (Tic-Tac-Toe)** en mode graphique à deux joueurs, utilisant une interface simple et intuitive réalisée avec Tkinter.

---

## 🧠 Objectif

Deux joueurs s'affrontent à tour de rôle pour placer leur symbole (`X` pour Joueur 1, `O` pour Joueur 2) sur une grille 3×3. Le premier à aligner trois symboles horizontalement, verticalement ou en diagonale remporte la partie.

---

## ⚙️ Fonctionnalités principales

- Grille 3×3 interactive avec boutons pour chaque case
- Tour par tour entre Joueur 1 (`X`) et Joueur 2 (`O`)
- Détection automatique de :
  - ✅ Victoire (alignement de trois symboles)
  - 🤝 Match nul (grille remplie sans vainqueur)
- 🔒 Gestion des erreurs :
  - Empêche de jouer sur une case déjà occupée
- Messages popup pour annoncer le résultat (victoire ou égalité)
- Bouton **🔁 Rejouer** pour recommencer une partie proprement

---

## ▶️ Lancer le jeu

### Prérequis

- Python 3.x (pour l'exécution du script)
- Bibliothèque `numpy`
- Tkinter (inclus par défaut sous Windows et macOS, sinon installer le paquet `python3-tk` sous Linux)
- python index.py pour lancer le jeu

### Installer numpy

```bash
pip install numpy
```
