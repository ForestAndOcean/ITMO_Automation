# Задачи:
# 2. Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.
def max_number(a, b):
    return max(a, b)


print(max_number(1, 2))


# 3. Функция на вход получает два произвольных числа. Вывести в консоль “yes”, если они отличаются
# друг от друга на 135, иначе вывести на экран “No”
def know_yes_no(a, b):
    if max(a, b) - min(a, b) == 135:
        return 'yes'
    else:
        return 'no'


print(know_yes_no(1, 136))


# 4. Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень)
def month(a):
    if a in range(1, 3) or a == 12:
        return 'зима'
    elif a in range(3, 6):
        return 'весна'
    elif a in range(6, 9):
        return 'лето'
    elif a in range(9, 12):
        return 'осень'


print(month(6))


# 5. Функция на вход получает три произвольных числа. Если все числа больше 10,
# то вывести на экран “yes”, иначе “no”;
def yes_or_no(x, y, z):
    if x + y + z > 10:
        return 'yes'
    else:
        return 'no'


print(yes_or_no(1, 1, 9))


# Доп *
# 6. Функция на вход получает список, состоящий из 5 произвольных чисел.
# Найти количество положительных чисел среди них.
def positive_numbers(a: list):
    count = 0
    for b in a:
        if b > 0:
            count += 1
    return count


print(positive_numbers([1, 2, 3, -4, -5]))


# 7. Функция на вход получает 2 переменные.
# a. Кол-во лет (int)
# b. Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
def sum_years_months(a: int, b: int):
    return a * 12 * 29 + b * 29


print(sum_years_months(1, 1))
