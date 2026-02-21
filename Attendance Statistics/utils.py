def display_menu():
    print("\n===== Attendance Dashboard =====")
    print("1. Load Data")
    print("2. Calculate Mean")
    print("3. Calculate Standard Deviation")
    print("4. Show Students Below 75%")
    print("5. Generate Pie Chart")
    print("6. Exit")


def get_choice():
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return 0