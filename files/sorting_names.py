import csv

students = []

# Coding defensively
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name": row[0], "house": row[1]})
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house.strip()}
#         students.append(student)

# def sort_name(student):
#     return student['name']

# def sort_house(student):
#     return student['house']

# lambda functions are functions without names. They can accept as many arguments as possible, and return an output.
for student in sorted(students, key=lambda student: student["house"], reverse=False):
    print(f"{student['name']} was born in {student['house']}")
