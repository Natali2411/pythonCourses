'''У вас есть список чисел.
1.	Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым
2.	** Как сделать это же задание со строкой?
3.	Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького до самого большого,
пока он не останется пустым.'''

''' 1. 
l = [1,2,3,4,5,6,7,8,9,10]
n = 0
while l:
    print(l.pop(n))
print(l) '''

''' 2.
s = 'Natalia'
n = 1
while s:
    s = s[n:]
    print(s)
print("This is an empty string " + s) '''

''' 3.'''
l = [6,5,9,4,1,2]
l = sorted(l)
n = 0
while l:
    print(l.pop(n))
print(l)

