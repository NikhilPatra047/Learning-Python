from sys import argv, exit

# try:
#     print("Hello, my name is", argv[1])
# except IndexError:
#     print("List out of index")
# finally:
#     print(argv[0])
#


coins = ["heads", "tails", "Ace"]
print(coins[::-1])

if len(argv) < 2:
    exit("Too few arguments")
elif len(argv) > 2:
    exit("Too many arguments")

print("Hello, my name is", argv[1])

# argv[0] - the name of the file itself where the python program is written
