def add_books():
    books = {}
    while True:
        book = input("Введіть назву книги (або 'stop' для завершення): ")
        if book.lower() == 'stop':
            return books
        author = input("Введіть автора книги: ")
        books[book] = author

def find_author(books, search_book):
    return books.get(search_book, "Книгу не знайдено")

books = add_books()
search_book = input("Введіть назву книги, щоб дізнатися автора: ")
author = find_author(books, search_book)
print("Автор:", author)