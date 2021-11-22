def greet():
    print("---------------------")
    print("Игра крестики-нолики!")
    print("---------------------")
    print("Формат ввода: х у")
    print("x - номер строки")
    print("у - номер столбца")
greet()

def show():
    print()
    print("  | 0 | 1 | 2 | ")
    print("-----------------")
    for i, row in enumerate(field):
        row_str = f"{i} | {' | '.join(row)} |"
        print(row_str)
        print("-----------------")
    print()


def ask():
    while True:
        coords = input ("     Ваш ход: ").split()

        if len(coords) != 2:
            print("Введите две координаты!")
            continue

        x, y = coords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y <0 or y >2:
            print("Вводимые точки вне диапазона!")
            continue

        if field [x] [y] != " ":
            print ("Даное поле занято!")
            continue

        return x, y

def chek_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                 ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for coords in win_coord:
        symbols = []
        for c in coords:
            symbols.append(field[c[0]] [c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0 !")
            return True
    return False


field = [[" "]*3 for i in range(3)]
num = 0
while True:
    num+=1
    show()
    if num %2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if num %2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if chek_win():
        break

    if num == 9:
        print("Ничья!")
        break