# Программа проверяет то, является ли число положительным
# или отрицательным и выводит соответствующее сообщение.

# num = 3
#
# # Также попробуйте следующие варианты значения num
# # num = -5
# # num = 0
#
# if num >= 0:
#     print('Число больше или равно 0')
# else:
#     print('Число отрицательное')
#
# num = -5
#
# if num >= 0:
#     print('Число больше или равно 0')
# else:
#     print('Число отрицательное')
#
# num = 0
#
# if num >= 0:
#     print('Число больше или равно 0')
# else:
#     print('Число отрицательное')
#
# # str_2 содержит в себе s str_1?
#
# str_1 = 'test'
# str_2 = 'test1'
#
# if str_1 == str_2:
#     print('yes')
# else:
#     print('no')
#
# num_float = 3.4
#
# # Также попробуйте варианты
# # num_float = 0
# # num_float = -4.5
#
# if num_float > 0:
#     print('Положительное число')
# elif num_float == 0:
#     print('ноль')
# else:
#     print('Число отрицательное')
#
# num_float = 0
#
# if num_float > 0:
#     print('Положительное число')
# elif num_float == 0:
#     print('ноль')
# else:
#     print('Число отрицательное')
#
# num_float = -4.5
#
# if num_float > 0:
#     print('Положительное число')
# elif num_float == 0:
#     print('ноль')
# else:
#     print('Число отрицательное')

# permit_print = True
# num = 1
#
# if num > 0 and permit_print:
#     print('num - положительное число')
# elif not permit_print:
#     print('Печать запрещена')

# course = 3
#
# if course == 1:
#     print('бакалавр')
# elif course == 2:
#     print('бакалавр')
# elif course == 3:
#     print('бакалавр')
# elif course == 4:
#     print('бакалавр')
# elif course == 5:
#     print('магистр')
# elif course == 6:
#     print('магистр')
# elif course == 7:
#     print('аспирант')
# elif course == 8:
#     print('аспирант')
# elif course == 9:
#     print('аспирант')
# elif course > 9:
#     print('Введите корректный год обучения')
# elif course < 1:
#     print('Введите корректный год обучения')

# def student_rank(year_of_study):
#     if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
#         print('Вы - бакалавр')
#     elif year_of_study in range(5,7):
#         print('Вы - магистр')
#     elif 7 <= year_of_study <= 9:
#         print('Вы - аспирант')
#     else:
#         print('Введите корректный год обучения')
#
# student_rank(10)

# Дано число. Если оно больше 100 или меньше -100, то вывести на экран символ "-",
# иначе вывести на экран "+"

number = 101

if number > 100 or number < -100:
    print('-')
else:
    print('+')