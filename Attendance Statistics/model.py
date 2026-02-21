import numpy as np
import matplotlib.pyplot as plt
import csv


class AttendanceStatistics:

    def __init__(self, filename):
        self.filename = filename
        self.names = []
        self.attendance = None

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)

                attendance_list = []
                for row in reader:
                    self.names.append(row[0])
                    attendance_list.append(float(row[1]))

                self.attendance = np.array(attendance_list)
                print("Data loaded successfully!")

        except FileNotFoundError:
            print("Error: File not found!")

    def calculate_mean(self):
        return np.mean(self.attendance)

    def calculate_std(self):
        return np.std(self.attendance)

    def students_below_75(self):
        below = []
        for i in range(len(self.attendance)):
            if self.attendance[i] < 75:
                below.append(self.names[i])
        return below

    def generate_pie_chart(self):
        below = np.sum(self.attendance < 75)
        above = np.sum(self.attendance >= 75)

        labels = ['Below 75%', '75% and Above']
        sizes = [below, above]

        plt.figure()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Attendance Distribution')
        plt.show()