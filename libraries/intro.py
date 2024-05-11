# A module is file containing code in Python that can be imported to other files for use.
# Improves code reusability and modularity
#
# import random - imports everything in the random module
from random import choice, randint, shuffle

coins = ["heads", "tails"]
coin = choice(coins)
random_number = randint(1, 100)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(cards)

print(coin)
print(random_number)
print([card for card in cards])
