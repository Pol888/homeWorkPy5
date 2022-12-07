# Создайте программу для игры с конфетами
from random import randint

# Первому игроку, чтобы победить надо взять столько конфет, сколько будет остаток от деления
# количества конфет на 29, если остаток будет 0 то игрок который ходит первым заведомо в проигрышной ситуации.
def vs_computer():
    number_of_candies = int(input('Задайте количество конфет\n'))
    move_playerS_move = randint(0, 1)
    list_names = ['Computer', input('Введите имя игрока играющего против машины: ')]
    print('Первый ходит игрок -', list_names[move_playerS_move])
    print('Ход не превышает 28 конфет, выигрывает тот кто последним ходом забирает оставшиеся конфеты.')
    while True:
        print(f'В строю {number_of_candies} к.')
        if list_names[move_playerS_move] == 'Computer':
            logic = number_of_candies % 29
            if logic == 0:
                a = randint(1, 28)
                number_of_candies = number_of_candies - a
                print(f'Компьютер взял {a} к.')
                print('Осталось =', number_of_candies, 'после хода компьютера')
            else:
                number_of_candies = number_of_candies - logic
                print(f'Компьютер взял {logic} к.')
                print('Осталось =', number_of_candies, 'после хода компьютера')
        else:
            motion = int(input(f'Ход игрока {list_names[-1]}\n'))
            number_of_candies -= motion
            print(f'Человек взял {motion} к.')

        if number_of_candies <= 0:
            print(f'Осталось {number_of_candies} к.')
            break

        if move_playerS_move == 1:
            move_playerS_move = 0
        else:
            move_playerS_move = 1
    print(f'Выиграл {list_names[move_playerS_move]}')


def players_games():
    number_of_candies = int(input('Задайте количество конфет\n'))
    move_playerS_move = randint(0, 1)
    list_names = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
    print(f'В строю {number_of_candies} к.')
    print('Первый ходит игрок -', list_names[move_playerS_move])
    print('Ход не превышает 28 конфет, выигрывает тот кто последним ходом забирает оставшиеся конфеты.')
    while True:
        motion = int(input(f'Ход игрока {list_names[move_playerS_move]}\n'))
        number_of_candies -= motion
        print(f'Осталось {number_of_candies} к.')
        if number_of_candies <= 0:
            break

        if move_playerS_move == 1:
            move_playerS_move = 0
        else:
            move_playerS_move = 1
    print(f'Выиграл {list_names[move_playerS_move]}')





def main():
    start = input('Введите "1" для игры с машиной и "белиберду" для игры -Человек vs Человек-\n')
    if start == '1':
        vs_computer()
    else:
        players_games()


if __name__ == '__main__':
    main()
