# ITA Softserve, DevOps - Oleh Smahliuk

import numpy as np
from random import randint


def check_ships(arr):  # fills the space around the ship
    for i in range(10):
        for j in range(10):
            if arr[i, j] == "S":
                if i + 1 <= 9 and arr[i + 1, j] != "S":
                    arr[i + 1, j] = "x"
                    if j + 1 <= 9:
                        arr[i + 1, j + 1] = "x"
                    if j - 1 >= 0:
                        arr[i + 1, j - 1] = "x"
                if arr[i - 1, j] != "S" and i > 0:
                    arr[i - 1, j] = "x"
                    if j - 1 >= 0:
                        arr[i - 1, j - 1] = "x"
                    if j + 1 <= 9:
                        arr[i - 1, j + 1] = "x"
                if j + 1 <= 9 and arr[i, j + 1] != "S":
                    arr[i, j + 1] = "x"
                    if i + 1 <= 9:
                        arr[i + 1, j + 1] = "x"
                    if i - 1 >= 0:
                        arr[i - 1, j + 1] = "x"
                if arr[i, j - 1] != "S" and j > 0:
                    arr[i, j - 1] = "x"
                    if i - 1 >= 0:
                        arr[i - 1, j - 1] = "x"
                    if i + 1 <= 9:
                        arr[i + 1, j - 1] = "x"


def battleship():
    ships_coordinate = {4: [], 3: [], 2: [], 1: []}
    field = np.full([10, 10], " ")
    type_ship = [4, 3, 2, 1]
    battle_result = {1: [], 2: [], 3: [], 4: []}
    count_miss = 0
    count_sunk_ships = 0
    game_field = np.full([10, 10], " ")

    for i in type_ship:  # adds the ships on the field
        if i == 4:  # adds the 4-decker ship on the field
            x, y = randint(0, 9), randint(0, 9)
            if x > 6:
                y = randint(0, 6)
            if y > 6:
                x = randint(0, 6)

            for j in range(i):
                if x <= 6:
                    field[x + j, y] = "S"
                    ships_coordinate[4].append([x + j, y])
                elif y <= 6:
                    field[x, y + j] = "S"
                    ships_coordinate[4].append([x, y + j])

            check_ships(field)

        if i == 3:  # adds the 3-decker ships on the field
            count = 0
            while count < 2:
                x, y = randint(0, 9), randint(0, 9)
                if x > 7:
                    y = randint(0, 7)
                if y > 7:
                    x = randint(0, 7)

                if x <= 7 and field[x, y] == " " and field[x + i - 1, y] == " ":
                    for j in range(i):
                        field[x + j, y] = "S"
                        ships_coordinate[3].append([x + j, y])
                    count += 1
                elif y <= 7 and field[x, y] == " " and field[x, y + i - 1] == " ":
                    for j in range(i):
                        field[x, y + j] = "S"
                        ships_coordinate[3].append([x, y + j])
                    count += 1

                check_ships(field)

        if i == 2:  # adds the 2-decker ships on the field
            count = 0
            while count < 3:
                x, y = randint(0, 9), randint(0, 9)
                if x > 8:
                    y = randint(0, 8)
                if y > 8:
                    x = randint(0, 8)

                if x <= 8 and field[x, y] == " " and field[x + i - 1, y] == " ":
                    for j in range(i):
                        field[x + j, y] = "S"
                        ships_coordinate[2].append([x + j, y])
                    count += 1
                elif y <= 8 and field[x, y] == " " and field[x, y + i - 1] == " ":
                    for j in range(i):
                        field[x, y + j] = "S"
                        ships_coordinate[2].append([x, y + j])
                    count += 1

                check_ships(field)

        if i == 1:  # adds the ones-decker ships on the field
            count = 0
            while count < 4:
                x, y = randint(0, 9), randint(0, 9)

                if field[x, y] == " ":
                    field[x, y] = "S"
                    ships_coordinate[1].append([x, y])
                    count += 1

                check_ships(field)

    while count_miss < 10:  # starts to play game
        print(game_field)
        print(ships_coordinate)  # if you want to win :)
        try:
            i, j = input("Enter two digits from 1 to 10 and press \"Enter\": ").split()
            i, j = int(i) - 1, int(j) - 1

            if i not in range(10) or j not in range(10):
                print("Wrong values, try again")

            else:
                if [i, j] in ships_coordinate[4] or [i, j] in ships_coordinate[3] or [i, j] in ships_coordinate[2]\
                        or [i, j] in ships_coordinate[1]:

                    game_field[i, j] = "X"

                    if [i, j] in ships_coordinate[4] and len(battle_result[4]) < 4:
                        battle_result[4].append([i, j])
                        if len(battle_result[4]) == 4:
                            count_sunk_ships += 1
                            print("You sunk the ship!")
                        else:
                            print("You hit the ship!")

                    if [i, j] in ships_coordinate[3] and len(battle_result[3]) < 3:
                        battle_result[3].append([i, j])
                        if len(battle_result[3]) == 3:
                            battle_result[3] = []
                            count_sunk_ships += 1
                            print("You sunk the ship!")
                        else:
                            print("You hit the ship!")

                    if [i, j] in ships_coordinate[2] and len(battle_result[2]) < 2:
                        battle_result[2].append([i, j])
                        if len(battle_result[2]) == 2:
                            battle_result[2] = []
                            count_sunk_ships += 1
                            print("You sunk the ship!")
                        else:
                            print("You hit the ship!")

                    if [i, j] in ships_coordinate[1]:
                        count_sunk_ships += 1
                        print("You sunk the ship!")

                else:
                    game_field[i, j] = "o"
                    count_miss += 1
                    print("You miss, try again")

        except ValueError:
            print("Wrong values, try again")

        if count_sunk_ships == 10:
            print("Congratulation! You win!")
            break

    if count_sunk_ships < 10:
        print("You lose.")


battleship()
