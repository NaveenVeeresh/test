class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    # Optional additional method
    def update_title(self, new_title):
        self.title = new_title


class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format


    def get_info(self):
        return f"{super().get_info()}, Format: {self.file_format}"


class Library:
    def __init__(self):
        self.books = []
        self.book_count = 0

    def add_book(self, book):
        self.books.append(book)
        self.book_count += 1

    def display_books(self):
        print(f"\nLibrary contains {self.book_count} books:")
        for book in self.books:
            print(book.get_info())

    # Optional additional method
    def find_book_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]


# Example usage:
if __name__ == "__main__":
    library = Library()

    # Add some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    ebook1 = EBook("Python Crash Course", "Eric Matthes", "9781593279288", "PDF")

    library.add_book(book1)
    library.add_book(ebook1)

    # Display all books
    library.display_books()

    # Optional: demonstrate additional methods
    book1.update_title("The Great Gatsby: Special Edition")
    print("\nAfter title update:")
    library.display_books()

    print("\nSearch results for 'python':")
    results = library.find_book_by_title("python crash course")
    for book in results:
        print(book.get_info())
