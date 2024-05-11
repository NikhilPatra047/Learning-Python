name = input("what's your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron": 
#   print("Gryffindor")
# elif name == "Draco": 
#   print("Slytherine")
# else: 
#   print("Who?")

# Match is the equivalent of switch cases in other programming languages

match name: 
  case "Harry": 
    print("Gryffindor")
  case "Hermione":
    print("Gryffindor")
  case "Ron": 
    print("Gryffindor")
  case "Draco": 
    print("Slytherine")
  case _: 
    print("Who?")