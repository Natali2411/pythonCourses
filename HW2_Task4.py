'''Даны три числа a, b, c. Определите, существует ли треугольник с такими сторонами. Если
треугольник существует, выведите строку YES, иначе выведите строку NO.
a = int(input('Enter a number "a": '))
b = int(input('Enter a number "b": '))
c = int(input('Enter a number "c": '))

if a + b > c:
    print('YES')
elif a + c > b:
    print('YES')
elif c + b > a:
    print('YES')
else:
    print('NO')'''