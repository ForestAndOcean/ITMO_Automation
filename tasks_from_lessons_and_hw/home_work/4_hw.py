# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.
class rectangle:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def area(self):
        return self.lenght * self.width

    def perimeter(self):
        return (self.lenght + self.width) * 2

first_object = rectangle(1,2)
second_object = rectangle(2,3)
third_object = rectangle(3,4)

print(first_object.area())
print(second_object.area())
print(third_object.area())

print(first_object.perimeter())
print(second_object.perimeter())
print(third_object.perimeter())

print('\n')

# 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.
class Math:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

fourth_object = Math(10,2)

print(fourth_object.addition())
print(fourth_object.multiplication())
print(fourth_object.division())
print(fourth_object.subtraction())

print('\n')
# 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Elements:

    type: str = 'Кнопка'

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

    def click(self):
        return 'Клик по кнопке {}'.format(self.text)

text_box_obj = Elements('Text Box','')
check_box_obj = Elements('Check Box','')
radio_button_obj = Elements('Radio Button','')
web_tables_obj = Elements('Web Tables','')
buttons_obj = Elements('Buttons','')
links_obj = Elements('links','')
broken_links_images_obj = Elements('Broken Links - Images','')
upload_and_download_obj = Elements('Upload and Download','')
dynamic_properties_obj = Elements('Dynamic Properties','')

print(text_box_obj.click())
print(check_box_obj.click())
print(radio_button_obj.click())
print(web_tables_obj.click())
print(buttons_obj.click())
print(links_obj.click())
print(broken_links_images_obj.click())
print(upload_and_download_obj.click())
print(dynamic_properties_obj.click())

print('\n')

# Доп*
# 4. В отдельном файле напишите программу с классом Car.
# a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
# iv. Пятый — присвоение автомобилю цвета.

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def work(self):
        if a == 1:
            return 'Автомобиль заведен'
        else:
            ''

    def not_work(self):
        if b == 0:
            return 'Автомобиль заглушен'
        else:
            ''

    def post_year(self):
        return 'Присвоен год выпуска {}'.format(self.year)

    def post_type(self):
        return 'Присвоен тип {}'.format(self.type)

    def post_color(self):
        return 'Присвоен цвет {}'.format(self.color)

work = Car('','','')
not_work = Car('','','')
new_year = Car('', '', '2000')
new_type = Car('', 'легковой автомобиль', '')
new_color = Car('синий', '', '')

a = 1
b = 0

print(work.work())
print(not_work.not_work())
print(new_year.post_year())
print(new_type.post_type())
print(new_color.post_color())