class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def getBook_details(self):
        return f"Title:{self.title},Author:{self.author},Price={self.price}"

    def update_book(self,new_title):
         self.title=new_title


class Ebook (book):
    def __init__(self, title, author, file_format, price):
        super().__init__(title, author, price)
        self.file_format=file_format

    def get_info(self):
        return f""



class Library():
    def add_books(self,book_id,):
        return ""



    def display_books(self):
        return ""
