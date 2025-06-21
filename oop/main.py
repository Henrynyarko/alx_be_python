from library_system import Book, EBook, PrintBook, Library

print("main.py is running")  # Debug message

def main():
    my_library = Library()
    my_library.add_book(Book("Pride and Prejudice", "Jane Austen"))
    my_library.add_book(EBook("Snow Crash", "Neal Stephenson", 500))
    my_library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))
    my_library.list_books()

if __name__ == "__main__":
    main()
