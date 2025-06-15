import sys

# -----------------------------
# Simple Book & Library Classes
# -----------------------------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        print(f"Book '{title}' is not available.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        print(f"Book '{title}' was not checked out.")
        return False

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        for book in available:
            print(f"{book.title} by {book.author}")
        if not available:
            print("No available books.")


# -----------------------------
# Robust Division Calculator
# -----------------------------

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom}"
    except ValueError:
        return "Error: Please enter numeric values only."


# -----------------------------
# Main Application Entry
# -----------------------------

def run_library():
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    print("Available books after setup:")
    library.list_available_books()

    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


def run_division(numerator, denominator):
    result = safe_divide(numerator, denominator)
    print(result)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py library")
        print("  python main.py division <numerator> <denominator>")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "library":
        run_library()

    elif mode == "division":
        if len(sys.argv) != 4:
            print("Usage: python main.py division <numerator> <denominator>")
            sys.exit(1)
        run_division(sys.argv[2], sys.argv[3])

    else:
        print("Invalid mode. Choose 'library' or 'division'.")


if __name__ == "__main__":
    main()
