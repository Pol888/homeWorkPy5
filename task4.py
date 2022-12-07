# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

stroka = 'ddddddhhhhhhhhhhhh77777lllllllllllllrrrrrrgggggggggggggggbbbzzzzzzzzzzvvvvvvvvlnnnnbveewaaaaaaa' \
         'rrrrrrrrrrrrrrrrrrrrryyyyyyyyyyyyyyyooooooiiiiqqwerrrrrrrrrrr888666666ttt'

the_string_is_compressed = ''

counter = 1
for i in range(1, len(stroka)):
    if stroka[i] != stroka[i - 1]:
        if stroka[i - 1].isdigit():
            the_string_is_compressed += f'|{counter}-{stroka[i - 1]}|'
            counter = 0
        else:
            the_string_is_compressed += f'{counter}{stroka[i - 1]}'
            counter = 0
    counter += 1

if stroka[-1].isdigit():
    the_string_is_compressed += f'|{counter}-{stroka[-1]}|'
else:
    the_string_is_compressed += f'{counter}{stroka[-1]}'

print(the_string_is_compressed)