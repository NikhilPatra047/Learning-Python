name = input("Enter your name: ")

# Automatically closes the file after we are done
with open("intro.txt", "a") as file:
    file.write(f"{name}\n")

# file = open("intro.txt", "a")
# file.write("blah blah blah")
# file.close()
