'''1. Записываем “Number: строка из файла” из одного файла в другой. Не
забываем закрывать файлы.
2. Воспользуйтесь менеджером контекста для файла, в который вы записываете
информацию.'''
import os

os.makedirs('D:\\PycharmProjects\\WorkWithFiles')

with open('D:\\PycharmProjects\\WorkWithFiles\\test1.txt') as t1:
    t2 = open('D:\\PycharmProjects\\WorkWithFiles\\test2.txt', 'a')
    n = 1
    for i in t1:
        t2.write(str(n)+': '+i)
        n += 1
    t2.closed
