# Создайте программу для игры в ""Крестики-нолики"".

size = int(input('Задайте размер игрального поля:')) + 1

playing_field = [['*'] * size for i in range(size)]
count = 0
for i in range(size):
    for j in range(size):

        if i == 0:
            playing_field[i][j] = count
            playing_field[j][i] = count
            count += 1
playing_field[0][0] = ' '

for i in range(size):
    for j in range(size):
        print(playing_field[i][j], end='  ')
    print()

pl = 1
f = 'Крестиком'
print('Координаты хода вводятся через пробел, первая цифра строчка, вторая столбик')
print(f'ходит {pl}-{f} игрок')
motion = input(f'Введите координаты хода\n').split()
stop = False
diagonalX = 0
diagonalO = 0
while True:
    if pl == 1:
        playing_field[int(motion[0])][int(motion[1])] = 'x'
    else:
        playing_field[int(motion[0])][int(motion[1])] = 'o'

    for i in range(size):
        verticalX = 0
        gorizontX = 0

        verticalO = 0
        gorizontO = 0
        for j in range(size):
            if playing_field[i][j] == 'x':
                verticalX += 1
            if playing_field[j][i] == 'x':
                gorizontX += 1

            if playing_field[i][j] == 'o':
                verticalO += 1
            if playing_field[j][i] == 'o':
                gorizontO += 1

            if playing_field[i][j] == 'o' and i == j:
                diagonalO += 1
            if playing_field[i][j] == 'x' and i == j:
                diagonalX += 1




            print(playing_field[i][j], end='  ')
        print()
        if verticalX == size - 1 or gorizontX == size - 1:
            print("Победил 1 игрок, играющий крестиком!")
            stop = True
        elif verticalO == size - 1 or gorizontO == size - 1:
            print("Победил 2 игрок, играющий ноликом!")
            stop = True

    if diagonalO == size - 1:
        print("Победил 2 игрок, играющий ноликом!")
        stop = True

    elif diagonalX == size - 1:
        print("Победил 1 игрок, играющий крестиком!")
        stop = True

    diagonalX = 0
    diagonalO = 0


    if stop:
        break

    if pl == 1:
        pl = 2
        f = 'Ноликом'
    else:
        pl = 1
        f = 'Крестиком'

    while True:
        print(f'ходит игрок {pl} - {f} \n')
        motion = input(f'Введите координаты хода\n').split()
        if playing_field[int(motion[0])][int(motion[1])] == 'x' or playing_field[int(motion[0])][int(motion[1])] == 'o':
            print('Ход был сотворен в прошлом, выберете новый ход')
            continue
        break
