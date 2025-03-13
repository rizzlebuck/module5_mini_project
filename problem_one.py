import mysql.connector
from datetime import date


def create_connection():
    try:
        return mysql.connector.connect(
            user='root', 
            password='Jokersol', 
            host='127.0.0.1',
            port=3306,
            database='module5_mini_project'
        )
    except mysql.connector.Error as err:
        print(f"Error: Unable to connect to database: {err}")
        return None

def close_connection(cursor, conn):
    cursor.close()
    conn.close()


class LibraryBook:
    def __init__(self, id=None, title=None, author_id=None, isbn=None, publication_date=None, available=True):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.available = available

    def save(self, cursor):
        query = """INSERT INTO books (title, author_id, isbn, publication_date, availability)
                   VALUES (%s, %s, %s, %s, %s)"""
        values = (self.title, self.author_id, self.isbn, self.publication_date, self.available)
        cursor.execute(query, values)

    @classmethod
    def fetch_all(cls, cursor):
        query = "SELECT * FROM books"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [cls(id=row[0], title=row[1], author_id=row[2], isbn=row[3], publication_date=row[4], available=row[5]) for row in rows]

    @classmethod
    def find_by_title(cls, cursor, search_title):
        query = "SELECT * FROM books WHERE title LIKE %s"
        cursor.execute(query, ('%' + search_title + '%',))
        rows = cursor.fetchall()
        return [cls(id=row[0], title=row[1], author_id=row[2], isbn=row[3], publication_date=row[4], available=row[5]) for row in rows]


def display_main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. Exit")

        choice = input("Select an option: ")
        if choice == '1':
            handle_book_operations()
        elif choice == '2':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


def handle_book_operations():
    print("\nBook Operations:")
    print("1. Add a new book")
    print("2. Show all books")
    choice = input("Choose an operation: ")
    if choice == '1':
        add_new_book()
    elif choice == '2':
        display_books()
    else:
        print("Invalid selection. Please try again.")


def add_new_book():
    title = input("Enter the title of the book: ")
    author_id = int(input("Enter the author ID: "))  # Author ID is input here.
    isbn = input("Enter the ISBN number: ")
    publication_date = input("Enter the publication date (YYYY-MM-DD): ")

    while True:
        available_input = input("Is the book available? (y/n): ").strip().lower()
        if available_input == 'y':
            available = True
            break
        elif available_input == 'n':
            available = False
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

    new_book = LibraryBook(title=title, author_id=author_id, isbn=isbn, publication_date=publication_date, available=available)
    
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        new_book.save(cursor)
        conn.commit()
        print("The book has been successfully added.")
        close_connection(cursor, conn)


def display_books():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        books = LibraryBook.fetch_all(cursor)
        for book in books:
            print(f"Title: {book.title}, Author ID: {book.author_id}, ISBN: {book.isbn}, Available: {'Yes' if book.available else 'No'}")
        close_connection(cursor, conn)


if __name__ == "__main__":
    display_main_menu()
