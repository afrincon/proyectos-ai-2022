import string
import random

class BookInfo:
    
    def __init__(self, book_name, editorial, catalog_price, hard_cover):
        self.book_name = book_name
        self.editorial = editorial
        self.catalog_price = catalog_price
        self.hard_cover = hard_cover

    def compute_tax(self):
        tax_percentage = 0.05
        if self.hard_cover:
            tax_percentage = 0.19
        return tax_percentage * self.catalog_price

    def print(self):
        print(f'Book name: {self.book_name}')
        print(f'Editorial: {self.editorial}')
        print(f'Payable taxes: {self.compute_tax()}')
        

class Book:

    def __init__(self, isbn, edition, info):
        self.isbn = isbn
        self.edition = edition
        self.info = info

    def print(self):
        print(f'ISBN: {self.isbn}')
        print(f'Edition: {self.edition}')
        self.info.print()


class BookRegistry:

    def __init__(self):
        self.book_info = {}
        self.add_book_info("The Silmarillion", "Booknet", 60000, False)
        self.add_book_info("The Silmarillion", "Penta", 120000, True)

    def add_book_info(self,book_name, editorial, catalog_price, hard_cover):
        self.book_info[book_name] = BookInfo(book_name,editorial, catalog_price, hard_cover)

    def generate_book_isbn(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_book_edition(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_book(self, book_name):
        isbn = self.generate_book_isbn(13)
        edition = self.generate_book_edition(isbn)
        return Book(isbn,edition, self.book_info[book_name])

class Application:

    def register_book(self, book_name: string):
        registry = BookRegistry()

        book = registry.create_book(book_name)

        book.print()

app = Application()
app.register_book("The Silmarillion")