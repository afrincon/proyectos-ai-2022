import string
import random

class BookRegistry:

    def generate_book_isbn(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_book_edition(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:

    def register_book(self, book: string, editorial: string):
        # create a registry instance
        registry = BookRegistry()

        # generate a vehicle id of length 12
        book_isbn = registry.generate_book_isbn(13)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        book_edition = registry.generate_book_edition(book_isbn)

        # compute the catalogue price
        catalogue_price = 0
        if editorial == "Minotauro":
            catalogue_price = 60000
        elif editorial == "Penta":
            catalogue_price = 35000
        elif editorial == "Booknet":
            catalogue_price = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if editorial == "Minotauro" or editorial == "Penta":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Registration complete. Book information:")
        print(f"Book: {book}")
        print(f"Editorial: {editorial}")
        print(f"ISBN: {book_isbn}")
        print(f"Edition: {book_edition}")
        print(f"Payable tax: {payable_tax}")

app = Application()
app.register_book("The Silmarillion","Penta")