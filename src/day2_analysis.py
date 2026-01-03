import csv
import os

# Find base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "students.csv")

students=[]

# Read CSV
with open(file_path,"r") as file:
    readers=csv.DictReader(file)
    for row in readers:
        students.append(row)

# Analyze data
for student in students:
    math = int (student["math"])
    science = int (student["math"])
    english = int (student["math"])

    total=math+science+english
    average=total/3

    if total>=40:
        result = "Pass"

    if total<40:
        result = "Fail"

    print(
        student['name'],
        "| Total:", total,
        "| Average:", round(average, 2),
        "| Result:", result
    )
  
  # print(f"{student['name']}'s total mark is {total} and average mark is {round(average,2)} and he/she is {result}")


