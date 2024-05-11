class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons {self.sickles} Sickles {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts

        return Vault(galleons, sickles, knuts)

    @classmethod
    def get(cls):
        galleons = int(input("Enter galleons: "))
        sickles = int(input("Enter sickles: "))
        knuts = int(input("Enter knuts: "))
        return cls(galleons, sickles, knuts)

def main():
    potter = Vault.get()
    weasly = Vault.get()
    hermione = Vault.get()

    print(potter)
    print(weasly)
    print(hermione)

    total = potter + weasly + hermione # + overloading
    print(total)

main()
