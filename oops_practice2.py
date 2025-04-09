class Book:
    def __init__(self, title, author, pages, avaliable):
        self.title = title
        self.author = author
        self.pages = pages
        self.avaliable = avaliable

    def borrow(self):
        if self.avaliable == FALSE:
            print ()



class Member:
    def __init__(self, name, books):
        self.name = name
        self.books = books

class Library:
    pass
