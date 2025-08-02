class Book:
    """A class representing a book with title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available (not checked out)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check whether the book is available."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books."""

    def __init__(self):
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title, if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title, making it available again."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not checked out or not found.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No available books.")
        for book in available_books:
            print(f"{book.title} by {book.author}")
