# # class Button:
#
#     type: # str = 'Кнопка'
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
# # # Создаём экземпляры класса
# home = Button('Домой', '/home')
# catalog_msk = Button('Каталог', '/msk/catalog')
#
# # # Получаем доступ к атрибутам
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)
#
# # print('\n')
#
# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)
#
# # print('\n')
#
class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

# создаём экземпляры класса
home_two = ButtonTwo('Домой', '/home', 'button#home')

# вызываем метод
print(home_two.click())

# создайте класс Input, принимающий 1 аргумент при инициализации (Loc)
# создайте объект search (экземпляр класса Input)
# выведите в консоль значение аргумента Loc, объекта search
class Input:
    def __init__(self, loc):
        self.Loc = Loc

search = Input('Place')

print(search.loc)

# добавьте к классу Input атрибут объекта text
# создайте класс Button, класс Title, класс Link
# для каждого класса пропишите атрибуты text и loc
# создайте каждому из чётырёх классов объекты с любыми данными
# выведите в консоль text и loc каждого класса

class Input:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search = Input('текст_search_input', 'Москва_search_input')

print(search.text, ' ', search.loc)

class Button:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

obj_button = Button('текст_obj_button_Button', 'loc_obj_button_Button')

print(obj_button.text, ' ', obj_button.loc)

class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

obj_title = Title('текст_obj_title_Title', 'loc_obj_title_Title')

print(obj_title.text, ' ', obj_title.loc)

class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

obj_link = Link ('текст_obj_link_Link', 'loc_obj_link_Link')

print(obj_link.text, ' ', obj_link.loc)

# создайте класс Page, который принимает один аргумент при инициализации url
# в этом классе реализуйте метод get(), который выводит на печать url
# создайте объект home и вызовите метод get

class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)

home = Page ('https://www.google.com/')

home.get()

# создайте класс Soda (для определения типа газированной воды), который принимает один аргумент при инициализации
# (отвечающий за добавку к выбираемому лимонаду).
# в этом классе реализуйте метод show_my_drink(), который выводит на печать "Газировка
# и {Добавка}" в случае наличия добавки, а иначе отобразится следующая фраза: "Обычная газировка".
# для теста класса создайте 2 объекта (один с добавкой, другой - без).
# вызовите метод show_my_drink() для каждого объекта

class Soda:
    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}')

        else:
            print('Обычная газировка')

drink1 = Soda()
drink2 = Soda('малина')
drink1.show_my_drink()
drink2.show_my_drink()