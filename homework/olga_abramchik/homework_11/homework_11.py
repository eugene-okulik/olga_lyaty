class Books:
    page_material = "бумага"
    text = True

    def __init__(self, name, author, pages, ISBN, reserve):
        self.name = name
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.reserve = reserve

    def book_info(self):
        if self.reserve is True:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.pages}, '
                  f'материал: {self.page_material}, зарезервирована')
        else:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.pages}, материал: {self.page_material}')


class Textbooks(Books):

    def __init__(self, name, author, pages, ISBN, reserve, subject, group, task):
        super().__init__(name, author, pages, ISBN, reserve)
        self.subject = subject
        self.group = group
        self.task = task

    def textbook_info(self):
        if self.reserve is True:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, '
                  f'класс: {self.group}, зарезервирована')
        else:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.pages}, материал: {self.subject}, '
                  f'класс: {self.group}')


book_1 = Books('Идиот', 'Достоевский', 500, '21202', True)
book_2 = Books('Война и мир', 'Толстой', 1000, '624120', False)
book_3 = Books('Три товарища', 'Ремарк', 375, '004567', False)
book_4 = Books('Морфий', 'Булгаков', 200, '654120', True)
book_5 = Books('Вий', 'Гоголь', 350, '50565', True)


book_1.book_info()
book_2.book_info()
book_3.book_info()
book_4.book_info()
book_5.book_info()

textbook_1 = Textbooks('Алгебра', 'Петров', 155, 5154, True, 'Математика', 6, True)
textbook_2 = Textbooks('Физическая география', 'Станкевич', 52, 554654, False, 'География', 7, False)
textbook_3 = Textbooks('Тригонометрия', 'Захарова ', 155, 654131, False, 'Геометрия', 10, True)
textbook_4 = Textbooks('Сборник задач по физике', 'Громыко ', 65, 5154, True, 'Физика', 10, True)
textbook_5 = Textbooks('Всемирная история', 'Иванов', 240, 65484, False, 'История', 9, True)


textbook_1.textbook_info()
textbook_2.textbook_info()
textbook_3.textbook_info()
textbook_4.textbook_info()
textbook_5.textbook_info()
