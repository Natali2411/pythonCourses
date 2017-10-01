'''1) Определите является ли строка записью числа.
s = input('Enter a string: ')
res = s.isdigit()
print(res)'''

'''2) Посчитайте сколько у вас пробелов в строке.
s = input('Enter a string: ')
n = s.count(' ', 0,len(s))
print('Count of symbol " ": ' + str(n))'''

'''3) Посчитайте сколько у вас символов точки &#39;.&#39; в строке.
s = input('Enter a string: ')
n = s.count('.', 0,len(s))
print('Count of symbol ".": ' + str(n))'''

'''4) Создайте строку "Homework". Преобразуйте ее в строку длиной 100 символов,
посередине которой исходное слово, а с обоих сторон строка заполнена
пробелами. Выведите ее на экран.
s = 'Homework'
s1 = s.center(100)
print(s1)'''

'''5) Сделайте первые буквы слов строки большими (upper case).
s = 'natali'
print(s.capitalize())'''