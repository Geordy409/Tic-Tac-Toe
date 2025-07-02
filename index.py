import numpy as np


map = np.full((3, 3), ' . ')

player = 'Joueur 1'


def draw():
    for i in range(3):
        for j in range(3):
            print(map[i][j], end='')
        print()

def check_win():
    for i in range(len(map)):
        if map[i][0] == map[i][1] == map[i][2] !=' . ' :
            return True
    for j in range(len(map)):
        if map[0][j] == map[1][j] == map[2][j] !=' . ' :
            return True
    if map[0][0] == map[1][1] == map[2][2] !=' . ' :
        return True
    elif map[0][2] == map[1][1] == map[2][0] !=' . ':
        return True
        
    return False

def check_draw():
    for i in range(3):
        for j in range(3):
            if map[i][j] == ' . ':
                return False
    return True
    

while True:
    try:
        choice = int(input(f'{player} [1-9] ? > '))
        if choice < 1 or choice > 9:
            raise ValueError

        row = (choice - 1) // 3
        column = (choice - 1) % 3

        if map[row][column] == ' . ':
            map[row][column] = ' X ' if player == 'Joueur 1' else ' O '
            draw()
            if check_win():
                print(f'{player} a gagné !')
                break
            if check_draw():
                print('Egalité !')
                break
            player = 'Joueur 2' if player == 'Joueur 1' else 'Joueur 1'
        else:
            print("❌ Case déjà occupée, choisissez une autre.")
    except ValueError:
        print('⛔ Choix non valide, veuillez entrer un nombre entre 1 et 9.')
