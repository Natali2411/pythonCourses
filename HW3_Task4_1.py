'''Создайте строку, в которой написан, какой-то текст. Пример:
We are not what we should be!
We are not what we need to be.
But at least we are not what we used to bе
 (Football Coach)
•
•	Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
Усложнённое ** (можно сначала его не делать):
•	Посчитать, сколько раз встречается каждое слово.
(Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях подсчитываем количество «встречаний» этого слова)
'''

# 1) Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
s = 'We are not what we should be!'
print(len(s.split(' ')))
# 2) Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
'''
s = 'We are not, what we should be!'
n = 0
while n <= len(s)-1:
    s = s.strip('!')
    s = s.strip(',')
    s = s.strip('.')
    s = s.strip('?')
    s = s.strip(':')
    s = s.strip(';')
    n += 1
print(s) '''

# 3) Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
s = 'We are not what we should be'
l = s.split(' ')
l.sort()
print(l)