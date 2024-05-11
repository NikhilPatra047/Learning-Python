import csv

name = input("Enter your name: ")
house = input("Enter your house: ")

with open("add_csv.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])
