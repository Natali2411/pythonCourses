'''Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести
одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).'''
a = int(input('Enter a number "a": '))
b = int(input('Enter a number "b": '))
c = int(input('Enter a number "c": '))

if a == b == c:
    print(3)
elif a == b or a == c or c == b:
    print(2)
elif a != b and b != c and a != c:
    print(0)