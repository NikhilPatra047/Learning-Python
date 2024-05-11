import csv

name = input("Enter your name: ")
house = input("Enter your house: ")

with open("add_csv.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({ "name": name, "house": house })
