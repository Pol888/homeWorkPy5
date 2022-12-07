#Напишите программу, удаляющую из текста все СЛОВА, содержащие ""абв"".
start = 'Привет забвение пошли на зимбабве пошалим незабвенно.'
start = start.split()

l = 0
for i in range(len(start)):
    i = l
    if 'абв' in start[i]:
        del start[i]
        l = l - 1   #  list index out of range - не словить
    l = l + 1

start = ' '.join(start)
if start[-1] != ".":
    start += '.'

print(start)



