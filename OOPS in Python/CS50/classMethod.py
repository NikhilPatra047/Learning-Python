from random import choice

# We can have a class inside a class
class Hat:
    houses_cls = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        random_house = choice(cls.houses_cls)
        print(name, "is in", random_house)

def main():
    Hat.sort("Harry")

if __name__ == "__main__":
    main()
