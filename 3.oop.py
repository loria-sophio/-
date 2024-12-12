class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def about(self):
        return f"{self.title} was written by {self.author} in {self.year}"


class BookManager:
    def __init__(self):
        self.books = []  # Initialize an empty list to store books

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"Book added: {new_book.about()}")

    def list_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Books in the library:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book.about()}")

    def search_book(self, search_term):
        found_books = [book for book in self.books if search_term.lower() in book.title.lower()]
        if not found_books:
            print(f"No books found with '{search_term}' in the title.")
        else:
            print(f"Books found with '{search_term}':")
            for book in found_books:
                print(book.about())


def main():
    manager = BookManager()

    while True:
        print("\nWelcome to the Book Manager Console!")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search for a book by title")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            title = input("Enter the book title: ").strip()
            author = input("Enter the author's name: ").strip()
            while True:
                try:
                    year = int(input("Enter the publication year: ").strip())
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid year.")

            manager.add_book(title, author, year)

        elif choice == "2":
            manager.list_books()

        elif choice == "3":
            search_term = input("Enter the title to search for: ").strip()
            manager.search_book(search_term)

        elif choice == "4":
            print("Exiting the Book Manager Console. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-4).")


# Run the console application
if __name__ == "__main__":
    main()