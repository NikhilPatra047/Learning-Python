

# Write a Python program to create a person class. Include attributes  like name, country and date of birth.
# Implement a method to determine the person’s age.

from datetime import date

class Person:
    name = None
    country = None
    date_of_birth = date.today()

    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date_of_birth = date

    def calc_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

def main():
    person1 = Person("Nikhil", "India", date(2000, 3, 1))
    age = person1.calc_age()
    print(age)

main()
