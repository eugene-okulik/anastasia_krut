class Book:
    material = 'бумага'
    text = True

    def __init__(self, name, author, number_str, isbn, reserve=False):
        self.name = name
        self.author = author
        self.number_str = number_str
        self.isbn = isbn
        self.reserve = reserve


book_1 = Book('Евгений Онегин', 'А.С. Пушкин', 177, '978-3-16-148410-0')
book_2 = Book('Капитанская дочка', 'А.С. Пушкин', 145, '978-3-16-148411-0')
book_3 = Book('Руслан и Людмила', 'А.С. Пушкин', 345, '978-3-16-148413-0')
book_4 = Book('Война и мир', 'Л.Н. Толстой', 23456, '978-3-16-148414-0')
book_5 = Book('Анна Каренина', 'Л.Н. Толстой', 674, '978-3-16-148415-0')

book_1.reserve = True
# print(book_1.reserve)

list_book = [book_1, book_2, book_3, book_4, book_5]

for book in list_book:
    if book.reserve:
        print(f"Название: {book.name}, Автор: {book.author}, страниц: {book.number_str}, "
              f"материал: {book.material}, зарезервирована")
    else:
        print(f"Название: {book.name}, Автор: {book.author}, страниц: {book.number_str}, "
              f"материал: {book.material}")


class SchoolBook(Book):
    def __init__(self, name, author, number_str, isbn, subject, number_class, exercise):
        super().__init__(name, author, number_str, isbn, reserve=False)
        self.subject = subject
        self.number_class = number_class
        self.exercise = exercise


text_book_1 = SchoolBook('Алгебра для средней школы', 'Иванов', 123, '978-3-16-148416-0',
                         'Алгебра', 7, True)

text_book_2 = SchoolBook('Физика для средней школы', 'Петров', 122, '978-3-16-148417-0',
                         'Физика', 8, True)

text_book_3 = SchoolBook('Новейшая история', 'Сидоров', 121, '978-3-16-148418-0',
                         'История', 9, False)

text_book_1.reserve = True
# print(text_book_1.reserve)

list_text_book = [text_book_1, text_book_2, text_book_3]

for book in list_text_book:
    if book.reserve:
        print(f"Название: {book.name}, Автор: {book.author}, страниц: {book.number_str}, "
              f"предмет: {book.subject}, класс: {book.number_class}, зарезервирована")
    else:
        print(f"Название: {book.name}, Автор: {book.author}, страниц: {book.number_str}, "
              f"предмет: {book.subject}, класс: {book.number_class}")
