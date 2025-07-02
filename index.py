import numpy as np
import tkinter as tk
from tkinter import messagebox


map = np.full((3, 3), ' . ')     # grille 3×3

def check_win():
    for i in range(len(map)):
        if map[i][0] == map[i][1] == map[i][2] != ' . ':
            return True
    for j in range(len(map)):
        if map[0][j] == map[1][j] == map[2][j] != ' . ':
            return True
    if map[0][0] == map[1][1] == map[2][2] != ' . ':
        return True
    if map[0][2] == map[1][1] == map[2][0] != ' . ':
        return True
    return False

def check_draw():
    return not np.any(map == ' . ')


class MorpionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Morpion – Tic Tac Toe")

        self.player = 'Joueur 1'                          # commence par Joueur 1 (X)
        self.symbols = {'Joueur 1': ' X ', 'Joueur 2': ' O '}  # mapping symbole/­joueur

        # Label d’information
        self.info = tk.Label(root, text="Tour du joueur : X",
                             font=('Arial', 14))
        self.info.grid(row=0, column=0, columnspan=3, pady=10)

        # Grille de boutons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_grid()

        # Bouton « Rejouer »
        self.reset_btn = tk.Button(root, text="🔁 Rejouer",
                                   font=('Arial', 12), command=self.reset)
        self.reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

    def create_grid(self):
        """Crée les 9 boutons de la grille."""
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root,
                                text=' . ',
                                font=('Arial', 20),
                                width=5, height=2,
                                command=lambda r=i, c=j: self.play(r, c))
                btn.grid(row=i+1, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

    def play(self, row, col):
        """Action lorsqu’on clique sur une case."""
        global map
        if map[row][col] == ' . ':              
            # Met à jour la grille et le bouton
            map[row][col] = self.symbols[self.player]
            self.buttons[row][col].config(text=self.symbols[self.player],
                                          state='disabled')

            # Vérifie victoire / nul
            if check_win():
                messagebox.showinfo("Victoire", f"🎉 {self.player} a gagné !")
                self.disable_all()
                return
            if check_draw():
                messagebox.showinfo("Égalité", "🤝 Match nul !")
                self.disable_all()
                return

            # Passe au joueur suivant
            self.player = 'Joueur 2' if self.player == 'Joueur 1' else 'Joueur 1'
            prochain_symbole = 'X' if self.player == 'Joueur 1' else 'O'
            self.info.config(text=f"Tour du joueur : {prochain_symbole}")

    def disable_all(self):
        """Désactive tous les boutons de la grille."""
        for row in self.buttons:
            for btn in row:
                btn.config(state='disabled')

    def reset(self):
        """Réinitialise la partie (bouton Rejouer)."""
        global map
        map = np.full((3, 3), ' . ')         # nouvelle grille vide
        self.player = 'Joueur 1'
        self.info.config(text="Tour du joueur : X")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' . ', state='normal')


if __name__ == '__main__':
    root = tk.Tk()
    MorpionGUI(root)        
    root.mainloop()
