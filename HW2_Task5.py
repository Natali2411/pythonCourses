'''Дано три числа. Упорядочите их в порядке неубывания. Программа должна считывать три
числа a, b, c, затем программа должна менять их значения так, чтобы стали выполнены
условия a <= b <= c, затем программа выводит тройку a, b, c.'''

a = int(input('Enter a number "a": '))
b = int(input('Enter a number "b": '))
c = int(input('Enter a number "c": '))

if a <= b and b <= c:  # a, b, c
    print(str(a)+ ', ' + str(b) + ', ' + str(c))
elif a <= c and c <= b:  # a, c, b
    b, c = c, b
    print(str(a) + ', ' + str(b) + ', ' + str(c))
elif b <= a and a <= c:  # b, a, c
    b, a = a, b
    print(str(a) + ', ' + str(b) + ', ' + str(c))
elif b <= c and c <= a:  # b, c, a
    b, a = a, b
    c, b = b, c
    print(str(a) + ', ' + str(b) + ', ' + str(c))
elif c <= a and a <= b:  # c, a, b
    a, c = c, a
    c, b = b, c
    print(str(a) + ', ' + str(b) + ', ' + str(c))
elif c <= b and b <= a: # c, b, a
    c, a = a, c
    print(str(a) + ', ' + str(b) + ', ' + str(c))

