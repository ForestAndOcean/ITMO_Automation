# # определяем функцию
# def add(x, y):
#     return x + y
#
# #вызываем функцию
# print(add(1, 2))
#
# print(add('I a', 'm tester'))

def arg(a, b, c=2, d=3):
    return a+b+c+d

print(arg(1, 1, 1, 1))

print(arg(2, 2))

print(arg(1, 1, 1))

print(arg(2,2, 0.3, 1))

# mistake
# print(arg(2,2, '1', 1))

def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))

# Задача №1.
# Напишите функцию, которая:
# принимает 1 аргумент (а - значение по умолчанию) (1, 2, 3, 4)
# возвращает первый элемент этого кортежа
def task_1(a=(1, 2, 3, 4)):
    return a[1]

print("первый элемент кортежа (1, 2, 3, 4):", task_1())

# Напишите функцию, которая
# принимает 2 аргумента:
# - radius
# - pi=3,14159
# и возвращает площадь круга

def task_2(radius, pi=3.14159):
    return pi * radius**2

print(task_2(5))




