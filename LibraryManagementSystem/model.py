# model.py
class Library:
    def __init__(self, data_file):
        self.data_file = data_file
        self.books = self.load_books()

    def load_books(self):
        books = []
        try:
            with open(self.data_file, "r") as f:
                for line in f:
                    book = line.strip().split("|")
                    if len(book) == 3:
                        books.append({
                            "id": book[0],
                            "title": book[1],
                            "status": book[2]
                        })
        except FileNotFoundError:
            open(self.data_file, "w").close()  # create file if doesn't exist
        return books

    def save_books(self):
        with open(self.data_file, "w") as f:
            for book in self.books:
                f.write(f"{book['id']}|{book['title']}|{book['status']}\n")

    def add_book(self, book_id, title):
        for book in self.books:
            if book["id"] == book_id:
                return False, "Book ID already exists!"
        self.books.append({"id": book_id, "title": title, "status": "available"})
        self.save_books()
        return True, "Book added successfully!"

    def issue_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                if book["status"] == "available":
                    book["status"] = "issued"
                    self.save_books()
                    return True, f"Book '{book['title']}' issued successfully!"
                else:
                    return False, "Book is already issued!"
        return False, "Book not found!"

    def return_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                if book["status"] == "issued":
                    book["status"] = "available"
                    self.save_books()
                    return True, f"Book '{book['title']}' returned successfully!"
                else:
                    return False, "Book is not issued!"
        return False, "Book not found!"

    def delete_book(self, book_id):
        for i, book in enumerate(self.books):
            if book["id"] == book_id:
                self.books.pop(i)
                self.save_books()
                return True, "Book deleted successfully!"
        return False, "Book not found!"

    def view_books(self):
        return self.books