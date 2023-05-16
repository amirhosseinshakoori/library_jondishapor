class Book:
    def __init__(self,title,year,price,count) -> None:
        self.title = title
        self.year = year
        self.price = price
        self.count = count

    def borrow(self):
        if self.count > 0:
            self.count -= 1
            return True
        return False

    def return_book(self):
        self.count += 1

class Nevel(Book):
    def __init__(self, title, year, price, count, isbn, publisher=None) -> None:
        super().__init__(title, year, price, count)
        self._isbn = isbn
        self.publisher = publisher
    
    def isbn(self):
        return self._isbn


class Poem(Book):
    def __init__(self, title, year, price, count, genre) -> None:
        super().__init__(title, year, price, count)
        self.genre = genre

class Article(Book):
    def __init__(self, title, year, price, count,field) -> None:
        super().__init__(title, year, price, count)
        self.field = field



