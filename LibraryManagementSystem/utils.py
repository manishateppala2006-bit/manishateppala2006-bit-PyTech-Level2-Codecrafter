# utils.py
def display_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Delete Book")
    print("5. View Available Books")
    print("6. Exit")

def get_choice():
    while True:
        choice = input("Enter your choice (1-6): ")
        if choice.isdigit() and 1 <= int(choice) <= 6:
            return int(choice)
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")