with open("intro.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    # print(f"hello, {line}", end="")
    print(f"hello, {line.strip()}")
