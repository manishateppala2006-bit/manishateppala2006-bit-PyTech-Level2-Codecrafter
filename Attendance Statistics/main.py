from model import AttendanceStatistics
from utils import display_menu, get_choice


def main():
    stats = AttendanceStatistics("attendance.csv")

    while True:
        display_menu()
        choice = get_choice()

        if choice == 1:
            stats.load_data()

        elif choice == 2:
            if stats.attendance is not None:
                print("Mean Attendance:", round(stats.calculate_mean(), 2))
            else:
                print("Load data first!")

        elif choice == 3:
            if stats.attendance is not None:
                print("Standard Deviation:", round(stats.calculate_std(), 2))
            else:
                print("Load data first!")

        elif choice == 4:
            if stats.attendance is not None:
                below = stats.students_below_75()
                print("\nStudents Below 75%:")
                for student in below:
                    print("-", student)
            else:
                print("Load data first!")

        elif choice == 5:
            if stats.attendance is not None:
                stats.generate_pie_chart()
            else:
                print("Load data first!")

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()