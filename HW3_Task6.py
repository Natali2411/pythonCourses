'''Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими
сторонами и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний),
Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).'''

def is_type_of_triangle(a,b,c):
    if a == b == c:
        res = 'Equilateral triangle'
    elif a == b or b == c or a == c:
        res = 'Isosceles triangle'
    elif a + b < c or b + c < a or a + c < b:
        res = 'Not a triangle'
    elif a != b != c:
        res = 'Versatile triangle'
    return res

print(is_type_of_triangle(5,6,0))