''' Create a Book class that has two attributes:
    1. .title
    2. .author

    and two methods:

    1. A method named .get_title() that returns: "Title: " + the instance title.
    2. A method named .get_author() that returns: "Author: " + the instance author.

    and instantiate this class by creating 3 new books:

    1. Pride and Prejudice - Jane Austen (PP)
    2. Hamlet - William Shakespeare (H)
    3. War and Peace - Leo Tolstoy (WP)

    Name the new instance should be PP, H, and WP, respectively.

    For instance, if I instantiated the following book using this Book class:

        . Harry Potter - J.K. Rowling(HP)

    I would get the follwing attributes and methods:
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return "Title: " + self.title

    def get_author(self):
        return "Author: " + self.author


        # Pride and Prejudice - Jane Austen (PP)
        # Hamlet - William Shakespeare (H)
        # War and Peace - Leo Tolstoy (WP)    

PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")
