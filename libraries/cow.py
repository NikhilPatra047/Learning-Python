from cowsay import cow, tux, dragon, kitty, turtle
from sys import argv

if len(argv) == 2:
    turtle(f"HELLO, {argv[1]}")
elif len(argv) < 2:
    cow("Too less arguments")
else:
    cow("Too many arguments")
