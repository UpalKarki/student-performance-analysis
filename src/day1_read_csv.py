import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "students.csv")

students = []

with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

for student in students:
    print(student['name'], "-", student['attendance'])
