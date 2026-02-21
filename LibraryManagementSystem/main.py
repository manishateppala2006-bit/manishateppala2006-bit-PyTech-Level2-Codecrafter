# main.py
from model import Library
from utils import display_menu, get_choice

def main():
    library = Library("data.txt")

    while True:
        display_menu()
        choice = get_choice()

        if choice == 1:
            book_id = input("Enter book ID: ").strip()
            title = input("Enter book title: ").strip()
            success, message = library.add_book(book_id, title)
            print(message)

        elif choice == 2:
            book_id = input("Enter book ID to issue: ").strip()
            success, message = library.issue_book(book_id)
            print(message)

        elif choice == 3:
            book_id = input("Enter book ID to return: ").strip()
            success, message = library.return_book(book_id)
            print(message)

        elif choice == 4:
            book_id = input("Enter book ID to delete: ").strip()
            success, message = library.delete_book(book_id)
            print(message)

        elif choice == 5:
            books = library.view_books()
            if not books:
                print("No books available.")
            else:
                print("\nID\tTitle\t\tStatus")
                print("-"*30)
                for book in books:
                    print(f"{book['id']}\t{book['title']}\t\t{book['status']}")

        elif choice == 6:
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()