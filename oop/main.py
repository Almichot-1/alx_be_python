import math

# Test Book class with magic methods
try:
    from book_class import Book
    print("=== Testing Book class ===")
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)
    print(repr(my_book))
    del my_book
    print()
except ImportError:
    print("Book class not found. Skipping...\n")

# Test Library system with inheritance and composition
try:
    from library_system import Book as BaseBook, EBook, PrintBook, Library
    print("=== Testing Library System ===")
    library = Library()
    library.add_book(BaseBook("Pride and Prejudice", "Jane Austen"))
    library.add_book(EBook("Snow Crash", "Neal Stephenson", 500))
    library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))
    library.list_books()
    print()
except ImportError:
    print("Library system not found. Skipping...\n")

# Test polymorphism with Shape, Rectangle, Circle
try:
    from polymorphism_demo import Shape, Rectangle, Circle
    print("=== Testing Polymorphism ===")
    shapes = [Rectangle(10, 5), Circle(7)]
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
    print()
except ImportError:
    print("Polymorphism demo not found. Skipping...\n")

# Test static and class methods with Calculator
try:
    from class_static_methods_demo import Calculator
    print("=== Testing Calculator ===")
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
    print()
except ImportError:
    print("Calculator class not found. Skipping...\n")


if __name__ == "__main__":
    pass  # Already executed everything above
